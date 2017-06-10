import unittest
import folding

class FoldingTestClass(unittest.TestCase):

    def test_folding(self):
        x = folding.chain(folding.str_to_dir_list("LRLLRLR"))
        self.assertListEqual(x.get_chain(), [0, 3, 0, 3, 2, 3, 2, 3])

        can_fold_list = [0, 2, 3, 6]
        cannot_fold_list = [1, 4, 5]

        print(x.get_chain())
        for i in can_fold_list:
            self.assertTrue(x.can_fold(i), str(i))

        for i in cannot_fold_list:
            self.assertFalse(x.can_fold(i), str(i))

        x.fold(3)

        can_fold_list = [0, 2]
        cannot_fold_list = [1]

        for i in can_fold_list:
            self.assertTrue(x.can_fold(i), str(i))

        for i in cannot_fold_list:
            self.assertFalse(x.can_fold(i), str(i))

        self.assertTrue(x.can_fold(0))
        x.fold(0)
        self.assertTrue(x.can_fold(0))
        x.fold(0)
        self.assertTrue(x.can_fold(0))
        x.fold(0)

        self.assertTrue(x.folded())
