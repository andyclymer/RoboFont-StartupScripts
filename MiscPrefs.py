import AppKit
from mojo.roboFont import version
from lib.tools.defaults import getDefault, setDefault


"""
Startup Script:
    Miscellaneous preferences
    -- Andy Clymer, github.com/andyclymer
"""



"""
----------------------------------------------------------------------
Set the menu bar name to include the RoboFont version number
"""

menu = AppKit.NSApp().mainMenu()
roboFontItem = menu.itemWithTitle_("RoboFont")
if roboFontItem:
    roboFontItem.submenu().setTitle_("RoboFont %s " % version)



"""
----------------------------------------------------------------------
Turn on all deprecation warnings,
useful when updating code for RF3
"""
alwaysWarn = False
if alwaysWarn:
    if version[0] == "3":
        print("RF3 Beta: Turning on deprecation warnings")
        import warnings
        # The default is to only warn once:
        # warnings.simplefilter("once")
        # Warn always:
        warnings.simplefilter("always")



"""
----------------------------------------------------------------------
Show full kerning group names
"""
setDefault("showFullKernGroupNames", True)


