"""
Nehemia Kaaya
04/10/2025
lab5.py.
"""

import turtle

# Named constants
NUM_ITERATIONS = 300
INITIAL_PEN_SIZE = 1
PEN_SIZE_GROWTH_RATE = 1.004
FORWARD_MULTIPLIER = 1.5
TURN_ANGLE = 91
FIRST_COLOR_PHASE = 101
SECOND_COLOR_PHASE = 201

def setup():
    """
    creates and configures the turtle and screen objects.
    They are returned in a tuple
    """
    pen = turtle.Turtle()
    screen = turtle.getscreen()

    screen.bgcolor("black")
    pen.color("white")
    pen.speed(0)  # Set speed to fastest
    pen.pensize(INITIAL_PEN_SIZE)

    return pen, screen


def main():
    #created a main function to serve as the entry point.

    pen, screen = setup()
    for i in range(NUM_ITERATIONS):
        # Move and turn the turtle.
        pen.forward(i * FORWARD_MULTIPLIER)
        pen.left(TURN_ANGLE)

        # Increase the pen size slightly with each iteration.
        current_pen_size = pen.pensize()
        pen.pensize(current_pen_size * PEN_SIZE_GROWTH_RATE)

        # Determine the color based on the current iteration.
        # The color transitions from red to yellow to a whitish-blue.
        if i < FIRST_COLOR_PHASE:
            # Red
            r = i / (FIRST_COLOR_PHASE - 1)
            g = 0
            b = 0
        elif i < SECOND_COLOR_PHASE:
            # Yellow
            segment_progress = (i - FIRST_COLOR_PHASE) / (SECOND_COLOR_PHASE - FIRST_COLOR_PHASE)
            r = 1 - segment_progress
            g = segment_progress
            b = 0
        else:
            # blue
            segment_progress = (i - SECOND_COLOR_PHASE) / (NUM_ITERATIONS - SECOND_COLOR_PHASE)
            r = 1 - segment_progress
            g = 1 - segment_progress
            b = segment_progress
            
        pen.color((r, g, b))

    # CLEANUP
    pen.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()