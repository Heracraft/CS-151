"""
Nehemia Kaaya
CS 151
Section B
Project 08

Growth.py
Draws a tree from a custom Lsystem
"""

import sys

from lib.lsystem import Lsystem
from lib.turtle_interpreter import TurtleInterpreter

def main(argv):

    lsystemFileName = "lsystem.json"
    lsystemKey = "custom"
    noOfIterations = int(argv[2])

    lsys = Lsystem()
    interpreter=TurtleInterpreter(1600,1600)

    lsys.read(lsystemFileName, lsystemKey)

    
    finalString = lsys.buildString(noOfIterations)

    print(finalString)

    interpreter.place(xpos=0, ypos="end")
    interpreter.orient(90)
    interpreter.drawString(finalString, 30, 22)

    interpreter.hold()

    print(finalString)

if __name__ == '__main__':
    main(sys.argv)
