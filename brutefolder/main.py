"""Main script of project"""
import copy
from multiprocessing import Queue, Pool, Manager

from typing import List

from . import folding
from . import direction
from . import chain


def pool_executor(index, chain):
    best_chain_len = len(chain) + 1
    best_fold = []
    for fold in folding.get_folds(chain, [index]):
        if len(fold) <= best_chain_len:
            best_chain_len = len(fold)
            best_fold = copy.deepcopy(fold)

    return best_fold 

def pool_main(search_chain) -> None:
    """Main function"""
    print("Input chain: {0}".format(search_chain.chain))
    indices = range(len(search_chain) - 1)
    chains = [search_chain] * (len(search_chain) - 1)
    params = zip(indices, chains)

    with Pool(processes=3) as pool:
        results = pool.starmap(pool_executor, params)

    results = (x for x in results if x)

    result = min(results, key=lambda x: len(x))
    print("Best result: {0}".format(result))


def single_main(search_chain) -> None:
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


if __name__ == "__main__":
    search_chain = chain.Chain(direction.str_to_dir_list("LRRLLLRRLRRRLLR"))
    #search_chain = chain.Chain(direction.str_to_dir_list("RLLLRRLRRRLL"))
    #pool_main(search_chain)
    single_main(search_chain)
