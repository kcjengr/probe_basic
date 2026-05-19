======================================
Probe Basic Trixie APT Develop Install
======================================

**Probe Basic APT development install guide for Debian 13 Trixie**

Important Requirements
----------------------

    - Probe Basic is currently designed for 1920x1080 screen sizes only.
    - Probe Basic requires graphics hardware that supports OpenGL 3.2 and OpenGL Shading Language (GLSL) 1.50 or later.
    - LinuxCNC must be installed before installing QtPyVCP and Probe Basic packages.

Installation Steps
------------------

1. Download the LinuxCNC Debian 13 Trixie PREEMPT-RT ISO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Download from:

    https://www.linuxcnc.org/iso/linuxcnc_2.9.8-amd64.hybrid.iso

    This Debian 13 Trixie ISO installs Debian with the required PREEMPT-RT kernel and LinuxCNC uspace package.

2. Update the system
^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt update
        sudo apt upgrade

3. Install LinuxCNC (if not installed)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt install linuxcnc-uspace

4. Add the Trixie develop APT repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **AMD64 for PC installation repository:**

    .. code-block:: bash

        sudo apt install curl
        echo 'deb [arch=amd64] https://repository.qtpyvcp.com/apt trixie-dev main' | sudo tee /etc/apt/sources.list.d/kcjengr.list
        curl -sS https://repository.qtpyvcp.com/repo/kcjengr.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/kcjengr.gpg
        gpg --keyserver keys.openpgp.org --recv-key 2DEC041F290DF85A

    **ARM64 for Raspberry Pi 4 and 5 installation repository:**

    .. code-block:: bash

        sudo apt install curl
        echo 'deb [arch=arm64] https://repository.qtpyvcp.com/apt trixie-dev main' | sudo tee /etc/apt/sources.list.d/kcjengr.list
        curl -sS https://repository.qtpyvcp.com/repo/kcjengr.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/kcjengr.gpg
        gpg --keyserver keys.openpgp.org --recv-key 2DEC041F290DF85A

5. Update repositories
^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt update

6. Install QtPyVCP and Probe Basic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: bash

        sudo apt install python3-qtpyvcp
        sudo apt install python3-probe-basic

Updating and Configuration
--------------------------

    Probe Basic and QtPyVCP update through normal APT upgrades.

    .. code-block:: bash

        sudo apt update
        sudo apt upgrade
