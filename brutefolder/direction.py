"""Keeps function to modify directions"""
from typing import List


def turn(start: int, turn_dir: int) -> int:
    """Turns given direction in given direction"""
    assert turn_dir in range(5)
    assert start in range(5)

    return (start + turn_dir) % 4

def get_turn_diff(start: int, end: int) -> int:
    """Returns the direction that is needed to turn from start to end"""
    assert start in range(5)
    assert end in range(5)

    return (end - start) % 4


def str_to_dir_list(inp: str)-> List[int]:
    """Return list with directions as given in input"""
    char_dir_map = {'r': 1, 'l': 3}
    return [char_dir_map[x] for x in inp.lower()]
