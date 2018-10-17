"""Main script of project"""
import copy
from multiprocessing import Queue, Pool, Manager

from typing import List

from . import folding
from . import direction
from . import chain

def pool_executor(index, queue, chain):
    best_chain_len = len(chain) + 1
    count = 0
    for fold in folding.get_folds(chain, [index]):
        count += 1
        if len(fold) <= best_chain_len:
            best_chain_len = len(fold)
            queue.put(fold)

    return count

def pool_main(chain) -> None:
    m = Manager()
    q = m.Queue()

    indices = range(len(chain) - 1)
    queues = [q] * (len(chain) - 1)
    chains = [chain] * (len(chain) - 1)
    params = zip(indices, queues, chains)

    with Pool(processes=4) as pool:
        x = pool.starmap_async(pool_executor, params, error_callback=lambda x: print(x))
        pool.close()
        while (not x.ready()) or (not q.empty()):
            try:
                result = q.get(timeout=1)
            except:
                if not x.ready():
                    continue
                break
            yield result

        print(x.ready())
        print(x.get(timeout=1))

    return



def main() -> None:
    """Main function"""
    search_chain = chain.Chain(direction.str_to_dir_list("LRRLLLRRLRRRLLR"))
    best_fold: List[int] = []
    best_fold_count = 0
    print("Input chain: {0}".format(search_chain.chain))
    fold_count = 0
    #for current_fold in pool_main(search_chain):
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


def x(index):
    for i in range(2):
        yield index


def manager(p, q):
    for i in x(p):
        q.put(i)
    return
