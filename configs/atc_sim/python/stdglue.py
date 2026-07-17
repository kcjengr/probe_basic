
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
# Unified tool database: #<_current_tool_*> G-code parameters (mill flavor of
# the lathe db config's mechanism -- see configs/probe_basic_lathe_db/python/
# stdglue.py). Written directly into self.params from INSIDE change_epilog --
# this runs in the interpreter process itself, with direct parameter-table
# write access, so the parameters are correct from the instant a tool change
# commits, unconditionally, with nothing for any user or program to call.
# The mill toolchange.ngc reads #<_current_tool_atc> to decide whether the
# tool in the spindle may be auto-stowed into the ATC carousel.
#
# Deliberately isolated from the tool change's own success/failure: any
# problem here (DB missing, locked, unexpected schema) is printed and
# swallowed, never turned into an M6 failure -- this is a convenience layer
# on top of the tool change, not part of its correctness. Configs running
# the classic file-based tool table (no [EMCIO]DB_PROGRAM / no .db file)
# simply no-op here.

def _resolve_tool_db_path():
    """Same DB file qtpyvcp's DBToolTable plugin resolves (see
    qtpyvcp.plugins.db_tool_table._default_db_path): [EMCIO] TOOL_DB_FILE
    if set, else a DB_PROGRAM argument, else <config dir>/tool_table.db.
    Resolved independently here (this runs inside milltask, a separate
    process from the GUI) via INI_FILE_NAME + linuxcnc.ini() -- the same
    environment variable NGC's own #<_ini[...]> syntax relies on, always
    exported by the linuxcnc launcher script before milltask starts."""
    ini_path = os.environ.get('INI_FILE_NAME')
    if not ini_path:
        return None
    config_dir = os.path.dirname(os.path.abspath(ini_path))
    ini = linuxcnc.ini(ini_path)

    def _resolve(value):
        if not os.path.isabs(value):
            value = os.path.join(config_dir, value)
        return os.path.abspath(os.path.expanduser(value))

    tool_db_file = ini.find('EMCIO', 'TOOL_DB_FILE')
    if tool_db_file:
        return _resolve(tool_db_file)
    db_program = ini.find('EMCIO', 'DB_PROGRAM')
    if db_program:
        for arg in db_program.split()[1:]:
            if arg.lower() in ('debug', '-d', '--debug'):
                continue
            return _resolve(arg)
    return os.path.join(config_dir, 'tool_table.db')


def _numeric_tool_mill_columns(cur):
    """(name, schema default) pairs for tool_mill's numeric columns,
    discovered from the DB's own schema (PRAGMA table_info) rather than a
    hardcoded list -- self-updating if tool_mill ever grows a column. The
    DDL default matters: a tool with no tool_mill row at all must read as
    the schema default (atc DEFAULT 1 = storable), never as 0."""
    cur.execute("PRAGMA table_info(tool_mill)")
    cols = []
    for row in cur.fetchall():
        name, col_type, dflt = row[1], (row[2] or '').upper(), row[4]
        if name == 'tool_id' or 'TEXT' in col_type:
            continue
        try:
            default = float(dflt) if dflt is not None else 0.0
        except (TypeError, ValueError):
            default = 0.0
        cols.append((name, default))
    return cols


def _cast_numeric_param(raw, value_type=None):
    if raw is None:
        return 0.0
    if value_type == 'bool':
        return 1.0 if str(raw).strip().lower() in ('1', 'true', 'yes', 'y') else 0.0
    return float(raw)


def refresh_current_tool_params(self, tool_number):
    """Write #<_current_tool_<key>> for every numeric tool_mill extras
    column and numeric custom column of `tool_number`, read straight from
    the unified tool database. Text columns are skipped (RS274 has no
    string type)."""
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
            numeric_extras = _numeric_tool_mill_columns(cur)

            select_cols = ', '.join('tm.' + name for name, _ in numeric_extras)
            cur.execute(
                "SELECT t.id" + (", " + select_cols if select_cols else "") +
                " FROM tool t LEFT JOIN tool_mill tm ON tm.tool_id = t.id"
                " WHERE t.tool_no = ?",
                (tool_number,))
            row = cur.fetchone()
            if row is None:
                return
            tool_id = row[0]
            extras_values = list(zip(numeric_extras, row[1:]))

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

        for (key, default), raw in extras_values:
            if raw is None:
                value = default  # no tool_mill row yet: schema default
            else:
                value = _cast_numeric_param(raw)
            self.params['_current_tool_' + key] = value
        for name, value_type, raw in custom_rows:
            self.params['_current_tool_' + name] = _cast_numeric_param(
                raw, value_type)
    except Exception as e:
        print("refresh_current_tool_params: %s" % (e,))


def _lookup_tool_atc(tool_number):
    """Return the tool_mill.atc flag for tool_number as 1 (storable in the
    ATC carousel) or 0 (manual only -- must be hand loaded/removed).

    Defaults to 1 (storable) whenever the answer isn't an explicit atc=0:
    no tool database configured (file-based tool table configs), the tool
    is not in the database, or it has no tool_mill row yet (a freshly
    imported tool -- schema default is storable). This matches the
    "everything is storable unless you uncheck it" model of the ATC column
    everywhere else, and keeps non-DB configs behaving exactly as before
    (no tool is ever manual-only). Only an explicit atc=0 in the database
    routes a tool to the manual tool change dialog.

    Read-only, its own short-lived connection (sqlite's default busy
    timeout rides out a transient GUI write); any failure falls back to
    storable and is printed, never raised -- consistent with
    refresh_current_tool_params, a convenience layer that must never fail
    a tool change."""
    try:
        tool_number = int(tool_number)
        if tool_number <= 0:
            return 1
        ini_path = os.environ.get('INI_FILE_NAME')
        if not ini_path:
            return 1
        ini = linuxcnc.ini(ini_path)
        # Only consult a tool database when the config actually declares one
        # (a DB tool-table config sets [EMCIO] DB_PROGRAM and/or
        # TOOL_DB_FILE). A file-based tool-table config has no ATC column at
        # all, so every tool is storable -- don't let a stray tool_table.db
        # left in the config dir (e.g. from testing a DB config) silently
        # turn that into manual-only behavior.
        if not (ini.find('EMCIO', 'DB_PROGRAM') or ini.find('EMCIO', 'TOOL_DB_FILE')):
            return 1
        db_path = _resolve_tool_db_path()
        if not db_path or not os.path.isfile(db_path):
            return 1
        conn = sqlite3.connect(db_path)
        try:
            row = conn.execute(
                "SELECT tm.atc FROM tool t"
                " LEFT JOIN tool_mill tm ON tm.tool_id = t.id"
                " WHERE t.tool_no = ?", (tool_number,)).fetchone()
        finally:
            conn.close()
        if row is None or row[0] is None:
            return 1
        return 1 if int(row[0]) != 0 else 0
    except Exception as e:
        print("_lookup_tool_atc: %s" % (e,))
        return 1


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
        # ATC-storable flags for the M6 macro's stow/fetch decisions, looked
        # up per tool from the tool database's ATC column right now (not the
        # session-global #<_current_tool_atc>, which is empty until the first
        # tool change after power-up). Passed to toolchange.ngc as
        # #<spindle_tool_atc> (the tool being removed) and
        # #<selected_tool_atc> (the tool being loaded); 1 = storable in the
        # carousel, 0 = manual only.
        self.params["spindle_tool_atc"] = _lookup_tool_atc(self.current_tool)
        self.params["selected_tool_atc"] = _lookup_tool_atc(self.selected_tool)
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
            # The M6 ngc= procedure called bare M6 itself (builtin
            # behavior) -- the change is fully committed by this point, so
            # self.current_tool already reflects the new tool; the
            # parameter refresh belongs here too or that path would never
            # get it.
            refresh_current_tool_params(self, self.current_tool)
            yield INTERP_OK
        else:
            if self.return_value > 0.0:

                # commit change
                # NOTE: use the change_prolog-stashed params, not
                # self.selected_tool/selected_pocket -- toolchange.ngc runs
                # bare T words inside the remap body (they set the manual
                # tool change dialog's tool number readout), and each one
                # overwrites the interp's live selected_* state.
                new_tool_number = int(self.params["selected_tool"])
                self.selected_pocket =  int(self.params["selected_pocket"])

                if "2.9" in VERSION:
                    emccanon.CHANGE_TOOL(self.selected_pocket)
                elif "2.10" in VERSION:
                    emccanon.SELECT_TOOL(new_tool_number)
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

