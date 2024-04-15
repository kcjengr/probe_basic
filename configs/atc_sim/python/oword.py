# coding=utf-8

#   This is a component of LinuxCNC
#   Copyright 2011, 2013 Dewey Garrett <dgarrett@panix.com>, Michael
#   Haberler <git@mah.priv.at>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

# from pprint import pprint

from utils import _read_store_file, _store_pocket, _store_spindle

from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)


def pocket_content(self, pocket_num):
    storage = _read_store_file()
    index = int(pocket_num)
    tool = storage.get("pockets")[index]

    LOG.debug(f"Pocket Numer {pocket_num} contains tool {tool}")

    return float(tool)


def spindle_spindle(self, spindle_num):
    storage = _read_store_file()
    tool = int(storage.get("spindle"))

    LOG.debug(f"Spindle Numer {spindle_num} contains tool {tool}")

    return float(tool)


def store_spindle(self, tool):
    _store_spindle(tool)


def store_pocket(self, pocket, tool):
    _store_pocket(pocket, tool)


# def toolparams(self, *args):
#     print("number of parameters passed:", len(args))
#     for a in args:
#         print(a)
#
#


    # session = Session()
    #
    # tool_tables = session.query(ToolTable).all()
    #
    # for tool_table in tool_tables:
    #     for tool in tool_table.tools:
    #
    #         tool_no = tool.tool_no
    #
    #         if tool_no == int(args[0]):
    #
    #             tool_x_offset = tool.x_offset
    #             tool_y_offset = tool.y_offset
    #             tool_z_offset = tool.z_offset
    #             tool_diameter = tool.diameter
    #
    #             tool_remark = tool.remark
    #
    #             print("###################################################")
    #             print(f"TOOL No: {tool_no} Offsets: X-{tool_x_offset} Y-{tool_y_offset} Z-{tool_z_offset} Diamteter: {tool_diameter} Description: {tool_remark}")
    #
    #             if len(tool.probe_params) > 0:
    #                 tool_diameter_probe_mode = tool.probe_params[0].tool_diameter_probe_mode
    #                 tool_diameter_offset_mode = tool.probe_params[0].tool_diameter_offset_mode
    #                 tool_diameter2 = tool.probe_params[0].tool_diameter
    #                 tool_breakage_detection_mode = tool.probe_params[0].tool_breakage_detection_mode
    #                 tool_breakage_tolerance = tool.probe_params[0].tool_breakage_tolerance
    #
    #                 print(f"probe params 1: diamerer mode {tool_diameter_probe_mode}")
    #                 print(f"probe params 2: diameter offset {tool_diameter_offset_mode}")
    #                 print(f"probe params 3: diamerer {tool_diameter2}")
    #                 print(f"probe params 4: breakage detection {tool_breakage_detection_mode}")
    #                 print(f"probe params 5: breakage tolerance {tool_breakage_tolerance}")
    #
    #                 self.params["_tool_diameter_probe_mode"] = float(tool_diameter_probe_mode)
    #                 self.params["_tool_diameter_offset_mode"] = float(tool_diameter_offset_mode)
    #                 self.params["_tool_diameter2"] = float(tool_diameter2)
    #                 self.params["_tool_breakage_detection_mode"] = float(tool_breakage_detection_mode)
    #                 self.params["_tool_breakage_tolerance"] = float(tool_breakage_tolerance)
    #
    #             else:
    #                 print("NO Tool Probe Params")
    #
    #
    #             print("###################################################")
    #
    #
    # session.close()
