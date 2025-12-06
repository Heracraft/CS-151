"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

Scene 3: Solar Ripples recursive visualization
"""

from graphics import GraphWin, Text, Point, color_rgb, Circle, Rectangle
from masoko_data_handler import readData, getValueRange, normalizeValue
from environmental_features import SolarRipple

def createRippleObjects(data):
    """Create SolarRipple objects from dataset"""
    magMin, magMax = getValueRange(data, "MagSus (m3/kg)")
    
    ripples = []
    
    for record in data:
        year = record["Age (AD)"]
        magSus = record["MagSus (m3/kg)"]
        
        if magSus == "-" or not isinstance(magSus, (int, float)):
            continue
        
        normalized = normalizeValue(magSus, magMin, magMax)
        ripple = SolarRipple(year, magSus, normalized)
        ripples.append(ripple)
    
    return ripples

def drawBackgroundLake(win, centerX, centerY, radius):
    """Draw background lake surface"""
    lake = Circle(Point(centerX, centerY), radius)
    lake.setFill(color_rgb(30, 60, 90))
    lake.setOutline(color_rgb(20, 40, 70))
    lake.setWidth(3)
    lake.draw(win)

def createInfoPanel(win, x, y, width, height):
    """Create info panel for ripple data"""
    panel = Rectangle(Point(x, y), Point(x + width, y + height))
    panel.setFill(color_rgb(250, 250, 245))
    panel.setOutline(color_rgb(100, 100, 100))
    panel.setWidth(2)
    panel.draw(win)
    
    infoObjects = {}
    
    title = Text(Point(x + width/2, y + 30), "Solar Activity Data")
    title.setSize(16)
    title.setStyle("bold")
    title.draw(win)
    infoObjects['title'] = title
    
    yearText = Text(Point(x + width/2, y + 80), "Year: ----")
    yearText.setSize(15)
    yearText.draw(win)
    infoObjects['year'] = yearText
    
    magText = Text(Point(x + width/2, y + 120), "")
    magText.setSize(12)
    magText.draw(win)
    infoObjects['mag'] = magText
    
    depthText = Text(Point(x + width/2, y + 160), "Ripple Depth: ----")
    depthText.setSize(13)
    depthText.draw(win)
    infoObjects['depth'] = depthText
    
    explainText = Text(Point(x + width/2, y + 230), "")
    explainText.setSize(10)
    explainText.setFill(color_rgb(80, 80, 120))
    infoObjects['explain'] = explainText
    
    navText = Text(Point(x + width/2, y + height - 40), "Click: Next Year\n'q' to Quit")
    navText.setSize(11)
    navText.setFill(color_rgb(100, 100, 100))
    navText.draw(win)
    infoObjects['nav'] = navText
    
    return infoObjects

def updateInfoPanel(infoObjects, year, depth, normalized, magSusValue):
    """Update info panel with ripple data and explanations"""
    infoObjects['year'].setText(f"Year: {year} AD")
    infoObjects['mag'].setText(f"MagSus: {magSusValue:.2e} m³/kg")
    infoObjects['depth'].setText(f"Ripple Depth: {depth}/7 levels")
    
    if normalized > 0.7:
        explanation = "High magnetic susceptibility\nStrong solar activity\n\nMore concentric circles\n= Higher solar energy\n= Stronger magnetic field"
    elif normalized > 0.4:
        explanation = "Moderate susceptibility\nNormal solar activity\n\nMedium ripple count\n= Average solar energy\n= Typical magnetic field"
    else:
        explanation = "Low magnetic susceptibility\nWeak solar activity\n\nFewer concentric circles\n= Lower solar energy\n= Weaker magnetic field"
    
    infoObjects['explain'].setText(explanation)

def createVisualExplanation(win, centerX, bottomY):
    """Create explanation of visual representation"""
    explanationText = Text(Point(centerX, bottomY - 100), 
        "VISUAL GUIDE: Concentric circles represent magnetic susceptibility over time Each ring is drawn recursively\n" +
        "more rings = higher solar activity Lake sediments preserve magnetic particles that reflect solar cycles")
    explanationText.setSize(11)
    explanationText.setFill(color_rgb(200, 200, 255))
    explanationText.draw(win)
    
    dataExplanation = Text(Point(centerX, bottomY - 30),
        "DATA MEANING: Magnetic susceptibility (MagSus) measures how magnetic the sediment is\n" +
        "Higher values correlate with increased solar activity and lake level changes")
    dataExplanation.setSize(11)
    dataExplanation.setFill(color_rgb(180, 200, 255))
    dataExplanation.draw(win)

def animateThroughTime(win, ripples, centerX, centerY, baseRadius, infoObjects):
    """Animate through time showing solar activity"""
    currentIndex = 0
    isRunning = [True]
    
    def quitHandler(event):
        if event.char == 'q':
            isRunning[0] = False
    
    if ripples:
        ripple = ripples[currentIndex]
        ripple.draw(win, centerX, centerY, baseRadius)
        updateInfoPanel(infoObjects, ripple.getYear(), ripple.getRecursionDepth(), 
                       ripple.getNormalizedValue(), ripple.getValue())
    
    win.bind_all('<Key>', quitHandler)
    
    try:
        while currentIndex < len(ripples) and isRunning[0]:
            try:
                win.getMouse()
            except:
                break
            
            currentIndex += 1
            if currentIndex >= len(ripples):
                currentIndex = 0
            
            ripple = ripples[currentIndex]
            
            drawBackgroundLake(win, centerX, centerY, baseRadius + 50)
            ripple.draw(win, centerX, centerY, baseRadius)
            updateInfoPanel(infoObjects, ripple.getYear(), ripple.getRecursionDepth(),
                          ripple.getNormalizedValue(), ripple.getValue())
            
    except:
        pass

def runScene(width=1600, height=1200):
    """Run Scene 3"""
    win = GraphWin("Scene 3: Solar Ripples", width, height)
    win.setBackground(color_rgb(15, 30, 45))
    
    data = readData("data.json")
    ripples = createRippleObjects(data)
    ripples.sort(key=lambda r: r.getYear())
    
    centerX = width // 2
    centerY = height // 2
    baseRadius = min(width, height) // 3
    
    panelWidth = width // 3.5
    panelHeight = height // 4
    panelX = width // 40
    panelY = height // 10
    
    drawBackgroundLake(win, centerX, centerY, baseRadius + 50)
    infoObjects = createInfoPanel(win, panelX, panelY, int(panelWidth), int(panelHeight))
    
    sceneTitle = Text(Point(centerX, 60), "Solar Activity Through Time")
    sceneTitle.setSize(22)
    sceneTitle.setStyle("bold")
    sceneTitle.setFill(color_rgb(220, 220, 255))
    sceneTitle.draw(win)
    
    createVisualExplanation(win, centerX, height)
    
    animateThroughTime(win, ripples, centerX, centerY, baseRadius, infoObjects)
    
    try:
        win.close()
    except:
        pass

def main():
    """Test Scene 3"""
    runScene()

if __name__ == "__main__":
    main()
