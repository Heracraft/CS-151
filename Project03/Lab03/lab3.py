"""
Nehemia Kaaya
CS 151 Section B
Lab 03
09/17/2025
"""

import random
from turtle import *
import sys

def movePen(destination):
    """
    takes in a cartesian tuple: (x,y) destination and moves the turtle
    to the destination and resets it's angle/inclination 
    I find myself writing up()goto()down() too many times so i created
    this function
    """
    up()
    goto(destination)
    down()
    setheading(0)


def rectangle(x, y, width, height, fill=True):
    '''Draws a `width` x `height` rectangle with bottom-left corner positioned at (`x`, `y`).
    '''

    colors=['#f2f7fd', '#e4ecfa', '#c3d9f4', '#8fbaea', '#5396dd', '#2c78cb', '#1b569e', '#194b8b', '#184174', '#1a3760', '#112340', '#fff7ec', '#ffeed2', '#ffd9a3', '#ffbe69', '#ff952c', '#ff7604', '#fc5800', '#d14000', '#a53207', '#852c09', '#220901', '#fffaeb', '#fdeec8', '#fbdd8c', '#f8c551', '#f6aa1c', '#f08d10', '#d5690a', '#b0480d', '#8f3811', '#762f11', '#441604']
    random.shuffle(colors) #Because I added them to the list in groups in order of their tint, I want them to be shuffled

    fillcolor=random.choice(colors)
    color("black", fillcolor)

    if fill:
        begin_fill()
    
    movePen([x, y])
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    # your code goes here

    if fill:
        end_fill()


def main():

    args=sys.argv

    if (len(args)<2):
        raise Exception("count argument not passed. Please include a size argument when running this module. eg python lab3.py <noOfRectangles>")

    rectangleCount=args[1]

    try:
        rectangleCount=int(rectangleCount)
    except:
        raise Exception(f"The type of Number of Rectangles is invalid. Expected an interger recieved {type(args[1])}")


    pensize(2)
    speed(500) #for debugging purposes

    for index in range(rectangleCount):
        if index < (0.4*200):
        #if its part of the 40%, fill
            fill=True
        x=random.randint(-500,500)
        y=random.randint(-500,500)
        width=random.randint(50,150)
        height=random.randint(50,150)

        rectangle(x,y, width, height, fill)

    exitonclick()

if __name__== '__main__':
  main()
