from typing import List, Literal, Tuple
from abc import ABC, abstractmethod


class RobotInterface(ABC):
    
    @abstractmethod
    def set_grid_size(self, width: int, height: int):
        pass

    @abstractmethod
    def set_is_lost(self, is_lost: bool):
        pass

    @abstractmethod
    def get_moves(self) -> List[Tuple[int, int]]:
        pass

    @abstractmethod
    def move(self, pace: int = 1, disappearing_positions: List[Tuple[int, int]] = []):
        pass

    @abstractmethod
    def get_last_marker(self) -> str:
        pass

    @abstractmethod
    def display_latest_position(self):
        pass

    @abstractmethod
    def turn(self, instruction: Literal["L", "R"]) -> str:
        pass


class Robot(RobotInterface):
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
    
    def get_moves(self) -> List[Tuple[int, int]]:
        return self.moves
    
    def set_grid_size(self, width: int, height: int):
        self.grid_size = (width, height)

    def get_last_marker(self) -> str:
        marker = None
        if self.direction == "N":
            marker = "^"
        elif self.direction == "S":
            marker = "v"
        elif self.direction == "E":
            marker = ">"
        elif self.direction == "W":
            marker = "<"
        return marker

    def turn(self, instruction: Literal["L", "R"]) -> str:
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
                new_y = self.y + pace
                new_position = (self.x, new_y)
            case "S":
                new_y = self.y - pace
                new_position = (self.x, new_y)
            case "E":
                new_x = self.x + pace
                new_position = (new_x, self.y)
            case "W":
                new_x = self.x - pace
                new_position = (new_x, self.y)
        
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
                self.turn(move)
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
