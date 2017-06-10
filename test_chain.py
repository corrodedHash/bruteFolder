"""Contains tests for chain module"""
import unittest
import direction
import chain


class ChainTestClass(unittest.TestCase):
    """Tests the chain class"""

    def test_folding(self):
        """Tests correct folding of chain"""
        test_chain = chain.Chain(direction.str_to_dir_list("LRLLRLR"))
        self.assertListEqual(test_chain.get_chain(), [0, 3, 0, 3, 2, 3, 2, 3])

        can_fold_list = [0, 2, 3, 6]
        cannot_fold_list = [1, 4, 5]

        for i in can_fold_list:
            self.assertTrue(test_chain.can_fold(i), str(i))

        for i in cannot_fold_list:
            self.assertFalse(test_chain.can_fold(i), str(i))

        test_chain.fold(3)

        can_fold_list = [0, 2]
        cannot_fold_list = [1]

        for i in can_fold_list:
            self.assertTrue(test_chain.can_fold(i), str(i))

        for i in cannot_fold_list:
            self.assertFalse(test_chain.can_fold(i), str(i))

        self.assertTrue(test_chain.can_fold(0))
        test_chain.fold(0)
        self.assertTrue(test_chain.can_fold(0))
        test_chain.fold(0)
        self.assertTrue(test_chain.can_fold(0))
        test_chain.fold(0)

        self.assertTrue(test_chain.folded())

    def test_reset_fold(self):
        """Tests correct reset folding of chain"""
        test_chain = chain.Chain(direction.str_to_dir_list("LRLLRLR"))
        self.assertListEqual(test_chain.get_chain(), [0, 3, 0, 3, 2, 3, 2, 3])

        self.assertTrue(test_chain.can_fold(3))
        test_chain.fold(3)
        self.assertListEqual(test_chain.get_chain(), [0, 3, 0, 3])

        self.assertTrue(test_chain.can_fold(2))
        test_chain.fold(2)
        self.assertListEqual(test_chain.get_chain(), [0, 3, 0])

        test_chain.reset_fold()
        self.assertListEqual(test_chain.get_chain(), [0, 3, 0, 3])

        test_chain.fold(0)
        self.assertListEqual(test_chain.get_chain(), [3, 0, 3])

        test_chain.reset_fold()
        self.assertListEqual(test_chain.get_chain(), [0, 3, 0, 3])

        test_chain.reset_fold()
        self.assertListEqual(test_chain.get_chain(), [0, 3, 0, 3, 2, 3, 2, 3])
