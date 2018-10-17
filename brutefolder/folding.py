#!/bin/python
"""Contains get_fold function"""

from typing import Iterator, List

from .chain import Chain

def spiral_number_map(index: int, start: int, end: int) -> int:
    """Translates a number in a range to a range sorted
spiral from the middle, ending on the largest element
[0, 4] -> 2, 1, 3, 0, 4
[0, 3] -> 1, 2, 0, 3"""

    assert index >= start
    assert index <= end
    assert start <= end

    middle = start + (end - start) // 2
    odd_range_length = (start + end) % 2 == 0
    index_odd = index % 2 != 0
    distance = (index + 1) // 2
    result = 0

    if odd_range_length == index_odd:
        result = middle - distance
    else:
        result = middle + distance

    assert result <= end
    assert result >= start
    return result


def get_folds(chain: Chain) -> Iterator[List[int]]:
    """Generator for all possible fold sequences for given chain"""
    start_index = 0
    fold_stack = []
    while True:
        if chain.folded():
            yield chain.fold_list

        for index in range(start_index, len(chain) - 1):
            spiral_index = spiral_number_map(index, 0, len(chain) - 2)
            if chain.can_fold(spiral_index):
                chain.fold(spiral_index)
                fold_stack.append(index)
                start_index = 0
                break
        else:
            if not fold_stack:
                return
            start_index = fold_stack.pop() + 1
            chain.reset_fold()
