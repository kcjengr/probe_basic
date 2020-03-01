
import os
import re

from linuxcnc import ini

print "\n****** atc_util initialization started ******"

INI_FILE = os.environ['INI_FILE_NAME']
CONFIG_DIR = os.environ.get('CONFIG_DIR') or os.path.dirname(INI_FILE)

INI = ini(INI_FILE)

fname = INI.find('EMCIO', 'TOOL_TABLE')
TOOL_TABLE_FILE = os.path.realpath(os.path.join(CONFIG_DIR, fname))

TOOL_TABLE = {}

ATC_NUM_POCKETS = int(INI.find("ATC", 'NUM_POCKETS') or 0)


def read_tool_table():
    with open(TOOL_TABLE_FILE, 'r') as fh:
        lines = fh.readlines()

    for line in lines:
        if line.startswith(';'):
            continue

        data, sep, remark = line.partition(';')
        items = re.findall(r"([A-Z]+[0-9.+-]+)", data.replace(' ', ''))

        tool_data = {}
        for item in items:
            key = item[0]
            if key in "TPQ":
                tool_data[key] = int(item[1:])
            else:
                tool_data[key] = float(item[1:])

        TOOL_TABLE[tool_data['T']] = tool_data


def get_tool_pocket(tnum):
    """Returns the ATC pocket number a tool is in."""
    print "Get Tool Pocket", tnum, TOOL_TABLE[tnum].get('P', -1.00)
    return TOOL_TABLE[tnum].get('P', -1)


def find_open_pocket():
    """Returns the number of the first open pocket in the ATC"""
    atc_model = atc_list_model()
    try:
        # Find the first empty pocket, excluding the spindle.
        return atc_model[1:].index(None) + 1
    except KeyError:
        # No empty pockets
        return -1


def getATCInfo(option, default=0):
    return INI.find('ATC', option)


def atc_list_model():
    """Returns a list with ATC_NUM_POCKETS + 1 elements.

    Each element contains the tool number in that pocket, or None.
    Element zero represents the spindle, all other elements represent
    pockets in the ATC.
    """
    atc_model = [None] * (ATC_NUM_POCKETS + 1)
    for tnum, tdata in TOOL_TABLE.items():
        pnum = tdata['P']

        if pnum > 0 and pnum < ATC_NUM_POCKETS:
            atc_model[pnum] = tnum

    return atc_model