#!/bin/python
import enum

def turn(start, turn):
    if turn == 0:
        return start
    if turn == 1:
        return (start + 1) % 4
    if turn == 2:
        return (start + 2) % 4
    if turn == 3:
        return (start + 3) % 4

def get_turn_diff(start, end):
    return (end - start) % 4

def str_to_dir_list(inp):
    result = []
    for x in inp.lower():
        if x == "r":
            result.append(1)
        elif x == "l":
            result.append(3)
        else:
            raise ValueError
    return result


class chain:
    def __init__(self, turn_chain):
        self._chain = [0]
        for direction in turn_chain:
            self._chain.append(turn(self._chain[-1], direction))

        self._fold_list = []
        self._cut_up = []
        self._chain_start = 0
        self._chain_end = len(self._chain)

    def get_chain(self):
        return self._chain[self._chain_start: self._chain_end]

    def can_fold(self, index):
        assert index < len(self.get_chain()) - 1

        turn_dir = get_turn_diff(self.get_chain()[index],self.get_chain()[index+1]) 
        for before, after in zip(self.get_chain()[:index+1][::-1], self.get_chain()[index+1:]):
            if get_turn_diff(before, turn(after, turn_dir)) != 2:
                return False
        return True

    def fold(self, index):
        self._fold_list.append(index)
        if 2 * index >= len(self) - 1:
            self._cut_up.append(-self._chain_end)
            self._chain_end = self._chain_start + index + 1
        else:
            self._cut_up.append(self._chain_start)
            self._chain_start += index + 1

    def reset_fold(self):
        if len(self._fold_list) > 0:
            self._fold_list.pop()
            if self._cut_up[-1] < 0:
                self._chain_end = self._cut_up[-1]
            else:
                self._chain_start = self._cut_up[-1]
            self._cut_up.pop()
            return True
        else:
            return False

    def folded(self):
        return len(self) == 1

    def get_fold_list(self):
        return self._fold_list

    def __len__(self):
        return len(self.get_chain())


def get_fold(chain):
    start_index = 0
    while True:
        if chain.folded():
            yield chain.get_fold_list()

        if len(chain.get_fold_list()) == 1:
            if start_index == 1:
                print("bla: " + str(chain.get_chain()))

        for index in range(start_index, len(chain) - 1):
            if chain.can_fold(index):
                chain.fold(index)
                start_index = 0
                break
        else:
            chain.reset_fold()
            if len(chain.get_fold_list()) == 0:
                return
            start_index = chain.get_fold_list()[-1] + 1


if __name__ == "__main__":
#for x in get_fold(chain(str_to_dir_list("LRRLLLRRLRRRLLR"))):
#    print(x)
    c = chain(str_to_dir_list("LRR"))
    print(c.get_chain())
    for x in get_fold(c):
        print(x)
