# coding=utf-8
"""LatheToolTable -- lathe flavor of qtpyvcp's unified tool table editor.

All the mechanism (header/cell context menus, item delegate, column
stretch behavior, save/load/add/delete slots) lives in
``qtpyvcp.widgets.input_widgets.tool_table_editor.ToolTableEditor``; this
module only points it at the lathe's model. Keeps the same public slot
surface as qtpyvcp's stock ``qtpyvcp.widgets.input_widgets.tool_table.ToolTable``
(saveToolTable/loadToolTable/addTool/deleteSelectedTool/...) so it can
promote the existing ``tooltable`` object in probe_basic_lathe.ui without
changing any `.ui` signal/slot wiring -- only the promoted class changes.
"""

from qtpyvcp.widgets.input_widgets.tool_table_editor import ToolTableEditor

from .lathe_tool_model import LatheToolModel


class LatheToolTable(ToolTableEditor):

    # Machine variants subclass and point this at their model (see
    # widgets.mill_tool_table.MillToolTable).
    MODEL_CLASS = LatheToolModel
