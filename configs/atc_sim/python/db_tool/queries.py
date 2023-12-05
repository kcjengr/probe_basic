# coding=utf-8

from probe_basic_db_tool.tool_table import ToolTable, Tool
from probe_basic_db_tool.base import Session

session = Session()

tool_tables = session.query(ToolTable).all()

for tool_table in tool_tables:
    for tools in tool_table.tools:
        print(tools.id, tools.remark, tools.x_offset, tools.y_offset)
        
session.close()
