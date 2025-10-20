"""
Nehemia Kaaya
CS151
Section B
Project 06 lab 06
"""

import graphicsPlus as gr
import time
import random

def Point(x, y):
    return gr.Point(x, y)

def createRectangle(x, y, sizeTuple, outlineColor="purple", fillColor="yellow", outlineWidth=20):
    width, height = sizeTuple

    rectangle = gr.Rectangle(gr.Point(x, y), gr.Point(x+width, y+height))
    rectangle.setFill(fillColor)
    rectangle.setWidth(outlineWidth)
    rectangle.setOutline(outlineColor)

    return rectangle


def createRightAngledTriangle(vertices, outlineColor="purple", fillColor="yellow", outlineWidth=0):
    points = []

    for vertex in vertices:
        points.append(Point(vertex[0], vertex[1]))

    triangle = gr.Polygon(points)

    triangle.setFill(fillColor)
    triangle.setWidth(outlineWidth)
    triangle.setOutline(outlineColor)

    return triangle


def createParallelogram(x, y, sizeTuple, scale=1, outlineColor="purple", fillColor="yellow", outlineWidth=5, xOffset=100):
    width, height = sizeTuple
    width = width*scale
    height = height*scale
    xOffset = xOffset * scale

    para=gr.Polygon(Point(x,y), Point(x+width, y), Point(x+width-xOffset, y+height), Point(x-xOffset, y+height))

    para.setFill(fillColor)
    para.setWidth(outlineWidth)
    para.setOutline(outlineColor)

    return para


def collageShapes():
    """
    Creates 4 shapes and returns them as a list
    """
    shapes=[]

    rectangle = createRectangle(100, 200, (150, 100))
    shapes.append(rectangle)

    triangle = createRightAngledTriangle(
        [(350, 200), (500, 450), (350, 450)], outlineColor="#585123", fillColor="#EEC170", outlineWidth=10)
    shapes.append(triangle)

    line = gr.Line(Point(100, 500), Point(1100, 500))
    line.setOutline("#772f1a")
    line.setWidth(10)
    shapes.append(line)

    parallelogram=createParallelogram(600,600, (250, 100,))
    shapes.append(parallelogram)

    return shapes

def drawShapes(win, shapes):
    for shape in shapes:
        shape.draw(win)

def main():
    windowWidth = 1200
    windowHeight = 1000

    window = gr.GraphWin("Lab 06", windowWidth, windowHeight)

    shapes=collageShapes()
    drawShapes(window, shapes)

    animating=True #set tot flase to stop the animation

    while animating:
        if window.checkMouse() is not None:
            window.close()
            break
        for shape in shapes:
            shape.move(random.randint(-10,10),random.randint(-50,50))
            time.sleep(0.5)

    # window.getMouse()
    # window.close()


if __name__ == "__main__":
    main()
