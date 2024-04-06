==========================================
Probe Basic .deb Installation instructions
==========================================


**Probe Basic .deb Installation Guide for use with Debian Bookworm and LinuxCNC version 2.9 or Later**


**Important Requirements:**

- Probe Basic is currently designed for 1920x1080 screen sizes only!
- Probe Basic Install by apt is for amd64 only currently!
- Probe Basic requires graphics hardware that supports OpenGL 3.2 and OpenGL Shading Language (GLSL) 1.50 or later
- Probe Basic is tested on xfce4, during install of Debian 12 ISO:
- DO NOT enter a Root password during installation, leave blank and skip this page.


    During installation, this screen below will appear, be sure to uncheck gnome and check xfce as pictured below. no other changes on this page are needed.


.. image:: images/xfce_check_doc.png
   :align: center





**Download the Linux Debian 12 Bookworkm ISO Image File**

::

    https://www.debian.org/download


Select the Linux Debian 12 Bookworm Netinst CD ISO from the above link. you will need to make a bootable dvd or USB thumb drive depending on how you plan to install.  The below software is extremely easy and works flawlessly with linux debian OS images. Below is the link for it. I recommend using 2-4gb USB drive for quicker flashing.

::

    https://www.balena.io/etcher/?ref=etcher_update


Once you have created your flash stick for linuxcnc proceed to install and boot the system. (note: It is advised to have an ethernet cable internet connection during install).  Select the graphical installation option. Follow the steps on screen to complete installation.  When you are greeted by the Linux Desktop Selection Page, uncheck the GNOME option and check the XFCE4 option.

After installation, copy the following in the main terminal one line at a time and hit enter, select Y for yes if asked at any point during installation.  If the return shows "All up to Date" then you can proceed to the next step.

::

    sudo apt update

    sudo apt upgrade



**To install Probe Basic using the .deb packages, you must install all 3 seperately using the following method:**

**Requirements:**

    - Debian 12 Bookworm
    - Python 3.11
    - Linuxcnc 2.9 or higher
    - xfce4 desktop environment (should be selected during installation of Debian 12 ISO)
    - OpenGL 1.50 or Later graphics support
    - QtPyVCP
    - hiyapyco


**If you have not already installed linuxcnc from apt, use the following line in main terminal:**

::

    sudo apt install linuxcnc-uspace linuxcnc-uspace-dev mesaflash



**Once you have installed linuxcnc, open linuxcnc and start the axis sim briefly and then you can shut it down to ensure the installation was succesful.**


**Installing QtPyVCP and Probe Basic, Download the following files into your chosen directory typically home/your-pc-name/downloads**


.. parsed-literal::
    
    |probe_basic_deb_link|
    
    |qtpyvcp_deb_link|
    
    https://repository.qtpyvcp.com/repo/hiyapyco/python3-hiyapyco_0.5.1-1_all.deb


**Go to the downloaded files directory folder, right click in the folder and select "Open Terminal Here". Enter the following commands in the new terminal one at a time and press enter, it will require your sudo password:**

::

    sudo apt install debhelper-compat dh-python python3-setuptools python3-yaml python3-pyqt5.qtmultimedia python3-pyqt5.qtquick qml-module-qtquick-controls libqt5multimedia5-plugins python3-dev python3-docopt python3-qtpy python3-pyudev python3-psutil python3-markupsafe python3-vtk9 python3-pyqtgraph python3-simpleeval python3-jinja2 python3-deepdiff python3-sqlalchemy qttools5-dev-tools python3-serial


*then enter the following using the recently downloaded file name :*

.. parsed-literal::

    sudo dpkg -i python3-hiyapyco_0.5.1-1_all.deb


*then enter the following using the recently downloaded file name :*

.. parsed-literal::

    sudo dpkg -i |qtpyvcp_deb|


*then enter the following using the recently downloaded file name :*

.. parsed-literal::

    sudo dpkg -i |probe_basic_deb|


**You are all installed!  You should now be able to launch the Probe Basic sim from within the linuxcnc applications dropdown menu.**


**When updating/installing the latest .deb files, the probe basic sim configuration files will be overwritten.  It is strongly recommended to create your machine configuration files with unique names to avoid having them overwritten during updates.**


**To build your own machine configuration, please follow the instructions in this document:**


https://forum.linuxcnc.org/qtpyvcp/48401-configuration-file-conversion-doc-for-probe-basic-py3


**To uninstall enter each of the following commands one at a time or which ever items you wish to uninstall in main terminal and press enter. This will completely remove each package:**

::

    sudo dpkg -P python3-probe-basic

    sudo dpkg -P python3-hiyapyco

    sudo dpkg -P python3-qtpyvcp



