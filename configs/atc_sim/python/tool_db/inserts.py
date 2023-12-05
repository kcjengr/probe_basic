# coding=utf-8

from datetime import date

from probe_basic_db_tool.tool_table import ToolTable, Tool, ProbeParams
from probe_basic_db_tool.base import Session, engine, Base


Base.metadata.create_all(engine)

session = Session()



probe_params_1 = ProbeParams(
    tool_diameter_probe_mode = "0.0",
    tool_diameter_offset_mode = "0.0",
    tool_diameter = "0.0",
    tool_breakage_detection_mode = "0.0",
    tool_breakage_tolerance = "0.0"
)

probe_params_2 = ProbeParams(
    tool_diameter_probe_mode = "0.0",
    tool_diameter_offset_mode = "0.0",
    tool_diameter = "0.0",
    tool_breakage_detection_mode = "0.0",
    tool_breakage_tolerance = "0.0"
)

probe_params_3 = ProbeParams(
    tool_diameter_probe_mode = "0.0",
    tool_diameter_offset_mode = "0.0",
    tool_diameter = "0.0",
    tool_breakage_detection_mode = "0.0",
    tool_breakage_tolerance = "0.0"
)



tool_1 = Tool(
    remark = "no tool",
    tool_no = 0,
    pocket = 0,
    in_use = 0,
    x_offset = 0.0,
    y_offset = 0.0,
    z_offset = 0.0,
    a_offset = 0.0,
    b_offset = 0.0,
    c_offset = 0.0,
    i_offset = 0.0,
    j_offset = 0.0,
    q_offset = 0.0,
    u_offset = 0.0,
    v_offset = 0.0,
    w_offset = 0.0,
    diameter = 0.0
)


tool_2 = Tool(
    remark = "Example Tool 1",
    tool_no = 1,
    pocket = 0,
    in_use = 0,
    x_offset = 0.0,
    y_offset = 0.0,
    z_offset = 0.0,
    a_offset = 0.0,
    b_offset = 0.0,
    c_offset = 0.0,
    i_offset = 0.0,
    j_offset = 0.0,
    q_offset = 0.0,
    u_offset = 0.0,
    v_offset = 0.0,
    w_offset = 0.0,
    diameter = 0.0
)
tool_3 = Tool(
    remark = "Example Tool 2",
    tool_no = 2,
    pocket = 0,
    in_use = 0,
    x_offset = 0.0,
    y_offset = 0.0,
    z_offset = 0.0,
    a_offset = 0.0,
    b_offset = 0.0,
    c_offset = 0.0,
    i_offset = 0.0,
    j_offset = 0.0,
    q_offset = 0.0,
    u_offset = 0.0,
    v_offset = 0.0,
    w_offset = 0.0,
    diameter = 0.0
)

tool_table = ToolTable(name="Test Tool Table")

tool_1.tool_probe_params = [probe_params_1]
tool_2.tool_probe_params = [probe_params_2]
tool_3.tool_probe_params = [probe_params_3]

tool_table.tools = [tool_1, tool_2, tool_3]

# 9 - persists data
session.add(tool_table)

session.add(tool_1)
session.add(tool_2)
session.add(tool_3)

# 10 - commit and close session
session.commit()
session.close()
