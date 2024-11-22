# Retinal Vessel Modeling with Turtle Graphics and Monte Carlo Simulations

## Overview
This project aims to model **retinal blood vessels** using Python **Turtle Graphics** and **Monte Carlo simulations**. The goal is to generate branching structures resembling retinal vessels to assist in understanding retinal detachment and post-surgery recovery. This model will later be integrated with real retinal image data to enhance its accuracy and clinical utility.

The generated patterns simulate the intricate structure of blood vessels in the retina, providing a foundation for future integration with medical imaging.

## How It Works

### Monte Carlo Simulations for Branching Angles
- The **Monte Carlo method** is used to generate a **lookup table of angles** based on a normal distribution. These angles determine the direction of branching, creating realistic vessel-like patterns.
- Parameters for the distribution include:
  - **Mean angle:** 0° (straight path).
  - **Standard deviation:** Derived from the desired branching angle range (e.g., -45° to +45°).
  - **Clipping:** Ensures angles stay within the realistic bounds for branching.
- The symbol "F" means **draw forward**.
- Symbols `+` and `-` represent **turning** by a specified angle.
- The symbols `[` and `]` are used to **save** and **restore** the turtle's position and orientation, creating branches in the drawing.

### Turtle Graphics for Visualization
- **Turtle Graphics** is used to visualize the branching structure.
- The process starts with a central "trunk" (representing the **Central Retinal Artery**) and recursively adds smaller branches (representing **Retinal Arterioles**).
- **Branch Thickness:** Each successive branch reduces in thickness, mimicking the tapering of blood vessels.
- **Random Walks:** Randomly varied forward movements and angle turns add a natural, organic feel to the branching pattern.

### Parameters Used
- **Initial Branch Count:** 6 main branches (Central Retinal Artery).
- **Branch Length:**: 125 units for the initial artery and arterioles.
- **Branching Probability:**: Controls how likely a branch is to split further.
- **Maximum Depth:**: Limits the recursion to ensure computational efficiency.

### How to Run
1. Make sure you have **Python** installed on your system.
2. Copy the code into a Python script file (e.g., `retinal_model.py`).
3. Run the script using Python:
   ```sh
   python retinal_model.py
   ```
4. The Turtle Graphics window will display the branching structure.

## Code Explanation
1. **Monte Carlo Angle Generation:**
   - The `generate_lookup_table()` function creates a list of random angles using a normal distribution. These angles are used to determine how the branches turn, making the branching pattern look more natural and realistic.
2. **Creating New Branches:**
   - The `create_new_person()` function creates a new "turtle" (a drawing object) that starts from the position and direction of its "parent branch." It reduces the thickness of the new branch to simulate the tapering of real blood vessels.
3. **Drawing Central Retinal Arteries:**
   - The `draw_parents()` function generates the main branches starting from the center, representing the Central Retinal Artery. These branches follow random directions and have a generally straight path with slight turns.
4. **Drawing Retinal Arterioles:**
    - The `draw_children()` function adds smaller branches to the main arteries, representing **Retinal Arterioles**. It uses a recursive approach to create a branching structure, with each new branch having a chance to split further based on a branching probability. This step uses the angles generated by the Monte Carlo method for realistic turns.
5. **Main Function:**
    - The main script initializes the turtle environment and sets up parameters for the simulation. It calls `draw_parents()` to create the main arteries and then uses `draw_children()` to add smaller branches. The final pattern is displayed in a Turtle Graphics window.

## Future Steps
- **Add Realism**: Further refine the branching logic and parameters to better mimic the complexity of real retinal vessels, including more natural curvature, varying thickness, and density.
- **Integrate Image Processing**: Extract data from retinal fundus images and use it to guide the branching structure, allowing the simulation to match actual retinal patterns.

## Dependencies
- **Python** (tested on version 3.7 and above)
- **Turtle Graphics** (comes included with standard Python libraries)
- **NumPy** and **SciPy** for Monte Carlo simulations

## Acknowledgments
- **Monte Carlo Methods:**: Inspired by probabilistic modeling techniques.
- **Turtle Graphics**: Provides an intuitive way to visualize branching structures.

## Contact
For questions or contributions, feel free to contact me.

