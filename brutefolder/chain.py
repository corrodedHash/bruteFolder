"""Contains Chain class"""

from typing import List
from .direction import turn, get_turn_diff


class Chain:
    """List of directions, folding of this directions"""

    def __init__(self, turn_chain: List[int]) ->None:
        self.whole_chain = [0]
        for direction in turn_chain:
            self.whole_chain.append(turn(self.whole_chain[-1], direction))

        self.fold_list: List[int] = []
        self.cut_up: List[int] = []
        self.chain_start = 0
        self.chain_end = len(self.whole_chain)

    @property
    def chain(self) -> List[int]:
        """Returns chain"""
        return self.whole_chain[self.chain_start: self.chain_end]

    def can_fold(self, index: int) -> bool:
        """Checks if the chain can be folded at the edge after the index"""
        assert index < len(self.chain) - 1
        assert index >= 0

        turn_dir = get_turn_diff(self.chain[index], self.chain[index + 1])
        assert turn_dir in (1, 3)

        first_part = self.chain[:index + 1][::-1]
        last_part = self.chain[index + 1:]
        parts = zip(first_part, last_part)

        def match(x, y):
            return get_turn_diff(x, turn(y, turn_dir)) == 2
        return all(match(before, after) for before, after in parts)

    def fold(self, index: int) -> None:
        """Actually folds the chain. Does not check for validity"""
        self.fold_list.append(index)
        if 2 * index >= len(self) - 2:
            self.cut_up.append(-self.chain_end)
            self.chain_end = self.chain_start + index + 1
        else:
            self.cut_up.append(self.chain_start)
            self.chain_start += index + 1

    def reset_fold(self) -> None:
        """Resets the last fold"""
        assert self.fold_list
        assert self.cut_up

        self.fold_list.pop()
        last_index = self.cut_up.pop()

        if last_index < 0:
            self.chain_end = -1 * last_index
        else:
            self.chain_start = last_index

    def folded(self) -> bool:
        """Checks if the chain can be folded further"""
        return len(self) == 1

    def __len__(self) -> int:
        """Returns the length of the chain"""
        return self.chain_end - self.chain_start
