"""
Nehemia Kaaya
CS 151
Section B
Project 07 
turtle_interpreter.py version 1

Draws a shape from a given l-system string
"""


from turtle import Turtle


def drawString(dstring, distance, angle, turtle=None, screen=None):
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

    if (not turtle):
        turtle = Turtle()
        if (not screen):
            screen = turtle.screen()

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
    screen.update()


def hold(turtle):
    '''Holds the screen open until user clicks or presses 'q' 
       key'''

    # Hide the turtle cursor and update the screen
    turtle.hideturtle()
    turtle.update()

    # Close the window when users presses the 'q' key
    turtle.onkey(turtle.bye(), 'q')

    # Listen for the q button press event
    turtle.listen()

    # Have the turtle listen for a click
    turtle.exitonclick()
