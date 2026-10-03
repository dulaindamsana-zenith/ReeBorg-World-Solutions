<h1 align="center">ReeBorg World Algorithmic Solutions</h1>

## Executive Overview

This repository contains production-grade, deterministic Python solution scripts for complex logic maps in the ReeBorg's World environment. Built as part of the **Project Zenith v4.0** curriculum (Week 02)[cite: 19, 20], these scripts demonstrate algorithmic control flow, state evaluation, dynamic pathfinding, dynamic hurdle traversal, and structural maze resolution mechanisms without external library dependencies.

---

## Key Algorithmic Mechanics

1. **Dynamic Boundary Detection:** Traversing non-deterministic terrain by evaluating real-time spatial indicators (`front_is_clear()`, `right_is_clear()`, `wall_in_front()`, `wall_on_right()`).
2. **Traversal State Machines:** Implementing the Right-Hand Wall-Following Rule for maze clearance and closed-loop boundary navigation.
3. **Variable-Height Obstacle Traversal:** Dynamically detecting vertical hurdle heights using unbounded `while` loops and positional state updating.
4. **Modular Abstraction:** Encapsulating low-level robotic movements into deterministic function routines (`turn_right()`, `jump()`).

---

## Solved World Environments

* **Around World 1:** Closed-grid edge boundary traversal using nested iteration loops.
* **Hurdle 1 & 2:** Fixed-step and goal-conditioned hurdle navigation models.
* **Hurdle 3:** Dynamic conditional execution based on positional wall detection.
* **Hurdle 4:** Variable-height and variable-placement obstacle climbing logic.
* **Maze World:** Closed-loop spatial navigation using wall-following state routines.

---

## Repository Directory Layout

```text
├── Day_Project_4.py           # Maze world solver implementing Right-Hand Rule
├── reeborgs_around_world.py   # Nested loop grid traversal script
├── reeborgs_hurdle-1_world.py # Fixed-step hurdle jumping logic
├── reeborgs_hurdle-2_world.py # Goal-oriented hurdle iteration loop
├── reeborgs_hurdle-3_world.py # Conditional wall detection and jump execution
├── reeborgs_hurdle-4_world.py # Dynamic height hurdle pathfinding engine
├── task-1.py                  # Functional abstraction and formatting module
├── LICENSE                    # MIT License documentation
└── README.md                  # System architecture documentation
```

---

## Execution Framework
All scripts are executed natively within the standard ReeBorg's World simulation environment or local Python CLI interpreters with simulated binding wrappers.

---

# Example local execution check via Python CLI
```bash
python3 Day_Project_4.py
Author & Contributor
Dulain Damsana (Dula)
```

---

# Author
Author: **Dulain Damsana (DCD)**
- Role: Primary Developer / Systems Architect
- Framework: Project Zenith v4.0 Quantum Cyber Physicist Roadmap

---

## License
This project is open-source and released under the terms of the MIT License.
