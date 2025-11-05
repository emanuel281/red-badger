from typing import List, Tuple
from matplotlib import pyplot as plt
from red_badger.entities.robot import RobotInterface
from abc import ABC, abstractmethod


class GridInterface(ABC):
    
    @abstractmethod
    def move_robots(self):
        pass

    @abstractmethod
    def display_latest_positions(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def add_robot(self, robot: RobotInterface):
        pass


class Grid(GridInterface):
    def __init__(self, width: int, height: int, robots: List[RobotInterface] = []):
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots()
        self.robots: List[RobotInterface] = robots
        self.disappearing_positions: List[Tuple[int, int]] = []
    
    def add_robot(self, robot: RobotInterface):
        robot.set_grid_size(self.width, self.height)
        self.robots.append(robot)
    
    def move_robots(self):
        for robot in self.robots:
            robot.move(disappearing_positions=self.disappearing_positions)
            if robot.is_lost:
                self.disappearing_positions.append(robot.lost_at)

    def display_latest_positions(self):
        for robot in self.robots:
            robot.display_latest_position()

    def show(self):
        self.display_latest_positions()
        for robot in self.robots:
            x_axis, y_axis = zip(*robot.get_moves())
            self.ax.plot(x_axis, y_axis, marker="x")
        plt.show()
