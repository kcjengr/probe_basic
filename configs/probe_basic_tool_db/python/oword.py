from qtpyvcp.lib.db_tool.base import Session
from qtpyvcp.lib.db_tool.tool_table import ToolTable, Tool, ToolModel

def foo(*args):
    print("foo!")

    return

def tool_props(self, *args):

    tool_no = args[0]
    query = self.blocks[0].comment

    print(f"task = {self.task}")
    print(f"ASKING FOR TOOL = {tool_no} IN {query}")

    # if self.task:

    session = Session()
    tool_data = session.query(ToolModel).filter(ToolModel.tool_no == tool_no).first()

    if tool_data is not None:
        print(tool_data.model)
    else:
        print("NO DATA")

    return