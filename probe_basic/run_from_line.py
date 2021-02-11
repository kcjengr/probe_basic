#!/usr/bin/env python

import os
import shutil
import subprocess

import linuxcnc
import gcode

from qtpyvcp.widgets.dialogs.base_dialog import BaseDialog
from qtpyvcp import plugins

from qtpyvcp.widgets.display_widgets.vtk_backplot.base_canon import BaseCanon


STATUS = plugins.status.Status()

# Temporarily removed requirement for INI and var
# def getEndState(ngc, toolTbl, INI, var, endLine):

class ParseCanon(BaseCanon):

    
    def change_tool(self, pocket):
        print("CHANGE TOOL", pocket)

    def check_abort(self):
        print("ABORT")

    def add_path_point(self, line_type, start_point, end_point):
        print("LINE", line_type, start_point, end_point)

    def comment(self, msg):
        print("COMMENT", msg)

    def message(self, msg):
        print("MESSAGE", message)

    def next_line(self, state):
        # state attributes
        # 'block', 'cutter_side', 'distance_mode', 'feed_mode', 'feed_rate',
        # 'flood', 'gcodes', 'mcodes', 'mist', 'motion_mode', 'origin', 'units',
        # 'overrides', 'path_mode', 'plane', 'retract_mode', 'sequence_number',
        # 'speed', 'spindle', 'stopping', 'tool_length_offset', 'toolchange',

        print("NEXT LINE")
        
        print('block', state.block)
        print('cutter_side', state.cutter_side)
        print('distance_mode', state.distance_mode)
        print('feed_mode', state.feed_mode)
        print('feed_rate', state.feed_rate)
        print('flood', state.flood)
        print('gcodes', state.gcodes)
        print('mcodes', state.mcodes)
        print('mist', state.mist)
        print('motion_mode', state.motion_mode)
        print('origin', state.origin)
        print('units', state.units)
        print('overrides', state.overrides)
        print('path_mode', state.path_mode)
        print('plane', state.plane)
        print('retract_mode', state.retract_mode)
        print('sequence_number', state.sequence_number)
        print('speed', state.speed)
        print('spindle', state.spindle)
        print('stopping', state.stopping)
        print('tool_length_offset', state.tool_length_offset)
        print('toolchange', state.toolchange)



class RFLDialog(BaseDialog):
    def __init__(self):
        super(RFLDialog, self).__init__(stay_on_top=True, ui_file=os.path.join(os.path.dirname(__file__), 'run_from_line_dialog.ui'))
        
        inifile = os.getenv("INI_FILE_NAME")
        
        self.config_dir = os.path.dirname(inifile)
        
        self.ini = linuxcnc.ini(inifile)
        self.stat = linuxcnc.stat()
        
        temp = self.ini.find("RS274NGC", "PARAMETER_FILE") or "linuxcnc.var"
        
        self.parameter_file = os.path.join(self.config_dir, temp)
        self.temp_parameter_file = os.path.join(self.parameter_file + '.temp')
        
        self.canon = None
        self.canon_class = ParseCanon
        

    def on_rfl_cycle_start_clicked(self):
        # TODO:
        # Step 1: Check if number in dialog is still correct
        # If not, recalculate
        # Step 2: check if machine state is correct. If not, goto
        # Step 3: All is good, start machining
        print("Test")
    
    def open(self, ngc, toolTbl, endLine):
        self.ngc = ngc
        
        self.canon = self.canon_class()
        
        if os.path.exists(self.parameter_file):
            shutil.copy(self.parameter_file, self.temp_parameter_file)

        self.canon.parameter_file = self.temp_parameter_file

        unitcode = "G%d" % (20 + (self.stat.linear_units == 1))
        initcode = self.ini.find("RS274NGC", "RS274NGC_STARTUP_CODE") or ""
        
        result, seq = gcode.parse(ngc, self.canon, unitcode, initcode)

        print(result)

        self.toolTbl = toolTbl
        self.endLine = endLine

        self.getEndState()
        self.setTexts()

        super(RFLDialog, self).open()
    
    def setTexts(self):
        self.run_from_line_entry.setText(str(self.endLine))
        
        self.rfh_x_pos_coords.setText(str(self.coords[0]))
        self.rfh_y_pos_coords.setText(str(self.coords[1]))
        self.rfh_z_pos_coords.setText(str(self.coords[2]))
        if self.coords[3]:
            self.rfh_a_pos_coords.setText(str(self.coords[3]))
        if self.coords[4]:
            self.rfh_b_pos_coords.setText(str(self.coords[4]))
        
        if self.coolant == 7:
            self.rfh_coolant_display.setText("M7 MIST")
        elif self.coolant == 8:
            self.rfh_coolant_display.setText("M8 FLOOD")
        else:
            self.rfh_coolant_display.setText("M9 OFF")

        if self.spindle[0] == 3:
            self.rfh_spindle_dir.setText("M3 FWD")
        elif self.spindle[0] == 4:
            self.rfh_spindle_dir.setText("M4 REV")
        else:
            self.rfh_spindle_dir.setText("OFF")

        self.rfh_spindle_rpm.setText(str(self.spindle[1]))
    
    def getEndState(self):
                      #X Y Z A B
        self.coords = [0,0,0,0,0]
        self.spindle = [3, 0.0] # Spindle direction and RPM
        self.coolant = 9 #7 = mist, 8 = flood, 9 = none
        self.tool = 0

        # Make a copy of the program only to the required line
        ngcFile = open(self.ngc, "r")
        tempFile = open("/tmp/runfromline.ngc", "w")
        for i in range(self.endLine):
            tempFile.write(ngcFile.readline())
        tempFile.write("%")
        ngcFile.close()
        tempFile.close()

        interp = subprocess.Popen(["rs274", "-t", self.toolTbl, "-g",
                                   "/tmp/runfromline.ngc", "/tmp/runfromline.rs274"])

        # Wait for interpreter to write the entire file.
        while interp.poll() is None:
            pass

        rsFile = open("/tmp/runfromline.rs274")

        for templine in rsFile.readlines():
            pastLineNo = False
            pastN = False
            line = ""
            for char in templine:
                if char == "N":
                    try:
                        lineNo = int(lineNo)
                    except:
                        pass
                    pastN = True
                elif not char in " 1234567890." and pastN:
                    pastLineNo = True

                if pastLineNo:
                    line += char

            try:
                command, arguments = line.split("(")
            except:
                continue # Skips current loop as current line cannot be interpreted as a command
            arguments = arguments[0:-2] # Simply remove the ending ) bracket.
            argList = arguments.split(",")

            if command == "STRAIGHT_FEED": # G1
                for i in range(0, len(self.coords)):
                    self.coords[i] = float(argList[i])
            if command == "STRAIGHT_TRAVERSE": # G0
                for i in range(0, len(self.coords)):
                    self.coords[i] = float(argList[i])
            elif command == "SET_SPINDLE_SPEED": # S
                self.spindle[1] = argList[1]
            elif command == "START_SPINDLE_CLOCKWISE": # M3
                self.spindle[0] == 3
            elif command == "START_SPINDLE_COUNTERCLOCKWISE": # M4 TODO: Check if this command is correct
                self.spindle[0] == 4
            elif command == "STOP_SPINDLE_TURNING": # M5
                self.spindle[0] == 5
            elif command == "SET_FEED_RATE": # F, this is not needed?
                pass
            elif command == "SELECT_TOOL":
                pass
            elif command == "START_CHANGE":
                pass
            elif command == "CHANGE_TOOL": # Most likely only need to handle this and not SELECT_TOOL or START_CHANGE.
                self.tool = int(argList[0])

        rsFile.close()

if __name__ == "__main__":
    home = os.path.expanduser("~")
    end = getEndState(home + "/Desktop/3D_Chips.ngc", home + 
                    "/linuxcnc/configs/probe_basic/tool.tbl", 55)
    print(end)
