from lib.tools.defaults import getDefault, setDefault
from mojo.events import addObserver

class SnapClosedOnlyWhileDragging(object):
    
    """
    Startup Script:
        Only "snap to close" open contours while the mouse clicked down and dragging.
        Prevents open ended contours from closing when nudging with the arrow keys.
        -- Andy Clymer, github.com/andyclymer
    """

    def __init__(self):
        
        self.snapToCloseDistance = 4

        addObserver(self, "mouseDownCallback", "mouseDown")
        addObserver(self, "mouseUpCallback", "mouseUp")

    def mouseDownCallback(self, info):
        setDefault("glyphViewCloseContourSnapDistance", self.snapToCloseDistance)

    def mouseUpCallback(self, info):
        setDefault("glyphViewCloseContourSnapDistance", 0)

SnapClosedOnlyWhileDragging()