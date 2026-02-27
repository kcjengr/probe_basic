
__version__ = '0.0.1'

import os
import qtpyvcp

# Register Qt resources early so icons are available during plugin init.
from . import probe_basic_lathe_rc  # noqa: F401

VCP_DIR = os.path.realpath(os.path.dirname(__file__))
VCP_CONFIG_FILE = os.path.join(VCP_DIR, 'probe_basic_lathe.yml')


def main(opts=None):

    if opts is None:
        from qtpyvcp.utilities.opt_parser import parse_opts
        opts = parse_opts(vcp_cmd='probebasiclathe',
                          vcp_name='Probe Basic Lathe',
                          vcp_version=__version__)

    qtpyvcp.run_vcp(opts, VCP_CONFIG_FILE)


if __name__ == '__main__':
    main()
