from shapelib import * 
"""
Nehemia Kaaya
CS151 Section B
Project01 drawing a landscape

Where's the turtle import? We're importing every function from shapelib.py
This includes the turtle methods/commands! and our custom shapes
"""

def testScene():
    if (not spire):
        raise Exception("shapes not accessible from shaplib.py, check the imports")
    

def outdoor_scene1():
    vertex=[0,700]
    bgcolor("#1B569E") #sets the background to blue
    color("#FFFFF0")

    tracer(False) #fordebugging purposes. Turns off drawing animation 
    # speed(300)    #fordebugging purposes

    print("main functionnnn")
    vertex,_=spire(vertex,100) # every shape function returns a new vertex, a new origin for the next shape to be drawn.
    # we reassign this return value to the global vertex variable which will be passed down to the next shape function
    # Most functions also return a width value which denotes the cross sectional width of the shape
    # This is used by the next shape if needed to inform it's scale and or positioning
    # in cases where it is not needed, We put a _ since the return value is a list.
    
    futureVertex, radius=hexagonalCylinderFace([vertex[0],vertex[1]-30],20, 50) #notice how we're not re-assigning vertex right now
    # despite it being returned by hexagonalCylinderFace. It's because i want the next shape to be drawn
    # starting where the spire ended then we'll update vertex with the new vertex

    # color("black", "white")

    semiCircle([radius/2,vertex[1]-(radius*0.3)],radius/2)

    vertex=futureVertex

    vertex,_=hexagonalCylinderFace(vertex,25, 60)
    vertex,_=hexagonalCylinderFace(vertex,40, 100)
    vertex,_=hexagonalCylinderFace(vertex,50, 60)
    vertex,_=hexagonalCylinderFace(vertex,60, 130)

    begin_fill()
    vertex=rectangle([vertex[0], vertex[1]+50], 230, 175, "#855646")
    end_fill()

    color("#FFFFF0")

    futureVertex,_=spire([vertex[0], vertex[1]+80], 120, 65)
    begin_fill()
    vertex,baseLength=spire([vertex[0], vertex[1]+70], 100, 65)
    end_fill()
    vertex=futureVertex

    vertex=rectangle(vertex, baseLength, 50, "#FFFFF0", True)

    color("#fefec7")
    # begin_fill()
    frieze([vertex[0], vertex[1]+50], baseLength, 10, 30)
    # end_fill()

    vertex=pillars(vertex, baseLength,200, 30)
    
    vertex,maxWidth=stairs(vertex, baseLength/2, 15, 5)
    vertex,maxWidth=stairs(vertex, maxWidth*1.4, 15, 5) #each stair stack will start wider than it's predecessor
    vertex,maxWidth=stairs(vertex, maxWidth*1.4, 15, 5) #each stair stack will start wider than it's predecessor
    #about 1.3 wider


    for _ in range(3):
        baseX=200
        baseY=700
        # We want to draw geometric clouds but want them spaced out in a random range of X,
        # We use the random module for that.
        deltaX=random.randrange(0,400)
        deltaY=random.randrange(0,200)
        clouds([baseX+deltaX,baseY-deltaY], 50)
        
    tracer(True)

testScene()

def main():
    outdoor_scene1()

main()

exitonclick()