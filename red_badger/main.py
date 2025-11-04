import matplotlib.pyplot as plt
from typing import Iterable, List, Literal, Tuple


class Robot:
    def __init__(self, starting_position: Tuple[int, int], grid_size: Tuple[int, int], direction: Literal["N", "S", "E", "W"]):
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
        self.grid_size = grid_size
        self.is_lost = False

    def check_if_lost(self, next_move: Tuple[int, int]):
        """Check if the robot is lost
        
        Args:
            next_move (Tuple[int, int]): The next position of the robot
        """
        x_max = self.grid_size[0]
        y_max = self.grid_size[1]
        next_x = next_move[0]
        next_y = next_move[1]
        if next_x < 0 or next_x > x_max or next_y < 0 or next_y > y_max or self.is_lost:
            self.is_lost = True
            return True
        return False

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

    def _get_new_position(self, direction: str, pace: int = 1) -> Tuple[int, int]:
        """
            Get the new position of the robot
        
        Args:
            direction (str): The direction to move the robot to.
            pace (int, optional): The number of steps to move the robot. Defaults to 1.
        
        Returns:
            Tuple[int, int]: The new position of the robot
        """
        match direction:
            case "N":
                return (self.x, self.y + pace)
            case "S":
                return (self.x, self.y - pace)
            case "E":
                return (self.x + pace, self.y)
            case "W":
                return (self.x - pace, self.y)

    def move(self, moves: Iterable[str], pace: int = 1):
        """Move the robot in the direction it is facing
        
        Args:
            moves (Iterable[str]): The moves to make the robot
            pace (int, optional): The number of steps to move the robot. Defaults to 1.
        """
        moves_len = min(100, len(moves))
        for i in range(moves_len):
            if self.is_lost:
                break
            move = moves[i]
            if move == "L" or move == "R":
                self._update_direction(move)
            elif move == "F":
                next_position = self._get_new_position(self.direction, pace)
                if self.check_if_lost(next_position):
                    break
                self.x, self.y = next_position
                self.moves.append(next_position)

    def display_latest_position(self):
        print(f"{self.x} {self.y} {self.direction} {'LOST' if self.is_lost else ''}")


class Grid:
    def __init__(self, width: int = 50, height: int = 50):
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots()
        self.robots: List[Robot] = []
    
    def add_robot(self, robot: Robot):
        self.robots.append(robot)

    def save_all_moves(self):
        plots = []
        for robot in self.robots:
            plots.append(robot.moves)
        self.plots = plots

    def display_latest_positions(self):
        for robot in self.robots:
            robot.display_latest_position()

    def show(self):
        self.save_all_moves()
        self.display_latest_positions()
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
    robot1 = Robot((1, 1), (5, 3), "E")
    robot1.move("RFRFRFRF")
    grid.add_robot(robot1)
    robot2 = Robot((3, 2), (5, 3), "N")
    robot2.move("FRRFLLFFRRFLL")
    grid.add_robot(robot2)
    robot3 = Robot((0, 3), (5, 3), "W")
    robot3.move("LLFFFLFLFL")
    grid.add_robot(robot3)
    grid.show()
