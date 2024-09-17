==============================
Probe Basic APT Stable Install
==============================

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

    Select the Linux Debian 12 Bookworm Netinst CD ISO. Create a bootable DVD or USB thumb drive using software like Etcher:

    https://www.balena.io/etcher/?ref=etcher_update

2. Install Debian 12
^^^^^^^^^^^^^^^^^^^^

    - Boot from the installation media
    - Select graphical installation
    - When prompted, uncheck GNOME and check XFCE4
    - Complete the installation

3. Update the System
^^^^^^^^^^^^^^^^^^^^

    Run the following commands:

    .. code-block:: bash

        sudo apt update
        sudo apt upgrade

4. Install LinuxCNC (if not already installed)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt install linuxcnc-uspace linuxcnc-uspace-dev mesaflash

5. Add the APT Repository
^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt install curl
        echo 'deb [arch=amd64] https://repository.qtpyvcp.com/apt stable main' | sudo tee /etc/apt/sources.list.d/kcjengr.list
        curl -sS https://repository.qtpyvcp.com/repo/kcjengr.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/kcjengr.gpg
        gpg --keyserver keys.openpgp.org --recv-key 2DEC041F290DF85A

6. Update Repositories
^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt update

7. Install QtPyVCP and Probe Basic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt install python3-qtpyvcp
        sudo apt install python3-probe-basic

Post-Installation
-----------------

    - You can now launch the Probe Basic sim from the LinuxCNC applications dropdown menu.
    - Updates for Probe Basic and QtPyVCP will occur with normal system updates.
    - It's recommended to create unique names for your machine configuration files to avoid overwriting during updates.

    For building your own machine configuration, please follow the instructions in this document:
    https://forum.linuxcnc.org/qtpyvcp/48401-configuration-file-conversion-doc-for-probe-basic-py3
