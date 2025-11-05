"""
Nehemia Kaaya
CS 151
Section B
Project 07

Draws a gradient bacground paired up with tiny stars and a beautiful tree in the foreground.
"""

from turtle import Screen, Turtle

from lib.lsystem import lSys, buildString
from lib.turtle_interpreter import drawString

COLOR = (0.9686, 0.9725, 0.9973)  # (154, 0, 254) : starting color in gradient
TARGET = (0.8392, 0.8627, 0.6863)  # (221, 122, 80): ending color in gradient


def goto(turtle, x, y):
    """
    moves the turtle to the specified x,y coordinate
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def drawGradient(turtle, windowWidth, windowHeight):
    """
    draws a gradient
    """
    deltas = [(hue - COLOR[index]) / windowHeight for index,
              hue in enumerate(TARGET)]

    direction = 1

    for distance, y in enumerate(range(windowHeight//2, -windowHeight//2, -1)):

        turtle.forward(windowWidth * direction)
        turtle.color([COLOR[i] + delta * distance for i,
                     delta in enumerate(deltas)])
        turtle.sety(y)

        direction *= -1


def drawTree(turtle, screen):
    """
    draws a tree with the provided turtle and screen objects
    """
    ls = lSys("-X", {"F": "FF", "X": "F+[[X]-X]-F[-FX]+X"})

    lstr = buildString(ls, 6)

    drawString(lstr, 7, 25, turtle=turtle, screen=screen)


def drawBackground(turtle, screen):
    """
    Draws the starry backgroundd
    """
    ls = lSys("F-F-F-F-F", {"F": "F-F++F+F-F-F"}) # stars background

    lstr = buildString(ls, 5)

    drawString(lstr, 5, 72, turtle=turtle, screen=screen)

def main():

    screen = Screen()
    screen.tracer(False)

    windowWidth, windowHeight = screen.window_width(), screen.window_height()

    turtle = Turtle()
    turtle.color(COLOR)

    goto(turtle, -windowWidth/2, windowHeight/2)

    drawGradient(turtle, windowWidth, windowHeight)

    # ----------
    goto(turtle,0,0)
    drawBackground(turtle, screen)
    
    # -----------
    goto(turtle, -(windowWidth*0.4), -windowHeight/2)
    turtle.color("#97A733")
    turtle.setheading(90)
    drawTree(turtle, screen)


    

    screen.exitonclick()


if __name__ == "__main__":
    main()
