"""Test grid"""
import pytest
from red_badger.entities.grid import Grid
from red_badger.entities.robot import Robot


@pytest.fixture
def grid() -> Grid:
    return Grid(50, 50)


def test_add_robot(grid: Grid):
    robot = Robot((0, 0), "FF", "E")
    grid.add_robot(robot)
    assert len(grid.robots) == 1
    assert grid.robots == [robot]


def test_move_robots(grid: Grid):
    robot = Robot((0, 0), "FF", "E")
    grid.add_robot(robot)
    grid.move_robots()
    assert grid.robots[0].x == 2
    assert grid.robots[0].y == 0
