===============================
Probe Basic APT Develop Install
===============================

**Probe Basic APT Installation Guide for use with Debian 12 Bookworm and LinuxCNC version 2.9 or Later**

Important Requirements
----------------------

    - Probe Basic is currently designed for 1920x1080 screen sizes only!
    - Probe Basic Install by apt is for amd64 only currently!
    - Probe Basic requires graphics hardware that supports OpenGL 3.2 and OpenGL Shading Language (GLSL) 1.50 or later
    - Probe Basic is tested on xfce4, during install of Debian 12 ISO:
    - DO NOT enter a Root password during installation, leave blank and skip this page.

    During installation, this screen below will appear, be sure to uncheck gnome and check xfce as pictured below. No other changes on this page are needed.

    .. image:: images/xfce_check_doc.png
       :align: center

Installation Steps
------------------

1. Download the Linux Debian 12 Bookworm ISO Image File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Download from: https://www.debian.org/download

    Select the Linux Debian 12 Bookworm Netinst CD ISO from the above link. You will need to make a bootable DVD or USB thumb drive depending on how you plan to install. We recommend using Etcher for creating bootable USB drives:

    https://www.balena.io/etcher/?ref=etcher_update

2. Install Debian 12
^^^^^^^^^^^^^^^^^^^^

    - Boot from the installation media and select the graphical installation option.
    - Follow the on-screen steps to complete installation.
    - When you reach the Desktop Selection Page, uncheck GNOME and check XFCE4.

3. Update the System
^^^^^^^^^^^^^^^^^^^^

    After installation, run the following commands in the terminal:

    ::

        sudo apt update
        sudo apt upgrade

4. Install LinuxCNC
^^^^^^^^^^^^^^^^^^^

    If you haven't already installed LinuxCNC, use the following command:

    ::

        sudo apt install linuxcnc-uspace linuxcnc-uspace-dev mesaflash

    Open LinuxCNC and start the axis sim briefly to ensure the installation was successful.

5. Add the APT Repository
^^^^^^^^^^^^^^^^^^^^^^^^^

    Run the following commands in the terminal:

    ::

        sudo apt install curl
        echo 'deb [arch=amd64] https://repository.qtpyvcp.com/apt develop main' | sudo tee /etc/apt/sources.list.d/kcjengr.list
        curl -sS https://repository.qtpyvcp.com/repo/kcjengr.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/kcjengr.gpg
        gpg --keyserver keys.openpgp.org --recv-key 2DEC041F290DF85A

6. Update the Repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^

    ::

        sudo apt update

7. Install QtPyVCP and Probe Basic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    ::

        sudo apt install python3-qtpyvcp
        sudo apt install python3-probe-basic

    Congratulations! You have now installed Probe Basic. You should be able to launch the Probe Basic sim from within the LinuxCNC applications dropdown menu.

Updating and Configuration
--------------------------

    - Updating Probe Basic and QtPyVCP will occur when you run the normal "sudo apt update" and "sudo apt upgrade" commands.
    - During updates, the Probe Basic sim configuration files will be overwritten.
    - It is strongly recommended to create your machine configuration files with unique names to avoid having them overwritten during updates.

    To build your own machine configuration, please follow the instructions in this document:
    https://forum.linuxcnc.org/qtpyvcp/48401-configuration-file-conversion-doc-for-probe-basic-py3
