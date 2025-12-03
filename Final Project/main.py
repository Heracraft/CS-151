"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

main.py
Main controller for the Interactive Environmental Art project.
Provides both graphical home page and text menu to navigate between scenes:
1. The Sediment Core (Zelle graphics, data visualization)
2. The Changing Forest (L-systems, climate)
3. The Solar Ripples (Recursion, solar activity)

Usage:
    python main.py              # Graphical home page (default)
    python main.py --text       # Text menu mode
    python main.py scene1       # Run Scene 1 directly
    python main.py scene2       # Run Scene 2 directly
    python main.py scene2 1750  # Run Scene 2 for year 1750
    python main.py scene3       # Run Scene 3 directly
"""

import sys
import os


def print_banner():
    """Display the project banner."""
    print("\n" + "="*70)
    print(" " * 10 + "THE BREATHING LAKE: 500 YEARS OF CHANGE")
    print(" " * 15 + "Lake Masoko Interactive Art Project")
    print("="*70)
    print("\nAn Interactive Environmental Artwork by Nehemia Kaaya")
    print("CS 151 - Fall 2025 - Final Project")
    print("\nBased on Lake Masoko Geochemical Data (1511-2002 AD)")
    print("Visualizing climate change through:")
    print("  • Sediment core analysis")
    print("  • Forest/vegetation patterns")
    print("  • Solar activity cycles")
    print("="*70 + "\n")


def print_menu():
    """Display the main menu."""
    print("\n" + "-"*70)
    print("MAIN MENU - Choose a Scene to Explore:")
    print("-"*70)
    print("\n1. The Sediment Core (Data Visualization)")
    print("   Interactive visualization of lake sediment layers")
    print("   Uses Fe/Ti ratios to show iron content and erosion")
    print("   Click on layers to see year and chemical composition")
    print()
    print("2. The Changing Forest (L-System Visualization)")
    print("   Climate-driven forest growth using L-systems")
    print("   Uses Si/Ti ratios to show wet/dry periods")
    print("   Enter a year to see the corresponding forest")
    print()
    print("3. The Solar Ripples (Recursive Visualization)")
    print("   Solar activity cycles shown as recursive ripples")
    print("   Uses Magnetic Susceptibility data")
    print("   Click through time to see changing patterns")
    print()
    print("0. Exit")
    print("-"*70)


def get_menu_choice():
    """
    Get and validate user's menu choice.
    
    :return: Menu choice (0-3) or None if invalid
    """
    choice = input("\nEnter your choice (0-3): ").strip()
    
    if choice in ['0', '1', '2', '3']:
        return choice
    else:
        print("Invalid choice. Please enter 0, 1, 2, or 3.")
        return None


def run_scene1():
    """Run Scene 1: The Sediment Core."""
    try:
        import scene1_sediment
        scene1_sediment.run_scene()
    except Exception as e:
        print(f"Error running Scene 1: {e}")
        print("Make sure all required files are present.")


def run_scene2(year=None):
    """
    Run Scene 2: The Changing Forest.
    
    :param year: Optional year to visualize (otherwise interactive)
    """
    try:
        import scene2_forest
        if year:
            scene2_forest.run_scene_with_year(year)
        else:
            scene2_forest.run_scene_interactive()
    except Exception as e:
        print(f"Error running Scene 2: {e}")
        print("Make sure all required files are present.")


def run_scene3():
    """Run Scene 3: The Solar Ripples."""
    try:
        import scene3_ripples
        scene3_ripples.run_scene()
    except Exception as e:
        print(f"Error running Scene 3: {e}")
        print("Make sure all required files are present.")


def run_graphical_home():
    """Run the application with graphical home page."""
    from views.home import run_home_page
    
    while True:
        scene = run_home_page()
        
        if scene == 0:
            print("\nThank you for exploring The Breathing Lake!")
            print("Goodbye.\n")
            break
        elif scene == 1:
            print("\nLaunching Scene 1: The Sediment Core...")
            run_scene1()
        elif scene == 2:
            print("\nLaunching Scene 2: The Changing Forest...")
            run_scene2()
        elif scene == 3:
            print("\nLaunching Scene 3: The Solar Ripples...")
            run_scene3()
        
        print("\nScene closed. Returning to home page...")


def run_menu_mode():
    """Run the application in interactive menu mode."""
    print_banner()
    
    while True:
        print_menu()
        choice = get_menu_choice()
        
        if choice is None:
            continue
        
        if choice == '0':
            print("\nThank you for exploring The Breathing Lake!")
            print("Goodbye.\n")
            break
        elif choice == '1':
            print("\nLaunching Scene 1: The Sediment Core...")
            run_scene1()
        elif choice == '2':
            print("\nLaunching Scene 2: The Changing Forest...")
            run_scene2()
        elif choice == '3':
            print("\nLaunching Scene 3: The Solar Ripples...")
            run_scene3()
        
        print("\nScene closed. Returning to main menu...")


def run_command_line_mode(args):
    """
    Run the application in command-line mode.
    
    :param args: Command-line arguments
    """
    if len(args) < 2:
        print("Invalid command-line usage.")
        print_usage()
        return
    
    scene = args[1].lower()
    
    if scene == 'scene1':
        print("\nRunning Scene 1: The Sediment Core...")
        run_scene1()
    elif scene == 'scene2':
        print("\nRunning Scene 2: The Changing Forest...")
        if len(args) > 2:
            try:
                year = int(args[2])
                run_scene2(year)
            except ValueError:
                print(f"Error: '{args[2]}' is not a valid year")
        else:
            run_scene2()
    elif scene == 'scene3':
        print("\nRunning Scene 3: The Solar Ripples...")
        run_scene3()
    else:
        print(f"Unknown scene: {scene}")
        print_usage()


def print_usage():
    """Print command-line usage information."""
    print("\nUsage:")
    print("  python main.py              # Graphical home page (default)")
    print("  python main.py --text       # Text menu mode")
    print("  python main.py scene1       # Run Scene 1 directly")
    print("  python main.py scene2       # Run Scene 2 interactively")
    print("  python main.py scene2 1750  # Run Scene 2 for year 1750")
    print("  python main.py scene3       # Run Scene 3 directly")


def main():
    """Main entry point for the application."""
    if len(sys.argv) > 1:
        # Check for text mode flag
        if sys.argv[1] == '--text':
            # Text menu mode
            run_menu_mode()
        else:
            # Command-line mode
            run_command_line_mode(sys.argv)
    else:
        # Default: Graphical home page
        try:
            run_graphical_home()
        except Exception as e:
            print(f"Error running graphical home: {e}")
            print("Falling back to text menu mode...")
            run_menu_mode()


if __name__ == "__main__":
    main()
