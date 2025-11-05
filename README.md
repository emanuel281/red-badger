# Martian Robot

## Solution
* Since this can be thought as just graphing problem, we can use matplotlib to solve this problem
* First we create a plain figure (grid class)
** Initialize the grid with width and height
** Create a function that will be used add robot to the grid
** Create a function that will be used to show robots on the grid
* Then we create a robot class:
** Initialize the robot with given grid, starting position, direction and steps
** Create a function that will be used to move the robot on the grid (turn and move)
*** Essentialy, converts the given input steps to coordinates, and makes sure the robot doesn't go out of bounds
** Create helper functions to convert instructions to coordinates, direction and check if the robot is lost
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

## Project testing
```bash
poetry run pytest
```
