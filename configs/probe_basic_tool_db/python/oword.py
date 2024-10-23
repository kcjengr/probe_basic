from qtpyvcp.lib.db_tool.base import Session
from qtpyvcp.lib.db_tool.tool_table import ToolTable, Tool, ToolProperties

def foo(*args):
    print("foo!")

    return

def tool_props(self, *args):

    # print(f"task = {self.task}")
    
    if self.task == 1:

        tool_no = args[0]
        query = self.blocks[0].comment

        print(f"Quering {query} for tool {tool_no}")
        session = Session()
        
        
        if query.split('.')[0] == "tool_properties":
            tool_data = session.query(ToolProperties).filter(ToolProperties.tool_no == tool_no).first()
        
            if tool_data is not None:
                if query.split('.')[1] == "max_rpm":
                    result = tool_data.max_rpm
                    print(f"Max RPM: {result}")
                elif query.split('.')[1] == "wear_factor":
                    result = tool_data.wear_factor
                    print(f"Wear factor: {result}")
                elif query.split('.')[1] == "bullnose_radious":
                    result = tool_data.bullnose_radious
                    print(f"Bullnose radious: {result}")
            else:
                print("NO DATA")
        elif query.split('.')[0] == "tool":
            tool_data = session.query(Tool).filter(Tool.tool_no == tool_no).first()
        
            if tool_data is not None:
                if query.split('.')[1] == "remark":
                    result = tool_data.remark
                    print(f"Remark: {result}")
                elif query.split('.')[1] == "pocket":
                    result = tool_data.pocket
                    print(f"Pocket: {result}")
                elif query.split('.')[1] == "x_offset":
                    result = tool_data.x_offset
                    print(f"x_offset: {result}")
                elif query.split('.')[1] == "y_offset":
                    result = tool_data.y_offset
                    print(f"y_offset: {result}")
                elif query.split('.')[1] == "z_offset":
                    result = tool_data.z_offset
                    print(f"z_offset: {result}")
                elif query.split('.')[1] == "a_offset":
                    result = tool_data.a_offset
                    print(f"a_offset: {result}")
                elif query.split('.')[1] == "b_offset":
                    result = tool_data.b_offset
                    print(f"b_offset: {result}")
                elif query.split('.')[1] == "c_offset":
                    result = tool_data.c_offset
                    print(f"c_offset: {result}")
                elif query.split('.')[1] == "i_offset":
                    result = tool_data.i_offset
                    print(f"i_offset: {result}")
                elif query.split('.')[1] == "j_offset":
                    result = tool_data.j_offset
                    print(f"j_offset: {result}")
                elif query.split('.')[1] == "q_offset":
                    result = tool_data.q_offset
                    print(f"q_offset: {result}")
                elif query.split('.')[1] == "u_offset":
                    result = tool_data.u_offset
                    print(f"u_offset: {result}")
                elif query.split('.')[1] == "u_offset":
                    result = tool_data.u_offset
                    print(f"v_offset: {result}")
                elif query.split('.')[1] == "w_offset":
                    result = tool_data.w_offset
                    print(f"w_offset: {result}")
                elif query.split('.')[1] == "diameter":
                    result = tool_data.diameter
                    print(f"Diameter: {result}")
                
            else:
                print("NO DATA")
                result = 0
                
            return result
        
        return