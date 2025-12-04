"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

Scene 1: Sediment Core visualization
"""

from graphics import GraphWin, Text, Point, color_rgb
from masoko_data_handler import readData, getValueRange, normalizeValue
from environmental_features import SedimentLayer

def createSedimentLayers(data, x=500, yStart=100, layerHeight=16):
    """Create SedimentLayer objects from dataset"""
    feMin, feMax = getValueRange(data, "Fe/Ti")
    
    layers = []
    yPos = yStart
    
    for record in data:
        year = record["Age (AD)"]
        feTi = record["Fe/Ti"]
        depth = record["Depth (cm)"]
        
        if feTi == "-" or not isinstance(feTi, (int, float)):
            continue
        
        normalized = normalizeValue(feTi, feMin, feMax)
        layer = SedimentLayer(year, feTi, depth, normalized)
        layer.setHeight(layerHeight)
        layer.yPosition = yPos
        
        layers.append(layer)
        yPos += layerHeight
    
    return layers

def drawSedimentCore(win, layers):
    """Draw all sediment layers"""
    title = Text(Point(500, 40), "Sediment Core")
    title.setSize(18)
    title.setStyle("bold")
    title.draw(win)
    
    for layer in layers:
        layer.draw(win, 250, layer.yPosition)
    
    if layers:
        oldest = layers[-1]
        oldestLabel = Text(Point(640, oldest.yPosition + 8), f"{oldest.getYear()} AD")
        oldestLabel.setSize(12)
        oldestLabel.draw(win)
        
        newest = layers[0]
        newestLabel = Text(Point(640, newest.yPosition + 8), f"{newest.getYear()} AD")
        newestLabel.setSize(12)
        newestLabel.draw(win)
    
    return layers

def createInfoDisplay(win, x=140, y=500):
    """Create text objects for displaying layer info"""
    infoObjects = {}
    
    title = Text(Point(x, y - 60), "Layer Info")
    title.setSize(16)
    title.setStyle("bold")
    title.draw(win)
    
    yearLabel = Text(Point(x, y), "Click a layer")
    yearLabel.setSize(13)
    yearLabel.draw(win)
    infoObjects['year'] = yearLabel
    
    feTiLabel = Text(Point(x, y + 40), "")
    feTiLabel.setSize(13)
    feTiLabel.draw(win)
    infoObjects['feTi'] = feTiLabel
    
    depthLabel = Text(Point(x, y + 80), "")
    depthLabel.setSize(13)
    depthLabel.draw(win)
    infoObjects['depth'] = depthLabel
    
    interpLabel = Text(Point(x, y + 140), "")
    interpLabel.setSize(11)
    interpLabel.setFill(color_rgb(80, 80, 120))
    infoObjects['interp'] = interpLabel
    
    return infoObjects

def updateInfoDisplay(infoObjects, layer):
    """Update info display with layer data"""
    feTi = layer.getValue()
    infoObjects['year'].setText(f"{layer.getYear()} AD")
    infoObjects['feTi'].setText(f"Fe/Ti: {feTi:.2f}")
    infoObjects['depth'].setText(f"Depth: {layer.getDepth():.2f} cm")
    
    if feTi > 4.0:
        interpretation = "High iron content\nWet period with\nincreased erosion"
    elif feTi > 3.7:
        interpretation = "Moderate iron\nNormal conditions"
    else:
        interpretation = "Low iron content\nDry period\n(Little Ice Age)"
    
    infoObjects['interp'].setText(interpretation)

def createExplanation(win, x=140, y=800):
    """Create explanation panel"""
    title = Text(Point(x, y), "What Fe/Ti Shows")
    title.setSize(14)
    title.setStyle("bold")
    title.draw(win)
    
    explanation = Text(Point(x, y + 60), "Fe/Ti ratio measures\niron vs titanium.\n\nDarker = More iron\n= Wet climate\n= More erosion\n\nLighter = Less iron\n= Dry climate\n= Less erosion")
    explanation.setSize(11)
    explanation.draw(win)

def handleClick(win, layers, infoObjects):
    """Handle mouse clicks on sediment layers"""
    clickPoint = win.getMouse()
    
    for layer in layers:
        if layer.containsPoint(clickPoint):
            updateInfoDisplay(infoObjects, layer)
            return True
    
    return False

def runScene(width=1000, height=1300):
    """Run Scene 1"""
    win = GraphWin("Scene 1: Sediment Core", width, height)
    win.setBackground(color_rgb(240, 240, 235))
    
    data = readData("data.json")
    centerX = width // 2
    layers = createSedimentLayers(data, x=centerX, yStart=100, layerHeight=16)
    drawnLayers = drawSedimentCore(win, layers)
    
    infoX = width // 7
    infoY = height // 2
    infoObjects = createInfoDisplay(win, x=infoX, y=infoY)
    createExplanation(win, x=infoX, y=800)
    
    try:
        while True:
            handleClick(win, drawnLayers, infoObjects)
    except:
        pass
    
    win.close()

def main():
    """Test Scene 1"""
    runScene()

if __name__ == "__main__":
    main()
