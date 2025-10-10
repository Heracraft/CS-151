'''lecture_17_objects_in_lists.py
Show slices of lists of objects not independent
CS 151: Computational Thinking: Visual Media
Spring 2021
'''
import turtle

def setColor(turtles, colorList):
    for i in range(len(turtles)):
        turtles[i].color(colorList[i])

def forward(turtles, amount=100):
    '''Move all turtles `amount` units in x direction'''
    for turt in turtles:
        turt.forward(amount)

def right(turtles, angle = 90):
    for turt in turtles:
        turt.right(angle)

def penup(turtles):
    for turt in turtles:
        turt.penup()
        

# Create the screen
screen = turtle.Screen()

turt1 = turtle.Turtle()
turt1.goto(0, 100)
turt2 = turtle.Turtle()
turt2.goto(0, 200)
turt3 = turtle.Turtle()
turt3.goto(0, 300)

# Add them to a list
turtles = [turt1, turt2, turt3]

# Set the color of each rectangle to a unique color
setColor(turtles, ['green', 'red', 'blue'])
penup(turtles)

# Wait until we hit enter
input('Pausing until you press Enter...')

# Slice the Turtle object list, taking the 1st two turtles to move them forward
turtSlice = turtles[:2]

# Draw all 3 in the original list
#Is there a way to make this code below more efficient?)
#forward(turtSlice)
forward(turtles)
forward(turtles)
right(turtles)

forward(turtles)
forward(turtles)
forward(turtles)
right(turtles)

forward(turtSlice)
forward(turtles)
forward(turtSlice)
forward(turtles)

# Close the window after the click
screen.exitonclick()
