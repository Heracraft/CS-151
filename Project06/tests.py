"""
Nehemia Kaaya
CS151
Section B
Project 06 Social realism scene
tests.py
A testing suite for project 06
"""

from realism import drawShapes
from complex_shapes import initBackground, initBombs, initShip, initClockTower

import graphicsPlus as gr

def main():
    windowWidth = 600
    windowHeight = 1000

    window = gr.GraphWin("Social realism scene", windowWidth, windowHeight)

    # window.setBackground("gray")
    window.setBackground("#2A3E4B")

    # shapes, _ =initBackground(paddingX=100, paddingY=100, windowHeight=windowHeight, windowWidth=windowWidth)

    shapes = initClockTower(windowWidth/2,100,5)

    # shapes,_ = initShip(100, 300, 1)

    # shapes = initBombs(windowWidth/2,100,count=5)

    drawShapes(window, shapes)

    window.getMouse()
    window.close()


if __name__ == "__main__":
    main()
