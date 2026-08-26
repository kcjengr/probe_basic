#!/usr/bin/env python3

"""Refresh the loader .py files in a probe_basic config directory.

User tabs, user buttons and user DRO displays are each a folder holding a
Qt Designer .ui plus a small loader .py. The .ui is the user's; the .py is
ours, and it is deliberately generic -- it derives the .ui filename from its
own __file__, so one file works in every folder.

When probe_basic changes how those loaders work, existing config directories
keep their old copies and stop working. This refreshes them from the templates
that shipped with the installed package, leaving every .ui untouched.

This is not installed with Probe Basic. Download it when you need it:

  $ wget https://raw.githubusercontent.com/kcjengr/probe_basic/pyside6/scripts/update_user_files.py

Usage:
  python3 update_user_files.py <config_dir> ...
  python3 update_user_files.py --dry-run <config_dir> ...
  python3 update_user_files.py -h

Example::

  $ python3 update_user_files.py --dry-run ~/linuxcnc/configs/probe_basic
  $ python3 update_user_files.py ~/linuxcnc/configs/probe_basic
"""

import os
import shutil
import sys

# folder under the config dir -> template that shipped with the package
TEMPLATES = {
    "user_tabs": os.path.join("user_tabs", "template_main", "template_main.py"),
    "user_buttons": os.path.join(
        "user_buttons", "template_user_buttons", "template_user_buttons.py"),
    "user_dro_display": os.path.join("user_dro_display", "user_dros", "dros_user.py"),
}

# ATC button folders are fixed by ATC_TAB_DISPLAY rather than named by the user,
# and each holds a differently named class, so each is its own template.
FIXED_TEMPLATES = {
    os.path.join("user_atc_buttons", "template_user_atc_buttons",
                 "template_user_atc_buttons.py"),
    os.path.join("user_atc_buttons", "template_user_rack_atc_buttons",
                 "template_user_rack_atc_buttons.py"),
}

SHIPPED_CONFIGS = "/usr/share/configs"

# DRO loaders differ per VCP -- each imports its own compiled resource module --
# so templates are taken from the shipped config matching the target's DISPLAY.
DEFAULT_VCP = "probe_basic"


def vcp_of(config_dir):
    """The VCP named by DISPLAY in this config's INI, e.g. probe_basic_lathe."""
    for name in sorted(os.listdir(config_dir)):
        if not name.endswith(".ini"):
            continue
        try:
            with open(os.path.join(config_dir, name), errors="replace") as fh:
                for line in fh:
                    line = line.strip()
                    if line.startswith("DISPLAY") and "=" in line:
                        value = line.split("=", 1)[1].strip()
                        if value:
                            return value
        except OSError:
            continue
    return DEFAULT_VCP

ok = "\033[32mok\033[0m"
skip = "\033[33mskipped\033[0m"
fail = "\033[31mERROR\033[0m"


def find_templates(source_dir):
    """Locate the shipped template for each folder type."""
    found = {}
    for kind, relpath in TEMPLATES.items():
        path = os.path.join(source_dir, relpath)
        if os.path.isfile(path):
            found[kind] = path
        else:
            print(f"  {fail} no {kind} template at {path}")
    return found


def loader_name(folder_type, folder):
    """The .py a loader looks for inside one of these folders.

    Tabs and buttons use <folder>/<folder>.py. DRO folders are named
    <geometry>_dros but hold dros_<geometry>.py.
    """
    if folder_type == "user_dro_display":
        if not folder.endswith("_dros"):
            return None
        return "dros_" + folder[: -len("_dros")] + ".py"
    return folder + ".py"


def update_folder(folder_path, target_py, template, dry_run):
    dest = os.path.join(folder_path, target_py)
    if not os.path.isfile(dest):
        print(f"    {os.path.basename(folder_path)}/{target_py} ... {skip} (no loader .py here)")
        return 0

    with open(dest, "rb") as fh:
        current = fh.read()
    with open(template, "rb") as fh:
        wanted = fh.read()
    if current == wanted:
        print(f"    {os.path.basename(folder_path)}/{target_py} ... already current")
        return 0

    if dry_run:
        print(f"    {os.path.basename(folder_path)}/{target_py} ... would update")
        return 1

    shutil.copy2(dest, dest + ".bak")
    with open(dest, "wb") as fh:
        fh.write(wanted)
    print(f"    {os.path.basename(folder_path)}/{target_py} ... {ok} (old kept as {target_py}.bak)")
    return 1


def update_config(config_dir, source_dir, templates, dry_run):
    updated = 0
    for relpath in sorted(FIXED_TEMPLATES):
        dest = os.path.join(config_dir, relpath)
        src = os.path.join(source_dir, relpath)
        if not os.path.isfile(dest) or not os.path.isfile(src):
            continue
        print(f"  {os.path.dirname(relpath)}/")
        updated += update_folder(os.path.dirname(dest), os.path.basename(dest),
                                 src, dry_run)

    for kind, template in templates.items():
        base = os.path.join(config_dir, kind)
        if not os.path.isdir(base):
            continue
        print(f"  {kind}/")
        for folder in sorted(os.listdir(base)):
            folder_path = os.path.join(base, folder)
            if not os.path.isdir(folder_path) or folder == "__pycache__":
                continue
            target_py = loader_name(kind, folder)
            if target_py is None:
                print(f"    {folder}/ ... {skip} (not a <geometry>_dros folder)")
                continue
            updated += update_folder(folder_path, target_py, template, dry_run)
    return updated


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    flags = [a for a in sys.argv[1:] if a.startswith("-")]

    if not args or "-h" in flags or "--help" in flags:
        print(__doc__)
        sys.exit(0 if args or "-h" in flags or "--help" in flags else 1)

    dry_run = "--dry-run" in flags or "-n" in flags

    configs_root = os.environ.get("PROBE_BASIC_CONFIGS", SHIPPED_CONFIGS)
    if not os.path.isdir(configs_root):
        print(f"{fail} shipped configs not found at {configs_root}")
        print("Set PROBE_BASIC_CONFIGS to the directory holding them to override.")
        sys.exit(1)

    total = 0
    for config_dir in args:
        config_dir = os.path.abspath(os.path.expanduser(config_dir))
        if not os.path.isdir(config_dir):
            print(f"{fail} not a directory: {config_dir}")
            continue

        vcp = vcp_of(config_dir)
        source_dir = os.path.join(configs_root, vcp)
        if not os.path.isdir(source_dir):
            print(f"\n{config_dir}\n  {fail} no shipped templates for DISPLAY = {vcp} "
                  f"(looked in {source_dir})")
            continue

        print(f"\n{config_dir}")
        print(f"  DISPLAY = {vcp}, templates from {source_dir}")
        templates = find_templates(source_dir)
        if not templates:
            continue
        total += update_config(config_dir, source_dir, templates, dry_run)

    verb = "would update" if dry_run else "updated"
    print(f"\n{verb} {total} loader file(s). Your .ui files were not touched.")


if __name__ == "__main__":
    main()
