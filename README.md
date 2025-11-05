# Martian Robot

## Solution
* Since this can be thought as just plotting a graph problem, we can use matplotlib to solve this problem
* First we create a plain figure (grid class)
    - Initialize the grid with width and height
    - Create a function that will be used add robot to the grid
    - Create a function that will be used to show robots on the grid
* Then we create a robot class:
    - Initialize the robot with starting position, direction and instructions
    - Create a function that will be used to set grid size
    - Create a function that will be used to move the robot on the grid (turn and move)
        - Essentialy, converts the given input steps to coordinates, and makes sure the robot doesn't go out of bounds
    - Create helper functions to convert instructions to coordinates, direction and check if the robot is lost
* Add tests for grid and robot classes


## Project Structure
```
└── README.md
├── red_badger
│   ├── __init__.py
│   ├── entities
│   │   ├── __init__.py
│   │   ├── grid.py
│   │   └── robot.py
│   └── main.py
├── tests
│   ├── __init__.py
│   ├── test_grid.py
│   └── test_robot.py
├── .vscode
│   └── launch.json
├── Coding_Challenge_2018.pdf
├── poetry.lock
└── pyproject.toml
```

## Project setup and running
```bash
poetry install
poetry run python red_badger/main.py
```
### Example
```
Enter grid size(e.g, 5 3): 5 3
Enter robot start position and direction(e.g, 1 1 E): 1 1 E
Enter robot instructions(e.g, RFRFRFRF): RFRFRFRF
Enter robot start position and direction(e.g, 1 1 E): 3 2 N
Enter robot instructions(e.g, RFRFRFRF): FRRFLLFFRRFLL
Enter robot start position and direction(e.g, 1 1 E): 0 3 W
Enter robot instructions(e.g, RFRFRFRF): LLFFFLFLFL
1 1 E 
3 3 N LOST
2 3 S
```

## Project testing
```bash
poetry run pytest
```
