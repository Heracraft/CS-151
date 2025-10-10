"""
Nehemia Kaaya
04/10/2025
spirals.py
"""

import turtle
import random

fillColors = ['#f2f7fd', '#e4ecfa', '#c3d9f4', '#8fbaea', '#5396dd', '#2c78cb', '#1b569e', '#194b8b', '#184174', '#1a3760', '#112340', '#fff7ec', '#ffeed2', '#ffd9a3', '#ffbe69', '#ff952c',
              "#ff7604", '#fc5800', '#d14000', '#a53207', '#852c09', '#220901', '#fffaeb', '#fdeec8', '#fbdd8c', '#f8c551', '#f6aa1c', '#f08d10', '#d5690a', '#b0480d', '#8f3811', '#762f11', '#441604']
numberOfTurtles=20
penSize=10

def make_turtle(x=0, y=0, color="black", shape="turtle"):
    """Create a turtle with specified properties"""
    newTurtle = turtle.Turtle()
    newTurtle.color(color)
    newTurtle.shape(random.choice(
        ['arrow', 'turtle', 'square', 'triangle', 'circle']))
    newTurtle.goto(x, y)
    newTurtle.pensize(penSize)

    # newTurtle.speed(0) #for debugging purposes

    return newTurtle


def reset_turtle(turtle, inclination):
    """
    Given a turtle, it sets its position to orign (0,0) and orients it towards the provided angle
    inclination
    """
    turtle.up()
    turtle.goto(0,0)
    turtle.setheading(inclination)
    turtle.down()

def setup(noOfTurtles=6):
    """
    creates a screen and a list of n numebr of turtles.
    They are returned in a tuple
    """
    screen = turtle.getscreen()
    turtles = []

    screen.bgcolor("black")

    random.shuffle(fillColors)

    for index in range(noOfTurtles):
        turtleColor = random.choice(fillColors)
        newTurtle = make_turtle(color=turtleColor)
        turtles.append(newTurtle)

        # newTurtle.heading

    return turtles, screen


def draw_spirals(turtles, spiralLength, changeInAngle=0, isDashed=False, isJittery=False, radiatesFromCenter=False):
    extent=90 #how much of the circle is drawn.

    incrementAngle=360/len(turtles)

    for index, turtle in enumerate(turtles):
        '''
        This loop goes over each turtle and draws an arm of the spiral. Each arm is spaced out from another by
        their relative angle/inclination to each other
        '''

        newAngle=(incrementAngle+changeInAngle)*(index+1) #the new angle
        reset_turtle(turtle, newAngle) # brings the turtle back to origin facing it's new angle

        radii=spiralLength # how long should the spiral be? By default this is set to the window height/2

        if not isDashed:
            turtle.circle(radii, 90)

        else:
            dashGap=5 # the gap between the dashes in arcdegrees
            noOfdashes= extent/dashGap # how many dashes to draw. The no is determined by dividing the arclength of the spiral arm
            # with the dash gap.

            for dashIndex, dashExtent in enumerate(range(int(noOfdashes))):
                #arc length 
                currentHeading=turtle.heading()
                currentPos=turtle.xcor(), turtle.ycor()

                turtle.down()

                if isJittery:
                    newHeading = currentHeading+(5*(dashIndex+1/noOfdashes)) if radiatesFromCenter else currentHeading+random.randint(-20,20)

                    # newHeading=currentHeading+random.randint(-20,20) # define a new heading +-20 from the original heading  
                    # newHeading=currentHeading+(5*(dashIndex+1/noOfdashes)) # make it so they radiate from the center  

                    turtle.setheading(newHeading)
                    
                    turtle.circle(radii, dashExtent)

                    turtle.up() # avoid drawing a streak as turtle moves back to originial cirlce line
                    turtle.goto(currentPos) # it also makes sure the straight part of the circle is not drawn just moved along
                    turtle.setheading(currentHeading)
                    

                turtle.circle(radii, dashExtent) # draw aki

                if isJittery:
                    turtle.setheading(currentHeading) # restore the turtle to the original angle along the circle after 
                    # drawing the jittery part

                turtle.up()
                turtle.circle(radii, dashGap) # move the turtle along the circle without drawing. This is that gap.


def main():
    turtles, screen = setup(noOfTurtles=numberOfTurtles)

    # turtle.tracer(False)

    windowHeight = screen.window_height()

    for deltaTheta in range(0, 50, 10):
        # Delta theta defines how the angle of each suscessive spiral changes. Essentially by how much it's rotated
    
        draw_spirals(turtles, windowHeight/2, changeInAngle=deltaTheta, isDashed=True, isJittery=True, )

    turtle.exitonclick()


if __name__ == '__main__':
    main()
