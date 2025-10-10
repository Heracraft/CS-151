import shapelib
# import turtle # unsed

def tree(x_position, y_position, scale):
    """
    Draws a single tree at a specified position and scale.
    A tree consists of a brown rectangular trunk and a green triangular top.
    """
    shapelib.tammy.penup()
    
    # fix: swapped arguments passed into goto to (x, y).
    shapelib.tammy.goto(x_position, y_position)
    
    shapelib.tammy.pendown()

    shapelib.rectangle(40 * scale, 100 * scale, "brown")
    
    shapelib.tammy.penup()
    
    # positions for the leaves centered on the trunk
    leaf_x = x_position - (30 * scale)
    leaf_y = y_position + (100 * scale)
    shapelib.tammy.goto(leaf_x, leaf_y)
    
    shapelib.tammy.pendown()
    
    # Draw the leaves
    shapelib.triangle(100 * scale, "green")


def main():
    """Main function to draw 4 trees made of triangles and a rectangle."""
    
    # turtle.tracer(False) # For debugging purposes

    # Four trees with different positions and scales
    tree(-200, -300, 3)
    tree(0, 0, 1)
    tree(100, 140, 0.7)
    tree(200, 230, 0.5)

    shapelib.tammy.hideturtle()
    
    #fix: added exitonclick() on the 'window' object from shapelib.
    shapelib.window.exitonclick()

# Run the main function
main()