#!/usr/bin/env python

import os
import subprocess
# Temporarily removed requirement for INI and var
#def getEndPos(ngc, toolTbl, INI, var, endLine):
def getEndPos(ngc, toolTbl, endLine):
             #X Y Z A B
    coords = [0,0,0,0,0]
    #interp = subprocess.Popen(["rs274", "-t", toolTbl, "-i", INI, "-v", var, "-g", ngc], stdout=subprocess.PIPE)
    interp = subprocess.Popen(["rs274", "-t", toolTbl, "-g", ngc], stdout=subprocess.PIPE)
    while True:
        templine = interp.stdout.readline().decode()
        pastLineNo = False
        pastN = False
        firstChar = True
        line = ""
        lineNo = ""
        for char in templine:
            if char == "N":
                try:
                    lineNo = int(lineNo)
                except:
                    pass
                pastN = True
            elif char in "1234567890" and not pastN:
                lineNo += char
            elif not char in " 1234567890." and pastN:
                pastLineNo = True

            if pastLineNo:
                line += char
            firstChar = False

        try:
            lineNo = int(lineNo)
        except:
			pass

        if templine == "" and interp.poll() is not None:
            break
        elif isinstance(lineNo, int) and lineNo >= endLine:
            break

        # Command string has been set, time to interpret it :)
        try:
            command, arguments = line.split("(")
        except:
		    continue # Skips current loop as current line cannot be interpreted as a command
        arguments = arguments[0:-2] # Simply remove the ending ) bracket.

        if command == "STRAIGHT_FEED":
			argList = arguments.split(",")
			for i in range(0, len(coords)):
				coords[i] = float(argList[i])

    return coords

if __name__ == "__main__":
    home = os.path.expanduser("~")
    end = getEndPos(home + "/Desktop/3D_Chips.ngc", home + 
                    "/linuxcnc/configs/probe_basic/tool.tbl", 50)

    print(end)
