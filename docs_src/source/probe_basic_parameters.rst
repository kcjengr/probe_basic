======================
Probe Basic Parameters
======================

**Probe basic requires the following parameters be created in the var file**

   Probe Basic's devlop version is now using the var file in the configs folder for storing parameters used in subroutines and other functions throughout linuxcnc. These are callable the same as all other parameters which allows them to be used in remap subroutines.  This will allow users a greater degree of flexibility in modifying and using features such as tool touch off during tool changes, programmable coolant, probing etc all while being able to make changes from the from within the probe basic user interfaces entry boxes.  Once changes to the entries are made they are recorded to the var file and are available immediately after the changes are made.  This allows users the ability to change vital settings to ensure their machines run optimally and reliably without major config modifications.

   The Probe Basic Sim Config Folder contains the sim.var file which has been updated with these now required parameters. please be sure to add them to your machine connfiguration for proper functionality.  


.. list-table:: **Probe Basic Numbered Parameters**
   :header-rows: 1
   :widths: 10 40 10 300

   * - Var #
     - Used For
     - Persistent/Volatile
     - Description of stored Variable
   * - 3000
     - Programmed Coolant
     - Persistent
     - Activates programmable coolant option in subroutines
   * - 3001
     - Programmed Coolant
     - Persistent
     - Horizontal distance from spindle centerline to coolant nozzle rotation axis
   * - 3002
     - Programmed Coolant
     - Persistent
     - Vertical distance from spindle gauge line to coolant nozzle rotation axis
   * - 3003
     - Programmed Coolant
     - Persistent
     - User input for desired offset of calculated angle of coolant nozzle rotational axis
   * - 3004
     - Tool Setting
     - Persistent
     - Fast feed rate for initial tool setter probe search
   * - 3005
     - Tool Setting
     - Persistent
     - Slow feed rate for secondary tool setter probe search
   * - 3006
     - Tool Setting
     - Persistent
     - Traverse feed rate for any tool setter motion that is non probing
   * - 3007
     - Tool Setting
     - Persistent
     - Z axis max probe search travel distance for probe search before error triggers
   * - 3008
     - Tool Setting
     - Persistent
     - X and Y axis max probe search travel distance for probe search before error triggers
   * - 3009
     - Tool Setting
     - Persistent
     - Retract Distance to move above tool setter trigger point after initial fast probe move
   * - 3010
     - Tool Setting
     - Persistent
     - Spindle zero, distance from spindle nose home position to tool setter trigger height (abs)
   * - 3011
     - Tool Setting
     - Persistent
     - Tool Diameter Offset mode activation
   * - 3012
     - Tool Setting
     - Persistent
     - Tool Diameter Probe mode activation (not yet implemented)
   * - 3013
     - Tool Setting
     - Persistent
     - Tool diameter offset mode direction to offset tool during probing
   * - 3014
     - Touch Probe
     - Persistent
     - Probe Tool Number
   * - 3015
     - Touch Probe
     - Persistent
     - Probe Slow Feedrate, secondary probing speed for final probing moves, (no secondary probing if set to 0.0)
   * - 3016
     - Touch Probe
     - Persistent
     - Probe Fast Feedrate, initial probing speed of touch probe used
   * - 3017
     - Touch Probe
     - Persistent
     - Probe Traverse Feedrate, repositioning probing speed for traversing work piece to next initial probing position
   * - 3018
     - Touch Probe
     - Persistent
     - Max XY Distance, max distance in XY probing routine will move before stopping with error (safety Feature)
   * - 3019
     - Touch Probe
     - Persistent
     - XY Clearance, distance in XY the probe after recording a probe event and between initial and secondary probes
   * - 3020
     - Touch Probe
     - Persistent
     - Max Z Distance, max distance in Z probing routine will move before stopping with error (safety Feature)
   * - 3021
     - Touch Probe
     - Persistent
     - Z Clearance, distance in Z the probe after recording a probe event and between initial and secondary probes
   * - 3022
     - Touch Probe
     - Persistent
     - Extra Probe Depth, Additional Probe Depth added to the probe Z- move, Added to the Probe Tip's Diameter
   * - 3023
     - Touch Probe
     - Persistent
     - Step Off Width, Distance probe moves from the starting position in X and Y to clear work edge
   * - 3024
     - Touch Probe
     - Persistent
     - Edge Width, Distance between edge probes when probing to find the angle offset of a work piece
   * - 3025
     - Touch Probe
     - Persistent
     - Boss and Pocket Diameter Hint
   * - 3026
     - Touch Probe
     - Persistent
     - Boss and Pocket X Hint
   * - 3027
     - Touch Probe
     - Persistent
     - Boss and Pocket Y Hint
   * - 3028
     - Touch Probe
     - Persistent
     - Ridge and Valley X Hint
   * - 3029
     - Touch Probe
     - Persistent
     - Ridge and Valley Y Hint
   * - 3030
     - Touch Probe
     - Persistent
     - Probe Mode, to switch between probing position only and setting wco
   * - 3031
     - Touch Probe
     - Persistent
     - wco rotation mode, for switching between setting rotational wco or to probe angle of probed work only
   * - 3032
     - Touch Probe
     - Persistent
     - calibration offset for touch probe, used in probe subroutines
   * - 3033
     - Touch Probe
     - Persistent
     - Probe Calibration Diameter
   * - 3034
     - Touch Probe
     - Persistent
     - Probe X Calibration Width
   * - 3035
     - Touch Probe
     - Persistent
     - Probe Y Calibration Width
   * - 3036
     - Touch Probe
     - Persistent
     - Square Calibration Axis Selection
   * - 3973
     - ATC Tool Change
     - Persistent
     - Rack Pocket Count
   * - 3974
     - ATC Tool Change
     - Persistent
     - Rack ATC User Parameter 1
   * - 3975
     - ATC Tool Change
     - Persistent
     - Rack ATC User Parameter 2
   * - 3976
     - ATC Tool Change
     - Persistent
     - Rack ATC User Parameter 3
   * - 3977
     - ATC Tool Change
     - Persistent
     - Rack ATC User Parameter 4
   * - 3978
     - ATC Tool Change
     - Persistent
     - Rack ATC User Parameter 5
   * - 3979
     - ATC Tool Change
     - Persistent
     - Rack ID to determine ATC Mechanical Configuration
   * - 3980
     - ATC Tool Change
     - Persistent
     - Rack Traverse Speed
   * - 3981
     - ATC Tool Change
     - Persistent
     - Rack ATC Load Height Spindle on Tool
   * - 3982
     - ATC Tool Change
     - Persistent
     - Rack ATC Safe Z Clearance Height for Tool
   * - 3983
     - ATC Tool Change
     - Persistent
     - Rack ATC Pocket 1 X axis machine coordinate
   * - 3984
     - ATC Tool Change
     - Persistent
     - Rack ATC Pocket 1 Y axis machine coordinate
   * - 3985
     - ATC Tool Change
     - Persistent
     - Rack ATC Pocket 2 X axis machine coordinate
   * - 3986
     - ATC Tool Change
     - Persistent
     - Rack ATC Pocket 2 X axis machine coordinate
   * - 3987
     - ATC Tool Change
     - Persistent
     - Rack ATC Pocket 1 Clearance X axis machine coordinate
   * - 3988
     - ATC Tool Change
     - Persistent
     - Rack ATC Pocket 1 Clearance X axis machine coordinate
   * - 3989
     - ATC Tool Change
     - Volatile
     - Used to track if the carousel is homed (M13) (volatile)
   * - 3990
     - ATC Tool Change
     - Persistent
     - Used to track the current tool pocket
   * - 3991
     - ATC Tool Change
     - Persistent
     - Used to track the current tool loaded in the spindle
   * - 4000
     - ATC Tool Change
     - Volatile
     - Used in the math to calculate the ATC Calculations
   * - 4001
     - ATC Tool Change
     - Persistent
     - ATC Pocket 1 Parameter where tool number is recorded
   * - 4002
     - ATC Tool Change
     - Persistent
     - ATC Pocket 2 Parameter where tool number is recorded
   * - 4003
     - ATC Tool Change
     - Persistent
     - ATC Pocket 3 Parameter where tool number is recorded
   * - 4004
     - ATC Tool Change
     - Persistent
     - ATC Pocket 4 Parameter where tool number is recorded
   * - 4005
     - ATC Tool Change
     - Persistent
     - ATC Pocket 5 Parameter where tool number is recorded
   * - 4006
     - ATC Tool Change
     - Persistent
     - ATC Pocket 6 Parameter where tool number is recorded
   * - 4007
     - ATC Tool Change
     - Persistent
     - ATC Pocket 7 Parameter where tool number is recorded
   * - 4008
     - ATC Tool Change
     - Persistent
     - ATC Pocket 8 Parameter where tool number is recorded
   * - 4009
     - ATC Tool Change
     - Persistent
     - ATC Pocket 9 Parameter where tool number is recorded
   * - 4010
     - ATC Tool Change
     - Persistent
     - ATC Pocket 10 Parameter where tool number is recorded
   * - 4011
     - ATC Tool Change
     - Persistent
     - ATC Pocket 11 Parameter where tool number is recorded
   * - 4012
     - ATC Tool Change
     - Persistent
     - ATC Pocket 12 Parameter where tool number is recorded
   * - 4013
     - ATC Tool Change
     - Persistent
     - ATC Pocket 13 Parameter where tool number is recorded
   * - 4014
     - ATC Tool Change
     - Persistent
     - ATC Pocket 14 Parameter where tool number is recorded
   * - 4015
     - ATC Tool Change
     - Persistent
     - ATC Pocket 15 Parameter where tool number is recorded
   * - 4016
     - ATC Tool Change
     - Persistent
     - ATC Pocket 16 Parameter where tool number is recorded
   * - 4017
     - ATC Tool Change
     - Persistent
     - ATC Pocket 17 Parameter where tool number is recorded
   * - 4018
     - ATC Tool Change
     - Persistent
     - ATC Pocket 18 Parameter where tool number is recorded
   * - 4019
     - ATC Tool Change
     - Persistent
     - ATC Pocket 19 Parameter where tool number is recorded
   * - 4020
     - ATC Tool Change
     - Persistent
     - ATC Pocket 20 Parameter where tool number is recorded
   * - 4021
     - ATC Tool Change
     - Persistent
     - ATC Pocket 21 Parameter where tool number is recorded
   * - 4022
     - ATC Tool Change
     - Persistent
     - ATC Pocket 22 Parameter where tool number is recorded
   * - 4023
     - ATC Tool Change
     - Persistent
     - ATC Pocket 23 Parameter where tool number is recorded
   * - 4024
     - ATC Tool Change
     - Persistent
     - ATC Pocket 24 Parameter where tool number is recorded