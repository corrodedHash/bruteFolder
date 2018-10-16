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
    print("chain: " + str(search_chain.chain))
    counter = 0
    for current_fold in folding.get_folds(search_chain):
        counter += 1

        if counter >= 2000:
            print("Checked " + str(counter))
            counter = 0

        if not best_fold or len(current_fold) < len(best_fold):
            best_fold = copy.deepcopy(current_fold)
            best_fold_count = 1
            print("Found: " + str(current_fold))

        elif len(current_fold) == len(best_fold):
            best_fold_count += 1

    print(best_fold)
    print(best_fold_count)

if __name__ == "__main__":
    main()
