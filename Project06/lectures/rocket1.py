'''CS151
Zelle Object Practice 
rocket.py'''

import graphicsPlus as gr


def body_init(x,y,scale):
    shapes = []
    r = gr.Rectangle(gr.Point(x-10*scale, y),gr.Point(x+ 10 * scale, y - 80* scale))
    r.setFill(gr.color_rgb(185 ,185 ,185))
    shapes.append(r)
    return shapes # you need to return the object 


def nose_init(x,y,scale):
    shapes = [] #you need an empyt list to create the object list in each part
    #the order of the points parameters need to be in the right order
    nose = gr.Polygon(gr.Point(x - 10 * scale, y - 80 * scale), gr.Point(x, y - 100 * scale), gr.Point(x + 10 * scale, y - 80 * scale))
    shapes.append(nose)# just like body you need to append it to the list
    return shapes # you need to return the object 


def lfin_init(x,y,scale):
    shapes = []
    lf = gr.Polygon(gr.Point(x - 10 * scale, y), gr.Point(x - 10 * scale, y - 20 * scale), gr.Point(x - 25 * scale, y + 5 * scale))
    lf.setFill(gr.color_rgb(200, 170, 150))
    shapes.append(lf)
    return shapes


def rfin_init(x,y,scale):
    shapes = []
    rf = gr.Polygon(gr.Point(x + 10 * scale, y), gr.Point(x + 10 * scale, y - 20 * scale), gr.Point(x + 25 * scale, y + 5 * scale))
    rf.setFill(gr.color_rgb(200, 170, 150))
    shapes.append(rf)
    return shapes


def draw (objlist , win):
    for item in objlist:
        item.draw(win)
        

def rocket_init(x, y, scale): #I did a lot of rearranging here
    # define the rocket shapes here and put them in a list
    shapes = []
    body = body_init(x,y, scale)
    shapes.append(body)
    nose = nose_init(x, y, scale)
    shapes.append(nose)
    lf = lfin_init(x,y,scale)
    shapes.append(lf)
    rf = rfin_init(x,y,scale)
    shapes.append(rf)
    return shapes

def main():
    win = gr.GraphWin('Space Scene', 500 , 500)
    rocket1 = rocket_init(100,300,1)
    rocket2 = rocket_init(400,200, 1.5)
    rocket3 = rocket_init(300,400, 0.5)


    for part in rocket1:
        draw(part,win)
    
    for part in rocket2: 
        draw(part, win)

    for part in rocket3: 
        draw(part, win)
        
    win.update()
    win.getMouse()
    win.close()

if __name__=="__main__":
    main()
