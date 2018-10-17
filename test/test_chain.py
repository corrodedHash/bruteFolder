"""Contains tests for chain module"""
import unittest

from .context import brutefolder  # pylint: disable=unused-import
from brutefolder import direction  # pylint: disable=wrong-import-order
from brutefolder import chain  # pylint: disable=wrong-import-order


class ChainTestClass(unittest.TestCase):
    """Tests the chain class"""

    def test_folding(self) -> None:
        """Tests correct folding of chain"""
        test_chain = chain.Chain(direction.str_to_dir_list("LRLLRLR"))
        self.assertListEqual(
            test_chain.chain, direction.str_to_dir_list("ULULDLDL"))

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

    def test_reset_fold(self) -> None:
        """Tests correct reset folding of chain"""
        test_chain = chain.Chain(direction.str_to_dir_list("LRLLRLR"))
        self.assertListEqual(
            test_chain.chain, direction.str_to_dir_list("ULULDLDL"))

        self.assertTrue(test_chain.can_fold(3))
        test_chain.fold(3)
        self.assertListEqual(
            test_chain.chain, direction.str_to_dir_list("ULUL"))

        self.assertTrue(test_chain.can_fold(2))
        test_chain.fold(2)
        self.assertListEqual(
            test_chain.chain, direction.str_to_dir_list("ULU"))

        test_chain.reset_fold()
        self.assertListEqual(
            test_chain.chain, direction.str_to_dir_list("ULUL"))

        test_chain.fold(0)
        self.assertListEqual(
            test_chain.chain, direction.str_to_dir_list("LUL"))

        test_chain.reset_fold()
        self.assertListEqual(
            test_chain.chain, direction.str_to_dir_list("ULUL"))

        test_chain.reset_fold()
        self.assertListEqual(
            test_chain.chain, direction.str_to_dir_list("ULULDLDL"))
