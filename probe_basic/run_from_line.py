#!/usr/bin/env python

import os
import subprocess
# Temporarily removed requirement for INI and var
# def getEndPos(ngc, toolTbl, INI, var, endLine):
def getEndPos(ngc, toolTbl, endLine):
             #X Y Z A B
    coords = [0,0,0,0,0]
    ngcFile = open(ngc, "r")
    tempFile = open("/tmp/runfromline.ngc", "w")
    for i in range(endLine):
        tempFile.write(ngcFile.readline())
    ngcFile.close()
    tempFile.close()

    interp = subprocess.Popen(["rs274", "-t", toolTbl, "-g", "/tmp/runfromline.ngc", "/tmp/runfromline.rs274"])
    
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

        if command == "STRAIGHT_FEED":
            argList = arguments.split(",")
            print(argList)
            for i in range(0, len(coords)):
                coords[i] = float(argList[i])

    rsFile.close()
    return coords

if __name__ == "__main__":
    home = os.path.expanduser("~")
    end = getEndPos(home + "/Desktop/3D_Chips.ngc", home + 
                    "/linuxcnc/configs/probe_basic/tool.tbl", 55)
    print(end)
