#project 5

import graphicsPlus as gr


win = gr.GraphWin('messing', 400, 400)


# to draw a point

pt = gr.Point(100,50)
pt.draw(win)

#to draw a circle
cir = gr.Circle(pt, 25)
cir.draw(win)
cir.setOutline('red')
cir.setFill('blue')


#to draw a line
line = gr.Line(pt,gr.Point(150, 200))
line.draw(win)


# to draw a rectangle and move it

rect = gr.Rectangle(gr.Point(300,200), pt)
rect.draw(win)

line.move(200, 40)

def draw_shapes():
    my_circle = gr.Circle(gr.Point(100, 150), 20)
    my_circle.setFill(gr.color_rgb(250, 200, 210))
    #my_rec = gr.
    my_circle.draw(win)
    win.getMouse()
    win.close() #closes window


draw_shapes()