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


Uninstallation
--------------

    To completely remove Probe Basic, QtPyVCP, and the APT repository from your system, run:

    .. code-block:: bash

        sudo uninstall-probe-basic

    Probe Basic and QtPyVCP are now fully removed. Your LinuxCNC installation is unaffected.
