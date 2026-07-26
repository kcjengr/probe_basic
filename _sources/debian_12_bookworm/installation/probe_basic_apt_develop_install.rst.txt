===============================
Probe Basic APT Develop Install
===============================

**Probe Basic APT Installation Guide for use with Debian 12 Bookworm and LinuxCNC version 2.9 or Later**

Important Requirements
----------------------

    - Probe Basic is currently designed for 1920x1080 screen sizes only!
    - Probe Basic requires graphics hardware that supports OpenGL 3.2 and OpenGL Shading Language (GLSL) 1.50 or later
    - Probe Basic is tested on xfce4, during install of Debian 12 ISO:
    - DO NOT enter a Root password during installation, leave blank and skip this page.

    During installation, this screen below will appear, be sure to uncheck gnome and check xfce as pictured below. No other changes on this page are needed.

    .. image:: ../../images/xfce_check_doc.png
        :align: center


Installation Steps
------------------

1. Download the Linux Debian 12 Bookworm ISO Image File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Download from: https://www.debian.org/releases/bookworm/debian-installer/

    Select the Linux Debian 12 Bookworm Netinst CD ISO from the above link. You will need to make a bootable DVD or USB thumb drive depending on how you plan to install. The below software is extremely easy and works flawlessly with Linux Debian OS images:

    https://www.balena.io/etcher/?ref=etcher_update

    Once you have created your flash stick for LinuxCNC, proceed to install and boot the system. (Note: It is advised to have an ethernet cable internet connection during install). Select the graphical installation option. Follow the steps on screen to complete installation. When you are greeted by the Linux Desktop Selection Page, uncheck the GNOME option and check the XFCE4 option.

2. Update the System
^^^^^^^^^^^^^^^^^^^^

    After installation, run the following commands in the main terminal:

    .. code-block:: bash

        sudo apt update
        
        
        sudo apt upgrade
        

3. Install LinuxCNC
^^^^^^^^^^^^^^^^^^^

   Amd64 Deb (for PC's):
   
      https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-uspace_2.9.8_amd64.deb



   Arm64 Deb (for Pi 4/5)

      https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-arm64/linuxcnc-uspace_2.9.8_arm64.deb



   In a terminal, enter the following lines one at a time and press enter after each:

      .. code-block:: bash

         cd ~
         
         cd Downloads
         
         sudo dpkg -i linuxcnc-uspace_2.9.8_amd64.deb


    Once you have installed LinuxCNC, open it and start the axis sim briefly and then shut it down to ensure the installation was successful.


4. Add the APT Repository for the Installation type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Run the following command. It detects your Debian release and
    architecture (AMD64 or ARM64) and configures the correct repository and
    signing key for you:

    .. code-block:: bash

        curl -fsSL https://repository.qtpyvcp.com/install.sh | sudo sh

    .. note::

        Do not add the repository by hand. Adding the wrong suite for your
        Debian release installs packages built for the wrong Qt version,
        and putting the signing key in the wrong place causes
        ``apt update`` to fail with a "Missing key" error.

    .. warning::

        If ``apt update`` already reports a ``Missing key
        50F874571F20C5B0BA225E2F0CDFCCE0388CFA48`` error, your machine has
        an old or incomplete repository configuration. Clear it out first,
        then run the install command above:

        .. code-block:: bash

            curl -fsSL https://repository.qtpyvcp.com/uninstall.sh | sudo sh

        This removes only this repository's configuration, keys and
        packages. Other repositories and your LinuxCNC configs in
        ``~/linuxcnc`` are left untouched.



5. Update the Repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt update

6. Install QtPyVCP and Probe Basic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt install python3-qtpyvcp


        sudo apt install python3-probe-basic

    You are now installed! You should be able to launch the Probe Basic sim from within the LinuxCNC applications dropdown menu.

Updating and Configuration
--------------------------

    Updating of Probe Basic and QtPyVCP will occur when you run the normal "sudo apt update, sudo apt upgrade" commands. During updating, the Probe Basic sim configuration files will be overwritten. It is strongly recommended to create your machine configuration files with unique names to avoid having them overwritten during updates.


Uninstallation
--------------

    To completely remove QtPyVCP and all VCPs (Probe Basic, TurboNC,
    MonoKrom), along with the APT repository and its signing key, run:

    .. code-block:: bash

        curl -fsSL https://repository.qtpyvcp.com/uninstall.sh | sudo sh

    This works even if ``apt update`` is currently failing. It removes only
    this repository's packages, sources and keys -- other repositories on
    your machine, and your LinuxCNC configs in ``~/linuxcnc``, are left
    untouched.

    To reinstall afterwards:

    .. code-block:: bash

        curl -fsSL https://repository.qtpyvcp.com/install.sh | sudo sh
        sudo apt install python3-probe-basic

    Probe Basic and QtPyVCP are now fully removed. Your LinuxCNC installation is unaffected.
