import turtle
from My_Functions import *

# Define the L-system parameters
axiom = "F"  # Starting point
rules = {"F": "F[+F]F[-F]F"}  # Updated rules for realistic branching
base_length = 10  # Base length of each line segment
length_decrement = 0.85  # Factor to reduce length for each iteration
thickness = 4  # Initial thickness of the lines
angle = 25  # Angle for branching
iterations = 4  # Number of iterations for L-system

# Monte Carlo Parameters for Capillary Branching
max_depth = 3
branch_probability = 0.5
angle_range = (-20, 20)
length_range = (5, 10)

# Main code
if __name__ == "__main__":
    instructions = create_lsystem(axiom, rules, iterations)

    # Set up the turtle for drawing
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("white")
    t.hideturtle()
    t.speed(0)
    t.color("black")
    t.penup()
    t.goto(0, -250)  # Start near the center-bottom of the screen
    t.left(90)
    t.pendown()
    t.pensize(thickness)

    lookup_table = generate_lookup_table()
    
    # Draw using multiple turtles
    initial_turtles = [t]
    draw_with_multiple_turtles(initial_turtles, instructions, lookup_table, base_length, branch_probability)

    # Keep the window open until clicked
    screen.exitonclick()