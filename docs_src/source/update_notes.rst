====================
Update Release Notes
====================
|


Overview of updates for MILL configurations
-------------------------------------------

    Probe basic and probe basic lathe have just received major updates that will require users to make some changes to their configurations in order for probe basic to properly function.  These changes offer a variety of benefits at the cost of some initial configuration editing.  Below is a list of changes being rolled out in this update:

    - DRO Displays are now user configurable from the ini file with options for mill configs being xyz, xyza, xyzab, xyzac, xyzbc, xyzabc and a user template has been included with xyzabc dros for users to easily edit and make changes to suit their machine builds. using only the dro's required has significantly sped up probe basic where it is not having to track and query multiple hidden dro's as it previously was doing. The jog button display will also update based on the dro display settings. Users will need to copy the user_dro_display folder from the sim config to their machine config and edit the ini file to set the appropriate dros and jog buttons to display by adding the following lines to the [DISPLAY] section of the ini:
        - USER_DROS_PATH = user_dro_display/
        - DRO_DISPLAY = XYZ (or desired configuration)
    - JOG axis buttons received a preconfigured addition of xyzbc
    - Offset table column display now set in the ini file with the following line in [DISPLAY] section:
        - OFFSET_COLUMNS = XYZ (or desired configuration)
    - Tool table columns display now set in the ini file with the following line in [DISPLAY] section:
        - TOOL_TABLE_COLUMNS = TZDR (or desired configuration)
    - Keyboard jog settings are now user configurable with the following ini file [DISPLAY] entries:
        - KEYBOARD_JOG = true
            - true sets KB jog active
            - false turns KB jog off
        - KEYBOARD_JOG_SAFETY_OFF = true
            - true turns requirement of safety keys off for KB jogging
            - false sets KB jog safety keys active
    - ATC updates, you can now set the desired ATC Tab Display Setting to hide the atc tab, display carousel atc or display rack atc from the ini [DISPLAY] section in the following line.
        - ATC_TAB_DISPLAY = 0
            - 0 sets the atc tab hidden
            - 1 sets the atc tab to display the carousel type atc
            - 2 sets the atc tab to display the new rack type atc
    - ATC page received a user button widget, users can now easily customize their required atc buttons in this widget separate from the main ui so it will not be overwritten during future updates, the user_atc_buttons folder is located in the updated sim config folder and will need to be copied to the users machine config folder for use.  user will need to add the following line to the [DISPLAY] section of the ini file to activate it.
        - USER_ATC_BUTTONS_PATH = user_atc_buttons/

    - User Tabs adds a main tab and a sidebar tab where the user can fully configure their own required widgets, buttons, line entries etc. and have the ui file stored safely in their config folder and it will not be overwritten during updates.  Add this feature, by copying the user_tabs from the sim config folder to the user's machine config folder and add the following lines to the [DISPLAY] section of the ini file.
        - USER_TABS_PATH = user_tabs/
    - Custom config YAML file will require edits or the newly edited version in the sim config will need to be copied over for some of the above features to work, be sure to do this or you will receive some errors.
    - A few probing routines were found to have an error using the hints, particularly the following and will need to be copied from the sim config subroutines folder to user's machine config subroutines folder, below are the corrected file names for reference:
        - probe_valley_x.ngc
        - probe_valley_x_center_start.ngc
        - probe_valley_y.ngc
        - probe_valley_y_center_start.ngc



Overview of updates for LATHE configurations
--------------------------------------------

    Probe basic lathe received major updates that will require users to make some changes to their configurations in order for probe basic lathe to properly function.  the Lathe user interface had been lagging pretty far behind and is now brought up to the same place as the mill ui in terms of features and functionality. These changes offer a variety of benefits at the cost of some initial configuration editing.  The layout for lathe has changed slightly to accommodate the configurable functionality, Below is a list of changes being rolled out in this update:

    - DRO Displays are now user configurable from the ini file with options for mill configs being xz, xzc, xyzc and a user template has been included also for custom dro displays with xyzc dros for users to easily edit and make changes to suit their machine builds. this also gives users using fewer axes some additional space for customizations specific to their machine right in the main lower panel dro section.  Using only the dro's required has significantly sped up probe basic where it is not having to track and query multiple hidden dro's as it previously was doing. The jog button display will also update based on the dro display settings. Users will need to copy the user_dro_display folder from the sim config to their machine config and edit the ini file to set the appropriate dros and jog buttons to display by adding the following lines to the [DISPLAY] section of the ini:
        - USER_DROS_PATH = user_dro_display/
        - DRO_DISPLAY = XZ (or desired configuration)
    - JOG axis buttons received a preconfigured addition of xyzbc
    - Offset table column display now set in the ini file with the following line in [DISPLAY] section:
        - OFFSET_COLUMNS = XZ (or desired configuration)
    - Tool table columns display now set in the ini file with the following line in [DISPLAY] section:
        - TOOL_TABLE_COLUMNS = TXYZIJDQR (or desired configuration)
    - Keyboard jog settings are now user configurable with the following ini file [DISPLAY] entries:
        - KEYBOARD_JOG = true
            - true sets KB jog active
            - false turns KB jog off
        - KEYBOARD_JOG_SAFETY_OFF = true
            - true turns requirement of safety keys off for KB jogging
            - false sets KB jog safety keys active
    - User Tabs adds a main tab and a sidebar tab where the user can fully configure their own required widgets, buttons, line entries etc. and have the ui file stored safely in their config folder and it will not be overwritten during updates.  Add this feature, by copying the user_tabs from the sim config folder to the user's machine config folder and add the following lines to the [DISPLAY] section of the ini file.
        - USER_TABS_PATH = user_tabs/
    - Custom config YAML file will require edits or the newly edited version in the sim config will need to be copied over for some of the above features to work, be sure to do this or you will receive some errors.