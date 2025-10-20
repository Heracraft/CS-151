#This file has some of the elements of shape_group and
# demonstrates how to animate an image
import graphicsPlus as gr
import time


# These functions make it possible to draw, undraw, and move a
# shape group.
def draw( shape_list, win ):
	for shape in shape_list:
		shape.draw( win )
		
def undraw( shape_list, win ):
	for shape in shape_list:
		shape.undraw( )
		
def move( shape_list, dx, dy ):
	for shape in shape_list:
		shape.move( dx, dy )
		
# An XXXX_init function should generate a set of objects to draw a complex object
# that complex objects should be at position (x,y) and have the given scale.
# This returns the shapes for a cannon with the upper lefthand corner at (x,y).		
def cannon_init(x, y, scale):
	""" Make the shapes necessary to draw a cannon with top left corner at x, y
	Cannon is about 100*scale pixeks wide. Return the list of shapes"""
	topLeft = gr.Point(x,y)
	bottomRight = gr.Point(x+100*scale,y+26*scale)
	barrel = gr.Rectangle(topLeft, bottomRight)
	barrel.setFill('black')

	barrelEnd = gr.Circle(gr.Point(x,y+13*scale),13*scale)
	barrelEnd.setFill('black')

	barrelFuse = gr.Line(gr.Point(x+10*scale,y), gr.Point(x+10*scale,y-10*scale))
	barrelFuse.setWidth(3)

	rearwheel = gr.Circle(gr.Point(x,y+40*scale), 15*scale)
	rearwheel.setFill('brown')
	frontwheel = gr.Circle(gr.Point(x+50*scale,y+40*scale), 15*scale)
	frontwheel.setFill('brown')

	bullet = gr.Polygon(gr.Point(x+110*scale,y+2*scale), gr.Point(x+110*scale,y+24*scale), gr.Point(x+140*scale,y+13*scale))
	bullet.setFill('red')

	return [barrel, barrelEnd, rearwheel, frontwheel, bullet]

	
# XXXX_animation_frame is meant to perform 1 frame of the animation
# It takes in the shape list for this shape group, a frame_num
# (which is sort of a measure of time) and a GraphWin	
def cannon_animation_frame( cannon_list, frame_num, win ):
	if frame_num < 5:
		just_cannon = cannon_list[:-1]
		move( just_cannon, -3, 0 )
	elif frame_num < 8:
		just_cannon = cannon_list[:-1]
		move( just_cannon, 3, 0 )
	bullet = cannon_list[-1]
	bullet.move( 5, 0 )

# And here is an init function for a tree shape group	
def tree_init( x, y, scale ):
	leaves = gr.Circle( gr.Point( x, y ), 30*scale )
	leaves.setFill( 'green' )
	trunk = gr.Rectangle( gr.Point( x-3*scale, y+30*scale ),
						 gr.Point( x+3*scale, y+(30+15)*scale ) )
	trunk.setFill( 'brown' )
	return [trunk, leaves]			
	
# And here is an animation function for a tree shape group	
def tree_animation_frame( tree_list, frame_num, win ):
	if frame_num % 8  < 2 or frame_num % 8 >= 6:
		tree_list[1].move( 2, 0 )
	else:	
		tree_list[1].move( -2, 0 )
	
# This is an example main function
def test():
    #make a window
	w = 500
	h = 300
	win = gr.GraphWin("Cannon Demo", w, h)

    # Make the shape groups
	tree1 = tree_init( 300, 200, 1 )
	tree2 = tree_init( 150, 100, 1 )
	cannon_list = cannon_init( 75, 250, 1 )
	
	# Draw the shapes
	draw( tree1, win )
	draw( tree2, win )
	draw( cannon_list, win )
	
	# Loop over the frames, animating each time.
	for frame_num in range(1000):
		cannon_animation_frame( cannon_list, frame_num, win )
		tree_animation_frame( tree1, frame_num, win )
		if win.checkMouse():
			break
		time.sleep( 0.1 )
	
	#win.getMouse()
	
if __name__ == '__main__':
	test()