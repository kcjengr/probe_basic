#!/usr/bin/env python3
"""Refuse to build if a shipped tool database is newer than qtpyvcp can read.

The failure this exists to prevent: a developer's editable qtpyvcp checkout
carries migrations that are not committed yet. Running a sim config opens the
tracked .db file, applies those migrations, and writes the higher
meta.schema_version back into the tracked binary. Git records it as a normal
modification, the package ships it, and every user whose qtpyvcp only knows the
committed migrations gets a hard refusal at startup:

    MigrationError: database schema_version=8 is newer than this qtpyvcp build
    knows about (latest=6); refusing to touch it.

It works on the developer's machine precisely because it is the machine that
wrote the file. So the check has to run against the qtpyvcp the BUILD sees,
not the one the developer has.
"""

import glob
import os
import re
import sqlite3
import subprocess
import sys

CONFIGS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'configs')


MIGRATION_RE = re.compile(r'(\d{3})_.*\.sql$')


def _committed_migrations(repo):
    """Migration versions COMMITTED in a qtpyvcp checkout at `repo`.

    Deliberately not the files on disk. On a developer machine the checkout
    holds untracked migrations that no build will ever contain, and asking the
    working tree is exactly the question that returns the wrong answer.
    """
    try:
        out = subprocess.run(
            ['git', '-C', repo, 'ls-files', 'src/qtpyvcp/lib/db_tool/migrations/'],
            capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    versions = [int(m.group(1)) for m in
                (MIGRATION_RE.search(line) for line in out.splitlines()) if m]
    return max(versions) if versions else None


def _qtpyvcp_repo():
    """A qtpyvcp git checkout to read committed migrations from, if there is one."""
    env = os.environ.get('QTPYVCP_REPO')
    if env and os.path.isdir(os.path.join(env, '.git')):
        return env
    try:
        import qtpyvcp
    except Exception:
        return None
    # editable install -> src/qtpyvcp/__init__.py, repo root is two levels up
    root = os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(qtpyvcp.__file__))))
    return root if os.path.isdir(os.path.join(root, '.git')) else None


def latest_known_migration():
    """Highest migration version a built qtpyvcp will actually contain."""
    repo = _qtpyvcp_repo()
    if repo:
        version = _committed_migrations(repo)
        if version is not None:
            print("Checking against migrations COMMITTED in %s (latest=%d)"
                  % (repo, version))
            return version

    # Installed (non-editable) qtpyvcp: what is importable is what shipped.
    try:
        from qtpyvcp.lib.db_tool.migrate import _scripts
    except Exception as exc:
        print("SKIP: qtpyvcp not importable, cannot check shipped DBs (%s)" % exc)
        return None
    scripts = _scripts()
    if not scripts:
        print("SKIP: qtpyvcp exposes no migration scripts")
        return None
    print("Checking against installed qtpyvcp (latest=%d)" % scripts[-1][0])
    return scripts[-1][0]


def db_version(path):
    conn = sqlite3.connect('file:%s?mode=ro' % path, uri=True)
    try:
        cur = conn.cursor()
        has_meta = cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='meta'"
        ).fetchone()
        if not has_meta:
            return 0
        row = cur.execute("SELECT schema_version FROM meta").fetchone()
        return row[0] if row else 0
    finally:
        conn.close()


def main():
    latest = latest_known_migration()
    if latest is None:
        return 0

    offenders = []
    checked = 0
    for path in sorted(glob.glob(os.path.join(CONFIGS_DIR, '*', '*.db'))):
        try:
            version = db_version(path)
        except sqlite3.Error as exc:
            print("SKIP: %s is not a readable sqlite file (%s)"
                  % (os.path.relpath(path, CONFIGS_DIR), exc))
            continue
        checked += 1
        if version > latest:
            offenders.append((os.path.relpath(path, CONFIGS_DIR), version))

    if offenders:
        print("ERROR: shipped tool databases are newer than qtpyvcp knows "
              "(latest migration = %d):" % latest)
        for rel, version in offenders:
            print("    schema_version=%d  configs/%s" % (version, rel))
        print("")
        print("These would refuse to open on every user's machine. Either commit "
              "and publish the missing qtpyvcp migrations first, or restore the "
              "database files to a schema_version <= %d." % latest)
        return 1

    print("OK: %d shipped tool database(s), none newer than migration %d"
          % (checked, latest))
    return 0


if __name__ == '__main__':
    sys.exit(main())
