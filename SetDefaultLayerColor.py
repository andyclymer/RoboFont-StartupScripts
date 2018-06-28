from mojo.events import addObserver

class SetDefaultLayerColors():
    
    """
    Startup Script:
        Set the default layer color for new fonts
        -- Andy Clymer, github.com/andyclymer
    """

    def __init__(self):
        
        self.foregroundColor = (0.0628, 0.7641, 0.4612, 0.7)
        self.backgroundColor = (0.9324, 0.4373, 1.0, 0.7)
        addObserver(self, "setLayerColors", "newFontDidOpen")

    def setLayerColors(self, info):
        font = info["font"]
        font.setColorForLayer("foreground", self.foregroundColor)
        font.setColorForLayer("background", self.backgroundColor)

SetDefaultLayerColors()
