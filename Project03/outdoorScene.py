"""
Nehemia Kaaya
CS 151
Section B
Project 03
09/20/2025
"""

from turtle import *

import better_shapelib as bsl

def outdoorScene():
    '''Draws my scene.
    Requires a command-line argument to change the color of a part of the scene. The following makes it pink:
    python3 outdoorScene.py pink
    The following makes it blue
        python3 outdoorScene.py blue
    '''

    screen = Screen()
    windowWidth, windowHeight = [screen.window_width(), screen.window_height()]

    paddingX, paddingY = [100, 100]  # padding on the x, y axes respectively

    widthAvailable = windowWidth-(paddingX*2)
    heightAvailable = windowHeight-(paddingY*2)
    # sets the origin to the top left corner of the canvas
    x, y = (-(widthAvailable/2), heightAvailable/2)
    
    frameWidth=500
    frameHeight=600

    gap= (widthAvailable-(frameWidth*2)) #gap between frames

    tracer(False) #for debugging purposes

    bsl.artFrame(x, y, 40, frameWidth, frameHeight, bsl.pattern, numShapes=70, scale=0.4, title="Blighted, 2024", metadata="Digital, Python Turtle Graphics")

    bsl.artFrame(x+gap+frameWidth, y, 40, frameWidth, frameHeight, bsl.myNatureScene, numShapes=4, scale=1, title="Stairway to Heaven, 2025", metadata="Digital, Python Turtle Graphics")

def main():
    outdoorScene()

if __name__ == '__main__':
    main()

exitonclick()
