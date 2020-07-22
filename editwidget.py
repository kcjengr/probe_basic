#!/usr/bin/env python

"""
Command line tool to set up and launch QtDesigner for editing VCPs::

 Usage:
   editwidget [<widget>]
              [--log-level=LEVEL] [--log-file=PATH]
   editwidget (-h | --help)

 File Options:
    --widget WIDGET     Name of an installed VCP, or a path to either a
                        YAML or UI file. If a YAML file will load any UI
                        and QSS files specified in the qtdesigner section.

 Logging Options:
   --log-level (DEBUG | INFO | WARN | ERROR | CRITICAL)
                      Sets the log level. [default: ERROR]
   --log-file PATH    Specifies the log file. [default: ~/qtpyvcp-designer.log]

 Other Options:
   -h --help          Show this help and exit.
   --designer-args <args>...
"""

import os
import sys
import linuxcnc
import subprocess
from pkg_resources import iter_entry_points

from docopt import docopt
from qtpy.QtWidgets import QApplication, QFileDialog

from qtpyvcp.lib.types import DotDict
from qtpyvcp.utilities.logger import initBaseLogger

LCNC_VERSION_ERROR_MSG = """
\033[31mERROR:\033[0m Unsupported LinuxCNC version

QtPyVCP only supports LinuxCNC 2.8, current version is {}.
If you have LinuxCNC installed as a RIP make sure you have
activated the run-in-place environment by running:\n"

    $ . <linuxcnc-rip-dir>/scripts/rip-environment

Otherwise you will need to install LinuxCNC 2.8, info on how
to do that can be found here: https://gnipsel.com/linuxcnc/uspace/
""".strip()

INSTALLED_ERROR_MSG = """
\033[31mERROR:\033[0m Can not edit an installed VCP

The specified VCP appears to be installed in the `python2.7/site-packages` 
directory. Please set up a development install to edit the VCP.
""".strip()

if linuxcnc.version.startswith('2.7'):
    print LCNC_VERSION_ERROR_MSG.format(linuxcnc.version)
    sys.exit(1)

LOG = initBaseLogger('qtpyvcp', log_file=os.devnull, log_level='WARNING')

def launch_designer(opts=DotDict()):


    folderpath = os.path.dirname(os.path.abspath(__file__))
    fname = folderpath +"/widgets/" + opts.widget + "/" + opts.widget + ".ui"
    cmd = ['designer']

    cmd.append(fname)

    print "Loading UI file:", fname


    base = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, base)
    os.environ['QTPYVCP_LOG_FILE'] = opts.log_file
    os.environ['QTPYVCP_LOG_LEVEL'] = opts.log_level
    os.environ['QT_SELECT'] = 'qt5'
    os.environ['PYQTDESIGNERPATH'] = os.path.join(base, 'widgets')

    print "\nStarting QtDesigner ..."
    sys.exit(subprocess.call(cmd))


def main():
    raw_args = docopt(__doc__)
    # convert raw argument keys to valid python names
    opts = DotDict({arg.strip('-<>').replace('-', '_'):
                    value for arg, value in raw_args.items()})

    app = QApplication(sys.argv)
    launch_designer(opts)


if __name__ == '__main__':
    main()
