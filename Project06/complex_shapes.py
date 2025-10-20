import graphicsPlus as gr
import time
import random

def Point(x, y):
    return gr.Point(x, y)

def getPointsOnCirlce(x,y, radius):
    """
    Returns an array of points given a circle's origin and radius
    """

    # (x-h)^2 + (y-k)^2=r^2
    # h,k center (x,y)
    # circleFormula=

def eyeOfNest(x,y,s, radius):
    shapes=[]

    centerCircle=gr.Circle(Point(x,y), radius)
    shapes.append(centerCircle)

    yOffset= 0.5 * radius #how far off the second circle will be from the first circle
    radius=radius*1.5
    secondCirlce=gr.Circle(Point(x,y-yOffset), radius)
    shapes.append(secondCirlce)


    return shapes

def initNest(x,y,s):
    """
    Assembles the nest shape given an origin x, y and a scale s
    """

    radius=50

    shapes = []
    shapes = shapes + eyeOfNest(x,y,s, radius*s)
    return shapes
