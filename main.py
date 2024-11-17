from My_Functions import *
import turtle

# Parameters for the central retinal artery
central_retinal_artery_length = 125  # Length of the central retinal artery
num_cra = 6  # Number of main branches from the optic nerve

# Parameters for the retinal arterioles
retinal_arterioles_length = 125  # Length of the retinal arterioles
thickness = 6
branch_probability = 0.3  # More likely to branch in the later stages
max_depth = 4  # Controlling the depth of the branching process

# Parameters for the monte carlo lookup table
size = 10000  # Number of angles to generate
mean = 0
left_angle = -45  # Left turn angle limit
right_angle = 45  # Right turn angle limit

if __name__ == "__main__":
    # Set up turtle environment
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("white")
    t.hideturtle()
    t.speed(0)
    t.color("red")
    t.pensize(thickness)

    # Generate the lookup table for angles
    lookup_table = generate_lookup_table(size, mean, left_angle, right_angle)

    # Draw initial branches
    central_retinal_artery = draw_parents(t, num_cra, central_retinal_artery_length)

    # Draw further branches with random walk-like segments and multiple splits
    draw_with_children(central_retinal_artery, lookup_table, retinal_arterioles_length, branch_probability)

    # Keep the window open until clicked
    screen.exitonclick()