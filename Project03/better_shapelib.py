from turtle import *
import math
import random

fillColors = ['#f2f7fd', '#e4ecfa', '#c3d9f4', '#8fbaea', '#5396dd', '#2c78cb', '#1b569e', '#194b8b', '#184174', '#1a3760', '#112340', '#fff7ec', '#ffeed2', '#ffd9a3', '#ffbe69', '#ff952c',
              '#ff7604', '#fc5800', '#d14000', '#a53207', '#852c09', '#220901', '#fffaeb', '#fdeec8', '#fbdd8c', '#f8c551', '#f6aa1c', '#f08d10', '#d5690a', '#b0480d', '#8f3811', '#762f11', '#441604']


def rectangle(x, y, width, height, fill="none"):
    """
    Draws a regular rectangle given an origin (x,y), width, height and an optional field kewarg.
    """
    movePen([x, y])
    if fill != "none":
        color("black", fill)
        begin_fill()
    for _ in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)
    if fillcolor != "none":
        end_fill()


def sector(x, y, radius, fill=True):
    '''Draws circles of `radius` at origin (`x`, `y`).
       A random fill color is assigned if the keyword argument fill is set to true
    '''

    # Because I added them to the list in groups in order of their tint, I want them to be shuffled
    random.shuffle(fillColors)

    if fill:
        fillcolor = random.choice(fillColors)
        color(fillcolor, fillcolor)  # use the same color as the background
        begin_fill()

    movePen([x, y])
    # use the random module to select a random extent (pi/2, 2pi or pi)
    circle(radius, random.choice([90, 360, 180]))
    # forward(radius)
    # right(90)
    # forward(height)
    # right(90)
    # forward(width)
    # right(90)
    # forward(height)

    if fill:
        end_fill()


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


def pillars(x, y, length, height, width, fill="none"):
    """
    Takes in the length, height of the pillar section and the width of 
    each individual pillar.

    """

    noOfPillars = 6

    gapSpace = length*0.8-(noOfPillars*width)
    individualGap = gapSpace/(noOfPillars-1)

    startingXOffset=(length-(length*0.8))/2
    x=x+startingXOffset

    for _, index in enumerate(range(0, noOfPillars)):
        if fill != "none":
            fillcolor(fill)
            begin_fill()
        xOffset = (width*(index+1))+individualGap*index
        movePen([x+xOffset, y])
        setheading(270)
        forward(height)
        right(90)
        forward(width)
        right(90)
        forward(height)
        right(90)
        forward(width)

        end_fill()
    return y-height


def stairs(x, y, width, height, count):
    """
    Given a starting width, height of each stair and a count, This function draws a staircase
    with increasing length
    """
    length = (width/2)
    individualHeight = height/count

    for nthStair in range(count):
        # growth function to ever so slightly increase the width with each stair
        length = length*(1.05**nthStair)

        movePen([x, y])

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

        y = y-individualHeight


def museumCard(x,y, title, metadata):
    """
    Draws a simple exhibition label given an orgin: x,y, title and metadata. 

    """

    cardLength=400
    cardHeight=90

    movePen([x,y])
    setheading(0)

    color("white","#2c365e")
    begin_fill()

    forward(cardLength/2)
    right(90)
    forward(cardHeight)
    right(90)
    forward(cardLength)
    right(90)
    forward(cardHeight)
    right(90)
    forward(cardLength/2)

    end_fill()

    x,y=[x, y-cardHeight/2]
    movePen([x, y])
    font=("Times New Roman", 10, 'bold')
    write(title, font=font, align="center")

    movePen([x, y-30])
    font=("Times New Roman", 8, 'italic')
    write(metadata, font=font, align="center")

# ------- COMPOUND shapes


def artFrame(x, y, thickness, width, height, content, numShapes=100, scale=0.5, title="Some title", description="some description lorem ipusum", metadata="Digital, Python Turtle Graphics"):
    """
    Takes in an origin coordinate x,y, the thickness of the frame, fill color and the content function
    The content function is the function that draws the piece inside the frame
    """

    contentWidth = width - 2*thickness
    contentHeight = height - 2*thickness

    contentX = x+thickness
    contentY = y-thickness

    setheading(0)

    # The outer rectangle of the frame
    rectangle(x, y, width, height, fill="#2b193d")

    # The inner, colored rectangle
    rectangle(contentX, contentY, contentWidth, contentHeight, fill="#2c365e")

    content(contentX, contentY, contentWidth, contentHeight, scale, numShapes)

    museumCard(x+width/2, y-height-100, title, metadata)


def clouds(vertex, maxRadii, strokeColor="none"):
    """
    Takes in a vertex and the maximum radius to draw a cloud (compound shape) made up of 4 groups of concentric circles
    """
    def ConcentricCircles(vertex, radius):
        # random number of circles
        noOfCircles = range(1, random.randint(3, 8))
        # print("radius", radius)
        for no in noOfCircles:
            x, y = vertex

            radius = radius*(0.6**(no-1))  # decay function on radius
            movePen([x, y-radius])
            circle(radius, 360)

    x, y = vertex

    if strokeColor != "none":
        color("white", strokeColor)
        begin_fill()

    ConcentricCircles(vertex, maxRadii)

    ConcentricCircles([x+(maxRadii*1), y-(maxRadii*0.5)], maxRadii*0.7)
    ConcentricCircles([x-(maxRadii*1), y-(maxRadii*0.5)], maxRadii*0.7)

    ConcentricCircles([x+(maxRadii*0.3), y-maxRadii], maxRadii/2)
    ConcentricCircles([x-(maxRadii*0.3), y-maxRadii], maxRadii/2)

    if strokeColor != "none":
        end_fill()

# ------------ SCENES

def pattern(x, y, width, height, s, numShapes):
    """
    Takes in a starting x, y coordinate and draws a mondrian art piece with `numShapes` number of sectors at scale s.
    The sectors are filled even if they are not complete circles, creating beautiful trails
    """
    fill = False
    pensize(2)
    # speed(500)  # for debugging purposes

    for _ in range(numShapes):
        if random.randint(0, 100) <= 40:
            fill = True
            # only fill 40% of the time
        radius = random.randint(50, 150) * s
        xOffset = random.randint(math.ceil(radius*2), int(width-(radius*2)))
        yOffset = random.randint(math.ceil(radius*2), int(height-(radius*2)))

        sector(x+xOffset, y-yOffset, radius, fill)

def myNatureScene(x, y, width, height, s, numClouds):
    """
    Takes in a starting x, y coordinate and draws a scene with the `numClouds` number of clouds
    """

    # tracer(False)  # for debugging purposes
    for _ in range(numClouds):
        baseX = x
        baseY = y

        maxRadii = 25*s
        minWidth = maxRadii*s*2  # an estimate of the minimum width of the cloud
        minHeight = maxRadii*s*2  # an estimate of the minimum height of the cloud

        # We want to draw geometric clouds but want them spaced out in a random range of X,
        # We use the random module for that.
        deltaX = random.randrange(int(minWidth), int(width-minWidth), minWidth)
        deltaY = random.randrange(int(minHeight), int((height/3)-minHeight), minHeight)
        clouds([baseX+deltaX, baseY-deltaY], maxRadii,
               strokeColor=random.choice(fillColors))

    # tracer(True)
    newY = pillars(x, y-height/2, width, 200, 20,fill="#e4ecfa")

    heightLeft = height-abs(newY-y)

    stairs(x+(width/2), newY, width, heightLeft, 5)
