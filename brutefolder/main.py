"""Main script of project"""
import copy
from typing import List

from . import folding
from . import direction
from . import chain


def main() -> None:
    """Main function"""
    search_chain = chain.Chain(direction.str_to_dir_list("LRRLLLRRLRRRLLR"))
    best_fold: List[int] = []
    best_fold_count = 0
    print("Input chain: {0}".format(search_chain.chain))
    fold_count = 0
    for current_fold in folding.get_folds(search_chain):
        fold_count += 1

        if fold_count % 2000 == 0:
            print("Checked {0} folds".format(fold_count))

        if not best_fold or len(current_fold) < len(best_fold):
            best_fold = copy.deepcopy(current_fold)
            best_fold_count = 1
            print("Found {0}".format(current_fold))

        elif len(current_fold) == len(best_fold):
            best_fold_count += 1

    print("There are {0} ways to fold the sequence".format(fold_count))
    print("There are {0} optimal ways to fold the sequence".format(
        best_fold_count))
    print("One of those is: {0}".format(best_fold))


if __name__ == "__main__":
    main()
