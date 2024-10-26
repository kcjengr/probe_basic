from qtpyvcp.lib.db_tool.base import Session
from qtpyvcp.lib.db_tool.tool_table import ToolTable, Tool, ToolProperties


def tool_db(self, *args):

    # # print(f"task = {self.task}")
    
    if self.task == 1:
        pass
    
    
    tool_no = args[0]
    query = self.blocks[0].comment
    # result = 0

    # # print(f"Quering {query} for tool {tool_no}")
    session = Session()
    
    table = query.split('.')[0]
    column = query.split('.')[1]
    
    if table == "tool_properties":
        tool_data = session.query(ToolProperties).filter(ToolProperties.tool_no == tool_no).first()
    
        if tool_data is not None:
            return getattr(tool_data, column, None)
        

    elif table == "tool":
        tool_data = session.query(Tool).filter(Tool.tool_no == tool_no).first()
    
        if tool_data is not None:
            return getattr(tool_data, column, None)

