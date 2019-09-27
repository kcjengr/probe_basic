import versioneer
from setuptools import setup, find_packages
from qtpyvcp.tools.qcompile import compile

with open("README.md", "r") as fh:
    long_description = fh.read()

# compile .qrc and .ui files
compile(['probe_basic',])

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
    entry_points={
        'gui_scripts': [
            'probe_basic=probe_basic:main',
        ],
        'qtpyvcp.vcp': [
            'probe_basic=probe_basic',
        ],
    },
    install_requires=[
       # 'qtpyvcp',
       # 'docopt',
    ],
    # dependency_links=[
    #     'https://github.com/kcjengr/qtpyvcp/tarball/master#egg=qtpyvcp-0.0.1'
    # ]
)
