'''Test animation and depth'''

import graphicsPlus as gr
import time

def main():
    win = gr.GraphWin('Back and Forth', 300, 300)
    #win.yUp() # make right side up coordinates!

    rect = gr.Rectangle(gr.Point(200, 90), gr.Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)

    cir1 = gr.Circle(gr.Point(40,100), 25)
    cir1.setFill("yellow")
    cir1.draw(win)
    
    cir2 = gr.Circle(gr.Point(150,125), 25)
    cir2.setFill("red")
    cir2.draw(win)

    for i in range(46):
        cir1.move(5, 0)
        time.sleep(.05)

    for i in range(46):
        cir1.move(-5, 0)
        time.sleep(.05)

    message = gr.Text(gr.Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()
