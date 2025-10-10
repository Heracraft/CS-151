"""
Nehemia Kaaya
10/08/2025
Practice Zelle Objects
rocket ship
"""
import graphicsPlus as gr
windowWidth = 1600
windowHeight = 900


def body_init(x, y, scale):
    shapes = []
    r = gr.Rectangle(gr.Point(x-10*scale, y),
                     gr.Point(x + 10 * scale, y - 80 * scale))
    r.setFill(gr.color_rgb(185, 185, 185))
    shapes.append(r)
    return shapes  # you need to return the object


def nose_init(x, y, scale):
    shapes = []  # you need an empyt list to create the object list in each part
    # the order of the points parameters need to be in the right order
    nose = gr.Polygon(gr.Point(x - 10 * scale, y - 80 * scale), gr.Point(x,
                      y - 100 * scale), gr.Point(x + 10 * scale, y - 80 * scale))
    shapes.append(nose)  # just like body you need to append it to the list
    return shapes  # you need to return the object


def lfin_init(x, y, scale):
    shapes = []
    lf = gr.Polygon(gr.Point(x - 10 * scale, y), gr.Point(x - 10 *
                    scale, y - 20 * scale), gr.Point(x - 25 * scale, y + 5 * scale))
    lf.setFill(gr.color_rgb(200, 170, 150))
    shapes.append(lf)
    return shapes


def rfin_init(x, y, scale):
    shapes = []
    rf = gr.Polygon(gr.Point(x + 10 * scale, y), gr.Point(x + 10 *
                    scale, y - 20 * scale), gr.Point(x + 25 * scale, y + 5 * scale))
    rf.setFill(gr.color_rgb(200, 170, 150))
    shapes.append(rf)
    return shapes


def draw(objlist, win):
    for item in objlist:
        item.draw(win)


def rocket_init(x, y, scale):  # I did a lot of rearranging here
    # define the rocket shapes here and put them in a list
    shapes = []
    body = body_init(x, y, scale)
    shapes.append(body)
    nose = nose_init(x, y, scale)
    shapes.append(nose)
    lf = lfin_init(x, y, scale)
    shapes.append(lf)
    rf = rfin_init(x, y, scale)
    shapes.append(rf)
    return shapes

def drawRockets(rockets, window):
    for rocket in rockets:
        for part in rocket:
            draw(part, window)

def moveRockets(rockets):
    for rocket in rockets:
        for part in rocket:
            for shape in part:
                shape.move(0,-500)

def main():
    win = gr.GraphWin('Space Scene', 1000, 1000)
    rocket1 = rocket_init(100, 300, 2)
    rocket2 = rocket_init(500, 600, 3)
    rocket3 = rocket_init(300, 800, 5)

    rockets=[rocket1, rocket2, rocket3]

    drawRockets(rockets, win)

    moveRockets(rockets)

    win.update()
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
