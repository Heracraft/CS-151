import graphicsPlus as gr
import time
import random
import math


def Point(x, y):
    return gr.Point(x, y)


def getPointsOnCirlce(x, y, radius, noOfPoints=5):
    """
    Returns an array of points given a circle's origin and radius
    """

    # x= h+r * cos (theta)
    # y= k + r * sin(theta)
    # h,k center (x,y)

    def getX(theta):
        # formula only works with radians
        return x + radius * math.cos(math.radians(theta))

    def getY(theta):
        return y + radius * math.sin(math.radians(theta))

    points = []

    deltaTheta = 360/noOfPoints

    for angle in range(int(deltaTheta), int(360+deltaTheta), int(deltaTheta)):
        if angle >= 180:
            angle = 180-angle
        elif angle >= 270:
            angle = angle-180
        elif angle >= 360:
            angle = angle-360

        points.append((getX(angle), getY(angle)))

    return points


def getPointsOnCircle(tangetX, tangetY, radius, originX=0, originY=0, length=100, yOffset=0):
    """
    Draws a line tanget to a circle given a point on the cricle tangetX, tangetY, a length and a yOffset
    """

    # derivitive of the  cirlce equation
    slope = - (tangetX-originX)/(tangetY-originY)

    if yOffset > 0:
        """"""
        # slope= slope + random.randint(0,int(abs(1*slope)))
        # print("range", slope)

    initialX = tangetX-(length/2)  # where the line will start
    finalX = tangetX+(length/2)  # where the line will end

    if (abs(finalX)-abs(initialX) > length):
        print("initalX", initialX, "finalX", finalX)
        print("tangetX", tangetX, "tangetY", tangetY, "radius",
              radius, "originX", originX, "originY", originY,)
        print("slope", slope)

    def y(x):
        return slope*x - (slope*tangetX) + tangetY

    initialY = y(initialX) + yOffset
    finalY = y(finalX) + yOffset

    return [(initialX, initialY), (finalX, finalY)]


def eyeOfNest(x, y, s, radius):
    shapes = []

    radius = radius*s

    centerCircle = gr.Circle(Point(x, y), radius)
    shapes.append(centerCircle)

    yOffset = 0.5 * radius  # how far off the second circle will be from the first circle
    radius = radius*1.5
    secondCirlce = gr.Circle(Point(x, y-yOffset), radius)
    shapes.append(secondCirlce)

    pointsOnSecondCirlce = getPointsOnCirlce(
        x, y-yOffset, radius, noOfPoints=20)

    for yOffset in range(0, 5):
        yOffset = yOffset*10
        for point in pointsOnSecondCirlce:
            whereToPutDot = Point(point[0], point[1])
            # draw a point on the circle
            tinyCircle = gr.Circle(whereToPutDot, 10)
            tinyCircle.setFill("purple")
            shapes.append(tinyCircle)

            start, end = getPointsOnCircle(
                point[0], point[1], radius, originX=x, originY=y, yOffset=yOffset)
            line = gr.Line(Point(start[0], start[1]), Point(end[0], end[1]))
            shapes.append(line)

    return shapes


def initNest(x, y, s):
    """
    Assembles the nest shape given an origin x, y and a scale s
    """

    # radius=50
    radius = 200

    shapes = []
    shapes = shapes + eyeOfNest(x, y, s, radius*s)
    return shapes
