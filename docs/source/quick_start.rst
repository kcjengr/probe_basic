===============================
Probe Basic Quick Start Install
===============================


**Probe Basic Quick Start Installation Guide**


**Note: Probe Basic is currently designed for 1920x1080 screen sizes only!**

**For Whatever reason mesa ehternet setups go much more smoothly when a wired ethernet internet connection is used during linux installation.  The debian installer does some magic that sets up the network perfectly with only one minor tweak once installed.  The wireless setup after install is much easier to get working.  I HIGHLY RECOMMEND using the wired internet connection and choosing to setup that connection during installation to avoid unforeseen issues in connecting to the mesa card(s) post install.**


**1- Download the Linuxcnc ISO Image File**

::

    http://www.linuxcnc.org/downloads/

Select the "LinuxCNC 2.8.0 Debian 10 Buster PREEMPT-RT ISO" option. you will need to make a bootable dvd or USB thumb drive depending on how you plan to install.  The below software is extremely easy and works flawlessly with linux debian OS images. Below is the link for it. I recommend using 2-4gb USB drive for quicker flashing.

::

    https://www.balena.io/etcher/?ref=etcher_update

Once you have created your flash stick for linuxcnc proceed to install and boot the system. (note: It is advised to have an ethernet cable internet connection during install).  Select the graphical installation option. Follow the steps on screen to complete installation.

After installation, copy the following in the main terminal one line at a time and hit enter, select Y for yes if asked at any point during installation.

::

    sudo apt update

    sudo apt upgrade



**2- Start Linuxcnc first time**

Now linuxcnc needs to be started for the first time for it to create its directory folders. This can be done by the drop down menu and selecting CNC and then LinuxCNC. After the program has started, you can shut it down and continue below.


**3- Install Probe Basic requiremens**

On a terminal emulator run:

::

    sudo apt install python-pyqt5 python-pyqt5.qtquick python-dbus.mainloop.pyqt5 python-pyqt5.qtopengl python-pyqt5.qsci python-pyqt5.qtmultimedia qml-module-qtquick-controls gstreamer1.0-plugins-bad libqt5multimedia5-plugins pyqt5-dev-tools python-dev python-wheel python-setuptools python-pip git python-pyqtgraph python-pyqt5.qtwebkit


**4- Download ProbeBasicInstaller**

Cick the link below to download the ProbeBasicInstaller file.  Once downloaded, find in its destination folder and right click and selecxt properties.  Select the Permissions Tab in the window that appears and check the box for "Allow this file to run as a program", see images below for reference. now double click the installer icon to begin the installation.  Follow the installer instructions to install Probe Basic.  Select all of the available items during initial installation.  after installation probe basic should show up in the linuxcnc launch screen and you can select to create a desktop icon for it by selecting the check box to do so at the bottom of the page.


https://github.com/kcjengr/probe_basic/releases/download/v0.2.9/ProbeBasic-Installer-0.2.9.run



.. image:: https://raw.githubusercontent.com/kcjengr/probe_basic/master/probe_basic/images/properties.png
   :align: center


.. image:: https://raw.githubusercontent.com/kcjengr/probe_basic/master/probe_basic/images/permissions.png
   :align: center



Congratulations! You now should be able to launch Probe basic!


**4- Removing, Modifying, Updating Probe Basic**

The maintenancetool file in the newly installed probe_basic file can be double clicked to bring up window for removing or modifying the probe basic installation.  we are currently still working on a more convenient update method but will update this page or create a new one as progress is made!


