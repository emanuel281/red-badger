import matplotlib.pyplot as plt
import numpy as np
from typing import Iterable, List, Tuple


class Robot:
    def __init__(self, starting_x: int, starting_y: int, direction: str):
        """Initialize the robot with given grid and starting position
        
        Args:
            grid (Grid): The grid the robot is on
            starting_x (int): The starting x position of the robot
            starting_y (int): The starting y position of the robot
            direction (str): The direction the robot is facing
        """
        self.x = starting_x
        self.y = starting_y
        self.direction = direction
        self.moves: List[Tuple[int, int]] = [(starting_x, starting_y)]

    def _get_new_direction(self, direction: str) -> str:
        """
            Change the robot direction by 90 degrees.

        
        Args:
            direction (str): The direction to turn the robot to.
            
        Returns:
            str: The new direction of the robot
        """
        new_direction = self.direction
        match direction:
            case "L":
                if self.direction == "N":
                    new_direction = "W"
                elif self.direction == "S":
                    new_direction = "E"
                elif self.direction == "E":
                    new_direction = "N"
                elif self.direction == "W":
                    new_direction = "S"
            case "R":
                if self.direction == "N":
                    new_direction = "E"
                elif self.direction == "S":
                    new_direction = "W"
                elif self.direction == "E":
                    new_direction = "S"
                elif self.direction == "W":
                    new_direction = "N"
        return new_direction

    def move(self, moves: Iterable[str], pace: int = 1):
        """Move the robot in the direction it is facing
        
        Args:
            moves (Iterable[str]): The moves to make the robot
            pace (int, optional): The number of steps to move the robot. Defaults to 1.
        """
        for move in moves:
            if move == "L" or move == "R":
                self.direction = self._get_new_direction(move)
            elif move == "F":
                if self.direction == "N":
                    self.y += pace
                    self.moves.append((self.x, self.y))
                elif self.direction == "S":
                    self.y -= pace
                    self.moves.append((self.x, self.y))
                elif self.direction == "E":
                    self.x += pace
                    self.moves.append((self.x, self.y))
                elif self.direction == "W":
                    self.x -= pace
                    self.moves.append((self.x, self.y))


class Grid:
    def __init__(self, width: int = 50, height: int = 50):
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots()
        self.robots: List[Robot] = []
    
    def test_graphing(self):
        self.ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        self.ax.plot([1, 2, 3, 4], [1, 40, 20, 30])
    
    def add_robot(self, robot: Robot):
        self.robots.append(robot)

    def save_all_moves(self):
        plots = []
        for robot in self.robots:
            plots.append(robot.moves)
        self.plots = plots
    
    def display_final_positions(self):
        for robot in self.robots:
            print(f"{robot.x} {robot.y} {robot.direction}")

    def show(self):
        self.save_all_moves()
        self.display_final_positions()
        for plot in self.plots:
            x_axis, y_axis = zip(*plot)
            self.ax.plot(x_axis, y_axis, marker="x")
        plt.show()


if __name__ == "__main__":
    """
    Sample Input
        5 3
        1 1 E
        RFRFRFRF
        3 2 N
        FRRFLLFFRRFLL
        0 3 W
        LLFFFLFLFL
    """
    grid = Grid()
    robot1 = Robot(1, 1, "E")
    robot1.move("RFRFRFRF")
    grid.add_robot(robot1)
    robot2 = Robot(3, 2, "N")
    robot2.move("FRRFLLFFRRFLL")
    grid.add_robot(robot2)
    robot3 = Robot(0, 3, "W")
    robot3.move("LLFFFLFLFL")
    grid.add_robot(robot3)
    grid.show()
