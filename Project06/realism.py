"""
Nehemia Kaaya
CS151
Section B
Project 06 Social realism scene
To run, python realism.py <optional bom count int argument>
"""

import graphicsPlus as gr

from complex_shapes import initShapes

def drawShapes(win, shapes):
    """
    Draws all the shapes provided on the specified window
    """
    for shape in shapes:
        shape.draw(win)

def main():
    windowWidth = 600
    windowHeight = 1000

    window = gr.GraphWin("Social realism scene", windowWidth, windowHeight)

    window.setBackground("#2A3E4B")

    shapes=initShapes(windowWidth/2, 900,1, windowHeight=windowHeight, windowWidth=windowWidth)
    drawShapes(window, shapes)

    # animating=True #set tot flase to stop the animation

    # while animating:
    #    
    window.getMouse()
    window.close()


if __name__ == "__main__":
    main()
