======================
Probe Basic Parameters
======================

**Probe basic requires the following parameters be created in the var file**

   Probe Basic's devlop version is now using the var file in the configs folder for storing parameters used in subroutines and other functions throughout linuxcnc. These are callable the same as all other parameters which allows them to be used in remap subroutines.  This will allow users a greater degree of flexibility in modifying and using features such as tool touch off during tool changes, programmable coolant, probing etc all while being able to make changes from the from within the probe basic user interfaces entry boxes.  Once changes to the entries are made they are recorded to the var file and are available immediately after the changes are made.  This allows users the ability to change vital settings to ensure their machines run optimally and reliably without major config modifications.

   The Probe Basic Sim Config Folder contains the sim.var file which has been updated with these now required parameters. please be sure to add them to your machine configuration for proper functionality.



.. list-table::
   :header-rows: 1
   :widths: 10 50 10 150

   * - Var #
     - Used For
     - Persistence
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
     - Spindle zero, spindle nose home position to tool setter trigger height (abs)
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
     - Probe Slow Feedrate, secondary probing speed probing moves (single touch if set to 0)
   * - 3016
     - Touch Probe
     - Persistent
     - Probe Fast Feedrate, initial probing speed of touch probe used
   * - 3017
     - Touch Probe
     - Persistent
     - Probe Traverse Feedrate, probing speed for traversing work piece to next probe position
   * - 3018
     - Touch Probe
     - Persistent
     - Max XY Distance, XY probe motion distance before triggering an error (safety Feature)
   * - 3019
     - Touch Probe
     - Persistent
     - XY Clearance, XY retract distance after probe trigger event
   * - 3020
     - Touch Probe
     - Persistent
     - Max Z Distance, Z probe motion distance before triggering an error (safety Feature)
   * - 3021
     - Touch Probe
     - Persistent
     - Z Clearance, Z retract distance after probe trigger event
   * - 3022
     - Touch Probe
     - Persistent
     - Extra Probe Depth, distance added to probe tip diameter to control z- probe depth
   * - 3023
     - Touch Probe
     - Persistent
     - Step Off Width, XY move distance from start probe position to clear work edge
   * - 3024
     - Touch Probe
     - Persistent
     - Edge Width, Distance between edge probes when probing angle offset of a work piece
   * - 3025
     - Touch Probe
     - Persistent
     - Boss and Pocket Diameter Hint use to set rough probing motion distances
   * - 3026
     - Touch Probe
     - Persistent
     - Boss and Pocket X Hint use to set rough probing motion distances
   * - 3027
     - Touch Probe
     - Persistent
     - Boss and Pocket Y Hint use to set rough probing motion distances
   * - 3028
     - Touch Probe
     - Persistent
     - Ridge and Valley X Hint use to set rough probing motion distances
   * - 3029
     - Touch Probe
     - Persistent
     - Ridge and Valley Y Hint use to set rough probing motion distances
   * - 3030
     - Touch Probe
     - Persistent
     - Probe Mode, to switch between probing position only and setting wco
   * - 3031
     - Touch Probe
     - Persistent
     - wco rotation mode, sets rotation wco or probes to find angle of work only
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