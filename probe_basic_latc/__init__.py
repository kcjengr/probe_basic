import pydevd_pycharm
pydevd_pycharm.settrace('localhost', port=1337, stdoutToServer=True, stderrToServer=True)

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

import os
import qtpyvcp

VCP_DIR = os.path.realpath(os.path.dirname(__file__))
VCP_CONFIG_FILE = os.path.join(VCP_DIR, 'probe_basic_latc.yml')


def main(opts=None):

    if opts is None:
        from qtpyvcp.utilities.opt_parser import parse_opts
        opts = parse_opts(vcp_cmd='probe_basic_latc',
                          vcp_name='Probe Basic Linear ATC',
                          vcp_version=__version__)

    qtpyvcp.run_vcp(opts, VCP_CONFIG_FILE)


if __name__ == '__main__':
    main()
