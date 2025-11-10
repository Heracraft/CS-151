import turtle

def goto(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

    turtle.setheading(0)


def greenThinCrust(windowWidth, y):
    crustHeight=20
    turtle.fillcolor(124/255, 252/255, 0/255)  # #7CFC00 LawnGreen

    goto(-windowWidth/2, y+crustHeight)

    turtle.begin_fill()
    turtle.forward(windowWidth)
    turtle.right(90)
    turtle.forward(crustHeight)
    turtle.right(90)
    turtle.forward(windowWidth)
    turtle.right(90)
    turtle.forward(crustHeight)
    turtle.end_fill()


def soil(windowWidth, windowHeight):
    soilHeight=200
    turtle.fillcolor(84/255, 42/255, 32/255)  # #542A20

    goto(-windowWidth/2, (-windowHeight/2)+soilHeight)

    turtle.begin_fill()
    turtle.forward(windowWidth)
    turtle.right(90)
    turtle.forward(soilHeight)
    turtle.right(90)
    turtle.forward(windowWidth)
    turtle.right(90)
    turtle.forward(soilHeight)
    turtle.end_fill()

    return (-windowHeight/2)+soilHeight

def setUpBackground(windowWidth, windowHeight):
    currentY=soil(windowWidth, windowHeight)

    greenThinCrust(windowWidth, currentY)

    return currentY
