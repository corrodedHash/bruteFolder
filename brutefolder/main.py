"""Main script of project"""
import copy
from multiprocessing import Pool

from typing import List

from . import folding
from . import direction
from . import chain


def pool_executor(index: int, search_chain: chain.Chain) -> List[int]:
    """
    Executor of parallel brute forcing
    """
    best_chain_len = len(search_chain) + 1
    best_fold: List[int] = []
    for fold in folding.get_folds(search_chain, [index]):
        if len(fold) <= best_chain_len:
            best_chain_len = len(fold)
            best_fold = copy.deepcopy(fold)

    return best_fold


def pool_main(search_chain: chain.Chain) -> None:
    """Parallel main function"""
    print("Input chain: {0}".format(search_chain.chain))
    indices = range(len(search_chain) - 1)
    chains = [search_chain] * (len(search_chain) - 1)
    params = zip(indices, chains)

    with Pool(processes=3) as pool:
        pool_results = pool.starmap(pool_executor, params)

    results = (x for x in pool_results if x)

    result = min(results, key=len)
    print("Best result: {0}".format(result))


def single_main(search_chain: chain.Chain) -> None:
    """Main function"""
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


def main() -> None:
    """
    Main function
    """
    search_chain = chain.Chain(direction.str_to_dir_list("RRRLLRLLLRR"))
    #search_chain = chain.Chain(direction.str_to_dir_list("RLLLRRLRRRLL"))
    #pool_main(search_chain)
    single_main(search_chain)


if __name__ == "__main__":
    main()
