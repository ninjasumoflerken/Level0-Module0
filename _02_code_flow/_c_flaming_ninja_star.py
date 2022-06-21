import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def get_next_color(i):
    return colors[i % len(colors)]

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    colors = ['red', 'blue', 'green', 'yellow', 'orange']

    baseSize = 200          # the size of the black part of the star
    flameSize = 130         # the length of the flaming arms
    
    # Make a new turtle
    dart=turtle.Turtle()
    # Make the turtle shape 'turtle', .shape('turtle')
    dart.shape('turtle')
    # Set the turtle width to 2
    dart.pensize(2)
    # Set the turtle speed to 0 (fastest)
    dart.speed(0)
    # Use a for loop to repeat all of the code below ONE time (we will change
    # this later)
    for i in range(39):

        # Set the turtle .fillcolor() to orange
        dart.fillcolor('orange')
        # Call the turtle .begin_fill() function
        dart.begin_fill()
        # TURN RIGHT     Turn the turtle 1/8 of a circle (hint: 360 degrees
        #                will turn a full circle)
        dart.right(45)
        # DRAW           Move the turtle 64 pixels
        dart.forward(64)
        # TURN LEFT      Turn the turtle 40 degrees to the LEFT. (Negative
        #                numbers will turn the turtle counter-clockwise.)
        dart.left(40)
        # DRAW FLAME     Move the turtle the distance in the variable flameSize
        dart.forward(flameSize)
        #                Turn the turtle to the right 170 degrees
        dart.right(170)
        #                Move the turtle the distance in the variable flameSize (again)
        dart.forward(flameSize)
        #  TURN RIGHT    Turn the turtle 62 degrees to the right
        dart.right(62)
        #  DRAW          Move the turtle the distance in the variable baseSize
        dart.forward(baseSize)
        # Call the turtle .end_fill() method
        dart.end_fill()
    # Hide your turtle so you can see the pattern.
        dart.hideturtle()
    # TEST   Run the program. Check that your shape is the same as the first
    #        picture in the recipe. This is one arm of the ninja star.

    # COLOR  Change the turtle's pen color so that the flame is a different
    #        color to the rest of the star. Run the program again. Check the
    #        second picture in the recipe.

    # LOOP   When you have one arm looking right, change your for loop to
    #        repeat 25 times.
    
    # call the turtle .done() method
    turtle.done()
