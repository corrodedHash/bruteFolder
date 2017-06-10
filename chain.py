"""Contains Chain class"""
from direction import turn, get_turn_diff


class Chain:
    """List of directions, folding of this directions"""

    def __init__(self, turn_chain):
        self._chain = [0]
        for direction in turn_chain:
            self._chain.append(turn(self._chain[-1], direction))

        self._fold_list = []
        self._cut_up = []
        self._chain_start = 0
        self._chain_end = len(self._chain)

    def get_chain(self):
        """Returns chain"""
        return self._chain[self._chain_start: self._chain_end]

    def can_fold(self, index):
        """Checks if the chain can be folded at this index"""
        assert index < len(self.get_chain()) - 1

        turn_dir = get_turn_diff(
            self.get_chain()[index], self.get_chain()[index + 1])
        for before, after in zip(self.get_chain()[:index + 1][::-1], self.get_chain()[index + 1:]):
            if get_turn_diff(before, turn(after, turn_dir)) != 2:
                return False
        return True

    def fold(self, index):
        """Actually folds the chain. Does not check for validity"""
        self._fold_list.append(index)
        if 2 * index >= len(self) - 2:
            self._cut_up.append(-self._chain_end)
            self._chain_end = self._chain_start + index + 1
        else:
            self._cut_up.append(self._chain_start)
            self._chain_start += index + 1

    def reset_fold(self):
        """Resets the last fold"""
        if self._fold_list:
            if self._cut_up[-1] < 0:
                self._chain_end = -self._cut_up[-1]
            else:
                self._chain_start = self._cut_up[-1]
            self._cut_up.pop()
            self._fold_list.pop()
        else:
            raise ValueError

    def folded(self):
        """Checks if the chain can be folded further"""
        return len(self) == 1

    def get_fold_list(self):
        """Returns the sequence in which the chain has been folded so far"""
        return self._fold_list

    def __len__(self):
        """Returns the length of the chain"""
        return len(self.get_chain())
