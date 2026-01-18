"""
Nehemia Kaaya
CS 151
Section B
Project 08

"""

import sys

from lib.lsystem import Lsystem
from lib.turtle_interpreter import TurtleInterpreter

from lib.basic_shapes import setUpBackground


def scrubs(y, windowWidth, noOfIterations=3):
    """
    Draws multiple tiny srubs
    """
    deltaX = 60

    xInitial = -windowWidth/2+deltaX

    lsys = Lsystem()
    interpreter = TurtleInterpreter()

    lsys.read("lsystem.json", "SystemCL.txt")

    finalString = lsys.buildString(noOfIterations)

    for x in range(int(xInitial), -int(xInitial), deltaX):
        interpreter.place(x, y, 90)
        interpreter.drawString(finalString, 4, 22)


def trees(y, windowWidth, noOfIterations=4):
    """
    Draws multiple tiny srubs
    """

    treeLsys = ['SystemGL.txt', 'SystemC.txt', 'SystemFL.txt']
    noOfTrees=len(treeLsys)

    deltaX = windowWidth/(noOfTrees+2)

    x = -windowWidth/2+deltaX


    for index, lsystemKey in enumerate(treeLsys):

        lsys = Lsystem()
        interpreter = TurtleInterpreter()

        lsys.read("lsystem.json", lsystemKey)
        finalString = lsys.buildString(noOfIterations)

        interpreter.place(x, y, 90)
        interpreter.drawString(finalString, 15, 22)
        x=x+(deltaX*(index+1))


def main(argv):

    interpreter = TurtleInterpreter(bgColor="skyblue")

    windowWidth, windowHeight = interpreter.getDimensions()

    y = setUpBackground(windowWidth=windowWidth, windowHeight=windowHeight)

    scrubs(y, windowWidth, )

    trees(y, windowWidth)

    interpreter.hold()


if __name__ == '__main__':
    main(sys.argv)
