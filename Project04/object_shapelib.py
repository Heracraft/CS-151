# Nehemia Kaaya
# CS 151 F25
# Project 04
# object_shapelib.py: Library for drawing the race scene using turtle objects.

"""
object_shapelib.py
Functions for drawing shapes and the race scene using Turtle objects
"""

import turtle
import random

def make_screen(width=800, height=600, title="Turtle Race"):
    """Create and configure the screen for the race"""
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title(title)
    screen.bgcolor("lightgreen")
    return screen

def make_turtle(x=0, y=0, color="black", shape="turtle"):
    """Create a turtle with specified properties"""
    turt = turtle.Turtle()
    turt.color(color)
    turt.shape(shape)
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    return turt

def goto(turt, x, y, heading=0):
    """Move turtle to position without drawing"""
    turt.penup()
    turt.goto(x, y)
    turt.setheading(heading)
    turt.pendown()

def circle(turt, x, y, radius, penWidth=3, fill=True, fillColor='brown', penColor='black'):
    """Draw a circle at specified position"""
    goto(turt, x, y - radius, 0)
    turt.pensize(penWidth)
    turt.pencolor(penColor)
    
    if fill:
        turt.fillcolor(fillColor)
        turt.begin_fill()
    
    turt.circle(radius)
    
    if fill:
        turt.end_fill()

def rectangle(turt, x, y, width, height, penWidth=2, fill=True, fillColor='brown', penColor='black'):
    """Draw a rectangle at specified position"""
    goto(turt, x, y, 0)
    turt.pensize(penWidth)
    turt.pencolor(penColor)
    
    if fill:
        turt.fillcolor(fillColor)
        turt.begin_fill()
    
    for _ in range(2):
        turt.forward(width)
        turt.right(90)
        turt.forward(height)
        turt.right(90)
    
    if fill:
        turt.end_fill()

def draw_track_lines(turt, x, y, radius):
    """Draw lane divider lines on the circular track"""
    mid_radius = radius
    goto(turt, x, y - mid_radius, 0)
    turt.pensize(2)
    turt.pencolor("white")
    
    circumference = 2 * 3.14159 * mid_radius
    num_dashes = 20
    circumference / (num_dashes * 2)
    
    for i in range(num_dashes):
        turt.pendown()
        turt.circle(mid_radius, extent=360/(num_dashes*2)) # draws a dashed line by dividing some extent
        turt.penup()
        turt.circle(mid_radius, extent=360/(num_dashes*2))

def draw_starting_line(turt, x, y, inner_radius, outer_radius):
    """Draw the starting/finish line"""
    turt.pensize(5)
    turt.pencolor("white")
    goto(turt, x, y - inner_radius, 90)
    turt.pendown()
    turt.backward(outer_radius - inner_radius)
    turt.penup()

def draw_spectator(turt, x, y, color):
    """Draw a simple spectator"""
    goto(turt, x, y, 0)
    turt.pencolor(color)
    turt.fillcolor(color)
    turt.begin_fill()
    turt.circle(5) 
    turt.end_fill()
    
    goto(turt, x, y - 5, 270)
    turt.pendown()
    turt.forward(10)
    turt.penup()

def draw_flag(turt, x, y):
    """Draw a checkered flag"""
    goto(turt, x, y, 0)
    turt.pensize(3)
    turt.pencolor("black")
    turt.pendown()
    turt.forward(30)
    
    # Flag pattern
    flag_x = x + 30
    flag_y = y
    size = 5
    
    for row in range(4):
        for col in range(6):
            color = "black" if (row + col) % 2 == 0 else "white"
            rectangle(turt, flag_x + col * size, flag_y - row * size, 
                     size, size, penWidth=1, fill=True, fillColor=color)
    
    # Pole
    goto(turt, x, y, 270)
    turt.pensize(3)
    turt.pencolor("brown")
    turt.pendown()
    turt.forward(40)
    turt.penup()

def draw_race_scene():
    """Draw the complete race track scene"""
    scene_turtle = turtle.Turtle()
    scene_turtle.speed(0)
    scene_turtle.hideturtle()
    
    
    circle(scene_turtle, 0, 0, 350, penWidth=5, fill=True, 
           fillColor='gray', penColor='black')

    
    circle(scene_turtle, 0, 0, 250, penWidth=5, fill=True, 
           fillColor='gray', penColor='black')
    
    circle(scene_turtle, 0, 0, 150, penWidth=5, fill=True, 
           fillColor='lightgreen', penColor='black')
    
    
    # lane divider
    draw_track_lines(scene_turtle, 0, 0, 200)
    draw_track_lines(scene_turtle, 0, 0, 300)
    
    # starting line
    draw_starting_line(scene_turtle, 0, 0, 150, 350)
    
    # An array of spectator positions and colors
    spectator_positions = [
        (-420, 200, "red"), (-420, 150, "blue"), (-380, 100, "yellow"),
        (420, 200, "red"), (420, 150, "blue"), (420, 100, "yellow"),
        (-480, -200, "green"), (-340, -200, "orange"), (-400, -200, "purple"),
        (380, -200, "green"), (340, -200, "orange"), (400, -200, "purple")
    ]
    
    for x, y, color in spectator_positions:
        draw_spectator(scene_turtle, x, y, color)
    
    draw_flag(scene_turtle, -50, 400)
    draw_flag(scene_turtle, 20, 400)
    
    goto(scene_turtle, 0, 500, 0)
    scene_turtle.pencolor("darkgreen")
    scene_turtle.write("TURTLESTAN CHAMPIONSHIP", align="center", 
                       font=("Arial", 24, "bold"))

    goto(scene_turtle, -30, -190, 0)
    scene_turtle.pencolor("white")
    scene_turtle.write("Lane 1", align="center", font=("Arial", 8, "normal")) # lane labels
    
    goto(scene_turtle, -30, -240, 0)
    scene_turtle.write("Lane 2", align="center", font=("Arial", 8, "normal"))

    goto(scene_turtle, -30, -290, 0)
    scene_turtle.write("Lane 3", align="center", font=("Arial", 8, "normal"))

    goto(scene_turtle, -30, -340, 0)
    scene_turtle.write("Lane 4", align="center", font=("Arial", 8, "normal"))


    scene_turtle.hideturtle()

if __name__ == '__main__':
    screen = make_screen(1200, 1200)
    draw_race_scene()
    screen.exitonclick()