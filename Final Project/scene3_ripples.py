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
    
    title = Text(Point(x + width/2, y + 40), "Solar Activity")
    title.setSize(18)
    title.setStyle("bold")
    title.draw(win)
    infoObjects['title'] = title
    
    yearText = Text(Point(x + width/2, y + 100), "Year: ----")
    yearText.setSize(16)
    yearText.draw(win)
    infoObjects['year'] = yearText
    
    depthText = Text(Point(x + width/2, y + 150), "Intensity: ----")
    depthText.setSize(13)
    depthText.draw(win)
    infoObjects['depth'] = depthText
    
    explainText = Text(Point(x + width/2, y + 220), "")
    explainText.setSize(11)
    explainText.setFill(color_rgb(80, 80, 120))
    infoObjects['explain'] = explainText
    
    navText = Text(Point(x + width/2, y + height - 60), "Click: Next\n'q' to Quit")
    navText.setSize(12)
    navText.setFill(color_rgb(100, 100, 100))
    navText.draw(win)
    infoObjects['nav'] = navText
    
    return infoObjects

def updateInfoPanel(infoObjects, year, depth, normalized):
    """Update info panel with ripple data"""
    infoObjects['year'].setText(f"Year: {year} AD")
    infoObjects['depth'].setText(f"Intensity: {depth}/7")
    
    if normalized > 0.7:
        explanation = "High magnetic\nsusceptibility\nStrong solar activity"
    elif normalized > 0.4:
        explanation = "Moderate magnetic\nsusceptibility\nNormal solar activity"
    else:
        explanation = "Low magnetic\nsusceptibility\nWeak solar activity"
    
    infoObjects['explain'].setText(explanation)

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
        updateInfoPanel(infoObjects, ripple.getYear(), ripple.getRecursionDepth(), ripple.getNormalizedValue())
    
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
            updateInfoPanel(infoObjects, ripple.getYear(), ripple.getRecursionDepth(), ripple.getNormalizedValue())
            
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
    
    panelWidth = width // 4
    panelHeight = height // 2.5
    panelX = width // 40
    panelY = height // 30
    
    drawBackgroundLake(win, centerX, centerY, baseRadius + 50)
    infoObjects = createInfoPanel(win, panelX, panelY, int(panelWidth), int(panelHeight))
    
    sceneTitle = Text(Point(centerX, 60), "Solar Activity Through Time")
    sceneTitle.setSize(20)
    sceneTitle.setStyle("bold")
    sceneTitle.setFill(color_rgb(220, 220, 255))
    sceneTitle.draw(win)
    
    explanation = Text(Point(centerX, width - 100), "MagSus shows magnetic susceptibility\nMore ripples = Higher solar activity")
    explanation.setSize(12)
    explanation.setFill(color_rgb(200, 200, 255))
    explanation.draw(win)
    
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
