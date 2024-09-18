=======================================
Machine Configuration (INI, HAL, Files)
=======================================

Creating a working Machine Configuration for Probe Basic
--------------------------------------------------------

   Probe Basic uses some different methods to offer its feature-rich user experience, which requires customized files and settings inside the HAL and INI files to function properly. Below is a guide to help create a working machine configuration for Probe Basic. This guide assumes a basic installation with manual tool changes. A future document will be available for more complex configurations with ATC and Coolant Cannon functionality.

Step 1: Create a basic configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   1. Create a configuration for your machine using Pncconf or mesact/mesact2 from the LinuxCNC menu in the applications drop-down in the upper menu bar. In this example, we are using Pncconf.
   2. It is recommended to use the Axis GUI display for this initial build.
   3. Have your machine's wiring schematic premade to make filling in the required information fast, easy, and accurate in Pncconf.
   4. After completing the Pncconf configuration builder and creating a new machine configuration saved in the LinuxCNC config directory, start LinuxCNC using your new config to verify there are no errors.
   5. Test the machine to verify the base functionality is correct (e.g., jogging, spindle function, axis motion).
   6. Once completed and found to function correctly, proceed to step 2.

Step 2: Copy required files
^^^^^^^^^^^^^^^^^^^^^^^^^^^

   1. In the LinuxCNC config folder, locate your new config folder and the "probe_basic_machine_config_setup_files" folder.
   2. Open two folder windows on the desktop: the new Pncconf folder created for your machine and the probe_basic_machine_config_setup_files folder.
   3. Clean up the Pncconf folder by removing unneeded files (see images below for reference).
   4. Copy the required files from the probe_basic_machine_config_setup_files folder to the Pncconf config folder.


   **As built pncconfig folder**

   .. image:: images/pb_instruction_1.png
      :align: center

   |


   **Unneeded pncconfig files highlighted**

   .. image:: images/pb_instruction_2.png
      :align: center

   |


   **Cleaned up pncconfig folder**
   
   .. image:: images/pb_instruction_3.png
      :align: center

   |


   **Files to be Copied from probe_basic_machine_config_setup_files folder**

   .. image:: images/pb_instruction_4.png
      :align: center

   |


   **Files Copied to pncconfig folder**

   .. image:: images/pb_instruction_5.png
      :align: center
      :alt: Files Copied to pncconfig folder

   |

Step 3: Edit INI files
^^^^^^^^^^^^^^^^^^^^^^

   1. Open the Pncconf "my_LinuxCNC_machine.ini" file side by side with the supplied "probe_basic_required_ini_items.ini" file in a text editor.
   2. Integrate the lines from "probe_basic_required_ini_items.ini" into your existing file:
      - If a line is present in your machine file, use the Probe Basic settings for that line.
      - If a line is not in your machine file, copy it to the appropriate section in "my_LinuxCNC_machine.ini".
   3. Note that only ONE postgui HAL file can be called. Add any additional items to the existing probe_basic_postgui.hal file.
   4. Save the file and delete the "probe_basic_required_ini_items.ini" file from the folder.


   **Side by Side ini files for editing**

   .. image:: images/pb_instruction_7.png
      :align: center

   |
   
Step 4: Modify HAL file
^^^^^^^^^^^^^^^^^^^^^^^

   1. Add digital and analog IO to the HAL file by modifying the following line:

      ::

         loadrt [EMCMOT]EMCMOT servo_period_nsec=[EMCMOT]SERVO_PERIOD num_joints=[KINS]JOINTS

      Add this to the end of the line:

      ::

         num_dio=6 num_aio=3

      The finished edit should look like this:

      ::

         loadrt [EMCMOT]EMCMOT servo_period_nsec=[EMCMOT]SERVO_PERIOD num_joints=[KINS]JOINTS num_dio=6 num_aio=3

   .. image:: images/pb_instruction_8.png
      :align: center
      :alt: HAL file modification

   |

   2. Remove the red highlighted manual tool change dialog section from the bottom of the hal file as shown in the image below.  Probe basic uses its own built in dialog for manual tool changes which give the user better tool information and matches the ui visual theme more appropriately.

   .. image:: images/pb_instruction_9.png
      :align: center
      :alt: Tool change section to remove

   |

Launching Probe Basic
---------------------

   1. Under the CNC section of the drop-down applications menu, find your machine configuration and select it to launch.
   2. Check the box at the bottom of the launch window to create a desktop icon for easier starts.
   3. To set the Probe Basic icon:
      - Right-click the desktop launcher and select "edit launcher"
      - Click the current icon image, this will open the icon folder
      - Find and select the icon named "probe_basic_mill"

   You should now be ready to use Probe Basic with your machine configuration.
