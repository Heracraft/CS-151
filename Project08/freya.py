'''Freya Hurlburt
CS151 F2025
10/29/2025
turtle_interpreter.py'''

#version 2
import turtle as t
import random as r
import sys

class TurtleInterpreter:

    def __init__(self, dx = 800, dy = 800):
        t.setup(dx,dy)
        t.tracer(False)

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
        L : increases width and sets color to green, goes left distance
        </>: save t.color/restores t.color
        g,y,r: set t.color to green, yellow, or red
        q : begin fill
        a : end fill
        """
        # assign to stack the empty list
        #defcolor = t.color(color)
        #defsize = t.width(1)
        
        #stack = [] 
        colorstack = []
    
        for c in dstring:
            if c == 'F':
                t.forward(distance)
            elif c == '-':
                t.right(angle)
            elif c =='+':
                t.left(angle)
            
            elif c == '<':
                colorstack.append(t.pos())
                colorstack.append(t.heading())   

            elif c == '>':
                t.penup()
                t.setheading(colorstack.pop())
                t.goto(colorstack.pop())
                t.pendown()
                
            elif c == "L":
                #(pclr,fclr) = t.color()
                (w) = t.width()
                colorstack.append(t.color()[0])
                t.left(30)
                t.color('green')
                t.width(4)
                t.forward(distance/2)
                t.color(colorstack.pop())
                t.width(w)

            elif c == '<':
                colorstack.append(t.color()[0] )
            
            elif c =='>' :
                t.color(colorstack.pop())
            
            elif c == 'g':
                t.color(0.15, 0.5, 0.2)
            elif c == 'y':
                t.color(0.8, 0.8, 0.3)
            elif c == 'r':
                t.color(0.7, 0.2, 0.3)

            elif c == 'q':
                t.begin_fill()

            elif c == 'a':
                t.end_fill()
    
                
        t.update()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' 
       key'''

        # Hide the turtle cursor and update the screen
        t.hideturtle()
        t.update()

        # Close the window when users presses the 'q' key
        t.onkey(t.bye, 'q')

        # Listen for the q button press event
        t.listen()

        # Have the turtle listen for a click
        t.exitonclick()     

    def place(self, xpos, ypos, angle= None):
        t.penup()
        t.goto(xpos,ypos)
        if angle != None:
            t.setheading(angle)
        t.pendown()

    def orient(self, angle):
        t.setheading(angle)

    def goto(self, xpos, ypos):
        t.penup()
        t.goto(xpos,ypos)
        t.pendown()

    def setColor(self, c, fill= None):
        t.color(c)
        if fill != None:
            t.fillcolor(fill)

    def setWidth(self, w):
        t.width(w)