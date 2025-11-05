"""
Nehemia Kaaya
CS 151
Section B
Project 07 Scene with l-systems
09/20/2025
Adapted from project 03 
"""


from turtle import *

import lib.better_shapelib as bsl
from lib.lsystem import lSys, buildString
from lib.turtle_interpreter import drawString


def fractalBacground(x,y):
    """
    Draws the fractal background given an origin (x,y)
    """
    turtle=getturtle()
    screen=getscreen()

    turtle.up()
    turtle.goto(x,y)
    turtle.down()

    lst=lSys("F", {'F':'F+G', 'G':'F-G'})

    lstr=buildString(lst,13)

    # turtle.setheading(90)   

    width(2)
    color("#2c365e")
    drawString(lstr, 20, angle=90, turtle=turtle, screen=screen)



def sierpinskiTrianglePainting(contentX, contentY, contentWidth, contentHeight, scale, _):
    """
    Draws a Sierpiński triangle given an origin (contentX, contentY)
    """
    x=contentX+contentWidth
    y=contentY-contentHeight*0.9


    turtle=getturtle()
    screen=getscreen()
    turtle.up()
    turtle.goto(x-50,y+10)
    turtle.down()

    lst=lSys("FZF--FF--FF", {'F':'FF', 'Z':'--FZF++FZF++FZF--'})

    lstr=buildString(lst,4)
    turtle.setheading(90)   
    turtle.color("#F8C551")
    turtle.begin_fill()

    drawString(lstr, 12, angle=120, turtle=turtle, screen=screen)

    turtle.end_fill()


def outdoorScene():
    '''Draws my scene.
    The command line argument 'bgColor' is expected. It sets the background color for the screen, if not specified, an exception will be raised.
    eg. python outdoorScene.py pink
    '''

    screen = Screen()
    screen.bgcolor("#5d6491")

    windowWidth, windowHeight = [screen.window_width(), screen.window_height()]

    paddingX, paddingY = [100, 100]  # padding on the x, y axes respectively

    widthAvailable = windowWidth-(paddingX*2)
    heightAvailable = windowHeight-(paddingY*2)
    # sets the origin to the top left corner of the canvas
    x, y = (-(widthAvailable/2), heightAvailable/2)

    frameWidth = 500
    frameHeight = 600

    gap = (widthAvailable-(frameWidth*2))  # gap between frames

    tracer(False)  # for debugging purposes

    # fractalBacground(0,0)
    fractalBacground((widthAvailable/2), -heightAvailable/2)


    bsl.artFrame(x, y, 40, frameWidth, frameHeight, bsl.pattern, numShapes=70,
                 scale=0.4, title="Blighted, 2024", metadata="Digital, Python Turtle Graphics")

    bsl.artFrame(x+gap+frameWidth, y, 40, frameWidth, frameHeight, sierpinskiTrianglePainting, numShapes=4,
                 scale=1, title="Sierpiński Sieve, 2025", metadata="Digital, Python Turtle Graphics")


def main():
    outdoorScene()


if __name__ == '__main__':
    main()

exitonclick()
