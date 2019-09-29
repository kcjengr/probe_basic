![](probe_basic/images/probe_basic_icon.png)

# Probe Basic

Probe Basic is a interface for the LinuxCNC machine control.

## Quick install

install linuxcnc using the 64 bits stretch iso

http://www.linuxcnc.org/testing-stretch-rtpreempt/ 

* Upgrade linuxcnc

```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt dist-upgrade
$ sudo apt install dirmngr
$ sudo apt install software-properties-common
$ sudo apt-key adv --keyserver hkp://keys.gnupg.net --recv-key E0EE663E
$ sudo add-apt-repository "deb http://buildbot.linuxcnc.org/ stretch 2.8-rtpreempt"
$ sudo apt update
$ sudo apt upgrade
$ sudo apt dist-upgrade
```


* Dependencies

```bash
$ sudo apt install python-pyqt5 python-pyqt5.qtquick python-dbus.mainloop.pyqt5 python-pyqt5.qtopengl python-pyqt5.qsci python-pyqt5.qtmultimedia qml-module-qtquick-controls gstreamer1.0-plugins-bad libqt5multimedia5-plugins pyqt5-dev-tools python-dev python-setuptools python-pip git
```

* install pip package

```bash
$ pip install qtpyvcp
$ pip install probe_basic
```

## Development install

clone the Probe Basic repository

```bash
$ git clone https://github.com/kcjengr/probe_basic.git
```

install the dev version using pip

```bash
$ cd probe_basic
$ pip install -e .
```

now you can edit the files from the cloned directory and run editvcp to edit the interface

```bash
$ editvcp probe_basic
```


## Documentation

See the [documentation](https://kcjengr.github.io/qtpyvcp/).


## Resources

* [Development](https://github.com/kcjengr/ProbeBasic/)
* [Documentation](https://kcjengr.github.io/qtpyvcp/)
* [Freenode IRC](http://webchat.freenode.net/?channels=%23hazzy) (#hazzy)
* [The Matrix](https://riot.im/app/#/room/#qtpyvcp:matrix.org) (#qtpyvcp:matrix.org)
* [Gitter](https://gitter.im/kcjengr/qtpyvcp)
* [Discord](https://discord.gg/463hMhd)
* [Issue Tracker](https://github.com/kcjengr/ProbeBasic/issues)


## Dependancies

* [LinuxCNC](https://linuxcnc.org)
* Python 2.7
* PyQt5 or PySide2
* [QtPyVCP](https://qtpyvcp.kcjengr.com/)

Probe Basic is developed and tested using the LinuxCNC Debian 9 x64 (stretch)
[Live ISO](http://www.linuxcnc.org/testing-stretch-rtpreempt/) and Ubuntu 18.10 x64 SIM. It should run
on any system that can have PyQt5 installed, but Debian 9 x64 is the only OS
that is officially supported.


## DISCLAIMER

THE AUTHORS OF THIS SOFTWARE ACCEPT ABSOLUTELY NO LIABILITY FOR
ANY HARM OR LOSS RESULTING FROM ITS USE.  IT IS _EXTREMELY_ UNWISE
TO RELY ON SOFTWARE ALONE FOR SAFETY.  Any machinery capable of
harming persons must have provisions for completely removing power
from all motors, etc, before persons enter any danger area.  All
machinery must be designed to comply with local and national safety
codes, and the authors of this software can not, and do not, take
any responsibility for such compliance.

This software is released under the GPLv2.
