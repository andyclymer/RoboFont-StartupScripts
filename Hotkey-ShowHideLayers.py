from mojo.UI import SetCurrentLayerByName
from mojo.events import addObserver, removeObserver
                     
class ShowHideLayers():
    
    """
    Startup Script:
        Assigns the "h" key to show/hide layer outlines
        -- Andy Clymer, github.com/andyclymer
    """

    def __init__(self):
        addObserver(self, "keyDown", "keyDown")

    def keyDown(self, info):
        event = info["event"]
        characters = event.characters()
        modifierFlags = event.modifierFlags()
        if characters == "h":
            f = CurrentFont()
            # Get the current display status
            currentDisplayOption = f.getLayer("background").getDisplayOption()["Stroke"]
            # Set the oppoosite display status on all other layers:
            for layerName in f.layerOrder:
                if not layerName == "foreground":
                    f.getLayer(layerName).setDisplayOption("Stroke", not currentDisplayOption)

ShowHideLayers()



