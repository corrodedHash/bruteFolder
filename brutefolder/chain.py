"""Contains Chain class"""

from typing import List, Tuple
from .direction import turn, get_turn_diff, Direction


class Chain:
    """List of directions, folding of this directions"""

    def __init__(self, turn_chain: List[Direction]) ->None:
        self.whole_chain = [Direction.up]
        for direction in turn_chain:
            self.whole_chain.append(turn(self.whole_chain[-1], direction))

        self.fold_list: List[int] = []
        self.chain_history: List[Tuple[int, int]] = []
        self.chain_start = 0
        self.chain_end = len(self.whole_chain)

    @property
    def chain(self) -> List[Direction]:
        """Returns chain"""
        return self.whole_chain[self.chain_start: self.chain_end]

    def can_fold(self, index: int) -> bool:
        """Checks if the chain can be folded at the edge after the index"""
        assert index < len(self.chain) - 1
        assert index >= 0

        turn_dir = get_turn_diff(self.chain[index], self.chain[index + 1])
        assert turn_dir in (Direction.left, Direction.right)

        first_part = self.chain[:index + 1][::-1]
        last_part = self.chain[index + 1:]
        parts = zip(first_part, last_part)

        def match(x: Direction, y: Direction) -> bool:
            return get_turn_diff(x, turn(y, turn_dir)) == Direction.down
        return all(match(before, after) for before, after in parts)

    def fold(self, index: int) -> None:
        """Actually folds the chain. Does not check for validity"""
        assert index + 1 < len(self)

        self.fold_list.append(index)
        self.chain_history.append((self.chain_start, self.chain_end))

        actual_index = self.chain_start + index + 1

        if 2 * (index + 1) >= len(self):
            self.chain_end = actual_index
        else:
            self.chain_start = actual_index

    def reset_fold(self) -> None:
        """Resets the last fold"""
        assert self.fold_list

        self.fold_list.pop()
        self.chain_start, self.chain_end = self.chain_history.pop()

    def folded(self) -> bool:
        """Checks if the chain can be folded further"""
        return len(self) == 1

    def __len__(self) -> int:
        """Returns the length of the chain"""
        return self.chain_end - self.chain_start
