"""
Nehemia Kaaya
CS 151/Section B
09/24/2025

Lab_04
lab4.py

the main file for my lab 4 code
"""
# --mint-green: #c9fbffff;
# --celeste: #c2fcf7ff;
# --tiffany-blue: #85bdbfff;
# --paynes-gray: #57737aff;
# --rich-black: #040f0fff;

import turtle as t
import random

# Global vars
paddingY = 10
paddingX = 10


def moveTurtle(turtle, destination):
    """
    takes in a cartesian tuple: (x,y) destination and moves the specified turtle
    to the destination and resets it's angle.
    """
    turtle.up()
    turtle.goto(destination)
    turtle.down()
    turtle.setheading(0)


def make_screen(width, height, title, color='black'):
    """
    Makes a 'Screen object: the window in each turtles can draw shapes

    Parameters:

    width: int.
        The width of the window/screen in pixels.
    height: int.
        The height of the window/screen in pixels.
    title: str.
        The name that you'd like to call the pop-up window. Appears at the center of top of the window.
    color: str.
        Color string name (e.g. 'black', 'white', etc). This is the background color of the screen.

    Returns:

    The `Screen` object that you create..
    """

    newScreen = t.Screen()
    newScreen.setup(width, height)
    newScreen.bgcolor(color)
    newScreen.title(title)

    return newScreen


def make_turtle(shape='turtle', penColor='white'):
    """
    Makes a Turtle object

    Parameters:
        shape: str.
    From the turtle documentation website, possible options are:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
    penColor:str.
        Color string name (e.g. 'black', 'white', etc) that is to be the pen color of this turtle.

    Returns:
    The `Turtle` object that you create.
    your code here
    """

    newTurtle = t.Turtle()
    newTurtle.shape(shape)
    newTurtle.color(penColor)
    newTurtle.penup()

    newTurtle.speed(500) # for debugging purposes

    return newTurtle


def reset_turtle(turtle, screen_width, screen_height):
    # turtleThickness = turtle.width()

    # newX = random.randint(turtleThickness, int(screen_width/2-paddingX), 100)

    # why this very complicated way to simply generate x? simple answer: spread.
    # I want to make sure the selected value of x varies enough for 3 successive choices
    # Therefore I am generating a range of values with a max, min and a step
    # shuffling them then selecting a random item. This should make sure each turtle spwans sufficintly spaced out from the others

    # the 100 step is here to ensure a gap between the turtles

    # newX = random.choice(random.shuffle(
    #     list(range(turtleThickness, int(screen_width/2-paddingX), 100))))

    # spreadOptionsForX=list(range(turtleThickness, int(screen_width/2-paddingX), 100))

    spreadOptionsForX=list(range(-int(screen_width/2-paddingX), int(screen_width/2-paddingX), 10))
    random.shuffle(spreadOptionsForX)
    
    newX=random.choice(spreadOptionsForX)

    turtle.goto(newX, int(screen_height/2-(paddingY)))
    turtle.setheading(270)
    turtle.color(random.random(), random.random(), random.random())


def move_and_stamp(turtle, distance, step=10):
    # type casting to int just in case
    # print(list(range(int(step), int(distance+step), step)))
    for _ in range(int(step), int(distance+step), step):
        turtle.stamp()
        turtle.forward(step)


def writeNumStrides(turtle, numStrides, y):
    moveTurtle(turtle, [0, y])
    turtle.clear()
    turtle.write(numStrides, font=('Arial', 30, 'normal'))
    turtle.hideturtle()
    # pkrefkf

def main():
    screen = make_screen(1000, 1000, "One screen to rule them all", "#0F172A")

    screenHeight = screen.window_height()
    screenWidth = screen.window_width()

    strideCounter=0

    jimmy = make_turtle("triangle", "pink")
    tommy = make_turtle("turtle", "#85bdbf")
    willy = make_turtle("circle", "blue")

    counterTurtle = make_turtle("circle", "white")

    jimmy.goto(-200, 0)
    tommy.goto(-50, -50)
    willy.goto(100, 100)

    for _ in range(50):
        reset_turtle(jimmy, screen_width=screenWidth,screen_height=screenHeight)

        strideCounter+=1
        writeNumStrides(counterTurtle, strideCounter, y=screenHeight/2-paddingY)

        reset_turtle(tommy, screen_width=screenWidth,screen_height=screenHeight)

        strideCounter+=1
        writeNumStrides(counterTurtle, strideCounter, y=-(screenHeight/2-paddingY))


        reset_turtle(willy, screen_width=screenWidth,screen_height=screenHeight)

        move_and_stamp(jimmy, screenHeight-paddingY*2, random.randint(60,200))
        move_and_stamp(tommy, screenHeight-paddingY*2, random.randint(60,200))
        move_and_stamp(willy, screenHeight-paddingY*2, random.randint(60,200))

    t.exitonclick()


if __name__ == '__main__':
    main()


# jimmy.forward(100)
# jimmy.right(90)
# jimmy.forward(100)
