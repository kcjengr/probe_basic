==================
Tool Length Setter
==================


   We recently updated the tool touch off page and it is now located under a tab on the main probing tab.  there are explanations and visual graphics for better understanding on the tool touch off setup and parameter functions.  Be sure to review the updated information/explanation tabs.  We also have eliminated the need to use G59.3 as a storing location for the probed coordinates used in the length offset calculation.  Below is an image of the new toolsetter page for reference.


   .. image:: toolsetter_page_doc_image.png
      :align: center

   |

Tool Touch Off Position
-----------------------

   .. important::
      Tool touch off position (G30), X and Y should be centered on the fixed tool setter platter.  Z should always be set to Z Home position Z0.0000

   |

   1- Setting the tool touch off position, jog the machine to the center point of the tool setter platter and indicate it in or probe it with the touch probe to find exact center point.
   2- Next, retract the z axis to the home position Z0.0000
   3- Press the "SET TOOL TOUCH OFF POS" button, this will capture and store the current locating for probing tools from the touch off routine.

   Spindle Zero is the length/distance from the empty spindle nose at the Z home Position Z0.0000 to the top of the tool setter (at the trip point)

   the value for ``Spindle Zero`` can be measured by probing the top of the setter using the spindle nose itself to find the distance (spindle empty spindle no holder loaded)


Measuring Tools
---------------

   1- To measure a tool, Load the tool in the spindle using the tool page in the probe basic interface
   2- Press the "TOUCH OFF CURRENT TOOL" button, this will  initiate the tool touch off routine and move the machine to the tool touch off position and probe the tool length to capture and store the current length of the tool in the tool table.
   
   .. image:: images/mill/tool_length_measure.png
      :align: center

   |
