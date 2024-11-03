import turtle

# Define the L-system parameters
axiom = "F"
rules = {
    "F": "FF+[+F-F-F]-[-F+F+F]"
}

angle = 22.5  # Angle to turn (adjust for more natural branching)
iterations = 4  # Number of iterations (increase for more complexity)


def apply_rules(axiom, rules):
    """Apply production rules to the axiom."""
    return ''.join(rules.get(ch, ch) for ch in axiom)


def create_lsystem(axiom, rules, iterations):
    """Generate the L-system string after a number of iterations."""
    for _ in range(iterations):
        axiom = apply_rules(axiom, rules)
    return axiom


def draw_lsystem(t, instructions, angle, length):
    """Interpret the L-system string and draw the result."""
    stack = []
    for command in instructions:
        if command == "F":
            t.forward(length)
        elif command == "+":
            t.right(angle)
        elif command == "-":
            t.left(angle)
        elif command == "[":
            # Save the turtle's state
            position = t.position()
            heading = t.heading()
            stack.append((position, heading))
        elif command == "]":
            # Restore the turtle's state
            position, heading = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()


# Main code
if __name__ == "__main__":
    # Create the L-system string
    instructions = create_lsystem(axiom, rules, iterations)

    # Set up the turtle graphics
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.hideturtle()
    t.speed(0)
    t.left(90)  # Start facing upwards
    t.penup()
    t.goto(0, -250)  # Start near the bottom of the screen
    t.pendown()

    # Draw the L-system
    draw_lsystem(t, instructions, angle, length=5)

    # Keep the window open until clicked
    screen.exitonclick()