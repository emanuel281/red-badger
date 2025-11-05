import matplotlib.pyplot as plt
from typing import Iterable, List, Literal, Tuple


class Robot:
    def __init__(self, starting_position: Tuple[int, int], instructions: str, direction: Literal["N", "S", "E", "W"]):
        """Initialize the robot with given grid and starting position
        
        Args:
            grid (Grid): The grid the robot is on
            starting_position (Tuple[int, int]): The starting position of the robot
            direction (str): The direction the robot is facing
        """
        self.x = starting_position[0]
        self.y = starting_position[1]
        self.direction = direction
        self.moves: List[Tuple[int, int]] = [(self.x, self.y)]
        self.instructions = instructions
        self.is_lost = False
        self.grid_size = (50, 50)

    def set_is_lost(self, is_lost: bool):
        self.is_lost = is_lost
    
    def set_grid_size(self, width: int, height: int):
        self.grid_size = (width, height)

    def _update_direction(self, instruction: Literal["L", "R"]) -> str:
        """
            Change the robot direction by 90 degrees.

        
        Args:
            instruction (str): Instruction to turn the robot to.
            
        Returns:
            str: The new direction of the robot
        """
        new_direction = self.direction
        match instruction:
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
        self.direction = new_direction
        return new_direction

    def _is_out_of_bounds(self, position: Tuple[int, int]) -> bool:
        """
            Check if the robot is out of bounds
        
        Args:
            position (Tuple[int, int]): The position to check
        
        Returns:
            bool: True if the robot is lost, False otherwise
        """
        x_max = self.grid_size[0]
        y_max = self.grid_size[1]
        x_min = 0
        y_min = 0
        return position[0] < x_min or position[0] > x_max or position[1] < y_min or position[1] > y_max
    def _get_new_position(self, direction: str, pace: int = 1) -> Tuple[int, int]:
        """
            Get the new position of the robot
        
        Args:
            direction (str): The direction to move the robot to.
            pace (int, optional): The number of steps to move the robot. Defaults to 1.
        
        Returns:
            Tuple[int, int]: The new position of the robot
        """
        new_position = (self.x, self.y)
        match direction:
            case "N":
                new_position = (self.x, self.y + pace)
            case "S":
                new_position = (self.x, self.y - pace)
            case "E":
                new_position = (self.x + pace, self.y)
            case "W":
                new_position = (self.x - pace, self.y)
        
        is_lost = self._is_out_of_bounds(new_position)

        return new_position, is_lost

    def move(self, pace: int = 1, disappearing_positions: List[Tuple[int, int]] = []):
        """Move the robot in the direction it is facing
        
        Args:
            pace (int, optional): The number of steps to move the robot. Defaults to 1.
            disappearing_positions (List[Tuple[int, int]], optional): The positions where the robot will disappear. Defaults to [].
        """
        moves_len = min(100, len(self.instructions))
        for i in range(moves_len):
            if self.is_lost:
                break
            move = self.instructions[i]
            if move == "L" or move == "R":
                self._update_direction(move)
            elif move == "F":
                next_position, is_lost = self._get_new_position(self.direction, pace)
                if next_position in disappearing_positions:
                    continue
                if is_lost:
                    self.lost_at = next_position[0], next_position[1]
                    self.set_is_lost(True)
                    break
                self.x, self.y = next_position
                self.moves.append(next_position)

    def display_latest_position(self):
        print(f"{self.x} {self.y} {self.direction} {'LOST' if self.is_lost else ''}")


class Grid:
    def __init__(self, width: int = 50, height: int = 50, robots: List[Robot] = []):
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots()
        self.robots: List[Robot] = robots
        self.disappearing_positions: List[Tuple[int, int]] = []
    
    def add_robot(self, robot: Robot):
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
            x_axis, y_axis = zip(*robot.moves)
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
    # grid = Grid(5, 3)
    # robot1 = Robot((1, 1), instructions="RFRFRFRF", direction="E")
    # grid.add_robot(robot1)
    # robot2 = Robot((3, 2), instructions="FRRFLLFFRRFLL", direction="N")
    # grid.add_robot(robot2)
    # robot3 = Robot((0, 3), instructions="LLFFFLFLFL", direction="W")
    # grid.add_robot(robot3)
    # grid.move_robots()
    # grid.show()
    grid_size = input("Enter grid size(e.g, 5 3): ")
    grid_size = grid_size.split(" ")
    grid = Grid(int(grid_size[0]), int(grid_size[1]))
    while True:
        """Improvement: Specify the number of robots and use that to break the loop"""
        line = input("Enter robot start position and direction(e.g, 1 1 E): \n").strip()
        if not line:
            break
        robot_start_position = line.split(" ")
    
        robot_instructions = input("Enter robot instructions(e.g, RFRFRFRF): \n").strip()
        if not robot_instructions:
            break
        robot = Robot((int(robot_start_position[0]), int(robot_start_position[1])), instructions=robot_instructions, direction=robot_start_position[2])
        grid.add_robot(robot)
    
    grid.move_robots()
    grid.show()
