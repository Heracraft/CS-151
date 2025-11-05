import sys

from lib.lsystem import Lsystem
from lib.turtle_interpreter import TurtleInterpreter

from freya import  TurtleInterpreter as FreyaTurtleInterpreter
def main(argv):

    if len(argv) < 3:
        print("Usage : python3 Lab08.py <lsystem-index> <num_iterations>")
        exit()

    if not int(argv[2]):
        raise Exception(f"lsystem-index must be an integer. receieved {type(argv[2])}")


    lsystemFileName = "lsystem.json"
    lsystemIndex = int(argv[1])
    noOfIterations = int(argv[2])

    lsys = Lsystem()
    interpreter=TurtleInterpreter()
    # interpreter=FreyaTurtleInterpreter()

    lsys.read(lsystemFileName, lsystemIndex)

    
    finalString = lsys.buildString(noOfIterations)

    print(finalString)

    interpreter.place(xpos=0, ypos="end")
    interpreter.orient(90)
    interpreter.drawString(finalString, 3, 22)

    interpreter.hold()

    print(finalString)

if __name__ == '__main__':
    main(sys.argv)
