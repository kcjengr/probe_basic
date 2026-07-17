=================================================
Lathe Tool Offsets as of 0.6.5-7 Develop Version
=================================================

Overview
--------

Probe Basic Lathe provides comprehensive tool offset management for precision lathe operations. This guide covers the step-by-step procedures for setting up tool offsets using both traditional LinuxCNC tool offset mode and Probe Basic's Master Tool Offset Mode.

Understanding G7/G8 Diameter and Radius Modes
----------------------------------------------

LinuxCNC lathes operate in one of two modes that affect how X-axis positions and tool offsets are displayed and entered:

**G7 - Diameter Mode**
   In diameter mode (G7), the X-axis DRO displays and accepts diameter values. This is the default mode for most lathe operations as it matches how parts are typically dimensioned. When G7 is active, tool offset inputs are interpreted as diameter values.

**G8 - Radius Mode**
   In radius mode (G8), the X-axis DRO displays and accepts radius values (half of diameter). This mode is useful when working from drawings that specify radii.

**Dynamic Button Labels**

The Touch Off page features intelligent button labeling that changes based on the active mode:

- When **G7 (Diameter Mode)** is active: Buttons display "**TOUCH X DIAM**"
- When **G8 (Radius Mode)** is active: Buttons display "**TOUCH X RAD**"

This visual feedback ensures you always know what type of value to enter. The touch-off subroutines automatically handle the conversion between diameter and radius as needed - tool offsets are always stored in radius mode internally, regardless of which mode you're working in.

To switch modes, use the G7/G8 buttons on the main DRO panel or include G7/G8 in your startup G-code.


Traditional Tool Offset Setup Procedure
----------------------------------------

This procedure is for machines using standard LinuxCNC tool offsets (when MASTER_TOOL_OFFSET_MODE is false or not set).

**Step 1: Prepare Your Setup**

1. Load the tool you want to measure into the spindle
2. Ensure your workpiece or reference stock is securely mounted in the chuck
3. Verify the correct tool number is active (the tool table will highlight the current tool)
4. Navigate to the **Touch Off** tab

**Step 2: Set X-Axis Tool Offset**

1. **Check Current Mode**: Look at the touch button - it will show either "TOUCH X DIAM" or "TOUCH X RAD"
   
   - If working in G7 (diameter mode): Button shows "TOUCH X DIAM"
   - If working in G8 (radius mode): Button shows "TOUCH X RAD"

2. **Position the Tool**: Jog the tool to touch the workpiece or skim pass the stock diameter (or radius reference surface)

3. **Measure the Reference**: 
   
   - If in DIAM mode: Use calipers or micrometer to measure the *diameter* of the workpiece where the tool is touching
   - If in RAD mode: Measure and calculate the *radius* value for user input and measuring it is typicaly easier to perform these tasks in diameter mode.

4. **Enter the Value**:

   - Click in the "X Offset Touch Value" input field
   - Enter the measured diameter (G7) or radius (G8) value
   - The field accepts the value appropriate to the current mode

5. **Apply the Offset**: Click the "TOUCH X DIAM" or "TOUCH X RAD" button (depending on active mode), or press ENTER

   - The system automatically calculates the tool offset
   - The tool table is updated with the X offset for the current tool
   - The subroutine handles diameter/radius conversion automatically

**Step 3: Set Z-Axis Tool Offset**

1. **Position the Tool**: Jog the tool to touch the face of the workpiece (or use a tool setter/gage block)

2. **Enter Gage Thickness**: In the "Z Gage Thickness" field, enter:
   
   - 0.0 if touching the workpiece face directly
   - The thickness of your gage block if using one

3. **Apply the Offset**: Click the "TOUCH Z" button

   - The system calculates the Z offset
   - The tool table is updated with the Z offset for the current tool
   - The updated tool length offset is then applied to the currently loaded tool.

**Step 4: Verify Offsets**

1. The X Axis DRO should now display the actual position of the newly measured tool while touching the workpiece
2. The Z axis should now display the tools relation to the z axis machine absolute zero when touching the reference face.
3. Verify the X and Z offset values for your tool are correct
4. The offsets represent the distance from machine home to the tool tip when touching the reference surfaces


Master Tool Offset Mode Setup Procedure
----------------------------------------

When MASTER_TOOL_OFFSET_MODE is enabled in your INI file, one tool is designated as the "master" with X0/Z0 offsets, and all other tools are measured relative to the master tool. This method simplifies tool management and enables the Master Tool Promotion feature.

**Step 1: Set Up Master Tool (Usually T1)**

1. **Navigate**: Go to the **Touch Off** tab and physically load your master tool (typically T1)

2. **Mount Reference Material/Stock**: Ensure your workpiece or reference stock is securely mounted in the chuck - this same reference will be used for all tools

3. **Set the Master Tool Number**: 

   - On the **Touch Off** tab, locate the Master Tool number field (labeled "MT")
   - Enter your desired master tool number (e.g., 1)
   - Press Enter
   - **Important - First Time Setup**: A confirmation dialog will appear asking if you want to promote this tool to master:
     
     * The dialog shows: "Promoting Tool X to Master Tool!" with details about the promotion
     * For first-time setup, click "Yes" to confirm the promotion
     * This designates your tool as the master with X0/Z0 offsets and must be done before measuring any secondary tools
     * If the tool table already has offsets, the system will recalculate all other tool offsets to maintain their spatial relationships

4. **Touch Off X-Axis**:

   - Check the button label: it shows either "TOUCH X DIAM" (G7 mode) or "TOUCH X RAD" (G8 mode)
   - Jog the tool to touch the workpiece diameter, or make a skim cut to true up the surface and do not move x axis after cutting
   - Measure the diameter (if in G7 diameter mode) or radius (if in G8 radius mode) of the workpiece at the touch point with calipers
   - Enter this measured value in the input field next to the "TOUCH X DIAM/RAD" button
   - Press Enter or Click the "TOUCH X DIAM/RAD" button
   - The master tool X offset in the tool table will be set to 0.0000, and the G54 work offset is adjusted to display the measured value at the touch point

5. **Touch Off Z-Axis**:

   - Jog the tool to touch the face of the workpiece or make a skim pass on the end of the stock face.  you can also use a gage block of known thickness between stock end and tool tip.
   - Enter 0.0 in "Z Gage Block Thickness" if touching directly to stock, or enter the gage block thickness if the gage block is used
   - Click the "TOUCH Z" button
   - The master tool Z offset in the tool table will be set to 0.0000, and the G54 work offset is adjusted so that the Z axis DRO now shows 0.0000 when the tool is touching the reference face or the face position plus gage block thickness if used.

6. **Verify Master Tool Setup**:

   - Confirm the **Master Tool Number** field on the **Touch Off** tab shows your master tool number (e.g., 1)
   - Navigate to the **Tool Table** tab and confirm the master tool shows X 0.0000 and Z 0.0000 offsets

7. **Important**: The subroutine looks for the user set Master Tool Number and compares the currently loaded tool being measured to the Master Tool Number. If they are the same tool, the subroutine will simply set the work coordinate offsets.  additionally the user when setting up a job with the master tool loaded may perform these steps and use the work offset zero buttons for z axis, and enter the measured diameter or radius direectly in the main dro.

**Step 2: Set Up Secondary Tools**

For each additional tool in your library, the subroutine will see the tool being measured is NOT the master tool and will correctly calculated the relative offset to the master tool and write them to the tool table.

1. **Load and Activate**: physically load the tool on the machine and load the tool in software by entering its tool number in the standard tool change input field next to the "T" Button. press enter or click the button to load the tool in software

2. **Touch Off X-Axis**:

   - Jog to touch the **same reference diameter** that you used for the master tool - consistency is critical
   - The previously entered X value should still be the same as when the master tool was measured - if not, re-enter the same value you used for the master tool
   - Click "TOUCH X DIAM/RAD"
   - The system calculates this tool's offset *relative to the master tool* and stores it in the tool table. you should see the X axis main DRO now displaying the reference pieces measured diameter or radius value

3. **Touch Off Z-Axis**:

   - Jog to touch the **same reference face** used for the master tool
   - Enter the gage block thickness in "Z Gage Block Thickness" or 0.0 if touching directly
   - Click "TOUCH Z"
   - The system calculates this tool's Z offset *relative to the master tool* and stores it in the tool table
   - the Z axis Main DRO should now show 0.0000

**Step 3: Verify Relationships**

1. Navigate to the **Tool Table** tab
2. Master tool shows X0.0000, Z0.0000
3. Each secondary tool shows offsets representing its physical position relative to the master tool
4. These relationships are preserved even if you promote a different tool to be the master tool

**Repeat for All Tools**: Repeat the secondary tool setup procedure for each tool in your library, always using the same reference diameter and face as the master tool to ensure consistent offsets.


Master Tool Promotion
----------------------

If your master tool needs repair or replacement, you can promote another tool to become the new master without remeasuring all tools.  This would be done to make the promoted master tool a "placeholder" which will recalculate all offsets relative to the promoted tool.  this is ueful when changing the physical position or replacing inserts of the original master tool.  it allows for the original master tool to be measured agains the promoted master tool as a secondary tool to create an updated spatial relationship for x and z offsets.  once the new offsets have been measured you can simple promotr the original master tool back to being the current master tool and you do not have to remeasure all other tools in your library.:

1. Navigate to the **TOUCH OFF** tab
2. Locate the **Master Tool Number** field
3. Enter the tool number you wish to promote (e.g., change from 1 to 5)
4. Press Enter - a confirmation dialog appears
5. Click "Yes" to proceed
6. All tool offsets are instantly recalculated to preserve spatial relationships
7. The promoted tool now shows X0/Z0 for its tool offsets and all other tools are adjusted accordingly

For complete details, see the Master Tool Promotion Feature in the update_notes.rst documentation.


Important Notes
---------------

**Consistency is Critical**

- Always use the same reference surfaces (workpiece diameter and face) for all tools
- In Master Tool Mode, all secondary tools must be measured against the same reference as the master
- Mixed references will result in incorrect tool offsets

**Tool Table Automatic Updates**

- Tool offsets are written to the tool table immediately upon touch-off
- No manual saving is required
- The active tool offset is automatically applied to the currently loaded tool during the touch off routine

**Diameter vs. Radius Input**

- The touch buttons dynamically show whether you're supposed to be inputting diameter or radius
- The subroutines handle all conversions automatically based off of those button labels
- Tool offsets are internally stored in radius mode regardless of input mode
- Watch the button label: "TOUCH X DIAM" means enter diameter, "TOUCH X RAD" means enter radius

**G-Code Programs**

- G-code programs can use either G7 or G8
- Tool offsets work correctly in both modes
- The mode affects display and manual input only, not programmed moves

**Switching Modes Mid-Operation**

- You can switch between G7 and G8 at any time
- Existing tool offsets remain valid
- DRO values and button labels update immediately


Configuration Requirements
---------------------------

**Version 0.6.5-7 Develop version or later is required for Master Tool Offset Mode and G7/G8 mode detection features.**

**For Traditional Tool Offsets:**

No special configuration required - this is the default Probe Basic behavior.

**For Master Tool Offset Mode:**

Add the following to the [DISPLAY] section of your probe_basic_lathe.ini file:

.. code-block:: bash

   MASTER_TOOL_OFFSET_MODE = true

For detailed information about this setting, see the machine_config.rst documentation.

**Touch-Off Subroutines:**

Ensure the following subroutines are in your config's subroutines folder:

- **Traditional Mode**: ``touch_off_x.ngc``, ``touch_off_z.ngc``
- **Master Tool Mode**: ``touch_off_x_mt.ngc``, ``touch_off_z_mt.ngc``

The correct subroutines are automatically called based on your MASTER_TOOL_OFFSET_MODE setting.


Troubleshooting
---------------

**Tool offset is half what I expected (or double)**

This usually indicates a diameter/radius mode mismatch:

- Check if the button showed "DIAM" but you entered a radius value (or vice versa)
- G7 expects diameter input; G8 expects radius input
- Re-touch the tool using the correct value type

**Tool offset is wrong after touching off**

- Verify you touched the reference surface properly (tool actually touching workpiece)
- Confirm you entered the correct workpiece dimension
- In Master Tool Mode: ensure you used the same reference surfaces as the master tool

**Button doesn't show DIAM or RAD label**

- The button label updates based on active G-code mode
- Issue MDI command ``G7`` for diameter mode or ``G8`` for radius mode
- Check that your INI file startup code includes G7 or G8

**Master Tool Promotion doesn't work**

- Verify MASTER_TOOL_OFFSET_MODE = true in INI file [DISPLAY] section
- Ensure you're entering a valid tool number that exists in your tool table
- Check that the promoted tool has been properly measured (has non-zero offsets unless it was already the master)


Related Documentation
---------------------

- **machine_config.rst**: MASTER_TOOL_OFFSET_MODE setting details
- **update_notes.rst**: Master Tool Promotion feature documentation
- **lathe_interface.rst**: Overview of lathe interface tabs and layout
- **probe_basic_parameters.rst**: Parameter reference for touch-off values
