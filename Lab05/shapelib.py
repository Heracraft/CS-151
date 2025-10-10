import turtle
# import math # unsed module

window = turtle.getscreen()
tammy = turtle.Turtle()


def triangle(width, fill_color):
    """Draws an equilateral triangle given a width."""
    tammy.color(fill_color)
    tammy.setheading(0)
    
    tammy.begin_fill()
    
    for _ in range(3):
        tammy.forward(width)
        tammy.left(120)

    tammy.end_fill()


def rectangle(width, height, fill_color):
    """Draws a rectangle given a width and height."""
    tammy.color(fill_color)
    tammy.setheading(0)
    
    tammy.begin_fill()
    # fix: An additional loop is required for the rectangle to be completed.
    for _ in range(2):
        tammy.forward(width)
        tammy.left(90)
        tammy.forward(height)
        tammy.left(90)
    tammy.end_fill()

# removed turtle.exitonclick(). Will be placed on the main file instead