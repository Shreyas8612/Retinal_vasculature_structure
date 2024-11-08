# Retinal Vessel Modeling with L-System and Turtle Graphics

## Overview
This project is part of a broader goal to create a model of **retinal blood vessels** to help understand retinal detachment and assist in post-surgery recovery. The main idea is to use **L-systems** (a type of formal grammar) to simulate the branching patterns of blood vessels in the retina. This project uses **Python Turtle Graphics** to visualize these branching patterns, with the generated structures resembling the intricate network of retinal blood vessels.

The ultimate aim is to compare vessel positions before and after surgery and assist patients in positioning their heads to promote the correct placement of the retina during healing. For now, the project focuses on modeling vessel-like branching structures as a foundation.

<img src="L-Systems.webp" alt="L-Systems" width="40%" style="display: block; margin: auto;"/>

*Note: The image above is a visual representation of what an L-system-generated branching structure might look like. The code in this project generates a similar pattern.*

## How It Works

### L-System Basics
- An **L-system** (Lindenmayer System) is a set of rules and an initial sequence (called an **axiom**) that, when iterated over, generates a complex pattern.
- Here, we use a starting axiom "F" and a rule that defines how "F" changes:
  - `F -> FF+[+F-F-F]-[-F+F+F]`
- The symbol "F" means **draw forward**.
- Symbols `+` and `-` represent **turning** by a specified angle.
- The symbols `[` and `]` are used to **save** and **restore** the turtle's position and orientation, creating branches in the drawing.

### Turtle Graphics
- The project uses **Python's Turtle Graphics** to draw the vessel-like structures.
- The turtle starts in the center of the screen, facing upwards, and follows the **L-system instructions** to draw the branches.

### Parameters Used
- **Axiom**: `"F"` — The starting point of our drawing sequence.
- **Rules**: `{"F": "FF+[+F-F-F]-[-F+F+F]"}` — Defines how "F" expands during each iteration.
- **Angle**: `22.5°` — The angle by which the turtle turns to create branches.
- **Iterations**: `4` — The number of times the axiom is expanded by applying the rules.

### How to Run
1. Make sure you have **Python** installed on your system.
2. Copy the code into a Python script file (e.g., `retinal_model.py`).
3. Run the script using Python:
   ```sh
   python retinal_model.py
   ```
4. A window will open, and you will see the turtle drawing the branching structure.

## Code Explanation
1. **L-system Generation**:
   - The `create_lsystem()` function iteratively applies the production rules to generate a sequence that represents the final structure.
2. **Drawing with Turtle**:
   - The `draw_lsystem()` function takes the generated sequence and commands the turtle to draw forward, turn, and create branches.
3. **Main Script**:
   - Sets up the turtle graphics, moves the turtle to the starting point, and then draws the branching structure based on the L-system instructions.

## Future Steps
- **Add Realism**: Adjust the rules and parameters to better mimic the retinal blood vessels' complexity, including the thickness and curvature.
- **Integrate Image Processing**: Use retinal fundus images to compare actual vessels with the generated patterns.
- **Layer Differentiation**: Create separate models for different retinal vascular layers, such as SVP (Superficial Vascular Plexus) and DCP (Deep Capillary Plexus).

## Dependencies
- **Python** (tested on version 3.7 and above)
- **Turtle Graphics** (comes included with standard Python libraries)

## Acknowledgments
- **Lindenmayer Systems**: Inspired by the biological modeling of plant growth.
- **Turtle Graphics**: Provides an intuitive way to visualize branching structures.

## Contact
For questions or contributions, feel free to contact me.

