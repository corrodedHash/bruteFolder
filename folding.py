#!/bin/python
"""Contains get_fold function"""


def get_fold(chain):
    """Generator for all possible fold sequences for given chain"""
    start_index = 0
    while True:
        if chain.folded():
            yield chain.get_fold_list()

        for index in range(start_index, len(chain) - 1):
            if chain.can_fold(index):
                chain.fold(index)
                start_index = 0
                break
        else:
            if not chain.get_fold_list():
                return
            start_index = chain.get_fold_list()[-1] + 1
            chain.reset_fold()
