# coding=utf-8
"""MillToolTable -- mill flavor of the unified tool table widget.

The same editing surface as LatheToolTable (core tool-table columns +
machine extras + user-defined custom columns, one Save action), with the
lathe-specific configuration -- insert/holder vocabularies, the tool_lathe
extras set -- swapped for the mill's. All the logic lives in
widgets.lathe_tool_table; this module only overrides the machine-flavor
class attributes those classes consult.

Mill extras today is a single column, ATC (tool_mill.atc, schema v3 --
qtpyvcp migrations/003_tool_mill.sql): a per-tool boolean for whether the
tool is physically storable in the ATC carousel. False marks an oversize
tool the M6 remap must never auto-stow into (or auto-fetch from) the
carousel -- it gets the manual tool change dialog instead. The value is
published to G-code as #<_current_tool_atc> by the config's
change_epilog (python/stdglue.py: refresh_current_tool_params) whenever a
tool change commits.

Pairs with the DBToolTable plugin configured for the mill extras table:

.. code-block:: yaml

    data_plugins:
      tooltable:
        provider: qtpyvcp.plugins.db_tool_table:DBToolTable
        kwargs:
          columns: {{ ini.DISPLAY.tool_table_columns }}
          extras: mill

Against the classic file-based tool_table plugin (every non-DB mill
config) it degrades exactly like LatheToolTable does: core columns only,
no extras/custom -- same editing behavior the stock qtpyvcp ToolTable
widget gave, so promoting it in probe_basic.ui is safe for all configs.
"""

from widgets.lathe_tool_table.lathe_tool_model import LatheToolModel
from widgets.lathe_tool_table.lathe_tool_table import LatheToolTable


class MillToolModel(LatheToolModel):

    EXTRAS_LABELS = {'atc': 'ATC'}
    TEXT_EXTRAS = frozenset()
    BOOL_EXTRAS = frozenset(('atc',))
    # A tool with no tool_mill row yet reads as storable -- matches the
    # schema default (003_tool_mill.sql: atc DEFAULT 1) and the established
    # all-tools-automatic behavior: only the oversize exceptions get
    # unchecked, a blank cell never silently means "manual only".
    EXTRAS_DEFAULTS = {'atc': True}
    DEFAULT_VISIBLE_EXTRAS = ['atc']
    STRICT_ENUM_OPTIONS = {}
    OPEN_VOCAB_SEED_OPTIONS = frozenset()
    EXTRAS_GROUP_LABEL = 'Mill Extras'
    # Remark renders last, so ATC (and any future mill extras) sit between
    # the numeric offset columns and the wide free-text Remark column.
    TRAILING_CORE_COLUMNS = ('R',)


class MillToolTable(LatheToolTable):

    MODEL_CLASS = MillToolModel
