"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

Environmental feature classes with inheritance and polymorphism
"""

import math

class EnvironmentalFeature:
    """Parent class for environmental visualization features"""
    
    def __init__(self, year, value, dataType="unknown"):
        self._year = year
        self._value = value
        self._dataType = dataType
        self._color = "gray"
    
    def getYear(self):
        return self._year
    
    def getValue(self):
        return self._value
    
    def getDataType(self):
        return self._dataType
    
    def getColor(self):
        return self._color
    
    def setYear(self, year):
        self._year = year
    
    def setValue(self, value):
        self._value = value
    
    def setDataType(self, dataType):
        self._dataType = dataType
    
    def setColor(self, color):
        self._color = color
    
    def draw(self, canvas):
        """Abstract draw method - must be implemented by child classes"""
        raise NotImplementedError("Subclasses must implement draw()")
    
    def __str__(self):
        return f"{self.__class__.__name__}(year={self._year}, value={self._value})"

class SedimentLayer(EnvironmentalFeature):
    """Sediment layer visualization using Fe/Ti ratio"""
    
    def __init__(self, year, feTiRatio, depth, normalizedValue=0.5):
        super().__init__(year, feTiRatio, "Fe/Ti")
        self._depth = depth
        self._normalizedValue = normalizedValue
        self._width = 30
        self._height = 8
        self._rectangle = None
        self._calculateColor()
    
    def _calculateColor(self):
        intensity = self._normalizedValue
        r = int(139 + (intensity * 80))
        g = int(90 + (intensity * 50))
        b = int(60 + (intensity * 30))
        self._color = (r, g, b)
    
    def getDepth(self):
        return self._depth
    
    def setDepth(self, depth):
        self._depth = depth
    
    def getWidth(self):
        return self._width
    
    def setWidth(self, width):
        self._width = width
    
    def getHeight(self):
        return self._height
    
    def setHeight(self, height):
        self._height = height
    
    def draw(self, win, x, y):
        """Draw sediment layer as rectangle"""
        from graphics import Point, Rectangle, color_rgb
        
        p1 = Point(x - self._width/2, y)
        p2 = Point(x + self._width/2, y + self._height)
        
        self._rectangle = Rectangle(p1, p2)
        r, g, b = self._color
        self._rectangle.setFill(color_rgb(r, g, b))
        self._rectangle.setOutline(color_rgb(r, g, b))
        self._rectangle.draw(win)
        
        return self._rectangle
    
    def containsPoint(self, point):
        """Check if point is inside layer"""
        if self._rectangle is None:
            return False
        
        x, y = point.getX(), point.getY()
        p1, p2 = self._rectangle.getP1(), self._rectangle.getP2()
        
        return (min(p1.getX(), p2.getX()) <= x <= max(p1.getX(), p2.getX()) and
                min(p1.getY(), p2.getY()) <= y <= max(p1.getY(), p2.getY()))

class ClimateTree(EnvironmentalFeature):
    """Forest visualization using L-systems based on climate"""
    
    def __init__(self, year, siTiRatio, normalizedValue=0.5):
        super().__init__(year, siTiRatio, "Si/Ti")
        self._normalizedValue = normalizedValue
        self._iterations = 1
        self._calculateIterations()
    
    def _calculateIterations(self):
        self._iterations = int(2 + self._normalizedValue * 3)
    
    def getIterations(self):
        return self._iterations
    
    def setIterations(self, iterations):
        self._iterations = iterations
    
    def draw(self, turtleInterp, lsystem, distance=10, angle=25):
        """Draw tree using L-system"""
        treeString = lsystem.buildString(self._iterations)
        turtleInterp.drawString(treeString, distance, angle)

class SolarRipple(EnvironmentalFeature):
    """Solar activity visualization using recursion"""
    
    def __init__(self, year, magSus, normalizedValue=0.5):
        super().__init__(year, magSus, "MagSus")
        self._normalizedValue = normalizedValue
        self._recursionDepth = 1
        self._calculateRecursionDepth()
        self._calculateColor()
    
    def _calculateRecursionDepth(self):
        self._recursionDepth = int(3 + self._normalizedValue * 4)
    
    def _calculateColor(self):
        intensity = self._normalizedValue
        r = int(50 + intensity * 100)
        g = int(100 + intensity * 100)
        b = int(200 + intensity * 55)
        self._color = (r, g, b)
    
    def getRecursionDepth(self):
        return self._recursionDepth
    
    def getNormalizedValue(self):
        return self._normalizedValue
    
    def setRecursionDepth(self, depth):
        self._recursionDepth = depth
    
    def draw(self, win, centerX, centerY, baseRadius=100):
        """Draw recursive ripples"""
        self._drawRecursiveRipples(win, centerX, centerY, baseRadius, self._recursionDepth)
    
    def _drawRecursiveRipples(self, win, x, y, radius, depth):
        from graphics import Circle, Point, color_rgb
        
        if depth <= 0 or radius < 5:
            return
        
        circle = Circle(Point(x, y), radius)
        alpha = depth / self._recursionDepth
        r, g, b = 50 + int(alpha * 100), 100 + int(alpha * 100), 200 + int(alpha * 55)
        circle.setOutline(color_rgb(r, g, b))
        circle.setWidth(2)
        circle.draw(win)
        
        self._drawRecursiveRipples(win, x, y, radius * 0.75, depth - 1)

def main():
    """Test environmental features"""
    sediment = SedimentLayer(year=1750, feTiRatio=3.76, depth=35.25, normalizedValue=0.6)
    tree = ClimateTree(year=1750, siTiRatio=16.01, normalizedValue=0.7)
    ripple = SolarRipple(year=1750, magSus=7.83e-06, normalizedValue=0.5)
    
    features = [sediment, tree, ripple]
    
    for feature in features:
        print(feature)

if __name__ == "__main__":
    main()
