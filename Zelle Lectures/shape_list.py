import graphicsPlus as gr


# A "shape group" is a list of component graphics objects.
# draw a shapes list of graphics objects in the given window

def draw (objlist , win):
    for item in objlist :
        item.draw(win)

# draw a funky ball at (x,y).
def ball_init ( x, y, scale ):
    shapes = []
    
    b = gr.Circle(gr.Point(x,y), 20 * scale )
    b.setFill('blue')
    b.setOutline('yellow')
    b. setWidth(4 * scale)
    
    shapes.append(b)

    b = gr.Circle(gr.Point(x +15 * scale ,y), 20 * scale )
    b.setFill('purple')
    b.setOutline('yellow')
    b.setWidth(4 * scale)
    shapes.append(b)

    print('printing ball ')
    print(shapes)
    return shapes

def beach_init ( x, y, scale ):
    shapes = []
    r = gr.Rectangle(gr.Point (x,y),
                    gr.Point(x +300 * scale ,y +130 * scale ) )
    r.setFill (gr.color_rgb (210 ,180 ,140))
    shapes.append(r)
    print('printing rectangle ')
    return shapes

