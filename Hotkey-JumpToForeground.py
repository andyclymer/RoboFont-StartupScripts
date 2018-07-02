from mojo.UI import SetCurrentLayerByName
from mojo.events import addObserver, removeObserver
                     
class JumpToForeground():
    
    """
    Startup Script:
        Assigns the "f" key to jump back to the "foreground" layer
        -- Andy Clymer, github.com/andyclymer
    """

    def __init__(self):
        addObserver(self, "keyDown", "keyDown")

    def keyDown(self, info):
        event = info["event"]
        characters = event.characters()
        modifierFlags = event.modifierFlags()
        if characters == "f":
            SetCurrentLayerByName("foreground")

JumpToForeground()
