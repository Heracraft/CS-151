"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

environmental_features.py
Defines parent and child classes for environmental data visualization.
Demonstrates inheritance, polymorphism, and encapsulation.
"""

# Lazy import of graphics modules to avoid display issues
# These will be imported when draw() methods are called
import math


class EnvironmentalFeature:
    """
    Parent class for all environmental visualization features.
    Demonstrates encapsulation with accessor and mutator methods.
    """
    
    def __init__(self, year, value, data_type="unknown"):
        """
        Initialize an environmental feature.
        
        :param year: The year (AD) this feature represents
        :param value: The primary data value for this feature
        :param data_type: Type of data being visualized
        """
        self._year = year
        self._value = value
        self._data_type = data_type
        self._color = "gray"
    
    # Accessor methods (getters)
    def get_year(self):
        """Get the year this feature represents."""
        return self._year
    
    def get_value(self):
        """Get the primary data value."""
        return self._value
    
    def get_data_type(self):
        """Get the type of data being visualized."""
        return self._data_type
    
    def get_color(self):
        """Get the color of this feature."""
        return self._color
    
    # Mutator methods (setters)
    def set_year(self, year):
        """Set the year this feature represents."""
        self._year = year
    
    def set_value(self, value):
        """Set the primary data value."""
        self._value = value
    
    def set_data_type(self, data_type):
        """Set the type of data being visualized."""
        self._data_type = data_type
    
    def set_color(self, color):
        """Set the color of this feature."""
        self._color = color
    
    def draw(self, canvas):
        """
        Abstract method to draw this feature.
        Must be implemented by child classes (polymorphism).
        
        :param canvas: The canvas/window to draw on
        """
        raise NotImplementedError("Subclasses must implement draw() method")
    
    def __str__(self):
        """String representation of this feature."""
        return f"{self.__class__.__name__}(year={self._year}, value={self._value}, type={self._data_type})"


class SedimentLayer(EnvironmentalFeature):
    """
    Child class representing a sediment layer in the lake core.
    Uses Fe/Ti ratio to determine color (iron content).
    """
    
    def __init__(self, year, fe_ti_ratio, depth, normalized_value=0.5):
        """
        Initialize a sediment layer.
        
        :param year: Year (AD) this layer represents
        :param fe_ti_ratio: Iron/Titanium ratio
        :param depth: Depth in the core (cm)
        :param normalized_value: Normalized Fe/Ti value (0-1)
        """
        super().__init__(year, fe_ti_ratio, "Fe/Ti")
        self._depth = depth
        self._normalized_value = normalized_value
        self._width = 30
        self._height = 8
        self._rectangle = None
        self._calculate_color()
    
    def _calculate_color(self):
        """Calculate color based on Fe/Ti ratio (private helper method)."""
        # High iron = darker brown/red, Low iron = lighter tan
        intensity = self._normalized_value
        
        # RGB values: higher Fe/Ti = more red/brown
        r = int(139 + (intensity * 80))  # 139-219
        g = int(90 + (intensity * 50))   # 90-140
        b = int(60 + (intensity * 30))   # 60-90
        
        # Store RGB tuple, will convert to color object when drawing
        self._color = (r, g, b)
    
    def get_depth(self):
        """Get the depth of this layer."""
        return self._depth
    
    def set_depth(self, depth):
        """Set the depth of this layer."""
        self._depth = depth
    
    def get_width(self):
        """Get the width of this layer."""
        return self._width
    
    def set_width(self, width):
        """Set the width of this layer."""
        self._width = width
    
    def get_height(self):
        """Get the height of this layer."""
        return self._height
    
    def set_height(self, height):
        """Set the height of this layer."""
        self._height = height
    
    def draw(self, win, x, y):
        """
        Draw this sediment layer as a rectangle.
        
        :param win: Zelle GraphWin object
        :param x: X position (center)
        :param y: Y position (top)
        :return: The Rectangle object created
        """
        from graphics import Point, Rectangle, color_rgb
        
        p1 = Point(x - self._width/2, y)
        p2 = Point(x + self._width/2, y + self._height)
        
        self._rectangle = Rectangle(p1, p2)
        # Convert RGB tuple to color object
        r, g, b = self._color
        self._rectangle.setFill(color_rgb(r, g, b))
        self._rectangle.setOutline(color_rgb(r, g, b))
        self._rectangle.draw(win)
        
        return self._rectangle
    
    def contains_point(self, point):
        """
        Check if a point is inside this layer's rectangle.
        
        :param point: Point object to check
        :return: True if point is inside, False otherwise
        """
        if self._rectangle is None:
            return False
        
        x, y = point.getX(), point.getY()
        p1, p2 = self._rectangle.getP1(), self._rectangle.getP2()
        
        return (min(p1.getX(), p2.getX()) <= x <= max(p1.getX(), p2.getX()) and
                min(p1.getY(), p2.getY()) <= y <= max(p1.getY(), p2.getY()))


class ClimateTree(EnvironmentalFeature):
    """
    Child class representing forest/vegetation based on climate.
    Uses Si/Ti ratio to determine tree complexity (aridity).
    """
    
    def __init__(self, year, si_ti_ratio, normalized_value=0.5):
        """
        Initialize a climate tree.
        
        :param year: Year (AD) this tree represents
        :param si_ti_ratio: Silicon/Titanium ratio (aridity proxy)
        :param normalized_value: Normalized Si/Ti value (0-1)
        """
        super().__init__(year, si_ti_ratio, "Si/Ti")
        self._normalized_value = normalized_value
        self._iterations = 1
        self._calculate_iterations()
    
    def _calculate_iterations(self):
        """Calculate L-system iterations based on Si/Ti (private helper)."""
        # High Si/Ti = wet/lush = more iterations
        # Low Si/Ti = dry = fewer iterations
        self._iterations = int(2 + self._normalized_value * 3)  # 2-5 iterations
    
    def get_iterations(self):
        """Get the number of L-system iterations."""
        return self._iterations
    
    def set_iterations(self, iterations):
        """Set the number of L-system iterations."""
        self._iterations = iterations
    
    def draw(self, turtle_interp, lsystem, distance=10, angle=25):
        """
        Draw this tree using L-system.
        
        :param turtle_interp: TurtleInterpreter object
        :param lsystem: Lsystem object with tree rules
        :param distance: Forward distance for turtle
        :param angle: Turn angle for turtle
        """
        # Build the L-system string with calculated iterations
        tree_string = lsystem.buildString(self._iterations)
        
        # Draw using the turtle interpreter
        turtle_interp.drawString(tree_string, distance, angle)


class SolarRipple(EnvironmentalFeature):
    """
    Child class representing solar activity cycles.
    Uses MagSus (Magnetic Susceptibility) for recursion depth.
    """
    
    def __init__(self, year, mag_sus, normalized_value=0.5):
        """
        Initialize a solar ripple.
        
        :param year: Year (AD) this ripple represents
        :param mag_sus: Magnetic susceptibility value
        :param normalized_value: Normalized MagSus value (0-1)
        """
        super().__init__(year, mag_sus, "MagSus")
        self._normalized_value = normalized_value
        self._recursion_depth = 1
        self._calculate_recursion_depth()
        self._calculate_color()
    
    def _calculate_recursion_depth(self):
        """Calculate recursion depth based on MagSus (private helper)."""
        # Higher magnetic susceptibility = more recursion depth
        self._recursion_depth = int(3 + self._normalized_value * 4)  # 3-7 levels
    
    def _calculate_color(self):
        """Calculate color based on MagSus intensity."""
        # Higher MagSus = brighter blue (more activity)
        intensity = self._normalized_value
        
        r = int(50 + intensity * 100)   # 50-150
        g = int(100 + intensity * 100)  # 100-200
        b = int(200 + intensity * 55)   # 200-255
        
        # Store RGB tuple, will convert to color object when drawing
        self._color = (r, g, b)
    
    def get_recursion_depth(self):
        """Get the recursion depth."""
        return self._recursion_depth
    
    def get_normalized_value(self):
        """Get the normalized value (0-1)."""
        return self._normalized_value
    
    def set_recursion_depth(self, depth):
        """Set the recursion depth."""
        self._recursion_depth = depth
    
    def draw(self, win, center_x, center_y, base_radius=200):
        """
        Draw recursive ripples representing solar activity.
        
        :param win: Zelle GraphWin object
        :param center_x: X coordinate of center
        :param center_y: Y coordinate of center
        :param base_radius: Base radius for ripples
        """
        self._draw_recursive_ripples(win, center_x, center_y, base_radius, 
                                     self._recursion_depth)
    
    def _draw_recursive_ripples(self, win, x, y, radius, depth):
        """
        Recursive function to draw concentric ripples.
        
        :param win: Zelle GraphWin object
        :param x: Center X coordinate
        :param y: Center Y coordinate
        :param radius: Current radius
        :param depth: Remaining recursion depth
        """
        from graphics import Circle, Point, color_rgb
        
        if depth <= 0 or radius < 5:
            return
        
        # Draw circle at this level
        circle = Circle(Point(x, y), radius)
        
        # Color intensity decreases with depth
        alpha = depth / self._recursion_depth
        r, g, b = 50 + int(alpha * 100), 100 + int(alpha * 100), 200 + int(alpha * 55)
        circle.setOutline(color_rgb(r, g, b))
        circle.setWidth(2)
        circle.draw(win)
        
        # Recursive call with smaller radius
        self._draw_recursive_ripples(win, x, y, radius * 0.75, depth - 1)


def main():
    """Test function demonstrating polymorphism with mixed object types."""
    print("Testing Environmental Feature Classes\n")
    
    # Create instances of each type
    sediment = SedimentLayer(year=1750, fe_ti_ratio=3.76, depth=35.25, normalized_value=0.6)
    tree = ClimateTree(year=1750, si_ti_ratio=16.01, normalized_value=0.7)
    ripple = SolarRipple(year=1750, mag_sus=7.83e-06, normalized_value=0.5)
    
    # Demonstrate polymorphism - list with mixed types
    features = [sediment, tree, ripple]
    
    print("Demonstrating Polymorphism:")
    print("-" * 50)
    for feature in features:
        print(feature)
        print(f"  Year: {feature.get_year()}")
        print(f"  Value: {feature.get_value()}")
        print(f"  Type: {feature.get_data_type()}")
        print()
    
    # Demonstrate accessor/mutator methods
    print("Demonstrating Encapsulation (Accessor/Mutator):")
    print("-" * 50)
    print(f"Original sediment year: {sediment.get_year()}")
    sediment.set_year(1800)
    print(f"Modified sediment year: {sediment.get_year()}")
    
    print(f"\nOriginal tree iterations: {tree.get_iterations()}")
    tree.set_iterations(4)
    print(f"Modified tree iterations: {tree.get_iterations()}")
    
    print(f"\nOriginal ripple depth: {ripple.get_recursion_depth()}")
    ripple.set_recursion_depth(6)
    print(f"Modified ripple depth: {ripple.get_recursion_depth()}")


if __name__ == "__main__":
    main()
