
#NOTE:
#     The legacy names *selected_pocket* and *current_pocket* actually reference
#     a sequential tooldata index for tool items loaded from a tool
#     table ([EMCIO]TOOL_TABLE) or via a tooldata database ([EMCIO]DB_PROGRAM)

# stdglue - canned prolog and epilog functions for the remappable builtin codes (T,M6,M61,S,F)
#
# we dont use argspec to avoid the generic error message of the argspec prolog and give more
# concise ones here


import os
import sqlite3

import emccanon
import linuxcnc

from linuxcnc import version
from interpreter import *
from emccanon import MESSAGE

throw_exceptions = 1

VERSION = version

# used so screens can get info.
# add this to toplevel to call it:

# import remap
# def __init__(self):
#     if self.task:
#         remap.build_hal(self)

def build_hal(self):
    import hal
    try:
        h=hal.component('remapStat')
        h.newpin("tool", hal.HAL_S32, hal.HAL_OUT)
        h.newpin("wear", hal.HAL_S32, hal.HAL_OUT)
        h.ready()
        self.hal_tool_comp = h
    except Exception as e:
        print(e)

# REMAP=T   prolog=prepare_prolog ngc=prepare epilog=prepare_epilog
# exposed parameters: #<tool> #<pocket>

def prepare_prolog(self,**words):
    try:
        cblock = self.blocks[self.remap_level]
        if not cblock.t_flag:
            self.set_errormsg("T requires a tool number")
            return INTERP_ERROR
        tool  = cblock.t_number
        if tool:
            (status, pocket) = self.find_tool_pocket(tool)
            if status != INTERP_OK:
                self.set_errormsg("T%d: pocket not found" % (tool))
                return status
        else:
            pocket = -1 # this is a T0 - tool unload
        self.params["tool"] = tool
        self.params["pocket"] = pocket
        return INTERP_OK
    except Exception as e:
        self.set_errormsg("T%d/prepare_prolog: %s" % (int(words['t']), e))
        return INTERP_ERROR

def prepare_epilog(self, **words):
    try:
        if not self.value_returned:
            r = self.blocks[self.remap_level].executing_remap
            self.set_errormsg("the %s remap procedure %s did not return a value"
                             % (r.name,r.remap_ngc if r.remap_ngc else r.remap_py))
            return INTERP_ERROR
        if self.blocks[self.remap_level].builtin_used:
            #print "---------- T builtin recursion, nothing to do"
            return INTERP_OK
        else:
            if self.return_value > 0:
                self.selected_tool = int(self.params["tool"])
                self.selected_pocket = int(self.params["pocket"])
                emccanon.SELECT_TOOL(self.selected_tool)
                return INTERP_OK
            else:
                self.set_errormsg("T%d: aborted (return code %.1f)" % (int(self.params["tool"]),self.return_value))
                return INTERP_ERROR
    except Exception as e:
        self.set_errormsg("T%d/prepare_epilog: %s" % (tool,e))
        return INTERP_ERROR

# REMAP=M6  modalgroup=6 prolog=change_prolog ngc=change epilog=change_epilog
# exposed parameters:
#    #<tool_in_spindle>
#    #<selected_tool>
#    #<current_pocket>
#    #<selected_pocket>

# ---------------------------------------------------------------------------
# Unified tool database: #<_current_tool_*> G-code parameters (plan §6 Phase
# 3/6 follow-up, Chris 2026-07-06/08). Written directly into self.params from
# INSIDE change_epilog -- this runs in the interpreter process itself, with
# direct parameter-table write access (the same mechanism this file already
# uses for tool_in_spindle/selected_tool/etc. above), so there is no gap at
# all: not the mid-program-M6 case that an earlier MDI-based approach
# (o<tool_data> call, retired) couldn't reach. By the time this runs the new
# tool has just been committed, so the parameters are correct from that
# instant on, unconditionally, with nothing for any user or program to call.
#
# Deliberately isolated from the tool change's own success/failure: any
# problem here (DB missing, locked, unexpected schema) is printed and
# swallowed, never turned into an M6 failure -- this is a convenience layer
# on top of the tool change, not part of its correctness.

def _resolve_tool_db_path():
    """Same DB file qtpyvcp's DBToolTable plugin resolves (see
    qtpyvcp.plugins.db_tool_table._default_db_path): [EMCIO] DB_PROGRAM's
    first non-flag argument, else <config dir>/tool_table.db. Resolved
    independently here (this runs inside milltask, a separate process
    from the GUI) via INI_FILE_NAME + linuxcnc.ini() -- the same
    environment variable NGC's own #<_ini[...]> syntax relies on, always
    exported by the linuxcnc launcher script before milltask starts."""
    ini_path = os.environ.get('INI_FILE_NAME')
    if not ini_path:
        return None
    config_dir = os.path.dirname(os.path.abspath(ini_path))
    ini = linuxcnc.ini(ini_path)
    db_program = ini.find('EMCIO', 'DB_PROGRAM')
    if db_program:
        for arg in db_program.split()[1:]:
            if arg.lower() in ('debug', '-d', '--debug'):
                continue
            if not os.path.isabs(arg):
                arg = os.path.join(config_dir, arg)
            return os.path.abspath(os.path.expanduser(arg))
    return os.path.join(config_dir, 'tool_table.db')


def _numeric_tool_lathe_columns(cur):
    """Extras columns to publish, discovered from the DB's own schema
    (PRAGMA table_info) rather than a hardcoded list -- self-updating if
    tool_lathe ever grows a column, matching how the retired
    tool_data_sub generator derived this from the ORM column types."""
    cur.execute("PRAGMA table_info(tool_lathe)")
    return [row[1] for row in cur.fetchall()
            if row[1] != 'tool_id' and 'TEXT' not in (row[2] or '').upper()]


def _cast_numeric_param(raw, value_type=None):
    if raw is None:
        return 0.0
    if value_type == 'bool':
        return 1.0 if str(raw).strip().lower() in ('1', 'true', 'yes', 'y') else 0.0
    return float(raw)


def refresh_current_tool_params(self, tool_number):
    """Write #<_current_tool_<key>> for every numeric extras/custom
    column of `tool_number`, read straight from the unified tool
    database. Text columns are skipped (RS274 has no string type)."""
    try:
        tool_number = int(tool_number)
        if tool_number <= 0:
            return
        db_path = _resolve_tool_db_path()
        if not db_path or not os.path.isfile(db_path):
            return

        conn = sqlite3.connect(db_path)
        try:
            cur = conn.cursor()
            numeric_extras = _numeric_tool_lathe_columns(cur)

            select_cols = ', '.join('tl.' + c for c in numeric_extras)
            cur.execute(
                "SELECT t.id" + (", " + select_cols if select_cols else "") +
                " FROM tool t LEFT JOIN tool_lathe tl ON tl.tool_id = t.id"
                " WHERE t.tool_no = ?",
                (tool_number,))
            row = cur.fetchone()
            if row is None:
                return
            tool_id = row[0]
            extras_values = dict(zip(numeric_extras, row[1:]))

            cur.execute(
                "SELECT d.name, d.value_type, v.value"
                " FROM custom_field_def d"
                " LEFT JOIN custom_field_value v"
                "   ON v.field_id = d.id AND v.tool_id = ?"
                " WHERE d.value_type IN ('float', 'int', 'bool')",
                (tool_id,))
            custom_rows = cur.fetchall()
        finally:
            conn.close()

        for key, raw in extras_values.items():
            self.params['_current_tool_' + key] = _cast_numeric_param(raw)
        for name, value_type, raw in custom_rows:
            self.params['_current_tool_' + name] = _cast_numeric_param(
                raw, value_type)
    except Exception as e:
        print("refresh_current_tool_params: %s" % (e,))


def change_prolog(self, **words):
    try:
        # this is relevant only when using iocontrol-v2.
        hard_fault_flag = 0.0
        hard_fault_code = 0.0
        try:
            hard_fault_flag = float(self.params[5600])
            hard_fault_code = float(self.params[5601])
        except KeyError:
            pass

        if hard_fault_flag > 0.0:
            if hard_fault_code < 0.0:
                self.set_errormsg("Toolchanger hard fault %d" % (int(hard_fault_code)))
                return INTERP_ERROR
            print("change_prolog: Toolchanger soft fault %d" % int(hard_fault_code))

        if self.selected_pocket < 0:
            self.set_errormsg("M6: no tool prepared")
            return INTERP_ERROR
        if self.cutter_comp_side:
            self.set_errormsg("Cannot change tools with cutter radius compensation on")
            return INTERP_ERROR
        self.params["tool_in_spindle"] = self.current_tool
        self.params["selected_tool"] = self.selected_tool
        self.params["current_pocket"] = self.current_pocket
        self.params["selected_pocket"] = self.selected_pocket
        return INTERP_OK
    except Exception as e:
        self.set_errormsg("M6/change_prolog: %s" % (e))
        return INTERP_ERROR

def change_epilog(self, **words):
    try:
        if not self.value_returned:
            r = self.blocks[self.remap_level].executing_remap
            self.set_errormsg("the %s remap procedure %s did not return a value"
                             % (r.name,r.remap_ngc if r.remap_ngc else r.remap_py))
            yield INTERP_ERROR
        # this is relevant only when using iocontrol-v2.
        hard_fault_flag = 0.0
        hard_fault_code = 0.0
        try:
            hard_fault_flag = float(self.params[5600])
            hard_fault_code = float(self.params[5601])
        except KeyError:
            pass

        if hard_fault_flag > 0.0:
            if hard_fault_code < 0.0:
                self.set_errormsg("Toolchanger hard fault %d" % (int(hard_fault_code)))
                yield INTERP_ERROR
            print("change_epilog: Toolchanger soft fault %d" % int(hard_fault_code))

        if self.blocks[self.remap_level].builtin_used:
            # The M6 ngc= procedure called bare M6 itself -- "use builtin
            # behavior" (manual tool change prompt, or stock random-
            # toolchanger handling; whatever this machine's ngc=
            # procedure falls through to when it doesn't implement its
            # own ATC-specific commit). This is the path most probe_basic
            # lathe configs actually take (Chris, 2026-07-08: only
            # machines with a real turret/carousel should get custom
            # carousel logic; manual tool change is the common case and
            # must keep its exact previous behavior). The builtin path
            # has already fully committed the tool change by this point,
            # so self.current_tool already reflects the new tool -- the
            # parameter refresh belongs here too, not just in the custom
            # ATC commit branch below, or manual-tool-change configs
            # would never get it at all.
            refresh_current_tool_params(self, self.current_tool)
            yield INTERP_OK
        else:
            if self.return_value > 0.0:

                # commit change

                new_tool_number = self.selected_tool  # captured before reset below

                self.selected_pocket =  int(self.params["selected_pocket"])

                if "2.9" in VERSION:
                    emccanon.CHANGE_TOOL(self.selected_pocket)
                elif "2.10" in VERSION:
                    emccanon.SELECT_TOOL(self.selected_tool)
                    emccanon.CHANGE_TOOL()

                self.current_pocket = self.selected_pocket
                self.selected_pocket = -1
                self.selected_tool = -1
                # cause a sync()
                self.set_tool_parameters()
                refresh_current_tool_params(self, new_tool_number)
                self.toolchange_flag = True
                yield INTERP_EXECUTE_FINISH
            else:
                # yield to print any messages from the NGC program
                yield INTERP_EXECUTE_FINISH
                self.set_errormsg("M6 aborted (return code %.1f)" % (self.return_value))
                yield INTERP_ERROR
    except Exception as e:
        self.set_errormsg("M6/change_epilog: %s" % (e))
        yield INTERP_ERROR

