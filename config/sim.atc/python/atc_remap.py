import os
import re
import sys
import emccanon
from linuxcnc import ini
from interpreter import *

throw_exceptions = 1

print "\n****** atc_remap initializing ******"

INI_FILE = os.environ['INI_FILE_NAME']
CONFIG_DIR = os.environ.get('CONFIG_DIR') or os.path.dirname(INI_FILE)

INI = ini(INI_FILE)

fname = INI.find('EMCIO', 'TOOL_TABLE')
TOOL_TABLE_FILE = os.path.realpath(os.path.join(CONFIG_DIR, fname))

ATC_NUM_POCKETS = int(INI.find("ATC", 'NUM_POCKETS') or 0)


CACHE_TOOL_TABLE = True
TOOL_TABLE_CACHE = None
TOOL_TABLE_DATA_COLUMNS = ''

COLUMN_LABELS = {
    'A': 'A Offset',
    'B': 'B Offset',
    'C': 'C Offset',
    'D': 'Diameter',
    'I': 'Fnt Ang',
    'J': 'Bak Ang',
    'P': 'Pocket',
    'Q': 'Orient',
    'R': 'Remark',
    'T': 'Tool',
    'U': 'U Offset',
    'V': 'V Offset',
    'W': 'W Offset',
    'X': 'X Offset',
    'Y': 'Y Offset',
    'Z': 'Z Offset',
}


def _read_tool_table(force_read=False):
    """Read tool table and return a dict of dicts of tool data."""

    global TOOL_TABLE_CACHE, TOOL_TABLE_DATA_COLUMNS
    if TOOL_TABLE_CACHE and CACHE_TOOL_TABLE and not force_read:
        print "using cached tool table"
        return TOOL_TABLE_CACHE

    print "reading tool table file"
    with open(TOOL_TABLE_FILE, 'r') as fh:
        lines = fh.readlines()

    tool_table = {}
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

            if key not in TOOL_TABLE_DATA_COLUMNS:
                TOOL_TABLE_DATA_COLUMNS += key

        tool_data['R'] = remark

        tool_table[tool_data['T']] = tool_data

    TOOL_TABLE_CACHE = tool_table
    return tool_table


def _update_tool_table(tnum, key, value):
    tool_table = _read_tool_table()
    tool_table[tnum][key] = value

    global TOOL_TABLE_CACHE
    TOOL_TABLE_CACHE.update(tool_table)


def _write_tool_table():
    """Write tooltable data to file.

    Args:
        tool_table (dict) : Dictionary of dictionaries containing
            the tool data to write to the file.
    """

    tool_table = _read_tool_table()
    lines = []

    # create the table header
    items = []
    for col in 'TPXYZABCUVWDIJQR':
        if col not in TOOL_TABLE_DATA_COLUMNS:
            continue

        if col == 'R':
            continue
        w = (6 if col in 'TPQ' else 12) - \
            (1 if col == 'T' else 0)
        items.append('{:<{w}}'.format(COLUMN_LABELS[col], w=w))

    items.append('Remark')
    lines.append(';' + ' '.join(items))

    # add the tools
    for tool_num in sorted(tool_table.iterkeys()):
        items = []
        tool_data = tool_table[tool_num]

        for col in 'TPXYZABCUVWDIJQR':
            if col not in TOOL_TABLE_DATA_COLUMNS:
                continue

            if col == 'R':
                continue
            if col in 'TPQ':
                items.append('{col}{val:<6}'
                             .format(col=col,
                                     val=tool_data.get(col, 0)))
            else:
                items.append('{col}{val:<+12.6f}'
                             .format(col=col,
                                     val=tool_data.get(col, 0.0)))

        comment = tool_data.get('R', '').strip()
        if comment is not '':
            items.append('; ' + comment)

        lines.append(''.join(items))

    # for line in lines:
    #     print line

    # write to file
    with open(TOOL_TABLE_FILE, 'w') as fh:
        fh.write('\n'.join(lines))
        fh.write('\n')  # new line at end of file
        fh.flush()
        os.fsync(fh.fileno())


def _find_tool_pocket(tnum):
    """Returns the pocket the specified tool is in."""
    tool_table = _read_tool_table()
    print "Find tool pocket", tnum, tool_table[tnum].get('P', -1.00)
    return tool_table[tnum].get('P', -1)


def _find_open_pocket():
    """Returns the number of the first open pocket in the ATC"""
    atc_model = _atc_list_model()
    try:
        # Find the first empty pocket, excluding the spindle.
        return atc_model[1:].index(None) + 1
    except KeyError:
        # No empty pockets
        return -1


def _atc_list_model():
    """Returns a list with ATC_NUM_POCKETS + 1 elements.

    Each element contains the tool number in that pocket, or None.
    Element zero represents the spindle, all other elements represent
    pockets in the ATC.
    """
    atc_model = [None] * (ATC_NUM_POCKETS + 1)
    for tnum, tdata in _read_tool_table().items():
        pnum = tdata['P']

        if pnum > 0 and pnum < ATC_NUM_POCKETS:
            atc_model[pnum] = tnum

    return atc_model


def prepare_prolog(self, **words):

    # update the cached tool table data
    _read_tool_table(force_read=True)


    cblock = self.blocks[self.remap_level]
    if not cblock.t_flag:
        self.set_errormsg("T word requires a tool number")
        return INTERP_ERROR

    tnum = cblock.t_number

    try:
        print 'T%d prepare_prolog' % tnum
        if tnum:
            pnum = _find_tool_pocket(tnum)
            if pnum == -1:
                self.set_errormsg("T%d: tool not available" % tnum)
                return INTERP_ERROR
            elif pnum == -2:
                self.set_errormsg("T%d: tool in external rack" % tnum)
                return INTERP_ERROR
        else:
            pnum = -1 # this is a T0 - tool unload

        # These variables will be visible in the ngc oword sub
        # as #<selected_tool> and #<selected_pocket> local variables,
        # and can be modified there. The epilog will retrieve and commit
        # any changes to the values.
        self.params["selected_tool"] = tnum
        self.params["selected_pocket"] = pnum

        self.params["current_tool"] = self.current_tool
        print "param", self.params[5171]
        self.params["current_pocket"] = self.params[5171]

        self.params["open_pocket"] = _find_open_pocket()

        return INTERP_OK

    except Exception, e:
        self.set_errormsg("T%d prepare_prolog: %s" % (tnum, e))
        return INTERP_ERROR


def prepare_epilog(self, **words):
    try:
        if self.return_value > 0:
            self.selected_tool = int(self.params["selected_tool"])
            self.selected_pocket = int(self.params["selected_pocket"])
            emccanon.SELECT_POCKET(self.selected_pocket, self.selected_tool)
            return INTERP_OK
        else:
            return "T%d: aborted (return code %.1f)" % (int(self.params["selected_tool"]), self.return_value)

    except Exception, e:
        return "T%d prepare_epilog: %s" % (int(self.params["selected_tool"]), e)


def change_prolog(self, **words):
    try:
        if self.selected_pocket < 0:
            self.set_errormsg("M6 prolog: No tool prepared")
            return INTERP_ERROR

        if self.cutter_comp_side:
            self.set_errormsg("M6 prolog: Cannot change tool with radius compensation on")
            return INTERP_ERROR

        self.params["atc_open_pocket"] = _find_open_pocket()
        self.params["atc_num_pockets"] = ATC_NUM_POCKETS

        self.params["current_tool"] = self.current_tool
        self.params["current_pocket"] = self.params[5171]
        self.params["selected_tool"] = self.selected_tool
        self.params["selected_pocket"] = self.selected_pocket

        self.params["stored_tool"] = self.selected_tool
        self.params["stored_pocket"] = self.params["atc_open_pocket"]

        return INTERP_OK

    except Exception, e:
        self.set_errormsg("M6 prolog: %s" % e)
        return INTERP_ERROR


def change_epilog(self, **words):
    try:
        if self.return_value > 0.0:
            # commit change

            print "current tool", self.current_tool
            _update_tool_table(int(self.params['stored_tool']), 'P', int(self.params['stored_pocket']))
            _update_tool_table(self.selected_tool, 'P', 0)
            _write_tool_table()

            self.current_tool = int(self.params['current_tool'])
            # self.current_pocket = self.params['stored_pocket']

            self.selected_tool = int(self.params["selected_tool"])
            self.selected_pocket = int(self.params["selected_pocket"])

            print "Tool", self.selected_tool
            print "Pocket", self.selected_pocket
            self.params["tool_in_spindle"] = self.selected_tool

            # emccanon.CHANGE_TOOL(self.current_tool)
            # # cause a sync()
            # self.tool_change_flag = True
            # self.set_tool_parameters()

            return INTERP_OK
        else:
            return "M6 aborted (return code %.1f)" % self.return_value

    except Exception, e:
        self.set_errormsg("M6 epilog: %s" % e)
        return INTERP_ERROR
