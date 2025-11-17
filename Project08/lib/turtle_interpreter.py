"""
Nehemia Kaaya
CS 151
Section B
Project 08
turtle_interpreter.py version 2

Draws a shape from a given l-system string
"""


import turtle


class TurtleInterpreter:

    def __init__(self, dx=800, dy=800, bgColor=None):
        self.windowWidth=dx
        self.windowHeight=dy

        turtle.setup(width=dx, height=dy)

        # turtle.tracer(False)

        if bgColor:
            turtle.getscreen().bgcolor(bgColor)

    def drawString(self, dstring, distance, angle):
        """ Interpret the characters in string dstring as a series
        of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the
        angle (in degrees) for each right or left command. The list
        of turtle supported turtle commands is:
        F : forward
        - : turn right
        + : turn left
        [ : save the turtle's heading and position
        ] : restore the turtle's heading and position
        """

        stack = []  # THE STACK. 👑
        colorStack = []

        screen = turtle.Screen()

        for char in dstring:
            if char == 'F' or char == 'G':
                turtle.forward(distance)
            elif char == '-':
                turtle.right(angle)
            elif char == '+':
                turtle.left(angle)
            elif char == '[':
                stack.append({
                    'heading': turtle.heading(),
                    'position': turtle.position()
                })
            elif char == ']':
                popped = stack.pop()
                poppedPosition = popped['position']

                turtle.setheading(popped['heading'])
                turtle.up()
                turtle.goto(poppedPosition[0], poppedPosition[1])
                turtle.down()

            elif char == 'L':
                (w) = turtle.width()
                colorStack.append(turtle.color()[0])
                turtle.left(30)
                turtle.color('green')
                turtle.width(4)
                turtle.forward(distance/2)
                turtle.color(colorStack.pop())
                turtle.width(w)

            elif char == '<':
                colorStack.append(turtle.color()[0])

            elif char == '>':
                turtle.color(colorStack.pop())

            elif char == 'g':
                turtle.color(0.15, 0.5, 0.2)
            elif char == 'y':
                turtle.color(0.8, 0.8, 0.3)
            elif char == 'r':
                turtle.color(0.7, 0.2, 0.3)

            elif char == 'q':
                turtle.begin_fill()

            elif char == 'a':
                turtle.end_fill()
        screen.update()

    def getDimensions(self):
        return (self.windowWidth, self.windowHeight)

    def place(self, xpos, ypos, angle=None):
        #  - the method should pick up the pen, place the turtle at location (xpos, ypos), orient the turtle if the angle argument is not None, and then put down the pen. Use the appropriate turtle commands to execute this.

        if ypos == "end":
            screen = turtle.getscreen()
            # width=screen.window_width()
            height = screen.window_height()

            ypos = -height/2

        turtle.up()
        turtle.goto(xpos, ypos)
        if angle != None:
            turtle.setheading(angle)
        turtle.down()

    def orient(self, angle):
        # - the method should use the turtle's setheading function to set turtle's heading to the given angle.
        turtle.setheading(angle)

    def setColor(self, c):
        # - the method should call turtle.color() with the argument c to set the turtle's color.
        turtle.color(c)

    def setWidth(self, w):
        # - the method should call turtle.width() with the argument w to set the turtle's width.
        turtle.width(w)

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' 
        key'''

        # Hide the turtle cursor and update the screen
        turtle.hideturtle()
        turtle.update()

        # Close the window when users presses the 'q' key
        turtle.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        turtle.listen()

        # Have the turtle listen for a click
        turtle.exitonclick()
