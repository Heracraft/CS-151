"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

scene1_sediment.py
Scene 1: The Sediment Core - Data-driven visualization of lake sediment layers.
Uses Fe/Ti ratio to visualize iron content over 500 years (1511-2002 AD).
Interactive: Click on layers to see year and chemical composition.
"""

from graphics import GraphWin, Text, Point, color_rgb
from masoko_data_handler import read_data, get_value_range, normalize_value
from environmental_features import SedimentLayer


def create_sediment_layers(data, x=500, y_start=100, layer_height=16):
    """
    Create SedimentLayer objects from the dataset.
    
    :param data: List of data dictionaries from masoko_data_handler
    :param x: X position for the center of layers (default: 500)
    :param y_start: Y position to start drawing (default: 100)
    :param layer_height: Height of each layer in pixels (default: 16)
    :return: List of SedimentLayer objects
    """
    # Get Fe/Ti value range for normalization
    fe_min, fe_max = get_value_range(data, "Fe/Ti")
    
    layers = []
    y_pos = y_start
    
    # Create layers from newest (top) to oldest (bottom)
    for record in data:
        year = record["Age (AD)"]
        fe_ti = record["Fe/Ti"]
        depth = record["Depth (cm)"]
        
        # Skip if Fe/Ti data is missing
        if fe_ti == "-" or not isinstance(fe_ti, (int, float)):
            continue
        
        # Normalize Fe/Ti value for color calculation
        normalized = normalize_value(fe_ti, fe_min, fe_max)
        
        # Create sediment layer object
        layer = SedimentLayer(year, fe_ti, depth, normalized)
        layer.set_height(layer_height)
        layer.y_position = y_pos  # Store y position for drawing
        
        layers.append(layer)
        y_pos += layer_height
    
    return layers


def draw_sediment_core(win, layers, title="The Sediment Core: 500 Years of Lake History"):
    """
    Draw all sediment layers in the window.
    
    :param win: GraphWin object to draw on
    :param layers: List of SedimentLayer objects
    :param title: Title text for the visualization
    :return: List of drawn layers with their y positions
    """
    # Draw title
    title_text = Text(Point(500, 40), title)
    title_text.setSize(18)
    title_text.setStyle("bold")
    title_text.draw(win)
    
    # Draw instruction text
    instruction = Text(Point(500, 70), "Click on a layer to see its data")
    instruction.setSize(12)
    instruction.setFill(color_rgb(100, 100, 100))
    instruction.draw(win)
    
    # Draw each layer
    drawn_layers = []
    for layer in layers:
        layer.draw(win, 250, layer.y_position)
        drawn_layers.append(layer)
    
    # Draw year labels on the side
    if layers:
        # Oldest layer (bottom)
        oldest = layers[-1]
        oldest_label = Text(Point(640, oldest.y_position + 8), 
                           f"{oldest.get_year()} AD")
        oldest_label.setSize(12)
        oldest_label.draw(win)
        
        # Newest layer (top)
        newest = layers[0]
        newest_label = Text(Point(640, newest.y_position + 8), 
                           f"{newest.get_year()} AD")
        newest_label.setSize(12)
        newest_label.draw(win)
        
        # Middle layer
        middle_idx = len(layers) // 2
        middle = layers[middle_idx]
        middle_label = Text(Point(640, middle.y_position + 8), 
                           f"{middle.get_year()} AD")
        middle_label.setSize(12)
        middle_label.draw(win)
    
    return drawn_layers


def create_info_display(win, x=140, y=400):
    """
    Create text objects for displaying layer information.
    
    :param win: GraphWin object
    :param x: X position for info display
    :param y: Y position for info display
    :return: Dictionary of Text objects for updating
    """
    info_objects = {}
    
    # Title for info panel
    title = Text(Point(x, y - 60), "Layer Information")
    title.setSize(16)
    title.setStyle("bold")
    title.draw(win)
    
    # Year label
    year_label = Text(Point(x, y), "Year: Click a layer")
    year_label.setSize(13)
    year_label.draw(win)
    info_objects['year'] = year_label
    
    # Fe/Ti label
    fe_ti_label = Text(Point(x, y + 40), "Fe/Ti: -")
    fe_ti_label.setSize(13)
    fe_ti_label.draw(win)
    info_objects['fe_ti'] = fe_ti_label
    
    # Depth label
    depth_label = Text(Point(x, y + 80), "Depth: -")
    depth_label.setSize(13)
    depth_label.draw(win)
    info_objects['depth'] = depth_label
    
    # Interpretation label
    interp_label = Text(Point(x, y + 140), "")
    interp_label.setSize(12)
    interp_label.setFill(color_rgb(80, 80, 120))
    interp_label.draw(win)
    info_objects['interpretation'] = interp_label
    
    return info_objects


def update_info_display(info_objects, layer):
    """
    Update the information display with layer data.
    
    :param info_objects: Dictionary of Text objects from create_info_display
    :param layer: SedimentLayer object to display
    """
    # Update year
    info_objects['year'].setText(f"Year: {layer.get_year()} AD")
    
    # Update Fe/Ti
    info_objects['fe_ti'].setText(f"Fe/Ti: {layer.get_value():.2f}")
    
    # Update depth
    info_objects['depth'].setText(f"Depth: {layer.get_depth():.2f} cm")
    
    # Add interpretation based on Fe/Ti value
    fe_ti = layer.get_value()
    if fe_ti > 4.0:
        interpretation = "High iron:\nWet period with\nincreased erosion"
    elif fe_ti < 3.5:
        interpretation = "Low iron:\nDry period\n(Little Ice Age?)"
    else:
        interpretation = "Moderate iron:\nNormal conditions"
    
    info_objects['interpretation'].setText(interpretation)


def handle_click(win, layers, info_objects):
    """
    Handle mouse clicks on sediment layers.
    
    :param win: GraphWin object
    :param layers: List of SedimentLayer objects
    :param info_objects: Dictionary of Text objects for info display
    """
    click_point = win.getMouse()
    
    # Check which layer was clicked
    for layer in layers:
        if layer.contains_point(click_point):
            update_info_display(info_objects, layer)
            return True
    
    return False


def run_scene(width=1000, height=1300):
    """
    Main function to run Scene 1: The Sediment Core.
    
    :param width: Window width in pixels
    :param height: Window height in pixels
    """
    # Create window
    win = GraphWin("Scene 1: The Sediment Core", width, height)
    win.setBackground(color_rgb(240, 240, 235))
    
    # Load data
    print("Loading Lake Masoko data...")
    data = read_data("data.json")
    print(f"Loaded {len(data)} records from {data[-1]['Age (AD)']} to {data[0]['Age (AD)']} AD")
    
    # Create sediment layers
    print("Creating sediment layers...")
    center_x = width // 2
    layers = create_sediment_layers(data, x=center_x, y_start=100, layer_height=16)
    print(f"Created {len(layers)} sediment layers")
    
    # Draw the sediment core
    print("Drawing sediment core...")
    drawn_layers = draw_sediment_core(win, layers)
    
    # Create info display (left side, vertically centered)
    info_x = width // 7  # About 1/7 from left
    info_y = height // 2  # Vertically centered
    info_objects = create_info_display(win, x=info_x, y=info_y)
    
    # Add legend (left side, lower portion)
    legend_x = width // 7
    legend_y = height * 0.62  # About 62% down
    legend_title = Text(Point(legend_x, legend_y), "Color Legend")
    legend_title.setSize(14)
    legend_title.setStyle("bold")
    legend_title.draw(win)
    
    legend_text = Text(Point(legend_x, legend_y + 60), "Darker = Higher Fe/Ti\n(More iron/erosion)\n\nLighter = Lower Fe/Ti\n(Drier conditions)")
    legend_text.setSize(12)
    legend_text.draw(win)
    
    # Add close instruction (centered at bottom)
    close_text = Text(Point(center_x, height - 40), "Click anywhere to interact | Close window to exit")
    close_text.setSize(12)
    close_text.setFill(color_rgb(100, 100, 100))
    close_text.draw(win)
    
    print("\nScene ready! Click on layers to see their data.")
    print("Close the window to exit.")
    
    # Interactive loop
    try:
        while True:
            handle_click(win, drawn_layers, info_objects)
    except:
        # Window closed
        pass
    
    win.close()


def main():
    """Test function for Scene 1."""
    print("="*60)
    print("Scene 1: The Sediment Core")
    print("="*60)
    print("\nThis scene visualizes Lake Masoko sediment layers using")
    print("Fe/Ti (Iron/Titanium) ratios to show climate changes")
    print("from 1511-2002 AD.")
    print("\nStarting visualization...")
    print("="*60)
    
    run_scene()


if __name__ == "__main__":
    main()
