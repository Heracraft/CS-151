"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

scene3_ripples.py
Scene 3: The Solar Ripples - Recursive visualization of solar activity cycles.
Uses MagSus (Magnetic Susceptibility) to determine recursion depth.
Interactive: Navigate through time to see changing solar activity.
"""

from graphics import GraphWin, Text, Point, color_rgb, Circle
from masoko_data_handler import read_data, get_value_range, normalize_value
from environmental_features import SolarRipple
import time


def create_ripple_objects(data):
    """
    Create SolarRipple objects from the dataset.
    
    :param data: List of data dictionaries from masoko_data_handler
    :return: List of SolarRipple objects
    """
    # Get MagSus value range for normalization
    mag_min, mag_max = get_value_range(data, "MagSus (m3/kg)")
    
    ripples = []
    
    for record in data:
        year = record["Age (AD)"]
        mag_sus = record["MagSus (m3/kg)"]
        
        # Skip if MagSus data is missing
        if mag_sus == "-" or not isinstance(mag_sus, (int, float)):
            continue
        
        # Normalize MagSus value
        normalized = normalize_value(mag_sus, mag_min, mag_max)
        
        # Create solar ripple object
        ripple = SolarRipple(year, mag_sus, normalized)
        ripples.append(ripple)
    
    return ripples


def draw_background_lake(win, center_x, center_y, radius):
    """
    Draw the background lake surface.
    
    :param win: GraphWin object
    :param center_x: X coordinate of lake center
    :param center_y: Y coordinate of lake center
    :param radius: Radius of the lake
    """
    # Draw the lake as a large circle
    lake = Circle(Point(center_x, center_y), radius)
    lake.setFill(color_rgb(30, 60, 90))
    lake.setOutline(color_rgb(20, 40, 70))
    lake.setWidth(3)
    lake.draw(win)


def draw_ripple_scene(win, ripple, center_x, center_y, base_radius):
    """
    Draw a solar ripple scene for a specific year.
    
    :param win: GraphWin object
    :param ripple: SolarRipple object to draw
    :param center_x: X coordinate of center
    :param center_y: Y coordinate of center
    :param base_radius: Base radius for ripples
    :return: Text objects for info display
    """
    # Clear previous ripples (by drawing background again)
    draw_background_lake(win, center_x, center_y, base_radius + 50)
    
    # Draw the ripples
    ripple.draw(win, center_x, center_y, base_radius)
    
    # Return info for updating
    return {
        'year': ripple.get_year(),
        'mag_sus': ripple.get_value(),
        'depth': ripple.get_recursion_depth()
    }


def create_info_panel(win, x, y, width, height):
    """
    Create an information panel for displaying ripple data.
    
    :param win: GraphWin object
    :param x: X position (top-left)
    :param y: Y position (top-left)
    :param width: Panel width
    :param height: Panel height
    :return: Dictionary of Text objects
    """
    from graphics import Rectangle
    
    # Draw panel background
    panel = Rectangle(Point(x, y), Point(x + width, y + height))
    panel.setFill(color_rgb(250, 250, 245))
    panel.setOutline(color_rgb(100, 100, 100))
    panel.setWidth(2)
    panel.draw(win)
    
    info_objects = {}
    
    # Title
    title = Text(Point(x + width/2, y + 40), "Solar Activity Cycles")
    title.setSize(18)
    title.setStyle("bold")
    title.draw(win)
    info_objects['title'] = title
    
    # Year display
    year_text = Text(Point(x + width/2, y + 100), "Year: ----")
    year_text.setSize(16)
    year_text.draw(win)
    info_objects['year'] = year_text
    
    # MagSus display
    mag_text = Text(Point(x + width/2, y + 150), "MagSus: ----")
    mag_text.setSize(13)
    mag_text.draw(win)
    info_objects['mag'] = mag_text
    
    # Recursion depth display
    depth_text = Text(Point(x + width/2, y + 190), "Intensity: ----")
    depth_text.setSize(13)
    depth_text.draw(win)
    info_objects['depth'] = depth_text
    
    # Interpretation
    interp_text = Text(Point(x + width/2, y + 260), "")
    interp_text.setSize(12)
    interp_text.setFill(color_rgb(80, 80, 120))
    interp_text.draw(win)
    info_objects['interpretation'] = interp_text
    
    # Navigation instructions
    nav_text = Text(Point(x + width/2, y + height - 60), "Click: Next Period\n'q' to Quit")
    nav_text.setSize(12)
    nav_text.setFill(color_rgb(100, 100, 100))
    nav_text.draw(win)
    info_objects['nav'] = nav_text
    
    return info_objects


def update_info_panel(info_objects, year, mag_sus, depth, normalized_value):
    """
    Update the information panel with current ripple data.
    
    :param info_objects: Dictionary of Text objects
    :param year: Year (AD)
    :param mag_sus: Magnetic susceptibility value
    :param depth: Recursion depth
    :param normalized_value: Normalized MagSus (0-1)
    """
    # Update year
    info_objects['year'].setText(f"Year: {year} AD")
    
    # Update MagSus
    info_objects['mag'].setText(f"MagSus: {mag_sus:.2e} m³/kg")
    
    # Update recursion depth
    info_objects['depth'].setText(f"Intensity Level: {depth}/7")
    
    # Generate interpretation
    if normalized_value > 0.7:
        interpretation = "High solar activity\nStrong magnetic signal\nHigh lake levels"
    elif normalized_value > 0.4:
        interpretation = "Moderate activity\nNormal conditions"
    else:
        interpretation = "Low solar activity\nWeak magnetic signal\nLower lake levels"
    
    info_objects['interpretation'].setText(interpretation)


def animate_through_time(win, ripples, center_x, center_y, base_radius, info_objects):
    """
    Animate through time showing changing solar activity.
    
    :param win: GraphWin object
    :param ripples: List of SolarRipple objects
    :param center_x: X coordinate of center
    :param center_y: Y coordinate of center
    :param base_radius: Base radius for ripples
    :param info_objects: Dictionary of Text objects for info panel
    """
    current_index = 0
    is_running = [True]  # Use list to allow modification in nested function
    
    def quit_handler(event):
        """Handle quit key press safely."""
        if event.char == 'q':
            is_running[0] = False
    
    # Draw initial ripple
    if ripples:
        ripple = ripples[current_index]
        draw_ripple_scene(win, ripple, center_x, center_y, base_radius)
        update_info_panel(info_objects, ripple.get_year(), ripple.get_value(), 
                         ripple.get_recursion_depth(), ripple.get_normalized_value())
    
    # Set up key handler for 'q' to quit
    win.bind_all('<Key>', quit_handler)
    
    # Animation loop
    try:
        while current_index < len(ripples) and is_running[0]:
            # Wait for click or key press
            try:
                win.getMouse()
            except:
                # Window closed or 'q' pressed
                break
            
            # Move to next ripple
            current_index += 1
            if current_index >= len(ripples):
                current_index = 0  # Loop back to start
            
            ripple = ripples[current_index]
            
            # Redraw background
            draw_background_lake(win, center_x, center_y, base_radius + 50)
            
            # Draw new ripple
            draw_ripple_scene(win, ripple, center_x, center_y, base_radius)
            
            # Update info
            update_info_panel(info_objects, ripple.get_year(), ripple.get_value(),
                            ripple.get_recursion_depth(), ripple.get_normalized_value())
            
    except:
        # Window closed
        pass


def run_scene(width=1600, height=1200):
    """
    Main function to run Scene 3: The Solar Ripples.
    
    :param width: Window width in pixels
    :param height: Window height in pixels
    """
    # Create window
    win = GraphWin("Scene 3: The Solar Ripples", width, height)
    win.setBackground(color_rgb(15, 30, 45))
    
    # Load data
    print("Loading Lake Masoko data...")
    data = read_data("data.json")
    print(f"Loaded {len(data)} records")
    
    # Create ripple objects
    print("Creating solar ripple objects...")
    ripples = create_ripple_objects(data)
    print(f"Created {len(ripples)} ripple objects")
    
    # Sort ripples by year (oldest to newest)
    ripples.sort(key=lambda r: r.get_year())
    
    # Set up visualization parameters
    center_x = width // 2
    center_y = height // 2
    base_radius = min(width, height) // 3
    
    # Draw background lake
    draw_background_lake(win, center_x, center_y, base_radius + 50)
    
    # Create info panel
    info_objects = create_info_panel(win, 40, 40, 400, 360)
    
    # Add scene title
    scene_title = Text(Point(center_x, 60), "Lake Masoko: Solar Activity Through Time")
    scene_title.setSize(20)
    scene_title.setStyle("bold")
    scene_title.setFill(color_rgb(220, 220, 255))
    scene_title.draw(win)
    
    print("\n" + "="*60)
    print("Scene 3: The Solar Ripples")
    print("="*60)
    print("Click to progress through time and see how solar activity")
    print("(reflected in magnetic susceptibility) changed over 500 years.")
    print("\nPress 'q' to quit or close the window.")
    print("="*60)
    
    # Run animation
    animate_through_time(win, ripples, center_x, center_y, base_radius, info_objects)
    
    # Close window
    try:
        win.close()
    except:
        pass


def main():
    """Test function for Scene 3."""
    print("="*60)
    print("Scene 3: The Solar Ripples")
    print("="*60)
    print("\nThis scene visualizes solar activity cycles using")
    print("recursive ripple patterns based on magnetic susceptibility.")
    print("\nStarting visualization...")
    print("="*60)
    
    run_scene()


if __name__ == "__main__":
    main()
