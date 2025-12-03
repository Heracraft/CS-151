"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

scene2_forest.py
Scene 2: The Changing Forest - L-system visualization of climate conditions.
Uses Si/Ti ratio to determine tree complexity (aridity proxy).
Interactive: User inputs a year to see the corresponding forest.
"""

import sys
from lib.lsystem import Lsystem
from lib.turtle_interpreter import TurtleInterpreter
from masoko_data_handler import read_data, get_data_by_year, get_value_range, normalize_value
from environmental_features import ClimateTree


def create_tree_lsystem(complexity_level):
    """
    Create an L-system for tree generation with varying complexity.
    
    :param complexity_level: Integer from 1-5 determining tree complexity
    :return: Configured Lsystem object
    """
    lsys = Lsystem()
    
    # Base L-system rules for tree generation
    # More complex trees have different branching patterns
    if complexity_level >= 4:
        # Lush, complex tree (wet period)
        lsys.setBase("F")
        lsys.setRule({
            "F": "FF-[rF+F+F]+[gF-F-F]"
        })
    elif complexity_level >= 3:
        # Moderate tree
        lsys.setBase("F")
        lsys.setRule({
            "F": "F[+gF]F[-rF]F"
        })
    elif complexity_level >= 2:
        # Simple tree (drier conditions)
        lsys.setBase("F")
        lsys.setRule({
            "F": "F[+F][-F]"
        })
    else:
        # Sparse vegetation (very dry - Little Ice Age)
        lsys.setBase("F")
        lsys.setRule({
            "F": "FF[-F][+F]"
        })
    
    return lsys


def get_climate_description(si_ti_value, normalized_value):
    """
    Generate a description of climate conditions based on Si/Ti ratio.
    
    :param si_ti_value: The actual Si/Ti ratio
    :param normalized_value: Normalized value (0-1)
    :return: String description of climate
    """
    if normalized_value > 0.7:
        return f"Wet/Windy Period (Si/Ti: {si_ti_value:.2f})\nLush forest with complex branching"
    elif normalized_value > 0.5:
        return f"Moderate Climate (Si/Ti: {si_ti_value:.2f})\nHealthy forest growth"
    elif normalized_value > 0.3:
        return f"Drier Conditions (Si/Ti: {si_ti_value:.2f})\nSimpler vegetation patterns"
    else:
        return f"Dry Period (Si/Ti: {si_ti_value:.2f})\nSparse vegetation - possible Little Ice Age"


def draw_forest_for_year(year, data, distance=10, angle=25, bg_color=None):
    """
    Draw a forest representation for a specific year using L-systems.
    
    :param year: Year (AD) to visualize
    :param data: Dataset from masoko_data_handler
    :param distance: Forward distance for turtle drawing
    :param angle: Angle for turtle turns
    :param bg_color: Background color (optional)
    """
    # Get data for the specified year
    record = get_data_by_year(data, year)
    
    if not record:
        print(f"No data found for year {year}")
        return
    
    actual_year = record["Age (AD)"]
    si_ti = record["Si/Ti"]
    
    # Check if Si/Ti data is available
    if si_ti == "-" or not isinstance(si_ti, (int, float)):
        print(f"No Si/Ti data available for year {actual_year}")
        return
    
    # Get Si/Ti range for normalization
    si_min, si_max = get_value_range(data, "Si/Ti")
    normalized = normalize_value(si_ti, si_min, si_max)
    
    # Create ClimateTree object
    tree = ClimateTree(actual_year, si_ti, normalized)
    iterations = tree.get_iterations()
    
    # Get climate description
    description = get_climate_description(si_ti, normalized)
    
    # Print information
    print("\n" + "="*60)
    print(f"Year: {actual_year} AD (requested: {year})")
    print(description)
    print(f"L-system iterations: {iterations}")
    print("="*60)
    
    # Create L-system based on complexity
    lsys = create_tree_lsystem(iterations)
    
    # Create turtle interpreter
    interpreter = TurtleInterpreter(800, 800, bgColor=bg_color)
    
    # Position turtle at bottom center, facing up
    interpreter.place(xpos=0, ypos="end", angle=90)
    interpreter.setColor((101, 67, 33))  # Brown trunk
    interpreter.setWidth(2)
    
    # Draw the tree using the ClimateTree object
    tree.draw(interpreter, lsys, distance, angle)
    
    # Hold the window open
    interpreter.hold()


def get_year_from_user(min_year, max_year):
    """
    Prompt user for a year within the data range.
    
    :param min_year: Minimum year in dataset
    :param max_year: Maximum year in dataset
    :return: Year entered by user, or None if invalid
    """
    print(f"\nEnter a year between {min_year} and {max_year} AD")
    print("(or type 'quit' to exit)")
    
    user_input = input("Year: ").strip()
    
    if user_input.lower() in ['quit', 'q', 'exit']:
        return None
    
    try:
        year = int(user_input)
        if min_year <= year <= max_year:
            return year
        else:
            print(f"Year must be between {min_year} and {max_year}")
            return get_year_from_user(min_year, max_year)
    except ValueError:
        print("Please enter a valid year (integer)")
        return get_year_from_user(min_year, max_year)


def run_scene_interactive():
    """
    Run Scene 2 in interactive mode - user chooses years to visualize.
    """
    # Load data
    print("Loading Lake Masoko data...")
    data = read_data("data.json")
    
    # Get year range
    from masoko_data_handler import get_year_range
    min_year, max_year = get_year_range(data)
    
    print("\n" + "="*60)
    print("Scene 2: The Changing Forest")
    print("="*60)
    print(f"\nAvailable data: {min_year}-{max_year} AD")
    print("\nThis scene uses Si/Ti ratios (aridity proxy) to visualize")
    print("how climate conditions affected vegetation over 500 years.")
    print("\nHigh Si/Ti = Wet/Windy = Lush, complex trees")
    print("Low Si/Ti = Dry (Little Ice Age) = Sparse vegetation")
    
    # Get year from user
    year = get_year_from_user(min_year, max_year)
    
    if year is None:
        print("Exiting Scene 2.")
        return
    
    # Draw forest for the selected year
    draw_forest_for_year(year, data)


def run_scene_with_year(year):
    """
    Run Scene 2 for a specific year (non-interactive).
    
    :param year: Year (AD) to visualize
    """
    # Load data
    data = read_data("data.json")
    
    # Draw forest for the year
    draw_forest_for_year(year, data)


def main():
    """Test function for Scene 2."""
    # Check if year is provided as command-line argument
    if len(sys.argv) > 1:
        try:
            year = int(sys.argv[1])
            run_scene_with_year(year)
        except ValueError:
            print(f"Error: '{sys.argv[1]}' is not a valid year")
            print("Usage: python scene2_forest.py [year]")
    else:
        # Interactive mode
        run_scene_interactive()


if __name__ == "__main__":
    main()
