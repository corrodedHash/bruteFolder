#!/bin/python
"""Contains get_fold function"""

from typing import Iterator, List

from .chain import Chain


def get_fold(chain: Chain) -> Iterator[List[int]]:
    """Generator for all possible fold sequences for given chain"""
    start_index = 0
    while True:
        if chain.folded():
            yield chain.fold_list

        for index in range(start_index, len(chain) - 1):
            if chain.can_fold(index):
                chain.fold(index)
                start_index = 0
                break
        else:
            if not chain.fold_list:
                return
            start_index = chain.fold_list[-1] + 1
            chain.reset_fold()
