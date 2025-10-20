import graphicsPlus as gr
import time


def main ():
    nsteps = 10
# create the window
    win = gr.GraphWin('Silence', 700 , 700)

# create and fancify my objects
    beach_ball = gr.Circle(gr.Point(350 ,350), 50)
    beach_ball.setFill('yellow')
    beach_ball.setOutline('blue')
    beach_ball.setWidth(4)
# beach_ball_part1= ba.createCircle(150, 150, 20,
# "blue", "yellow", 4)

# draw my objects
    beach_ball.draw( win )

# bounce the ball
    idx = 0
    while not win.checkMouse():
        time.sleep( 0.1 )
        if idx % (2 * nsteps) < nsteps:
            beach_ball.move( 0, 5)
        else :
            beach_ball.move( 0, -5 )
        idx = idx + 1

# wait till the user is sick of looking at it
        #win.getMouse ()
        #win.close ()

if __name__ == '__main__':
    main ()