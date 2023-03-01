<<<<<<< HEAD
import versioneer
from setuptools import setup
# from qtpyvcp.tools.qcompile import compile

with open("README.md", "r") as fh:
    long_description = fh.read()
#
# # compile .qrc and .ui files
# compile(['probe_basic', ])

setup(
    name="probe_basic",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Chris Polanski",
    author_email="",
    description="Probe Basic - A QtPyVCP based Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kcjengr/probe_basic",
    download_url="https://github.com/kcjengr/probe_basic/tarball/master",
    packages=[
        'debian',
        'example_gcode',
        'probe_basic',
        'probe_basic.fonts',
        'probe_basic.images',
        'probe_basic.virtual_keyboards',
        'probe_basic_latc',
        'probe_basic_latc.images',
        'probe_basic_lathe',
        'probe_basic_lathe.images',
        'probe_basic_vertical',
        'probe_basic_vertical.images',
        'widgets',
        'widgets.atc_widget',
        'widgets.atc_widget.images',
        'widgets.conversational',
        'widgets.conversational.images',
        'widgets.lathe_tool_touch_off',
        'widgets.lathe_tool_touch_off.images'],
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'probe_basic=probe_basic:main',
            'probe_basic_lathe=probe_basic_lathe:main',
        ],
        'qtpyvcp.vcp': [
            'probe_basic=probe_basic',
            'probe_basic_lathe=probe_basic_lathe',
        ],
        'qtpyvcp.widgets': [
            'Probe Basic Widgets=widgets'
        ]
    },
)
=======
from setuptools import setup
setup()
>>>>>>> toml
