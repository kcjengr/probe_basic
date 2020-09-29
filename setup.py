import versioneer
from setuptools import setup, find_packages
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
    packages=find_packages(),
    include_package_data=True,
    install_requires=['qtpyvcp>=0.3.9'],
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
