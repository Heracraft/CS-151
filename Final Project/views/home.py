"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

views/home.py
Home page/scene selector for navigating between the three scenes.
Provides an interactive graphical interface to launch each scene.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from graphics import GraphWin, Text, Point, Rectangle, color_rgb


def create_scene_button(win, x, y, width, height, scene_num, title, description):
    """
    Create a clickable button for a scene.
    
    :param win: GraphWin object
    :param x: X position (top-left corner)
    :param y: Y position (top-left corner)
    :param width: Button width
    :param height: Button height
    :param scene_num: Scene number (1, 2, or 3)
    :param title: Scene title
    :param description: Brief description
    :return: Dictionary with button rectangle and bounds
    """
    # Create button rectangle
    button = Rectangle(Point(x, y), Point(x + width, y + height))
    
    # Set colors based on scene number
    if scene_num == 1:
        fill_color = color_rgb(139, 115, 85)  # Brown/sediment color
        text_color = color_rgb(255, 255, 255)
    elif scene_num == 2:
        fill_color = color_rgb(76, 153, 76)  # Green/forest color
        text_color = color_rgb(255, 255, 255)
    else:  # scene 3
        fill_color = color_rgb(70, 130, 180)  # Blue/water color
        text_color = color_rgb(255, 255, 255)
    
    button.setFill(fill_color)
    button.setOutline(color_rgb(50, 50, 50))
    button.setWidth(3)
    button.draw(win)
    
    # Scene number badge
    badge = Text(Point(x + 40, y + 40), str(scene_num))
    badge.setSize(24)
    badge.setStyle("bold")
    badge.setFill(text_color)
    badge.draw(win)
    
    # Scene title
    title_text = Text(Point(x + width/2, y + 50), title)
    title_text.setSize(20)
    title_text.setStyle("bold")
    title_text.setFill(text_color)
    title_text.draw(win)
    
    # Scene description
    desc_text = Text(Point(x + width/2, y + 100), description)
    desc_text.setSize(14)
    desc_text.setFill(text_color)
    desc_text.draw(win)
    
    return {
        'button': button,
        'x1': x,
        'y1': y,
        'x2': x + width,
        'y2': y + height,
        'scene': scene_num
    }


def check_button_click(point, buttons):
    """
    Check if a point is inside any button.
    
    :param point: Point object from mouse click
    :param buttons: List of button dictionaries
    :return: Scene number if clicked, None otherwise
    """
    x, y = point.getX(), point.getY()
    
    for button in buttons:
        if (button['x1'] <= x <= button['x2'] and 
            button['y1'] <= y <= button['y2']):
            return button['scene']
    
    return None


def run_home_page():
    """
    Display the home page and return the selected scene number.
    
    :return: Scene number (1, 2, 3) or 0 for exit
    """
    # Create main window
    win = GraphWin("The Breathing Lake - Scene Selection", 1200, 900)
    win.setBackground(color_rgb(240, 240, 235))
    
    # Main title
    main_title = Text(Point(600, 80), "THE BREATHING LAKE")
    main_title.setSize(32)
    main_title.setStyle("bold")
    main_title.setFill(color_rgb(20, 60, 100))
    main_title.draw(win)
    
    # Subtitle
    subtitle = Text(Point(600, 130), "500 Years of Climate Change")
    subtitle.setSize(18)
    subtitle.setFill(color_rgb(80, 80, 80))
    subtitle.draw(win)
    
    # Project info
    info_text = Text(Point(600, 170), "Lake Masoko, Tanzania • 1511-2002 AD")
    info_text.setSize(14)
    info_text.setFill(color_rgb(100, 100, 100))
    info_text.draw(win)
    
    # Instructions
    instruction = Text(Point(600, 220), "Click on a scene to begin")
    instruction.setSize(16)
    instruction.setStyle("bold")
    instruction.setFill(color_rgb(60, 60, 60))
    instruction.draw(win)
    
    # Create scene buttons
    buttons = []
    
    # Scene 1 button
    button1 = create_scene_button(
        win, 150, 280, 300, 180, 1,
        "The Sediment Core",
        "Interactive data\nvisualization\nFe/Ti ratios"
    )
    buttons.append(button1)
    
    # Scene 2 button
    button2 = create_scene_button(
        win, 450, 280, 300, 180, 2,
        "The Changing Forest",
        "L-system trees\nClimate patterns\nSi/Ti aridity"
    )
    buttons.append(button2)
    
    # Scene 3 button
    button3 = create_scene_button(
        win, 750, 280, 300, 180, 3,
        "The Solar Ripples",
        "Recursive patterns\nSolar activity\nMagnetic data"
    )
    buttons.append(button3)
    
    # Add scene details
    details_y = 500
    
    # Scene 1 details
    detail1_title = Text(Point(300, details_y), "Scene 1: Sediment Core")
    detail1_title.setSize(14)
    detail1_title.setStyle("bold")
    detail1_title.draw(win)
    
    detail1_text = Text(Point(300, details_y + 40), 
                        "Click on sediment layers to explore\n65 years of geochemical data\nSee iron content and climate")
    detail1_text.setSize(11)
    detail1_text.draw(win)
    
    # Scene 2 details
    detail2_title = Text(Point(600, details_y), "Scene 2: Forest")
    detail2_title.setSize(14)
    detail2_title.setStyle("bold")
    detail2_title.draw(win)
    
    detail2_text = Text(Point(600, details_y + 40),
                        "Enter any year from 1511-2002\nWatch vegetation change\nSee climate interpretations")
    detail2_text.setSize(11)
    detail2_text.draw(win)
    
    # Scene 3 details
    detail3_title = Text(Point(900, details_y), "Scene 3: Solar Ripples")
    detail3_title.setSize(14)
    detail3_title.setStyle("bold")
    detail3_title.draw(win)
    
    detail3_text = Text(Point(900, details_y + 40),
                        "Click to progress through time\nRecursive ripple patterns\nSolar activity cycles")
    detail3_text.setSize(11)
    detail3_text.draw(win)
    
    # Technical info at bottom
    tech_info = Text(Point(600, 650), 
                    "Technologies: Object-Oriented Programming • L-Systems • Recursion • Data Visualization")
    tech_info.setSize(11)
    tech_info.setFill(color_rgb(120, 120, 120))
    tech_info.draw(win)
    
    # Credits
    credits = Text(Point(600, 690),
                  "Nehemia Kaaya • CS 151 Section B • Fall 2025")
    credits.setSize(12)
    credits.setFill(color_rgb(100, 100, 100))
    credits.draw(win)
    
    # Exit button
    exit_button = Rectangle(Point(500, 750), Point(700, 820))
    exit_button.setFill(color_rgb(200, 200, 200))
    exit_button.setOutline(color_rgb(100, 100, 100))
    exit_button.setWidth(2)
    exit_button.draw(win)
    
    exit_text = Text(Point(600, 785), "Exit")
    exit_text.setSize(18)
    exit_text.setStyle("bold")
    exit_text.setFill(color_rgb(60, 60, 60))
    exit_text.draw(win)
    
    buttons.append({
        'button': exit_button,
        'x1': 500,
        'y1': 750,
        'x2': 700,
        'y2': 820,
        'scene': 0
    })
    
    # Wait for click
    print("\n" + "="*60)
    print("Home Page displayed - Click a scene to begin")
    print("="*60)
    
    try:
        while True:
            click_point = win.getMouse()
            scene = check_button_click(click_point, buttons)
            
            if scene is not None:
                win.close()
                return scene
    except:
        win.close()
        return 0


def main():
    """Test function for home page."""
    scene = run_home_page()
    print(f"\nSelected scene: {scene}")
    
    if scene == 0:
        print("User chose to exit")
    else:
        print(f"Would launch Scene {scene}")


if __name__ == "__main__":
    main()
