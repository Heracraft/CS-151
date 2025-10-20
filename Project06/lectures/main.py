import graphicsPlus as gr

windowWidth=1600
windowHeight=900

def draw_shapes(win):
    c=gr.Circle(gr.Point(100,100), 100)

    c.draw(win)

    win.getMouse()

    win.close()

def main():
    win=gr.GraphWin("Some flipping title", windowWidth,windowHeight)

    draw_shapes(win)

if __name__ == "__main__":
    main()