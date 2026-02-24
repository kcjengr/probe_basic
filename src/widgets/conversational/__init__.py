import os

IN_DESIGNER = os.getenv('DESIGNER', False)

if IN_DESIGNER:
    from .designer_plugins import FacingWidget, HoleCircleWidget, XYCoordWidget
else:
    from .facing import FacingWidget
    from .hole_circle import HoleCircleWidget
    from .xy_coord import XYCoordWidget