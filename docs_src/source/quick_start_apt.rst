==========================================
Probe Basic APT Installation instructions
==========================================


**Probe Basic APT Installation Guide for use with Debian 12 Bookworm and LinuxCNC version 2.9 or Later**


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



**If you have not already installed linuxcnc from apt, use the following line in main terminal:**

::

    sudo apt install linuxcnc-uspace linuxcnc-uspace-dev mesaflash



**Once you have installed linuxcnc, open linuxcnc and start the axis sim briefly and then you can shut it down to ensure the installation was succesful.**


**Adding the apt repository to Debian 12, Run the following Lines in Main terminal one at a time**

::

    sudo apt install curl


    echo 'deb [arch=amd64] https://repository.qtpyvcp.com/apt develop main' | sudo tee /etc/apt/sources.list.d/kcjengr.list


    curl -sS https://repository.qtpyvcp.com/repo/kcjengr.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/kcjengr.gpg


    gpg --keyserver keys.openpgp.org --recv-key 2DEC041F290DF85A



**Update the Repositories**

::

    sudo apt update



**Install QtPyVCP and Probe Basic**

::

    sudo apt install python3-qtpyvcp

    sudo apt install python3-probe-basic



**You are all installed!  You should now be able to launch the Probe Basic sim from within the linuxcnc applications dropdown menu.**


**Updating of probe basic and qtpyvcp will occur when your run the normal "sudo apt update, sudo apt upgrade" commands.  During updating, the probe basic sim configuration files will be overwritten.  It is strongly recommended to create your machine configuration files with unique names to avoid having them overwritten during updates.**

**To build your own machine configuration, please follow the instructions in this document:**


https://forum.linuxcnc.org/qtpyvcp/48401-configuration-file-conversion-doc-for-probe-basic-py3


