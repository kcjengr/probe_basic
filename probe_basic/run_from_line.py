#!/usr/bin/env python

import os
import subprocess

import gcode
import linuxcnc

from shutil import copyfile

from qtpyvcp.utilities.info import Info
from qtpyvcp.widgets.dialogs.base_dialog import BaseDialog
from qtpyvcp import plugins, actions

from qtpyvcp.widgets.display_widgets.vtk_backplot.base_canon import BaseCanon, PrintCanon, StatCanon

STATUS = plugins.getPlugin("status")
TOOLTABLE = plugins.getPlugin("tooltable")
POS = plugins.positions.Position()
INFO = Info()


class RFLCanon(StatCanon):
        
    
    def change_tool(self, pocket):
        super(RFLCanon, self).change_tool(pocket)
        print("TOOL CHANGHE")
        print(pocket)
        
    def next_line(self, st):
        super(RFLCanon, self).next_line(st)
        print("SEQUENCE", st.sequence_number)
            
            
    def straight_traverse(self, *args):
        super(RFLCanon, self).straight_traverse(*args)
        print("TRAVERSE", args)
            
            
    def straight_feed(self, *args):
        super(RFLCanon, self).straight_traverse(*args)
        print("FEED", args)


class RFLDialog(BaseDialog):
    # TODO: Take into account amount of axis machine has
    def __init__(self):
        super(RFLDialog, self).__init__(stay_on_top=True, ui_file=os.path.join(os.path.dirname(__file__), 'run_from_line_dialog.ui'))
        
        self.units = STATUS.stat.program_units # 1=in, 2=mm

        

    def on_rfl_cycle_start_clicked(self):
        # TODO:
        # Step 1: Check if number in dialog is still correct
        # If not, recalculate
        # Step 2: check if machine state is correct. If not, goto
        # Step 3: All is good, start machining
        if not self.endLine == int(self.run_from_line_entry.text()):
            # Recalculate
            self.endLine = int(self.run_from_line_entry.text())
            self.getEndState()
            self.setTexts()
        elif not self.isInPos():
            # Move into position
            cmdStr = ""
            if len(self.coords) > 4:
                cmdStr += ("G0 B" + str(self.coords[4]) + ";")
            if len(self.coords) > 3:
                cmdStr += ("G0 A" + str(self.coords[3]) + ";")
            cmdStr += ("G0 X{}Y{}".format(self.coords[0], self.coords[1]) + ";")
            cmdStr += ("G0 Z{}".format(self.coords[2]))
            actions.machine_actions.issue_mdi(cmdStr)
        else:
            # Start running
            actions.program_actions.run(self.endLine)

    def open(self, endLine):
        self.ngc = STATUS.file()

        print("OPEN")        
        inifile = os.getenv("INI_FILE_NAME")
        if inifile is None or not os.path.isfile(inifile) and not IN_DESIGNER:
            raise ValueError("Invalid INI file: %s", inifile)

        self.stat = linuxcnc.stat()
        self.ini = linuxcnc.ini(inifile)
        self.config_dir = os.path.dirname(inifile)
        
        temp = self.ini.find("EMCIO", "RANDOM_TOOLCHANGER")
        self.random = int(temp or 0)
        
        temp = self.ini.find("DISPLAY", "GEOMETRY") or 'XYZ'
        self.geometry = temp.upper()
        
        temp = self.ini.find("RS274NGC", "PARAMETER_FILE") or "linuxcnc.var"
        self.parameter_file = os.path.join(self.config_dir, temp)
        self.temp_parameter_file = os.path.join(self.parameter_file + '.temp')
        
        print(self.parameter_file)
        print(self.temp_parameter_file)
        
        if os.path.exists(self.parameter_file):
            print("COPY PARAM FILE", self.parameter_file, self.temp_parameter_file)
            copyfile(self.parameter_file, self.temp_parameter_file)
        
        self.canon = RFLCanon()
        self.canon.parameter_file = self.temp_parameter_file
        self.stat.poll()
        self.canon.tools = list(self.stat.tool_table)
                
        self.unitcode = "G%d" % (20 + (self.stat.linear_units == 1))
        self.initcode = self.ini.find("RS274NGC", "RS274NGC_STARTUP_CODE") or ""
        
        if self.ngc:
            result, seq = gcode.parse(self.ngc, self.canon, self.unitcode, self.initcode)

            if result > gcode.MIN_ERROR:
                msg = gcode.strerror(result)
                fname = os.path.basename(self.ngc)
                print("MSG", msg)
                
            print("Result", result)
            print("Seq", seq)

        # clean up temp var file and the backup
        os.unlink(self.temp_parameter_file)
            
        self.toolTbl = INFO.getToolTableFile()
        self.endLine = endLine

        # self.getEndState()
        # self.setTexts()

        super(RFLDialog, self).open()

    def setTexts(self):
        if self.units == 1:
            fStr = "{0:.4f}"
        else:
            fStr = "{0:.3f}"

        self.run_from_line_entry.setText(str(self.endLine))

        self.rfh_x_pos_coords.setText(fStr.format(self.coords[0]))
        self.rfh_y_pos_coords.setText(fStr.format(self.coords[1]))
        self.rfh_z_pos_coords.setText(fStr.format(self.coords[2]))
        
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

    def getEndState2(self):
        # This function is to replace getEndState.
        pass

    def getEndState(self):
        # To be replaced with BaseCanon
                      #X  Y  Z  A  B
        self.coords = [0.,0.,0.,0.,0.]
        self.spindle = [3, 0.0] # Spindle direction and RPM
        self.coolant = 9 #7 = mist, 8 = flood, 9 = none
        self.tool_no = 0

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
                self.tool_no = int(argList[0])

        rsFile.close()
        
    def isInPos(self):
        for i in range(len(self.coords)):
            if not (self.coords[i] - 0.1 <= STATUS.stat.position[i] - STATUS.stat.g5x_offset[i] <= self.coords[i] + 0.01): # Bit dirty, needs better solution
                return False
        return True

if __name__ == "__main__":
    home = os.path.expanduser("~")
    end = getEndState(home + "/Desktop/3D_Chips.ngc", home + 
                    "/linuxcnc/configs/probe_basic/tool.tbl", 55)
    print(end)
