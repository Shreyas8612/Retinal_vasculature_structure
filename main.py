import turtle
from My_Functions import *

# Define the L-system parameters
axiom = "F" # The starting point
rules = { "F": "F[+F]F[-F]F" } # How to change the axiom as it grows
length = 5  # Length of each line segment
Thickness = 3  # Thickness of the lines

angle = 15  # Angle to turn (adjust for more natural branching)
iterations = 3  # Number of iterations (increase for more complexity)

if __name__ == "__main__":
    # Create the L-system string
    instructions = create_lsystem(axiom, rules, iterations)

    # Set up the turtle for drawing
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.hideturtle()  # Hide the turtle icon
    t.speed(0)  # Set the drawing speed to the fastest
    t.left(90)  # Start facing upwards (As Turtle starts facing right by default)
    t.penup()
    t.goto(0,0)  # Start at the center
    t.pendown()

    # Draw the L-system
    draw_lsystem(t, instructions, angle, length, Thickness)

    # Keep the window open until clicked
    screen.exitonclick()