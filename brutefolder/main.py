"""Main script of project"""
import copy

from brutefolder import folding
from brutefolder import direction
from brutefolder import chain


def main():
    """Main function"""
    search_chain = chain.Chain(direction.str_to_dir_list("LRRLLLRRLRRRLLR"))
    best_fold = []
    best_fold_count = 0
    print("chain: " + str(search_chain.get_chain()))
    counter = 0
    for current_fold in folding.get_fold(search_chain):
        counter += 1

        if counter % 2000 == 0:
            print("Checked " + str(counter))

        if not best_fold:
            best_fold = copy.deepcopy(current_fold)
            best_fold_count = 1
            print("Found: " + str(current_fold))
            continue

        if len(current_fold) < len(best_fold):
            best_fold = copy.deepcopy(current_fold)
            best_fold_count = 1
            print("Found: " + str(current_fold))
            continue

        if len(current_fold) == len(best_fold):
            best_fold_count += 1

    print(best_fold)
    print(best_fold_count)

if __name__ == "__main__":
    main()
