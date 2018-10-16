#!/bin/python
"""Contains get_fold function"""

from typing import Iterator, List

from .chain import Chain


def funny_increment(current: int, start: int, end: int) -> int:
    middle = start + (end - start) // 2
    result = current + 2 * (middle - current)
    odd_range = (start + end) % 2 != 0

    if (current <= middle) and odd_range:
        result += 1

    if (current >= middle) and not odd_range:
        result -= 1

    assert result >= start
    assert result <= end
    return result



def funny_translate(index: int, start: int, end: int) -> int:
    result = start + (end - start) // 2
    for i in range(start, index):
        result = funny_increment(result, start, end)
        assert result <= end
    return result


def get_folds(chain: Chain) -> Iterator[List[int]]:
    """Generator for all possible fold sequences for given chain"""
    start_index = 0
    fold_stack = []
    while True:
        if chain.folded():
            yield chain.fold_list

        for index in range(start_index, len(chain) - 1):
            funny_index = funny_translate(index, start_index, len(chain) - 2)
            if chain.can_fold(funny_index):
                chain.fold(funny_index)
                fold_stack.append(index)
                start_index = 0
                break
        else:
            if not chain.fold_list:
                return
            start_index = fold_stack.pop() + 1 
            chain.reset_fold()
