"""
Nehemia Kaaya
CS 151
Section B
Lab 11

Draws 3 trees using recursive functions
"""

import turtle
from random import randint

window = turtle.Screen()


def place(x, y):
    """
    Abstracts away the up, down and goto functions required to properly move a turtle
    """

    turtle.up()
    turtle.goto(x, y)
    turtle.down()


def drawTree(level, size, angle, ratio):
    """
    Draws a part of a tree given its leve, size, angle and ratio. 
    """
    if level >= 0:
        turtle.forward(size)
        turtle.left(angle)
        drawTree(level - 1, size/ratio, angle, ratio)
        turtle.right(2 * angle)

        drawTree(level - 1, size/ratio, angle, ratio)
        turtle.left(angle)
        turtle.forward(-size)
    else:
        # Stop the recursion
        return


def main():
    turtle.setheading(90)
    turtle.width(3)

    # deltaY=100
    # deltaX=100
    # noOfTrees=3

    turtle.tracer(False)

    positions=[
        (0,0),
        (300, -300),
        (-300, -300)
    ]

    for position in positions:
        x,y = position

        place(x, y)

        size = randint(80, 120)

        angle = randint(20, 40)
        ratio = randint(14, 18)/10
        level = randint(4, 6)

        drawTree(level,size,angle,ratio)


    window.exitonclick()


if __name__ == "__main__":
    main()
