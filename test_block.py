import unittest
from block import Block


class TestBlock(unittest.TestCase):
    def test_check_eq_when_blocks_equals_returns_true(self):
        self.assertEqual((Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10])).__eq__(Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10])), True)

    def test_check_eq_when_blocks_equals_returns_false(self):
        self.assertEqual((Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10])).__eq__(Block(["id", "x", "y", "z", "ore_tons"], [1, 2, 3, 4, 10])), False)

    def test_get_value_when_column_not_exist_return_values(self):
        self.assertEqual(Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, [1, 2, 3]]).getValue("tons"), [1, 2, 3])

    def test_get_value_when_column_not_exist_return_message(self):
        self.assertEqual(Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, [1, 2, 3]]).getValue("ore tons"), ["Column does not exist"])