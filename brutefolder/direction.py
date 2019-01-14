"""Keeps function to modify directions"""
from typing import List
import enum


@enum.unique
class Direction(enum.Enum):
    """
    Enum for 2D direction
    """

    up = 1
    right = 2
    down = 3
    left = 4

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


DIR_INT_MAP = {Direction.up: 0, Direction.right: 1,
               Direction.down: 2, Direction.left: 3}

INT_DIR_MAP = {DIR_INT_MAP[k]: k for k in DIR_INT_MAP}

DIR_CHAR_MAP = {Direction.up: 'u', Direction.left: 'l',
                Direction.down: 'd', Direction.right: 'r'}

CHAR_DIR_MAP = {DIR_CHAR_MAP[k]: k for k in DIR_CHAR_MAP}


def turn(start: Direction, turn_dir: Direction) -> Direction:
    """Turns given direction in given direction"""

    start_int = DIR_INT_MAP[start]
    turn_dir_int = DIR_INT_MAP[turn_dir]

    return INT_DIR_MAP[(start_int + turn_dir_int) % 4]


def get_turn_diff(start: Direction, end: Direction) -> Direction:
    """Returns the direction that is needed to turn from start to end"""

    start_int = DIR_INT_MAP[start]
    end_int = DIR_INT_MAP[end]

    return INT_DIR_MAP[(end_int - start_int) % 4]


def str_to_dir_list(inp: str)-> List[Direction]:
    """Return list with directions as given in input"""
    return [CHAR_DIR_MAP[x] for x in inp.lower()]
