#!/usr/bin/env python3

import os
import sys
import re

from tooldb import tooldb_callbacks # functions (g,p,l,u)
from tooldb import tooldb_tools     # list of tool numbers
from tooldb import tooldb_loop      # main loop

from qtpyvcp.lib.db_tool.base import Session, Base, engine
from qtpyvcp.lib.db_tool.tool_table import ToolTable, Tool

# Catch unhandled exceptions
def excepthook(exc_type, exc_msg, exc_tb):
    print(exc_type, file=sys.stderr)
    print(exc_msg, file=sys.stderr)
    print(exc_tb, file=sys.stderr)


sys.excepthook = excepthook


class DataBaseManager():
    def __init__(self):
        super(DataBaseManager, self).__init__()
        self.session = None
        
        Base.metadata.create_all(engine)
        
        self.session = Session()
        
        tools = self.session.query(Tool).all()
        tool_list = list()

        for tool in tools:
            tool_list.append(tool.tool_no)
    
        tooldb_tools(tool_list)
        tooldb_callbacks(self.user_get_tool,
                         self.user_put_tool,
                         self.user_load_spindle,
                         self.user_unload_spindle)
            
        
        self.tool_list = tool_list
        
        self.tools = dict()

  
    def close(self):
        self.session.close()

    def user_get_tool(self, tool_no):
        print(f"GET tool {tool_no}", file = sys.stderr)

        tool = self.session.query(Tool).filter(Tool.tool_no == tool_no).one()
        
        data = [f"T{tool.tool_no}",
                f"P{tool.pocket}",
                f"D{tool.diameter}",
                f"X{tool.x_offset}",
                f"Y{tool.y_offset}",
                f"Z{tool.z_offset}",
                f"A{tool.a_offset}",
                f"B{tool.b_offset}",
                f"C{tool.c_offset}",
                f"U{tool.u_offset}",
                f"V{tool.v_offset}",
                f"W{tool.w_offset}"]

        return " ".join(data)


    def user_put_tool(self, toolno, params):
        print(f"PUT tool {toolno} {params}", file=sys.stderr)
        
        tool = self.session.query(Tool).filter(Tool.tool_no==toolno).one()
        params_list = re.split(r'   | |;', params)
        
        tool_dict = dict()
        
        for param in params_list:
            column = param[0]
            value = param[1::]
            tool_dict[column] = value

        tool.tool_no = tool_dict.get("T")
        tool.pocket = tool_dict.get("P")
        tool.x_offset = tool_dict.get("X")
        tool.y_offset = tool_dict.get("Y")
        tool.z_offset = tool_dict.get("Z")
        tool.a_offset = tool_dict.get("A")
        tool.b_offset = tool_dict.get("B")
        tool.c_offset = tool_dict.get("C")
        tool.i_offset = tool_dict.get("I")
        tool.j_offset = tool_dict.get("J")
        tool.q_offset = tool_dict.get("Q")
        tool.u_offset = tool_dict.get("U")
        tool.v_offset = tool_dict.get("V")
        tool.w_offset = tool_dict.get("W")
        tool.diameter = tool_dict.get("D")
        
        self.session.commit()

    
    def user_load_spindle(self, toolno, params):
        print(f"LOAD SPINDLE {toolno} {params}", file=sys.stderr)
        #
        # tno = int(toolno)
        #
        # TMP = toolline_to_dict(params,['T','P'])
        # if TMP['P'] != "0": umsg("user_load_spindle_nonran_tc P=%s\n"%TMP['P'])
        # if tno      ==  0:  umsg("user_load_spindle_nonran_tc tno=%d\n"%tno)
        #
        # # save restore_pocket as pocket may have been altered by apply_db_rules()
        # D   = toolline_to_dict(self.tools[tno],all_letters)
        # restore_pocket[tno] = D['P']
        # D['P'] = "0"
        #
        # if p0tool != -1:  # accrue time for prior tool:
        #     stop_tool_timer(p0tool)
        #     RESTORE = toolline_to_dict(self.tools[p0tool],all_letters)
        #     RESTORE['P'] = restore_pocket[p0tool]
        #     self.tools[p0tool] = dict_to_toolline(RESTORE,all_letters)
        #
        # p0tool = tno
        # D['T'] = str(tno)
        # D['P'] = "0"
        # start_tool_timer(p0tool)
        # self.tools[tno] = dict_to_toolline(D,all_letters)
        # save_tools_to_file(db_savefile)
    
    def user_unload_spindle(self, toolno, params):
        print(f"UNLOAD SPINDLE {toolno} {params}", file=sys.stderr)
        #
        # tno = int(toolno)
        #
        # if p0tool == -1: return # ignore
        # TMP = toolline_to_dict(params,['T','P'])
        # if tno       !=  0:  umsg("user_unload_spindle_nonran_tc tno=%d\n"%tno)
        # if TMP['P']  != "0": umsg("user_unload_spindle_nonran_tc P=%s\n"%TMP['P'])
        #
        # stop_tool_timer(p0tool)
        # D = toolline_to_dict(self.tools[p0tool],all_letters)
        # D['T'] = str(p0tool)
        # D['P'] = restore_pocket[p0tool]
        # self.tools[p0tool] = dict_to_toolline(D,all_letters)
        #
        # p0tool = -1
        # save_tools_to_file(db_savefile)


def main():
    
    tool_db_man = DataBaseManager()
    
    try:
        tooldb_loop()  # loop forever, use callbacks
    except Exception as e:
        print(f"Exception = {e}", file=sys.stderr)
    
    tool_db_man.close()

if __name__ == "__main__":
    main()
