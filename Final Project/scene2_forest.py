"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

Scene 2: Changing Forest L-system visualization
"""

import sys
from lib.lsystem import Lsystem
from lib.turtle_interpreter import TurtleInterpreter
from masoko_data_handler import readData, getDataByYear, getValueRange, normalizeValue
from environmental_features import ClimateTree

def createTreeLsystem(complexityLevel):
    """Create L-system with varying complexity"""
    lsys = Lsystem()
    
    if complexityLevel >= 4:
        lsys.setBase("F")
        lsys.setRule({"F": "FF-[rF+F+F]+[gF-F-F]"})
    elif complexityLevel >= 3:
        lsys.setBase("F")
        lsys.setRule({"F": "F[+gF]F[-rF]F"})
    elif complexityLevel >= 2:
        lsys.setBase("F")
        lsys.setRule({"F": "F[+F][-F]"})
    else:
        lsys.setBase("F")
        lsys.setRule({"F": "FF[-F][+F]"})
    
    return lsys

def drawForestForYear(year, data, distance=10, angle=25, bgColor=None):
    """Draw forest for specific year"""
    record = getDataByYear(data, year)
    
    if not record:
        print(f"No data for year {year}")
        return
    
    actualYear = record["Age (AD)"]
    siTi = record["Si/Ti"]
    
    if siTi == "-" or not isinstance(siTi, (int, float)):
        print(f"No Si/Ti data for year {actualYear}")
        return
    
    siMin, siMax = getValueRange(data, "Si/Ti")
    normalized = normalizeValue(siTi, siMin, siMax)
    
    tree = ClimateTree(actualYear, siTi, normalized)
    iterations = tree.getIterations()
    
    lsys = createTreeLsystem(iterations)
    interpreter = TurtleInterpreter(1600, 1600, bgColor=bgColor)
    
    interpreter.place(xpos=0, ypos="end", angle=90)
    interpreter.setColor((101, 67, 33))
    interpreter.setWidth(2)
    
    tree.draw(interpreter, lsys, distance, angle)
    interpreter.hold()

def getYearFromUser(minYear, maxYear):
    """Prompt user for year"""
    print(f"\nEnter year ({minYear}-{maxYear} AD) or 'q' to quit")
    
    userInput = input("Year: ").strip()
    
    if userInput.lower() in ['quit', 'q', 'exit']:
        return None
    
    try:
        year = int(userInput)
        if minYear <= year <= maxYear:
            return year
        else:
            print(f"Year must be between {minYear} and {maxYear}")
            return getYearFromUser(minYear, maxYear)
    except ValueError:
        print("Please enter valid year")
        return getYearFromUser(minYear, maxYear)

def runSceneInteractive():
    """Run Scene 2 in interactive mode"""
    data = readData("data.json")
    from masoko_data_handler import getYearRange
    minYear, maxYear = getYearRange(data)
    
    year = getYearFromUser(minYear, maxYear)
    
    if year is None:
        return
    
    drawForestForYear(year, data)

def runSceneWithYear(year):
    """Run Scene 2 for specific year"""
    data = readData("data.json")
    drawForestForYear(year, data)

def main(argv):
    """Test Scene 2"""
    if len(argv) > 1:
        try:
            year = int(argv[1])
            runSceneWithYear(year)
        except ValueError:
            print(f"Error: '{argv[1]}' is not valid year")
    else:
        runSceneInteractive()

if __name__ == "__main__":
    main(sys.argv)
