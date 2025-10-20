'''Test animation of a group of objects making a face.'''

import graphicsPlus as gr
import time

def moveAll(shapeList, dx, dy):
    ''' Move all shapes in shapeList by (dx, dy).'''   
    for shape in shapeList: 
        shape.move(dx, dy)
            

def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    '''Animate the shapes in shapeList along a line.
    Move by (dx, dy) each time.
    Repeat the specified number of repetitions.
    Have the specified delay (in seconds) after each repeat.
    '''
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)
        

def main():
    win = gr.GraphWin('Back and Forth', 300, 300)
    #win.yUp() # make right side up coordinates!
    message = gr.Text(gr.Point(win.getWidth()/2, 30), ' ')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)


    rect = gr.Rectangle(gr.Point(200, 90), gr.Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)

    head = gr.Circle(gr.Point(40,100), 25)
    head.setFill("yellow")
    head.draw(win)

    eye1 = gr.Circle(gr.Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = gr.Line(gr.Point(45, 105), gr.Point(55, 105))
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = gr.Oval(gr.Point(30, 90), gr.Point(50, 85))
    mouth.setFill("red")
    mouth.draw(win)

    faceList = [head, eye1, eye2, mouth]
    
    cir2 = gr.Circle(gr.Point(150,125), 25)
    cir2.setFill("red")
    cir2.draw(win)

    moveAllOnLine(faceList, 5, 0, 46, .05)
    moveAllOnLine(faceList, -5, 0, 46, .05)

    message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close()

main()
