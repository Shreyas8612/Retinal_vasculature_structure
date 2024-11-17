import turtle
from My_Functions import *

# Define L-system parameters
base_length = 150  # Increase the base length to match the pattern in the image
length_decrement = 0.85
thickness = 6

# Monte Carlo branching parameters
max_depth = 4  # Limit the depth to create controlled branching
branch_probability = 0.7  # More likely to branch in the early stages
initial_branch_count = 6  # Number of main branches from the optic nerve
angle_range = (-45, 45)
radius = 180  # Radius for the initial circular spread of branches
length_range = (20, 35)

if __name__ == "__main__":

    # Set up turtle environment
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("white")
    t.hideturtle()
    t.speed(0)
    t.color("black")
    t.pensize(thickness)

    # Generate the lookup table for angles
    lookup_table = generate_lookup_table()

    # Draw initial branches
    initial_turtles = draw_initial_branches(t, initial_branch_count, base_length)

    # Draw further branches with multiple turtles
    draw_with_multiple_turtles(initial_turtles, lookup_table, base_length * 0.8, branch_probability)

    # Keep the window open until clicked
    screen.exitonclick()