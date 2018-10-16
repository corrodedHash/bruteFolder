"""Keeps function to modify directions"""
from typing import List


def turn(start: int, turn_dir: int) -> int:
    """Turns given direction in given direction"""
    assert turn_dir < 4

    if turn_dir == 0:
        return start
    if turn_dir == 1:
        return (start + 1) % 4
    if turn_dir == 2:
        return (start + 2) % 4

    return (start + 3) % 4


def get_turn_diff(start: int, end: int) -> int:
    """Returns the direction that is needed to turn from start to end"""
    return (end - start) % 4


def str_to_dir_list(inp: str)-> List[int]:
    """Return list with directions as given in input"""
    result = []
    for dir_char in inp.lower():
        if dir_char == "r":
            result.append(1)
        elif dir_char == "l":
            result.append(3)
        else:
            raise ValueError
    return result
