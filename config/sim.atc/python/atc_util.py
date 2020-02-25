
import os
import re

from linuxcnc import ini

INI_FILE = os.environ['INI_FILE_NAME']
CONFIG_DIR = os.environ.get('CONFIG_DIR') or os.path.dirname(INI_FILE)

INI = ini(INI_FILE)

fname = INI.find('EMCIO', 'TOOL_TABLE')
TOOL_TABLE_FILE = os.path.realpath(os.path.join(CONFIG_DIR, fname))

TOOL_TABLE = {}

print "****** atc_util initialization finished ******"

def readToolTable():
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

def getToolPocket(tnum):
    print "Get Tool Pocket", tnum, TOOL_TABLE[tnum].get('P', -1.00)
    return TOOL_TABLE[tnum].get('P', -1.00)
