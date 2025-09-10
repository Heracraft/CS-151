from turtle import *

# I chose a Rhombus
# Sides of equal length
# 2 sets of angles

# up()
# goto(-200, 200) #Start the 'pen' at -200,200 so that the 400 wide shape is centered
# down()


def drawRhombus(size=400, internalAngle=60):
    forward(size)
    right(internalAngle)
    forward(size)
    right(180-internalAngle)
    forward(size)
    right(internalAngle)
    forward(size)


# drawRhombus()
# exitonclick()
