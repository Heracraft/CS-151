"""
Nehemia Kaaya
CS 151
Section B
Project 08

Usage : python3 Lab08.py <lsystem-key> <num_iterations>
"""

import sys

from lib.lsystem import Lsystem, getAvailableLsystems
from lib.turtle_interpreter import TurtleInterpreter

def main(argv):

    if len(argv) < 3:
        print("Usage : python3 Lab08.py <lsystem-key> <num_iterations>")
        exit()

    availableLsystemKeys=getAvailableLsystems()    

    if argv[1] not in availableLsystemKeys:
        print(f"The lsystem specified could not be found. {argv[1]} not in lsystem.json")
        print(f"The available lystsems are {availableLsystemKeys}")
        print("Usage : python3 Lab08.py <lsystem-key> <num_iterations>")
        exit()

    lsystemFileName = "lsystem.json"
    lsystemKey = argv[1]
    noOfIterations = int(argv[2])

    lsys = Lsystem()
    interpreter=TurtleInterpreter()

    lsys.read(lsystemFileName, lsystemKey)

    
    finalString = lsys.buildString(noOfIterations)

    print(finalString)

    interpreter.place(xpos=0, ypos=0)
    interpreter.orient(90)
    interpreter.drawString(finalString, 10, 90)

    interpreter.hold()

    print(finalString)

if __name__ == '__main__':
    main(sys.argv)
