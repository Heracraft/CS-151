
"""
Nehemia Kaaya
CS 151 F25
Project 04
race.py
Main program for the turtle racing simulation
"""

import turtle
import random
import math
from object_shapelib import draw_race_scene, goto

def make_turtle(x=0, y=0, color="black", shape="turtle"):
    """Create a turtle with specified properties"""
    newTurtle = turtle.Turtle()
    newTurtle.color(color)
    newTurtle.shape(shape)
    newTurtle.penup()
    newTurtle.goto(x, y)
    newTurtle.speed(0)

    return newTurtle

def move_turtle(turt, angle, radius):
    """Moves the Turtle object turt speed units around the circular track"""
    turt.pencolor("gray")
    # The turtle moves 'angle' degrees around the circle. So a higher speed simply means a bigger circle is drawn faster
    turt.circle(radius, extent=angle/(2*math.pi))

def update_score_display(score_turtle, score, turtle_name, x, y):
    """Update the score display for a turtle"""
    score_turtle.clear()
    goto(score_turtle, x, y, 0)
    score_turtle.pencolor("darkblue")
    score_turtle.write(f"{turtle_name}: {score} laps", 
                       align="center", font=("Arial", 16, "bold"))

def main():
    """Main function to run the turtle race"""

    turtle.tracer(False)

    # Make a Screen object
    screen = turtle.Screen()
    screen.setup(1200, 1200)
    screen.title("Turtle Race Championship")
    screen.bgcolor("lightgreen")
    
    draw_race_scene()
    
    # Turtle 1 on 1st lane
    turtle1 = make_turtle(0, -175, "red", "turtle")
    turtle1.pensize(2)
    turtle1.setheading(0)
    
    # Turtle 2 on 2nd lane
    turtle2 = make_turtle(0, -225, "blue", "turtle")
    turtle2.pensize(2)
    turtle2.setheading(0)
    
    score_turtle1 = make_turtle(-200, -320, "red", "turtle")
    score_turtle1.hideturtle()
    
    score_turtle2 = make_turtle(200, -320, "blue", "turtle")
    score_turtle2.hideturtle()
    
    score1 = 0
    score2 = 2
    angle1 = 0
    angle2 = 0
    
    # display an initial score
    update_score_display(score_turtle1, score1, "Red Turtle", -200, -420)
    update_score_display(score_turtle2, score2, "Blue Turtle", 200, -420)
    
    base_speed1 = .5
    base_speed2 = .49
    
    turtle.tracer(True)
    
    for _ in range(1000):
        # bump the speed up and down randomly
        speed1 = base_speed1 + random.uniform(-.1, .001)
        speed2 = base_speed2 + random.uniform(-.1, .001)
        
        turtle1.pendown()
        move_turtle(turtle1, angle1, 175)
        turtle1.penup()
        
        turtle2.pendown()
        move_turtle(turtle2, angle2, 225)
        turtle2.penup()
        
        angle1 += speed1
        angle2 += speed2

        print(angle1, angle2, angle1>=360,  angle2>=360)
        
        # Check for lap completion
        if angle1 >= 360:
            score1 += 1
            angle1 = angle1 - 360
            update_score_display(score_turtle1, score1, "Red Turtle", -200, -420)
        
        if angle2 >= 360:
            score2 += 1
            angle2 = angle2 - 360
            update_score_display(score_turtle2, score2, "Blue Turtle", 200, -420)
            # Flash turtle to celebrate lap completion
            original_color = turtle2.pencolor()
            turtle2.color("yellow")
            screen.update()
            turtle2.color(original_color)
        
    
    winner_turtle = make_turtle(0, 0, "gold", "turtle")
    winner_turtle.hideturtle()
    goto(winner_turtle, 0, 50, 0)
    
    if score1 > score2:
        winner_text = "RED TURTLE WINS!"
        winner_turtle.pencolor("red")
    elif score2 > score1:
        winner_text = "BLUE TURTLE WINS!"
        winner_turtle.pencolor("blue")
    else:
        winner_text = "IT'S A TIE!"
        winner_turtle.pencolor("purple")
    
    winner_turtle.write(winner_text, align="center", 
                        font=("Arial", 28, "bold"))
    
    screen.exitonclick()

if __name__ == '__main__':
    main()