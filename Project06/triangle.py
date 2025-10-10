'''Program: triangle.py or triangle.pyw (best name for Windows)
Interactive graphics program to draw a triangle,
with prompts in a Text object and feedback via mouse clicks.'''

import graphicsPlus as gr

noOfPoints=4

def main():
    win = gr.GraphWin('Draw a Triangle', 1000, 1000)
    #win.yUp() # right side up coordinates
    win.setBackground('yellow')
    message = gr.Text(gr.Point(win.getWidth()/2, 30), f'Click on {noOfPoints} points')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)


    points=[]

    for _ in range(noOfPoints):
        points.append(win.getMouse())

    # Get and draw three vertices of triangle
    # p1 = win.getMouse()
    # p1.draw(win)
    # p2 = win.getMouse()
    # p2.draw(win)
    # p3 = win.getMouse()
    # p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = gr.Polygon(points)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4)  # width of boundary line
    triangle.draw(win)

    message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 

main()
