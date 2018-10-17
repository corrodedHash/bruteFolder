#!/bin/python
"""Contains get_fold function"""

from typing import Iterator, List, Optional, Sequence

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


def get_folds(chain: Chain, index_range: Optional[Sequence[int]] = None) -> Iterator[List[int]]:
    """Generator for all possible fold sequences for given chain"""
    if chain.folded():
        yield chain.fold_list
        return

    if not index_range:
        index_range = range(0, len(chain) - 1)

    for index in index_range:
        spiral_index = spiral_number_map(index, 0, len(chain) - 2)
        if chain.can_fold(spiral_index):
            chain.fold(spiral_index)
            yield from get_folds(chain)
            chain.reset_fold()
    return
