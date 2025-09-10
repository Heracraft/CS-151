from turtle import *
from random import randint

from shapeA import drawCross
from shapeB import drawRhombus

tracer(False)

# origin=(-400,350)

# up()
# goto(origin) #To Center ish the shapes
# down()

# cross dimensions: 500 x 700


def shapeC():

    up()
    # forward(400)
    goto(-700, 450)
    down()

    color("dark blue")
    begin_fill()
    drawRhombus(1000)
    end_fill()

    up()
    goto(0, 350)
    down()
    setheading(0)  # reset angle to 0

    color("white")
    begin_fill()
    drawCross()
    end_fill()

# shapeC()


def shapeD(origin, length, inclination, colorName,):
    # rotating square
    color(colorName)

    up()
    goto(origin)
    down()

    setheading(inclination)
    up()
    forward(length/2)
    down()
    right(90)

    begin_fill()
    for _ in range(4):
        forward(length)
        right(90)
    end_fill()

def shapeE():
    shapeC()
    for index, squareColor in enumerate(["#2118ff", "#3f42ff", "#767fff", "#a7b1ff"]):
        # 500
        origin= (-50, 100)
        size = 300*(.8**index)
        shapeD(origin, size, randint(60,90), squareColor)


shapeE()

exitonclick()
