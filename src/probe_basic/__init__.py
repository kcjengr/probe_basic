try:
    # Try to get version from package metadata (for installed packages)
    from importlib.metadata import version, PackageNotFoundError
    try:
        __version__ = version("probe-basic")
        # If version is placeholder (editable install), use git version
        if __version__ in ("0.0", "0.0.0"):
            raise PackageNotFoundError
    except PackageNotFoundError:
        # Fall back to dunamai for development installations
        try:
            from dunamai import Version
            git_version = Version.from_git()
            # Format to match poetry-dynamic-versioning: base+distance.gcommit
            if git_version.distance > 0:
                __version__ = f"{git_version.base}+{git_version.distance}.g{git_version.commit}"
            else:
                __version__ = git_version.base
        except Exception:
            __version__ = "0.0.0+unknown"
except ImportError:
    # Python < 3.8 fallback
    try:
        from dunamai import Version
        git_version = Version.from_git()
        if git_version.distance > 0:
            __version__ = f"{git_version.base}+{git_version.distance}.g{git_version.commit}"
        else:
            __version__ = git_version.base
    except Exception:
        __version__ = "0.0.0+unknown"

import os
import qtpyvcp

VCP_DIR = os.path.realpath(os.path.dirname(__file__))
VCP_CONFIG_FILE = os.path.join(VCP_DIR, 'probe_basic.yml')


def main(opts=None):

    if opts is None:
        from qtpyvcp.utilities.opt_parser import parse_opts
        opts = parse_opts(vcp_cmd='probe_basic',
                          vcp_name='Probe Basic',
                          vcp_version=__version__)

    qtpyvcp.run_vcp(opts, VCP_CONFIG_FILE)


if __name__ == '__main__':
    main()
