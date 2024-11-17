import numpy as np
import math
import random
from main import *

# Define the lookup table using a normal distribution
def generate_lookup_table(size=10000, mean=0, std_dev=15):
    angles = np.random.normal(mean, std_dev, size)
    return np.clip(angles, -45, 45).tolist()  # Clip the angles to [-45, 45] and convert to a list

def generate_vessel(start_point, depth=0):
    if depth > max_depth:  # Base case: stop generating branches if we reach the maximum depth to prevent from infinite branching
        return []

    branches = []
    if random.random() < branch_probability:  # Create a branch with a certain probability between 0 and 1
        num_branches = random.randint(1, 3)  # Generate 1 or 2 branches
        for i in range(num_branches):
            length = random.uniform(*length_range)
            angle = random.uniform(*angle_range)
            x_new = start_point[0] + length * np.cos(angle)
            y_new = start_point[1] + length * np.sin(angle)
            new_point = (x_new, y_new)
            branches.append((start_point, new_point))
            branches += generate_vessel(new_point, depth + 1)  # Recursive call for the next depth level

    return branches

# We apply the rules for each character in the axiom
# If the character is not in the rules, we keep it as is
# If the character is in the rules, we replace it with the rule
# We join all the characters back together to form the new axiom
def apply_rules(axiom, rules):
    return ''.join(rules.get(ch, ch) for ch in axiom)


# We apply the rules for the given number of iterations
# Each iteration updates the axiom based on the rules
def create_lsystem(axiom, rules, iterations):
    for _ in range(iterations):
        axiom = apply_rules(axiom, rules)
    return axiom


# Function to draw initial "straightish curvy" branches
def draw_initial_branches(t, num_branches, base_length):
    initial_turtles = []
    t.penup()
    t.goto(100, 0)  # Start at the approximate location of the optic nerve
    t.pendown()

    for _ in range(num_branches):
        new_turtle = create_new_turtle(t)

        # Set a random angle to create more irregular starting branches
        random_angle = random.uniform(0, 360)
        new_turtle.setheading(random_angle)

        # Draw a generally straight path with slight random turns
        num_segments = random.randint(20, 30)  # Number of segments per branch to control its length
        segment_length = base_length / num_segments

        for _ in range(num_segments):
            # Apply a small random turn to create a gentle curve
            turn_angle = random.uniform(-20, 20)  # Random small angle to turn slightly left or right
            new_turtle.right(turn_angle)
            new_turtle.forward(segment_length * random.uniform(0.8, 1.2))  # Add some variability to each segment length

        initial_turtles.append(new_turtle)

    return initial_turtles

# Function to create a new turtle
def create_new_turtle(t):
    new_turtle = turtle.Turtle()
    new_turtle.speed(0)
    new_turtle.penup()
    new_turtle.goto(t.position())
    new_turtle.setheading(t.heading())
    new_turtle.pendown()
    new_turtle.pensize(t.pensize() * 0.8)
    new_turtle.hideturtle()
    return new_turtle


def draw_with_multiple_turtles(turtles, lookup_table, base_length, branch_probability, depth=0):
    if depth > max_depth:
        return

    next_turtles = []
    for t in turtles:
        # Create branches from current turtle
        if random.random() < branch_probability and depth < max_depth:
            num_sub_branches = 2 if depth < 2 else random.randint(1, 2)
            for _ in range(num_sub_branches):
                new_turtle = create_new_turtle(t)
                angle = random.choice(lookup_table)
                new_turtle.right(angle if random.random() < 0.5 else -angle)
                new_turtle.forward(base_length)
                next_turtles.append(new_turtle)

    # Recursive call for the next depth level
    if next_turtles:
        draw_with_multiple_turtles(next_turtles, lookup_table, base_length * length_decrement, branch_probability, depth + 1)

