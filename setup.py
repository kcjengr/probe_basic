from setuptools import setup
import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=True,
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
        'widgets.lathe_tool_touch_off.images']
)
