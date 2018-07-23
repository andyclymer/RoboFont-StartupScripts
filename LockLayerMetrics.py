from mojo.events import addObserver, removeObserver

class LockLayerMetrics():
    
    """
    Lock Layer Metrics
        -- Andy Clymer, github.com/andyclymer
        
    Add as a RoboFont Startup Script to permanently lock all layer widths and side bearing changes.
    
    """

    def __init__(self): 
        self.glyph = None
        self.prevLeftMargins = []
        addObserver(self, "currentGlyphChanged", "currentGlyphChanged")
    
    def currentGlyphChanged(self, info):
        if self.glyph:
            self.glyph.removeObserver(self, "Glyph.WidthChanged")
            self.glyph.removeObserver(self, "Glyph.Changed")
        self.glyph = info["glyph"]
        if self.glyph:
            self.glyph.addObserver(self, "widthChanged", "Glyph.WidthChanged")
            self.glyph.addObserver(self, "glyphChanged", "Glyph.Changed")
        else: self.glyph = None
        self.glyphChanged(None)
        
    def glyphChanged(self, info):
        # Every time the glyph drawing changes, hold aside the LSB, but only keep the last two values. 
        # This is beacause when a width does finally change, glyphChanged() will be called first, 
        # so we really need to know the second to last LSB.
        if self.glyph:
            self.prevLeftMargins.insert(0, self.glyph.leftMargin)
            if len(self.prevLeftMargins) == 3:
                self.prevLeftMargins = self.prevLeftMargins[:2]
        else: self.prevLeftMargins.clear()
        
    def widthChanged(self, info):
        # Every time the width changes, apply the difference of the last LSB in the list, and update the width
        if self.glyph:
            leftDiff = 0
            if len(self.prevLeftMargins):
                leftDiff = self.glyph.leftMargin - self.prevLeftMargins[-1]
            currentLayer = self.glyph.layerName
            for layerName in self.glyph.font.layerOrder:
                if not layerName == currentLayer:
                    layerGlyph = self.glyph.getLayer(layerName)
                    layerGlyph.leftMargin += leftDiff
                    layerGlyph.width = self.glyph.width

LockLayerMetrics()
