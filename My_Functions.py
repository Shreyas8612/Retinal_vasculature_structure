from main import *
import random
import numpy as np
import turtle
from scipy.stats import norm

# Global branch counter to limit the total number of branches
branch_count = 0
max_branches = 150  # Set a limit for the maximum number of branches


# Define the lookup table of angles using a normal distribution
# Generates a random size of 10000 angles with a mean of 0 and standard deviation of 15
def generate_lookup_table(sample_size, sample_mean, min_angle, max_angle):
    std_dev = (max_angle - min_angle) / (norm.ppf(0.975) - norm.ppf(0.025))  # Calculate the standard deviation
    angles = np.random.normal(sample_mean, std_dev, sample_size)  # Generate random angles from a normal distribution
    return np.clip(angles, min_angle, max_angle).tolist()  # Clip the angles to [-45, 45] and convert to a list


# Function to create a new turtle for branching with adjusted thickness
def create_new_person(child):
    new_child = turtle.Turtle()
    new_child.speed(0)
    new_child.penup()
    new_child.goto(child.position())
    new_child.setheading(child.heading())
    new_child.pendown()

    # Reduce the thickness of the pen for new branches
    new_thickness = max(child.pensize() * 0.5, 1)  # Reduce the thickness, but not below 1
    new_child.pensize(new_thickness)
    new_child.hideturtle()
    return new_child


# Function to draw the initial branches (Central Retinal Artery) from the seed point (optic nerve)
def draw_parents(parent, num_parents, parent_length):
    cra = []  # List to store the turtle objects for the Central Retinal Artery
    parent.penup()
    parent.goto(0, 0)  # Start at the approximate location of the optic nerve
    parent.pendown()

    for _ in range(num_parents):  # Loop runs to create number of parents (Central Retinal Artery)
        new_parent = create_new_person(parent)

        # Set the random angle to create a distribution above and below 180 degrees
        if _ < num_parents // 2:
            # For the first half of the parents will be above 180 degrees
            random_angle = random.uniform(0, 180)
        else:
            # For the second half of the parents will be below 180 degrees
            random_angle = random.uniform(180, 360)
        new_parent.setheading(random_angle)  # Set the parent to face at the random angle

        # Draw a generally straight path with slight random turns
        num_segments = random.randint(25, 35)  # Number of segments per parent to control its variability in turns
        segment_length = parent_length / num_segments

        for _ in range(num_segments):
            # Apply a small random turn to create a gentle curve
            turn_angle = random.uniform(-10, 10)  # Random small angle to turn slightly left or right depending on the sign of the angle
            new_parent.right(turn_angle)
            new_parent.forward(segment_length * random.uniform(0.8, 1.2))  # Add some variability to each segment length

        cra.append(new_parent)  # Add the new parent to the list of Central Retinal Artery branches
    return cra


# Function to draw the further branches (Retinal Arterioles) from the initial branches (Central Retinal Artery)
def draw_with_children(parents, monte_carlo, child_length, child_probability, depth=0):
    global branch_count

    if depth > max_depth or branch_count >= max_branches:  # Stop if max depth or max branches reached
        return

    ra = []  # List to store the turtle objects for the Retinal Arterioles
    for child in parents:
        # Use random walk to draw the child
        num_segments = random.randint(15, 20)  # Number of segments per branch to control its length
        segment_length = child_length / num_segments

        for _ in range(num_segments):
            # Apply a small random turn to create a gentle curve
            turn_angle = random.uniform(-10, 10)  # Random small angle to turn slightly left or right
            child.right(turn_angle)
            child.forward(segment_length * random.uniform(0.8, 1.2))  # Add some variability to each segment length

            # Randomly decide whether to create sub-branches during the random walk
            if random.random() < child_probability and depth < max_depth and branch_count < max_branches:
                num_grandchildren = random.randint(1, 2)  # Randomly choose the number of sub-branches to create
                for _ in range(num_grandchildren):
                    new_grandchild = create_new_person(child)
                    angle = random.choice(monte_carlo)
                    new_grandchild.right(angle if random.random() < 0.5 else -angle)  # Randomly choose left or right turn

                    ra.append(new_grandchild)
                    branch_count += 1  # Increment the branch count each time a new branch is created

    # Recursive call for the next depth level
    if ra:
        # The deeper we go into the branching structure, the less likely it is to create new branches.
        new_branch_probability = child_probability * 0.9  # Reduce the probability of branching at each level
        draw_with_children(ra, monte_carlo, child_length, new_branch_probability, depth + 1)

