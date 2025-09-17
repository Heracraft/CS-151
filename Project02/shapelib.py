from turtle import *
import math
import random


def movePen(destination):
    """
    takes in a cartesian tuple: (x,y) destination and moves the turtle
    to the destination and resets it's angle/inclination 
    I find myself writing up()goto()down() too many times so i created
    this function
    """
    up()
    goto(destination)
    down()


def spire(vertex, height, interiorAngle=5):
    """
    Draws a triangle given an interior angle and height 
    """

    movePen(vertex)
    setheading(0)  # reset angle, just in case

    right(90-interiorAngle)
    # hyp=opposite/cosine(theta)
    sideLength = height/(math.cos(math.radians(interiorAngle)))
    forward(sideLength)
    setheading(180)
    base = height*(math.tan(math.radians(interiorAngle)))
    forward(base*2)
    right(90+interiorAngle)
    forward(sideLength)

    return [[vertex[0], vertex[1]-height], base*2]


def hexagonalCylinderFace(vertex, sideLength, height, hideVerticalStripes=False):
    """
    Draws a hexagonal cylinder face which I have simplified to be the body of miller tower
    takes in the origin (vertex) and the length of the hexagon's side and returns the cross-sectional width of the
    face
    """

    def drawVerticalStripe(returnAngle=0):
        """
        Draws a vertical stripe down of length height
        takes in an angle to face after drawing sthe tripe
        """
        setheading(270)
        forward(height)
        up()
        setheading(90)
        forward(height)
        setheading(returnAngle)
        down()

    if (hideVerticalStripes):
        # if hideVerticalStripes is true then do nothing
        # and stop function execution at the end
        def drawVerticalStripe(returnAngle=0):
            setheading(returnAngle)
            return

    movePen(vertex)  # custom function

    setheading(0)
    forward(sideLength/2)
    drawVerticalStripe(0)

    left(10)
    forward(sideLength)
    x2 = xcor()
    drawVerticalStripe(180)

    movePen(vertex)
    setheading(180)

    forward(sideLength/2)
    drawVerticalStripe(180)
    right(10)
    forward(sideLength)
    x1 = xcor()
    drawVerticalStripe()

    newVertex = [vertex[0], vertex[1]-height]

    if hideVerticalStripes:
        # base case
        return

    hexagonalCylinderFace([vertex[0], vertex[1]-5],sideLength*1.1, height, True)

    return [newVertex, x2-x1]


def semiCircle(vertex, radius):
    setheading(90)
    movePen(vertex)
    circle(radius, 180)

    return [vertex[0], vertex[1]-radius]


def rectangle(vertex, length, width, fillColor, noFill=False):
    """
    Draws a rectangle given length, width and fillColor
    It also takes in an optional parameter noFill which disables the color filling.
    """
    # I wanted to offset the drawing by half the length
    movePen([vertex[0]-length/2, vertex[1]])

    color(fillColor)

    setheading(0)

    if not noFill:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)

    if not noFill:
        end_fill()

    return [vertex[0], vertex[1]-width]


def frieze(vertex, length, height, width):
    """
    Takes in the length, height of the frieze and the width of 
    each individual square in the band.

    "Frieze" can refer to an architectural horizontal decorative band ~tracemyhouse.com,
    """

    # movePen([vertex[0]-length/2, vertex[1]])
    for slab in range(-int(length/2), int(length/2), width*2):
        movePen([slab, vertex[1]])
        setheading(0)
        forward(width)
        right(90)
        forward(height)
        right(90)
        forward(width)
        right(90)
        forward(height)


def pillars(vertex, length, height, width):
    """
    Takes in the length, height of the pillar section and the width of 
    each individual pillar.

    """

    x, y = vertex
    x = x-length/2

    noOfPillars = 6

    gapSpace = length-(noOfPillars*width)
    individualGap = gapSpace/(noOfPillars-1)

    for _,index in enumerate(range(0, noOfPillars)):
        xOffset = (width*(index+1))+individualGap*index 
        movePen([x+xOffset, y])
        setheading(270)
        forward(height)
        right(90)
        forward(width)
        right(90)
        forward(height)

    return [vertex[0], vertex[1]-height]
 

def stairs(vertex, width, individualHeight, count):
    """
    Given a starting width, height of each stair and a count, This function draws a staircase
    with increasing length
    """
    x,y=vertex
    length=width

    for nthStair in range(count):
        length=width*(1.1**nthStair) #growth function to ever so slightly increase the width with each stair

        movePen([x,y])

        setheading(0)
        forward(length/2)
        right(90)
        forward(individualHeight)
        right(90)
        forward(length)
        right(90)
        forward(individualHeight)
        right(90)
        forward(length/2)

        y=y-individualHeight

    return [[vertex[0], y], length]

def clouds(vertex, maxRadii):
    """
    Takes in a vertex and the maximum radius to draw a cloud made up of 4 groups of concentric circles
    """
    def ConcentricCircles(vertex, radius):
        noOfCircles=range(1,random.randint(6,10)) #random number of circles
        print("radius", radius)
        for no in noOfCircles:
            x,y=vertex

            radius=radius*(0.9**(no-1)) #decay function on radius
            movePen([x, y-radius])
            circle(radius, 360)

    x,y=vertex
    ConcentricCircles(vertex, maxRadii)

    ConcentricCircles([x+(maxRadii*1), y-(maxRadii*0.5)], maxRadii*0.7)
    ConcentricCircles([x-(maxRadii*1), y-(maxRadii*0.5)], maxRadii*0.7)

    ConcentricCircles([x+(maxRadii*0.3), y-maxRadii], maxRadii/2)
    ConcentricCircles([x-(maxRadii*0.3), y-maxRadii], maxRadii/2)