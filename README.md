# Martian Robot

## Solution
* Since this can be thought as just graphing problem, we can use matplotlib to solve this problem
* First we create a plain figure (grid class)
** Initialize the grid with given width and height
** Create a function that will be used add robot to the grid
** Create a function that will be used to show the grid
* Then we create a robot class:
** Initialize the robot with given grid, starting position, direction and steps
** Create a function that will be used to move the robot on the grid (turn and move)
*** Essentialy, converts the given input steps to coordinates, and makes sure the robot doesn't go out of bounds



## Project Structure
```
└── README.md
├── red_badger
│   ├── __init__.py
│   └── main.py
├── .vscode
│   └── launch.json
├── Coding_Challenge_2018.pdf
├── poetry.lock
└── pyproject.toml
```

## How run the project
```bash
poetry run python red_badger/main.py
```
