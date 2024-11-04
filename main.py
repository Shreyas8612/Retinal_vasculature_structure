import turtle
import random
import math

# Define the L-system parameters
axiom = "F" # The starting point
rules = { "F": "F[+F]F[-F]F" } # How to change the axiom as it grows
length = 5  # Length of each line segment
Thickness = 3  # Thickness of the lines

angle = 15  # Angle to turn (adjust for more natural branching)
iterations = 3  # Number of iterations (increase for more complexity)

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


# We provide instructions for the turtle to draw the L-system
# F: Move forward, +: Turn right, -: Turn left, [: Save state, ]: Restore state
# We use a stack to keep track of the turtle's position and direction
def draw_lsystem(t, instructions, angle, length, Thickness):
    stack = []
    for command in instructions:
        if command == "F":
            # Get current position
            x, y = t.position()
            # Convert to polar coordinates
            r = math.hypot(x, y)  # Distance from the origin (center)
            theta = math.atan2(y, x)  # Angle from the x-axis
            # Apply a transformation to warp the space
            # Adding Exponential decay to the radius to simulate less aggressive growth
            r_new = r + (length * random.uniform(0.8, 1.2) * math.exp(-r/100))
            theta_new = theta + random.uniform(-0.1, 0.1) # Random variation in the angle
            # Convert back to Cartesian coordinates
            x_new = r_new * math.cos(theta_new)
            y_new = r_new * math.sin(theta_new)
            # Draw to the new position
            t.pensize(Thickness)
            t.goto(x_new, y_new)
        elif command == "+":
            t.right(angle * random.uniform(0.8, 1.2))  # Add some random factor to the angle
            curvature_factor = random.uniform(0.5, 1.5)
            t.circle(length * curvature_factor , angle * random.uniform(0.8, 1.2))  # Make a smooth turn
        elif command == "-":
            t.left(angle * random.uniform(0.8, 1.2))  # Add some random factor to the angle
            curvature_factor = random.uniform(0.5, 1.5)
            t.circle(length * curvature_factor, angle * random.uniform(0.8, 1.2))  # Make a smooth turn
        elif command == "[":
            # Save the turtle's current state and thickness
            position = t.position()
            heading = t.heading()
            stack.append((position, heading, Thickness))
            # Reduce the thickness for the next branch
            Thickness = max(Thickness - 1, 1)  # Ensure thickness is at least 1
        elif command == "]":
            # Restore the turtle's state
            position, heading, Thickness = stack.pop()  # pop() removes the last saved state
            t.penup()  # We don't want to draw when restoring state
            t.goto(position)
            t.setheading(heading)
            t.pendown()


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