from tkinter import *
from turtle import RawTurtle, TurtleScreen
import json

def loadDataset(filename="data.json"):
    """
    Reads the json file which holds the dataset and returns the value as a dict
    
    :param filename: The DATASET!!!!
    """

    with open(filename, "r") as jsonFile:
        data: list[dict[str, str | float | int]] = json.load(jsonFile)

        print(data)

        jsonFile.close()


def createWindow(title, geometry):
    window = Tk()
    window.title(title)
    window.geometry(geometry)

    return window


def wahdwoda(t: RawTurtle):
    t.forward(100)
    t.right(90)


def main():
    window = createWindow("Counter", "500x500")

    canvas = Canvas(window)
    canvas.pack(fill="both", expand=True, ipadx=100, ipady=100)

    turtleScreen = TurtleScreen(canvas)
    turtle = RawTurtle(turtleScreen)

    button = Button(window, text="apomaoec",
                    command=lambda: wahdwoda(turtle)).pack(side="bottom")

    window.mainloop()


if __name__ == "__main__":
    # main()
    loadDataset()
