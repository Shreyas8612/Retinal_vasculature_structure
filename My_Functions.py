import numpy as np
import math
import random
from main import *

# Define the lookup table using a normal distribution
def generate_lookup_table(size=10000, mean=0, std_dev=1):
    angles = np.random.normal(mean, std_dev, size)
    angles = np.clip(angles, -45, 45)
    return angles.tolist()

def generate_vessel(start_point, depth=0):
    if depth > max_depth:
        return []

    branches = []
    if random.random() < branch_probability:
        num_branches = random.randint(1, 2)
        for _ in range(num_branches):
            length = random.uniform(*length_range)
            angle = random.uniform(*angle_range)
            x_new = start_point[0] + length * np.cos(np.radians(angle))
            y_new = start_point[1] + length * np.sin(np.radians(angle))
            new_point = (x_new, y_new)
            branches.append((start_point, new_point))
            branches += generate_vessel(new_point, depth + 1)

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

# Function to create a new turtle
def create_new_turtle(t):
    new_turtle = turtle.Turtle()
    new_turtle.speed(0)
    new_turtle.penup()
    new_turtle.goto(t.position())
    new_turtle.setheading(t.heading())
    new_turtle.pendown()
    new_turtle.pensize(t.pensize() * 0.8)  # Reduce thickness for new branches
    return new_turtle


# We provide instructions for the turtle to draw the L-system
# F: Move forward, +: Turn right, -: Turn left, [: Save state, ]: Restore state
# We use a stack to keep track of the turtle's position and direction
# Draw L-System with Monte Carlo extension
# Function to draw using multiple turtles
def draw_with_multiple_turtles(turtles, instructions, lookup_table, length, branch_probability, depth=0):
    next_turtles = []
    for t in turtles:
        stack = []
        current_length = length

        for command in instructions:
            if command == "F":
                t.pendown()
                t.forward(current_length)

                # Randomly decide if we create a new turtle to branch
                if random.random() < branch_probability and depth < max_depth:
                    new_turtle = create_new_turtle(t)
                    next_turtles.append(new_turtle)

            elif command == "+":
                angle_variation = random.uniform(-5, 5)
                angle = random.choice(lookup_table) + angle_variation
                t.right(angle)

            elif command == "-":
                angle_variation = random.uniform(-5, 5)
                angle = random.choice(lookup_table) + angle_variation
                t.left(angle)

            elif command == "[":
                position = t.position()
                heading = t.heading()
                stack.append((position, heading, current_length, t.pensize()))
                t.pensize(max(t.pensize() - 1, 1))  # Decrease thickness for branches
                current_length *= length_decrement  # Decrease length for branches

            elif command == "]":
                position, heading, current_length, thickness = stack.pop()
                t.penup()
                t.goto(position)
                t.setheading(heading)
                t.pensize(thickness)

        # Add all newly created turtles to the next round of drawing
    if next_turtles:
        draw_with_multiple_turtles(next_turtles, instructions, lookup_table, length * length_decrement, branch_probability, depth + 1)


