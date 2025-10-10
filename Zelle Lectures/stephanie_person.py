
# Make a window big enough to hold the scene
import graphicsPlus as gr
w = 300
h = 300
win = gr.GraphWin('Crazy Toy', w, h)
# Make a person
upper_left = gr.Point(w/2 -20 , 150)
lower_right = gr.Point(w /2+20 ,150+60)
body = gr.Rectangle( upper_left , lower_right )
body.setFill('blue')
body.setOutline('blue')
center = gr.Point(w/2, 150 -20)
head = gr.Circle(center , 20)
head.setOutline(gr.color_rgb(0 ,0 ,0))
head.setFill(gr.color_rgb(255 ,0 ,255))
# Draw the objects.
body.draw(win)
head.draw(win)
# Keep the window open for awhile
win.getMouse() # Pause to view result
win.close() # Close window when done