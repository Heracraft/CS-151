import graphicsPlus as gr
import time
import random
import math

import datetime


def Point(x, y):
    return gr.Point(x, y)


def getPointOnCircle(theta, radius, h=0, k=0,):
    """
        Returns an x,y coordinate on the circumference of a circle given its orign h,k, its radius and an angle
    """
    # formula only works with radians
    return h + radius * math.cos(math.radians(theta)), k + radius * math.sin(math.radians(theta))


def createRectangle(x, y, sizeTuple, outlineColor="purple", fillColor="yellow", outlineWidth=20):
    width, height = sizeTuple

    rectangle = gr.Rectangle(gr.Point(x, y), gr.Point(x+width, y+height))
    rectangle.setFill(fillColor)
    # if fillColor != "none":
    #     rectangle.setWidth(outlineWidth)
    #     rectangle.setOutline(outlineColor)

    return rectangle


def getCurrentTimeInDegrees():
    now = datetime.datetime.now()
    currentHour = abs(now.hour-12)
    currentMinute = now.minute

    # this reading is measured anti-clockwise, we gotta convert it to clockwise
    currentHourInDegrees = (currentHour/12)*(360)
    # we use this formula (450-theta)mod 360
    currentHourInDegrees = (450-currentHourInDegrees) % 360

    # gotta do the same with minutes
    currentMinuteInDegrees = (450-(currentMinute*6)) % 360

    return -currentHourInDegrees, -currentMinuteInDegrees  # gotta flip em


def initBackground(paddingX, paddingY, windowWidth, windowHeight):
    shapes = []
    x = windowWidth/2
    y = paddingY

    # yellowRectangleWidth = windowWidth-(2*paddingX)
    yellowRectangleHeight = windowHeight-(paddingY*2)

    # yellowRectangle=createRectangle(x,y, (yellowRectangleWidth,yellowRectangleHeight), outlineColor="none", fillColor="#FADF00",)
    # shapes.append(yellowRectangle)

    crowBackgroundLeft = gr.Image(
        Point(x-72, y+(yellowRectangleHeight/2)), "assets/left.ppm")
    shapes.append(crowBackgroundLeft)

    deltaW = crowBackgroundLeft.getWidth()

    crowBackgroundRight = gr.Image(
        Point(x+(deltaW*0.5)-10, y+(yellowRectangleHeight/2)), "assets/right.ppm")
    shapes.append(crowBackgroundRight)

    return shapes, (x, y+crowBackgroundLeft.getHeight()-50)


def initClockTower(x, y, s=1):
    """
    Creates the shapes that make up the clock tower given the axis of symmetry x,y
    """
    leftShapes = []
    rightShapes = []  # we'll save the right side and left side separately
    # so we can fill them with 2 different colors

    lineHeight = 20*s
    line = gr.Line(Point(x, y), Point(x, y+lineHeight))  # line height=100
    line.setWidth(5)
    leftShapes.append(line)
    y = y+lineHeight-(10*s)

    triangleHeight = 30*s
    triangleWidth = 30*s
    leftPieceOfTriangle = gr.Polygon(Point(x, y), Point(
        x-triangleWidth/2, y+triangleHeight), Point(x, y+triangleHeight))
    rightPieceOfTriangle = gr.Polygon(Point(x, y), Point(
        x+triangleWidth/2, y+triangleHeight), Point(x, y+triangleHeight))
    leftShapes.append(leftPieceOfTriangle)
    rightShapes.append(rightPieceOfTriangle)

    y = y+triangleHeight

    squareLength = 30*s
    leftSideOfSquare = gr.Rectangle(
        Point(x, y), Point(x-(squareLength/2), y+squareLength))
    rightSideOfSquare = gr.Rectangle(
        Point(x, y), Point(x+(squareLength/2), y+squareLength))
    leftShapes.append(leftSideOfSquare)
    rightShapes.append(rightSideOfSquare)

    y = y+squareLength

    parrallelogramHeight = 20*s
    parrallelogramALength = 30*s
    parrallelogramBLength = 50*s
    # create parallelogram shape with polygons in 2 pieces
    leftParallelogram = gr.Polygon(Point(x, y),
                                   Point(x-parrallelogramALength /
                                         2, y),
                                   Point(x-parrallelogramBLength /
                                         2, y+parrallelogramHeight),
                                   Point(x, y+parrallelogramHeight))
    rightParallelogram = gr.Polygon(Point(x, y),
                                    Point(x+parrallelogramALength /
                                          2, y),
                                    Point(x+parrallelogramBLength /
                                          2, y+parrallelogramHeight),
                                    Point(x, y+parrallelogramHeight))
    leftShapes.append(leftParallelogram)
    rightShapes.append(rightParallelogram)
    y = y + parrallelogramHeight

    rectangleWidth = 60*s
    rectangleHeight = 50*s
    # create rectangle with gr.rectangle shape in 2 pieces
    leftClockCase = gr.Rectangle(Point(x, y),
                                 Point(x-rectangleWidth/2, y+rectangleHeight))
    rightClockCase = gr.Rectangle(Point(x, y),
                                  Point(x+rectangleWidth/2, y+rectangleHeight))
    leftShapes.append(leftClockCase)
    rightShapes.append(rightClockCase)

    clockRadius = (rectangleWidth/2)*0.6
    clockOrigin = Point(x, y+rectangleHeight/2)
    clockFace = gr.Circle(clockOrigin, radius=clockRadius)
    clockFace.setFill("#FADF00")

    hourAngle, minuteAngle = getCurrentTimeInDegrees()

    finalPosForClockHand1 = getPointOnCircle(
        # we multiply radius by 0.8 to make the hour hand shorter
        hourAngle, clockRadius*0.8, clockOrigin.getX(), clockOrigin.getY())
    clockHand1 = gr.Line(clockOrigin, Point(
        finalPosForClockHand1[0], finalPosForClockHand1[1]))
    clockHand1.setWidth(2)

    finalPosForClockHand2 = getPointOnCircle(
        minuteAngle, clockRadius, clockOrigin.getX(), clockOrigin.getY())
    clockHand2 = gr.Line(clockOrigin, Point(
        finalPosForClockHand2[0], finalPosForClockHand2[1]))

    y = y + rectangleHeight

    rectangleHeight = 80
    rectangleWidth = 50
    # create rectangle with gr.rectangle shape in 2 pieces
    leftRect2 = gr.Rectangle(Point(x, y),
                             Point(x-rectangleWidth/2, y+rectangleHeight))
    rightRect2 = gr.Rectangle(Point(x, y),
                              Point(x+rectangleWidth/2, y+rectangleHeight))
    leftShapes.append(leftRect2)
    rightShapes.append(rightRect2)

    # Set colors for all shapes
    for shape in leftShapes:
        shape.setFill("gray")
    for shape in rightShapes:
        shape.setFill("black")

    shapes = leftShapes + rightShapes

    # to make sure it drawn ontop of the rectangles in the bg
    shapes.append(clockFace)
    shapes.append(clockHand1)
    shapes.append(clockHand2)
    return shapes


def initShip(x, y, s=1):
    originalX = x

    shapes = []
    shipHeight = 50*s

    rectangleWidth = 100*s
    rectangle = gr.Rectangle(Point(x-rectangleWidth/2, y),
                             Point(x+rectangleWidth/2, y+shipHeight))
    rectangle.setFill("#797777")
    shapes.append(rectangle)

    # ovalWidth=20*s
    # oval1=gr.Oval(Point(x-rectangleWidth/2, y), Point(x-rectangleWidth/2-ovalWidth, y+shipHeight)) # does not work
    leftCirlce = gr.Circle(
        Point(x-rectangleWidth/2, y+shipHeight/2), shipHeight/2)
    leftCirlce.setFill("#797777")
    # leftCirlce.setOutline("darkGray")
    leftCirlce.setWidth(0)

    rightCircle = gr.Circle(
        Point(x+rectangleWidth/2, y+shipHeight/2), shipHeight/2)
    rightCircle.setFill("#797777")
    rightCircle.setWidth(0)

    tailHeight = 20
    tailWidth = 20
    finWidth = 10

    rightCircleX = x + rectangleWidth/2
    rightCircleY = y + shipHeight/2
    pointOnRightCircle = getPointOnCircle(
        -90, shipHeight/2, rightCircleX, rightCircleY)

    tailX = pointOnRightCircle[0]
    tailY = pointOnRightCircle[1]

    tail = gr.Polygon(
        Point(tailX, tailY),
        Point(tailX + finWidth, tailY - tailHeight),
        Point(tailX + finWidth + tailWidth, tailY - tailHeight),
        Point(tailX + finWidth + tailWidth, tailY + finWidth)
    )
    tail.setFill("#4B4B4B")

    xFinal = (x+(rectangleWidth/2))*s
    x = (x-rectangleWidth/2)*s
    y = y+shipHeight

    basketHeight = 10
    xOffset = 20
    basket = gr.Polygon(Point(x, y), Point(x+xOffset, y+basketHeight),
                        Point(xFinal-xOffset, y+basketHeight), Point(xFinal, y))
    basket.setFill("#797777")
    basket.setWidth(0)

    shapes.append(leftCirlce)
    shapes.append(tail)
    shapes.append(rightCircle)
    shapes.append(basket)

    return shapes, (originalX, y+basketHeight)


def initBombs(x, y, count=2, leaveTrail=True):
    shapes = []

    originY = y
    possibleYOffsets = list(range(50, 200, 50))
    random.shuffle(possibleYOffsets)

    for index in range(count):
        xOffset = random.randint(-20, 20)
        yOffset = random.choice(possibleYOffsets)
        x = x+xOffset
        y = y+yOffset
        bomb = gr.Image(Point(x, y), "assets/bomb.png")

        streak = gr.Line(Point(x, y), Point(x, originY))
        streak.setOutline("#FCF55A")
        streak.setWidth(3)

        shapes.append(streak)
        shapes.append(bomb)

    return shapes


def initShapes(x, y, s, windowHeight=1600, windowWidth=500, paddingX=200, paddingY=100):
    """
    Assembles the shape given an origin x, y and a scale s
    """

    # radius=50
    radius = 200

    shapes = []
    backgroundShapes, newOrigin = initBackground(
        paddingX, paddingY, windowWidth, windowHeight, )

    shapes = shapes+backgroundShapes

    shipShapes, coordinatesAfterShip = initShip(windowWidth/2, paddingY+50)

    shapes = shapes+shipShapes

    x, y = newOrigin

    shapes = shapes + initClockTower(x, y, 1)

    x, y = coordinatesAfterShip

    shapes = shapes + initBombs(x, y)

    return shapes
