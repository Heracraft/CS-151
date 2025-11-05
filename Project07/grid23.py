"""
Nehemia Kaaya
CS151
Section B

Draws a 3x3 grid of trees each with a growing angle
"""

from turtle import Screen, Turtle

from lib.lsystem import buildString, createLsystemFromFile
from lib.turtle_interpreter import drawString

COLUMN_COUNT = 3
ROW_COUNT = 3


def goto(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def drawTree(turtle, screen, angle=22.5):
    """
    draws a tree using the provided turtle and screen
    """
    ls = createLsystemFromFile(index=3)

    lstr = buildString(ls, 3)

    drawString(lstr, 8, angle, turtle=turtle, screen=screen)


def main():

    screen = Screen()
    screen.tracer(False)

    windowWidth, windowHeight = screen.window_width(), screen.window_height()

    turtle = Turtle()
    turtle.color("#778327")

    x = -windowWidth/2  # our origin
    y = windowHeight/2

    widthPerCol = windowWidth/COLUMN_COUNT # subdivide width to the no of cols
    heightPerRow = windowHeight/ROW_COUNT # subdivide height to the no of rows

    treeAngles = [22, 46, 60] # the angles for trees in  each column

    for rowIndex in range(0, COLUMN_COUNT):
        yi = y-(heightPerRow)*rowIndex-(heightPerRow/2) # set the new y value for each row
        for columnIndex in range(0, ROW_COUNT):
            xi = x+(widthPerCol)*columnIndex+(widthPerCol/2) # set the new x value for each column

            goto(turtle, xi, yi)

            turtle.setheading(90)
            drawTree(turtle, screen, angle=treeAngles[columnIndex])

            goto(turtle, xi, yi-50)
            turtle.write(rowIndex+columnIndex)

    screen.exitonclick()


if __name__ == "__main__":
    main()
