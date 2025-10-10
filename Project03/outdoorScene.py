"""
Nehemia Kaaya
CS 151
Section B
Project 03
09/20/2025

"""

from turtle import *
import sys

import better_shapelib as bsl


def outdoorScene():
    '''Draws my scene.
    The command line argument 'bgColor' is expected. It sets the background color for the screen, if not specified, an exception will be raised.
    eg. python outdoorScene.py pink
    '''

    screen = Screen()

    args = sys.argv

    if len(args) < 2:
        raise Exception(
            "bgColor argument not passed. Please include a background color argument when running this module. eg python lab3.py <some bgColor>")
    elif isinstance(args[1], str):
        screen.bgcolor(args[1])
    else:
        raise Exception(
            f"The type of bgColor is invalid. Expected a string recieved {type(args[1])}")

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

    bsl.artFrame(x, y, 40, frameWidth, frameHeight, bsl.pattern, numShapes=70,
                 scale=0.4, title="Blighted, 2024", metadata="Digital, Python Turtle Graphics")

    bsl.artFrame(x+gap+frameWidth, y, 40, frameWidth, frameHeight, bsl.myNatureScene, numShapes=4,
                 scale=1, title="Stairway to Heaven, 2025", metadata="Digital, Python Turtle Graphics")


def main():
    outdoorScene()


if __name__ == '__main__':
    main()

exitonclick()
