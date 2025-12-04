"""
Nehemia Kaaya
CS 151
Section B
Project 11
turtle_interpreter.py version 2
Adapted from Project 08

Draws a shape from a given l-system string
"""


import turtle


class TurtleInterpreter:

    def __init__(self, dx=800, dy=800, bgColor=None, customTurtle=None):
        self.windowWidth=dx
        self.windowHeight=dy
        self.turtle = customTurtle

        if customTurtle is None:
            turtle.setup(width=dx, height=dy)
            turtle.tracer(False)
            
            if bgColor:
                turtle.getscreen().bgcolor(bgColor)

    def drawString(self, dstring, distance, angle):
        """Interpret the characters in string dstring as a series of turtle commands"""
        
        stack = []
        colorStack = []

        t = self.turtle if self.turtle else turtle
        
        if self.turtle is None:
            screen = turtle.Screen()

        for char in dstring:
            if char == 'F' or char == 'G':
                t.forward(distance)
            elif char == '-':
                t.right(angle)
            elif char == '+':
                t.left(angle)
            elif char == '[':
                stack.append({
                    'heading': t.heading(),
                    'position': t.position()
                })
            elif char == ']':
                popped = stack.pop()
                poppedPosition = popped['position']

                t.setheading(popped['heading'])
                t.up()
                t.goto(poppedPosition[0], poppedPosition[1])
                t.down()

            elif char == 'L':
                w = t.width()
                colorStack.append(t.color()[0])
                t.left(30)
                t.color('green')
                t.width(4)
                t.forward(distance/2)
                t.color(colorStack.pop())
                t.width(w)

            elif char == '<':
                colorStack.append(t.color()[0])

            elif char == '>':
                t.color(colorStack.pop())

            elif char == 'g':
                t.color(0.15, 0.5, 0.2)
            elif char == 'y':
                t.color(0.8, 0.8, 0.3)
            elif char == 'r':
                t.color(0.7, 0.2, 0.3)

            elif char == 'q':
                t.begin_fill()

            elif char == 'a':
                t.end_fill()
        
        if self.turtle is None:
            screen.update()
        elif hasattr(self.turtle.screen, 'update'):
            self.turtle.screen.update()

    def getDimensions(self):
        return (self.windowWidth, self.windowHeight)

    def place(self, xpos, ypos, angle=None):
        t = self.turtle if self.turtle else turtle
        
        if ypos == "end":
            if self.turtle is None:
                screen = turtle.getscreen()
                height = screen.window_height()
            else:
                height = self.windowHeight
            
            ypos = -height/2

        t.up()
        t.goto(xpos, ypos)
        if angle != None:
            t.setheading(angle)
        t.down()

    def orient(self, angle):
        t = self.turtle if self.turtle else turtle
        t.setheading(angle)

    def setColor(self, c):
        t = self.turtle if self.turtle else turtle
        t.color(c)

    def setWidth(self, w):
        t = self.turtle if self.turtle else turtle
        t.width(w)

    def hold(self):
        """Holds the screen open until user clicks or presses 'q' key"""
        if self.turtle is None:
            turtle.hideturtle()
            turtle.update()
            turtle.onkey(turtle.bye, 'q')
            turtle.listen()
            turtle.exitonclick()
