from red_badger.entities.robot import Robot
from red_badger.entities.grid import Grid

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
