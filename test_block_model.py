import unittest
from block_model import BlockModel
from block import Block


class TestBlockModel(unittest.TestCase):
    def test_eq_when_models_are_different_return_false(self):
        self.assertEqual(BlockModel.__eq__(BlockModel([Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10]), Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10])],
                                                      Block(["id", "x", "y", "z", "ores_tones"], [1, 2, 3, 4, 10]), Block(["id", "x", "y", "z", "ores_tones"], [1, 2, 3, 4, 10]))), False)

    def test_eq_when_models_are_not_different_return_true(self):
        self.assertEqual(BlockModel.__eq__(BlockModel([Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10]), Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10])],
                                                      Block(["id", "x", "y", "z", "tones"], [1, 2, 3, 4, 10]), Block(["id", "x", "y", "z", "tones"], [1, 2, 3, 4, 10]))), True)

    def test_get_block_when_block_exist_return_block(self):
        blocks = [Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10]), Block(["id", "x", "y", "z", "tons"], [2, 7, 8, 4, 10])]
        search = Block(["id", "x", "y", "z", "tons"], [2, 7, 8, 4, 10])
        self.assertEqual(BlockModel(blocks).getBlock(search), search)

    def test_get_block_when_block_do_not_exist_return_message(self):
        blocks = [Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10]), Block(["id", "x", "y", "z", "tons"], [2, 7, 8, 4, 10])]
        search = Block(["id", "x", "y", "z", "tons"], [2, 6, 8, 4, 10])
        self.assertEqual(BlockModel(blocks).getBlock(search), "Block does not exist")