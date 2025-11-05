"""
Testing file for this project. A sort-of catchall file.
"""

import turtle
import sys
import lib.lsystem as ls
import lib.turtle_interpreter as it


# takes in the list of strings from the command line
# reads in an lsystem file, generates the string and
# draws two copies of a pair of shapes

def pair( lstr, x, y, scale, angle ):
    oldheading = turtle.heading()

    turtle.up()
    turtle.goto(x, y )
    turtle.down()
    turtle.right(270)
    turtle.color( 0.5, 0.6, 0.8 )
    turtle.width( 2 )
    it.drawString( lstr, scale*0.75, angle )

    turtle.up()
    turtle.goto( x, y )
    turtle.down()

    turtle.color( 0.1, 0.2, 0.4 )
    turtle.width( 1 )
    turtle.left(135)
    it.drawString( lstr, scale*0.4, angle )


    turtle.setheading( oldheading )

    return

def main(argv):

    # check if there are enough arguments
    if len(argv) < 4:
        print("usage: %s <lsystem index> <distance> <angle>" % (argv[0]))
        exit()

    # create the lsystem from a file
    lsys = ls.createLsystemFromFile("lsystem.json", int(argv[1]))

    # build the lsystem string with 3 iterations
    lstr = ls.buildString(lsys, 3)

    # print(lstr)

    dist = float(argv[2])
    angle = float(argv[3])

    # setup and turn off tracing
    turtle.setup(500, 500)
    turtle.tracer(False)

    # # draw the lsystem to the tree is oriented up
    # turtle.left(90)
    # turtle.up()
    # turtle.goto(-100, 100)
    # turtle.down()
    # turtle.color('blue')
    # turtle.width(3)

    # it.drawString(lstr, dist, angle)

    # draw the two pairs
    turtle.tracer(False)
    pair( lstr, -100, 100, dist, angle )
    pair( lstr, 100, -100, dist*0.5, angle )

    # wait
    it.hold()


if __name__ == "__main__":
    main(sys.argv)
