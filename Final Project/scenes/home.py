"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

Home page for scene selection
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.graphicsPlus import GraphWin, Text, Point, Rectangle, color_rgb

def createSceneButton(win, x, y, width, height, sceneNum, title):
    """Create a clickable button for a scene"""
    button = Rectangle(Point(x, y), Point(x + width, y + height))
    
    if sceneNum == 1:
        fillColor = color_rgb(139, 115, 85)
        textColor = color_rgb(255, 255, 255)
    elif sceneNum == 2:
        fillColor = color_rgb(76, 153, 76)
        textColor = color_rgb(255, 255, 255)
    else:
        fillColor = color_rgb(70, 130, 180)
        textColor = color_rgb(255, 255, 255)
    
    button.setFill(fillColor)
    button.setOutline(color_rgb(50, 50, 50))
    button.setWidth(3)
    button.draw(win)
    
    badge = Text(Point(x + 50, y + 50), str(sceneNum))
    badge.setSize(28)
    badge.setStyle("bold")
    badge.setFill(textColor)
    badge.draw(win)
    
    centerX = x + width/2
    centerY = y + height/2
    titleText = Text(Point(centerX, centerY), title)
    titleText.setSize(16)
    titleText.setStyle("bold")
    titleText.setFill(textColor)
    titleText.draw(win)
    
    return {
        'button': button,
        'x1': x,
        'y1': y,
        'x2': x + width,
        'y2': y + height,
        'scene': sceneNum
    }

def checkButtonClick(point, buttons):
    """Check if a point is inside any button"""
    x, y = point.getX(), point.getY()
    
    for button in buttons:
        if (button['x1'] <= x <= button['x2'] and 
            button['y1'] <= y <= button['y2']):
            return button['scene']
    
    return None

def runHomePage():
    """Display the home page and return selected scene number"""
    win = GraphWin("The Breathing Lake", 1200, 900)
    win.setBackground(color_rgb(240, 240, 235))
    
    mainTitle = Text(Point(600, 80), "THE BREATHING LAKE")
    mainTitle.setSize(28)
    mainTitle.setStyle("bold")
    mainTitle.setFill(color_rgb(20, 60, 100))
    mainTitle.draw(win)
    
    subtitle = Text(Point(600, 130), "Click a scene to begin")
    subtitle.setSize(14)
    subtitle.setFill(color_rgb(80, 80, 80))
    subtitle.draw(win)
    
    description = Text(Point(600, 450), 
        "Lake Masoko's sediment layers preserve 500 years of climate history.\n" +
        "Geological data reveals solar cycles, rainfall patterns, and vegetation changes.\n" +
        "Iron ratios show wet vs dry periods. Silicon levels indicate tree growth.\n" +
        "Magnetic particles record solar activity - all visualized through interactive art.")
    description.setSize(11)
    description.setFill(color_rgb(60, 60, 80))
    description.draw(win)
    
    buttons = []
    
    button1 = createSceneButton(win, 150, 200, 280, 180, 1, "Sediment Core")
    buttons.append(button1)
    
    button2 = createSceneButton(win, 460, 200, 280, 180, 2, "Rain Forest")
    buttons.append(button2)
    
    button3 = createSceneButton(win, 770, 200, 280, 180, 3, "Solar Clock")
    buttons.append(button3)
    
    exitButton = Rectangle(Point(500, 550), Point(700, 620))
    exitButton.setFill(color_rgb(200, 200, 200))
    exitButton.setOutline(color_rgb(100, 100, 100))
    exitButton.setWidth(2)
    exitButton.draw(win)
    
    exitText = Text(Point(600, 585), "Exit")
    exitText.setSize(16)
    exitText.setStyle("bold")
    exitText.setFill(color_rgb(60, 60, 60))
    exitText.draw(win)
    
    buttons.append({
        'button': exitButton,
        'x1': 500,
        'y1': 550,
        'x2': 700,
        'y2': 620,
        'scene': 0
    })
    
    try:
        while True:
            clickPoint = win.getMouse()
            scene = checkButtonClick(clickPoint, buttons)
            
            if scene is not None:
                win.close()
                return scene
    except Exception:
        try:
            win.close()
        except:
            pass
        return 0

def main():
    """Test function for home page"""
    scene = runHomePage()
    print(f"\nSelected scene: {scene}")

if __name__ == "__main__":
    main()
