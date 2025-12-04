"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

Scene 2: Changing Forest L-system visualization with GUI
"""

from tkinter import *
from turtle import RawTurtle, TurtleScreen
from lib.lsystem import Lsystem
from masoko_data_handler import readData, getDataByYear, getValueRange, normalizeValue, getYearRange
from environmental_features import ClimateTree

class ForestScene:
    def __init__(self):
        self.data = readData("data.json")
        self.minYear, self.maxYear = getYearRange(self.data)
        self.currentYear = self.minYear
        
        self.window = Tk()
        self.window.title("Scene 2: Changing Forest")
        self.window.geometry("1600x1700")
        
        self.canvas = Canvas(self.window, width=1600, height=1600)
        self.canvas.pack()
        
        self.screen = TurtleScreen(self.canvas)
        self.screen.bgcolor("#F5F5DC")
        self.screen.tracer(0)
        
        controlFrame = Frame(self.window)
        controlFrame.pack(side=BOTTOM, pady=10)
        
        prevBtn = Button(controlFrame, text="<", command=self.previousYear, width=5, font=("Arial", 14))
        prevBtn.pack(side=LEFT, padx=5)
        
        self.yearEntry = Entry(controlFrame, width=10, font=("Arial", 14), justify=CENTER)
        self.yearEntry.insert(0, str(self.currentYear))
        self.yearEntry.bind('<Return>', lambda e: self.goToYear())
        self.yearEntry.pack(side=LEFT, padx=5)
        
        nextBtn = Button(controlFrame, text=">", command=self.nextYear, width=5, font=("Arial", 14))
        nextBtn.pack(side=LEFT, padx=5)
        
        goBtn = Button(controlFrame, text="Go", command=self.goToYear, width=8, font=("Arial", 14))
        goBtn.pack(side=LEFT, padx=5)
        
        self.infoLabel = Label(self.window, text="", font=("Arial", 11), bg="white", relief=RIDGE, padx=10, pady=5)
        self.infoLabel.pack(side=BOTTOM, pady=5)
        
        self.drawForest()
        
    def createTreeLsystem(self, complexityLevel):
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
    
    def drawTree(self, turtle, lsys, iterations, x, y, distance, angle):
        """Draw single tree using L-system"""
        treeString = lsys.buildString(iterations)
        turtle.up()
        turtle.goto(x, y)
        turtle.setheading(90)
        turtle.down()
        
        stack = []
        for char in treeString:
            if char == 'F' or char == 'G':
                turtle.forward(distance)
            elif char == '-':
                turtle.right(angle)
            elif char == '+':
                turtle.left(angle)
            elif char == '[':
                stack.append((turtle.pos(), turtle.heading()))
            elif char == ']':
                if stack:
                    pos, heading = stack.pop()
                    turtle.up()
                    turtle.goto(pos)
                    turtle.setheading(heading)
                    turtle.down()
    
    def drawForest(self):
        """Draw multiple trees for current year"""
        self.screen.clear()
        self.screen.bgcolor("#F5F5DC")
        
        record = getDataByYear(self.data, self.currentYear)
        
        if not record:
            return
        
        actualYear = record["Age (AD)"]
        siTi = record["Si/Ti"]
        
        if siTi == "-" or not isinstance(siTi, (int, float)):
            return
        
        siMin, siMax = getValueRange(self.data, "Si/Ti")
        normalized = normalizeValue(siTi, siMin, siMax)
        
        tree = ClimateTree(actualYear, siTi, normalized)
        iterations = tree.getIterations()
        
        lsys = self.createTreeLsystem(iterations)
        
        turtle = RawTurtle(self.screen)
        turtle.hideturtle()
        turtle.speed(0)
        turtle.color("#654321")
        turtle.width(2)
        
        treePositions = [
            (-600, -700), (-300, -700), (0, -700), (300, -700), (600, -700),
            (-450, -550), (-150, -550), (150, -550), (450, -550),
            (-300, -400), (0, -400), (300, -400)
        ]
        
        distance = 8
        angle = 25
        
        for x, y in treePositions:
            self.drawTree(turtle, lsys, iterations, x, y, distance, angle)
        
        self.screen.update()
        
        if normalized > 0.7:
            climate = "Wet/Windy Period"
            explanation = "High Si/Ti ratio indicates wet, windy conditions. Large, complex trees with dense branching."
        elif normalized > 0.5:
            climate = "Moderate Climate"
            explanation = "Medium Si/Ti ratio shows normal conditions. Healthy trees with regular branching."
        elif normalized > 0.3:
            climate = "Drier Conditions"
            explanation = "Lower Si/Ti ratio indicates drier conditions. Simpler tree structures with less branching."
        else:
            climate = "Dry Period (Little Ice Age)"
            explanation = "Very low Si/Ti ratio shows dry period. Sparse, simple vegetation with minimal branching."
        
        infoText = f"Year: {actualYear} AD | Si/Ti Ratio: {siTi:.2f} | {climate}\n{explanation}"
        self.infoLabel.config(text=infoText)
    
    def previousYear(self):
        """Go to previous year"""
        self.currentYear = max(self.minYear, self.currentYear - 10)
        self.yearEntry.delete(0, END)
        self.yearEntry.insert(0, str(self.currentYear))
        self.drawForest()
    
    def nextYear(self):
        """Go to next year"""
        self.currentYear = min(self.maxYear, self.currentYear + 10)
        self.yearEntry.delete(0, END)
        self.yearEntry.insert(0, str(self.currentYear))
        self.drawForest()
    
    def goToYear(self):
        """Jump to specific year"""
        try:
            year = int(self.yearEntry.get())
            if self.minYear <= year <= self.maxYear:
                self.currentYear = year
                self.drawForest()
            else:
                self.yearEntry.delete(0, END)
                self.yearEntry.insert(0, str(self.currentYear))
        except ValueError:
            self.yearEntry.delete(0, END)
            self.yearEntry.insert(0, str(self.currentYear))
    
    def run(self):
        """Run the scene"""
        self.window.mainloop()

def runSceneInteractive():
    """Run Scene 2 with GUI"""
    scene = ForestScene()
    scene.run()

def runSceneWithYear(year):
    """Run Scene 2 for specific year"""
    scene = ForestScene()
    scene.currentYear = year
    scene.yearEntry.delete(0, END)
    scene.yearEntry.insert(0, str(year))
    scene.drawForest()
    scene.run()

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
    import sys
    main(sys.argv)
