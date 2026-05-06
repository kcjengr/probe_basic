===========================================
Probe Basic Trixie Developer Installation
===========================================

This development install method uses the Trixie installer script and installs QtPyVCP and optional Probe Basic into a virtual environment at ``~/dev/venv``.

Important Requirements
----------------------

    - LinuxCNC must be installed system-wide before or during installer execution.
    - Internet access is required during installation.
    - Probe Basic is currently designed for 1920x1080 screen sizes only.

Installation Steps
------------------

1. Download the LinuxCNC Debian 13 Trixie PREEMPT-RT ISO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Download from:

    https://www.linuxcnc.org/iso/linuxcnc_2.9.8-amd64.hybrid.iso

    This Debian 13 Trixie ISO installs Debian with the required PREEMPT-RT kernel and LinuxCNC uspace package.

2. Ensure LinuxCNC is installed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt update
        sudo apt upgrade
        sudo apt install linuxcnc-uspace

3. Clone the Trixie installer repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        cd ~
        mkdir -p dev
        cd dev
        git clone https://github.com/Lcvette/qtpyvcp-trixie-installer.git
        cd qtpyvcp-trixie-installer

4. Run the installer script
^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        ./install_for_qtpyvcp.sh

5. Update an existing install
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        cd ~/dev/qtpyvcp-trixie-installer
        ./updater.sh

Uninstall
---------

    .. code-block:: bash

        rm -rf ~/dev
