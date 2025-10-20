"""
Nehemia Kaaya
CS151
Section B
Project 06 Social realism scene
"""

import graphicsPlus as gr
import time
import random

from complex_shapes import initNest

def drawShapes(win, shapes):
    for shape in shapes:
        shape.draw(win)

def main():
    windowWidth = 900
    windowHeight = 1600

    window = gr.GraphWin("Social realism scene", windowWidth, windowHeight)

    shapes=initNest(windowWidth/2, 900,1)
    drawShapes(window, shapes)

    # animating=True #set tot flase to stop the animation

    # while animating:
    #    
    window.getMouse()
    window.close()


if __name__ == "__main__":
    main()
