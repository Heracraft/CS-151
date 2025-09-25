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


def movePen(turtle, destination):
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

    newScreen=t.Screen()
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

    newTurtle=t.Turtle()
    newTurtle.shape(shape)
    newTurtle.color(penColor)
    newTurtle.penup()

    return newTurtle

def main():
    mainScreen=make_screen(1000,1000, "One screen to rule them all", "#0F172A")

    jimmy = make_turtle("triangle", "pink")
    tommy= make_turtle("turtle", "#85bdbf")
    willy = make_turtle("circle", "blue")

    jimmy.goto(-200,0)
    tommy.goto(-50,-50)
    willy.goto(100,100)

    t.exitonclick()

if __name__ == '__main__':
    main()


# jimmy.forward(100)
# jimmy.right(90)
# jimmy.forward(100)

