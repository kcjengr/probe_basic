try:
    # Try to get version from package metadata (for installed packages)
    from importlib.metadata import version, PackageNotFoundError
    try:
        __version__ = version("probe-basic")
    except PackageNotFoundError:
        # Fall back to versioneer for development installations
        from ._version import get_versions
        __version__ = get_versions()['version']
        del get_versions
except ImportError:
    # Python < 3.8 fallback
    try:
        from ._version import get_versions
        __version__ = get_versions()['version']
        del get_versions
    except:
        __version__ = "unknown"

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
