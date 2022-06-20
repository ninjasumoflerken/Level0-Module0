import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    dart = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    dart.shape('turtle')
    # Set your turtle's speed using .speed(2)
    dart.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    dart.color('green')
    dart.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    #yes
    # Move your turtle left or right using .left(90) or .right(90)
    for i in range(4):
        dart.forward(90)
        dart.left(90)


    # Now put the forward and left/right code into a for loop to repeat 4 times.

    # TEST    Did your turtle draw a square?
#yes
    # Move your turtle to a new place on the screen using .goto(x, y)
    dart.goto(45, 45)
    # x=0 and y=0 is the center of the screen
    dart.goto(0, 0)

    # Have your turtle draw a circle using .circle(radius, steps=30)
    dart.color('red')
    dart.begin_fill()
    dart.circle(45, steps=30)
    dart.end_fill()
    # TEST    Did your turtle draw a circle?
#yes
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    dart.goto(-70, -70)
dart.color('blue')
dart.begin_fill()
dart.circle(60, steps=30)
dart.end_fill()

dart.goto(-90, -70)
dart.color('green')
dart.begin_fill()
dart.circle(200, steps=30)
dart.end_fill()

dart.goto(-110, 32)
dart.color('yellow')
dart.begin_fill()
dart.circle(20000000, steps=30)
dart.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
