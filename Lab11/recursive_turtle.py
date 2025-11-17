"""
Nehemia Kaaya
CS 151
Section B
Lab 11

Draws a scene composed of 3 shapes
"""


import turtle


def place(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()


def zigzag(num, length):
    """Draws the specified number of zigzags with 
    the specified number of zigzags and the 
    length."""
    if (num > 0):
        turtle.setheading(-45)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)

        zigzag(num-1, length)


def zigzagColumn(x, y, distance, length=50, paddingY=100):
    """
    Draws a column of zigzags given an origin x,y and a distance to be covered.    
    """
    distance=distance-paddingY*1.4
    y=y-(paddingY/2)

    displacement=(length**2+length**2)**(1/2) # vertical distance travelled by a single zig zag piece 

    numOfPieces = distance/displacement

    print(numOfPieces, distance)

    place(x, y)
    zigzag(numOfPieces, length)


def circle(num, x, y, initialRadii):
    """
    Draws num no of circles anchored at specified origin 
    """
    r = initialRadii

    if (num > 0):

        place(x, y)

        turtle.circle(r)

        circle(num-1, x, y, r-20)


def intersectingCircles(deltaTheta=45):
    """
    Draws 4 intersecting circles
    """

    # if deltaTheta==45, -90, -45, 0, ...
    for angle in range(-90, 270, deltaTheta):
        turtle.setheading(angle)
        circle(10, 0, 0, 200)


def square(turns, length, deltaL=10):
    """
    Draws a recursive square from a central point outward. Requires a specified number of turns and length.
    """

    # turtle.setheading(0)

    if turns > 0:
        turtle.forward(length)
        turtle.left(90)
        square(turns-1, length+deltaL, deltaL)


def squaresAtCorners(windowWidth, windowHeight, deltaL=10):
    """
    Uses the `square` function to place 4 recursive squares at the corners of the scene
    """

    turns = 20
    length = 10

    finalShapeWidth = length+(turns-1)*deltaL  # arithmetric sequence

    x1 = -windowWidth/2+finalShapeWidth
    y1 = windowHeight/2-finalShapeWidth

    place(x1, y1)
    square(turns, length, deltaL)

    x2 = windowWidth/2 - finalShapeWidth
    y2 = windowHeight/2 - finalShapeWidth

    place(x2, y2)
    square(turns, length, deltaL)

    x3 = -windowWidth/2 + finalShapeWidth
    y3 = -windowHeight/2 + finalShapeWidth

    place(x3, y3)
    square(turns, length, deltaL)

    x4 = windowWidth/2 - finalShapeWidth
    y4 = -windowHeight/2 + finalShapeWidth

    place(x4, y4)
    square(turns, length, deltaL)

    # return the starting position for each top corner and the distance to the bottom of the window
    return [(x1, y1, abs(y3-y1)), (x2, y1, abs(y4-y2)), finalShapeWidth]


def main():
    screen = turtle.getscreen()

    windowWidth = screen.window_width()
    windowHeight = screen.window_height()

    turtle.width(3)

    # zigzag(10, 10)
    # zigzag(4, 100)
    turtle.speed(500)

    leftZigZagVector, rightZigZagVector, finalSquareWidth = squaresAtCorners(windowWidth, windowHeight)
    leftX, leftY, leftDisp = leftZigZagVector
    zigzagColumn(leftX, leftY, leftDisp, paddingY=finalSquareWidth)

    rightX, rightY, rightDisp = rightZigZagVector
    zigzagColumn(rightX, rightY, rightDisp, paddingY=finalSquareWidth)


    intersectingCircles()

    turtle.exitonclick()


if __name__ == '__main__':
    main()
