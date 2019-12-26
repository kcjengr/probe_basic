===============================
Probe Basic Quick Start Install
===============================


**Probe Basic Quick Start Installation Guide**



::

    http://www.linuxcnc.org/testing-stretch-rtpreempt/

Select the "linuxcnc-stretch-uspace-amd64-r13.iso" option. you will need to make a bootable dvd or USB thumb drive depending on how you plan to install.  The below software is extremely easy and works flawlessly with linux debian OS images. Below is the link for it. I recommend using 2-4gb USB drive for quicker flashing.

::

    https://www.balena.io/etcher/?ref=etcher_update

Once you have created your flash stick for linuxcnc proceed to install and boot the system. (note: It is advised to have an ethernet cable internet connection during install).  Select the graphical installation option. Follow the steps on screen to complete installation.

After installation, copy the following in the main terminal one line at a time and hit enter, select Y for yes if asked at any point during installation.

::

    sudo apt update

    sudo apt upgrade


**2- Upgrade to LinuxCNC version 2.8**

Copy the following in the main terminal one line at a time and hit enter, select Y for yes if asked at any point during installation.

::

    sudo apt-get update

    sudo apt-get dist-upgrade

    sudo apt-get install dirmngr

    sudo apt-get install software-properties-common

    sudo apt-key adv --keyserver hkp://keys.gnupg.net --recv-key E0EE663E

    sudo add-apt-repository "deb http://buildbot.linuxcnc.org/ stretch 2.8-rtpreempt"

    sudo apt update

    sudo apt upgrade

    sudo apt dist-upgrade


**3- Start Linuxcnc first time**

Now linuxcnc needs to be started for the first time for it to create its directory folders. This can be done by the drop down menu and selecting CNC and then LinuxCNC. After the program has started, you can shut it down and continue below.


**4- Download ProbeBasicInstaller**

Cick the link below to download the ProbeBasicInstaller zip file.  once downloaded, find in its destination folder and right click and selecxt "Extract To".  Select a location to extract the installer such as Desktop or another easy to find place. it can be deleted after installation is complete.


**DOWNLOAD LINK GOES HERE**


