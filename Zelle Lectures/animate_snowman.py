import graphicsPlus as gr
import time

def draw (objlist, win):
    '''A for loop that draws each item in the given list of shapes'''
    for item in objlist:
        item.draw(win)



def snowman_init(x, y, scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a snowman.
    Minimally, this is just three equal sized circles stack on top of each other
    with two smaller circles for the eyes

    Parameters:
    -----------
    x: int. x coordinate for the bottom circle center.
    y: int. y coordinate for the bottom circle center.
    scale: float. Scaled size of the snowman.

    Returns:
    -----------
    list with 5 Zelle Circle objects in it.
    '''
    radius = 30
    radius2 = 3
    head = gr.Circle(gr.Point(x,y),radius)
    middle = gr.Circle(gr.Point(x, y+radius*scale),radius)
    bottom = gr.Circle(gr.Point(x, y+2*radius*scale),radius)
    eye1 = gr.Circle(gr.Point(x-scale*radius2*2, y),radius2)
    eye2 = gr.Circle(gr.Point(x+scale*radius2*2, y),radius2)
    shapes = [head,middle,bottom,eye1,eye2]
    return shapes

def snowman_test():
    '''Main function that creates the screen, creates the snowman, draws it to the screen.
    '''
    win = gr.GraphWin('snowman',400,400)
    snowman = snowman_init(100,100,2)
    draw(snowman,win)
    for i in range(30):
        for man in snowman:
            man.undraw()
        snowman_animate(snowman,i,win)
        draw(snowman, win)
        win.update()
    win.getMouse()
    win.close()

def snowman_animate(shapes, frame, screen):
    '''Move the snowman at the current iteration of the animation (frame).

    Parameters:
    -----------
    shapes: list with the 5 Zelle Circle objects in it that make up the snowman
    frame: int. Current iteration of the animation
    screen: GraphWin. Screen/canvas that the snowman is on'''
    if frame %2 == 0:
        for shape in shapes:
            shape.move(10,5)
    if frame %2 == 1:
        for shape in shapes:
            shape.move(-10,5)
    screen.update()
        


if __name__ == "__main__":
    snowman_test()

