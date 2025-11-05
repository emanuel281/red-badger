"""Test robot class"""
import pytest
from red_badger.entities.robot import Robot


@pytest.fixture
def robot() -> Robot:
    return Robot((0, 0), "LR", "E")


def test_update_direction(robot: Robot):
    assert robot.direction == "E"
    robot.turn("L")
    assert robot.direction == "N"
    robot.turn("R")
    assert robot.direction == "E"


def test_get_last_marker(robot: Robot):
    robot.direction = "E"
    assert robot.get_last_marker() == ">"

    robot.turn("L")
    assert robot.get_last_marker() == "^"

    robot.turn("L")
    assert robot.get_last_marker() == "<"

    robot.turn("L")
    assert robot.get_last_marker() == "v"


def test_is_out_of_bounds(robot: Robot):
    robot._is_out_of_bounds((50, 50))
    assert not robot.is_lost


def test_set_grid_size(robot: Robot):
    robot.set_grid_size(50, 50)
    assert robot.grid_size == (50, 50)
    robot.set_grid_size(100, 100)
    assert robot.grid_size == (100, 100)
