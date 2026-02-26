import os
# Force PySide6 before any Qt-touching import (qtpy defaults to PyQt5 if both are installed)
os.environ.setdefault('QT_API', 'pyside6')
# Force OpenGL RHI backend for Qt Quick before any Qt context is created.
# Without this Qt6 defaults to Vulkan/Metal which causes a black screen +
# white triangle error indicator when those backends are unavailable.
os.environ.setdefault('QSG_RHI_BACKEND', 'opengl')

try:
    # Try to get version from package metadata (for installed packages)
    from importlib.metadata import version, PackageNotFoundError
    try:
        __version__ = version("probe-basic")
        # If version is placeholder (editable install), use git version
        if __version__ in ("0.0", "0.0.0"):
            raise PackageNotFoundError
    except PackageNotFoundError:
        # Fall back to dunamai for development installations
        try:
            from dunamai import Version
            from pathlib import Path
            # Use this module's directory for git lookup
            module_dir = Path(__file__).parent.parent.parent
            # Use same pattern as poetry-dynamic-versioning in pyproject.toml
            git_version = Version.from_git(path=module_dir, pattern=r"^(?P<base>\d+\.\d+\.\d+)")
            # Format to match poetry-dynamic-versioning: base+distance.gcommit
            if git_version.distance > 0:
                __version__ = f"{git_version.base}+{git_version.distance}.g{git_version.commit}"
            else:
                __version__ = git_version.base
        except Exception:
            __version__ = "0.0.0+unknown"
except ImportError:
    # Python < 3.8 fallback
    try:
        from dunamai import Version
        from pathlib import Path
        module_dir = Path(__file__).parent.parent.parent
        git_version = Version.from_git(path=module_dir, pattern=r"^(?P<base>\d+\.\d+\.\d+)")
        if git_version.distance > 0:
            __version__ = f"{git_version.base}+{git_version.distance}.g{git_version.commit}"
        else:
            __version__ = git_version.base
    except Exception:
        __version__ = "0.0.0+unknown"

import qtpyvcp

VCP_DIR = os.path.realpath(os.path.dirname(__file__))
VCP_CONFIG_FILE = os.path.join(VCP_DIR, 'probe_basic.yml')


def main(opts=None):

    # Must be called BEFORE QApplication is created.
    # Qt6 defaults to RHI/Vulkan which causes a black screen + white triangle
    # on systems that don't have Vulkan; force OpenGL instead.
    try:
        from PySide6.QtQuick import QQuickWindow, QSGRendererInterface
        QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.OpenGL)
    except Exception as _e:
        import sys
        print(f"[probe_basic] WARNING: could not set OpenGL graphics API: {_e}", file=sys.stderr)

    if opts is None:
        from qtpyvcp.utilities.opt_parser import parse_opts
        opts = parse_opts(vcp_cmd='probe_basic',
                          vcp_name='Probe Basic',
                          vcp_version=__version__)

    qtpyvcp.run_vcp(opts, VCP_CONFIG_FILE)


if __name__ == '__main__':
    main()
