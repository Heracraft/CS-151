
import graphicsPlus as gr
import shape_list as sl
def main ():
    win = gr.GraphWin('Beach Scene', 300 , 300)

    ball = sl.ball_init( 150 , 150 , 1 )
    beach = sl.beach_init ( 0, 170 , 1 )
    scene_list =[beach , ball ]

    for part in scene_list :
        sl.draw(part, win)

    win.update()
    # close
    win.getMouse ()
    win.close ()

if __name__ == '__main__':
    main ()