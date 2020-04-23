import unittest
from block_model import BlockModel
from block import Block


class TestBlockModel(unittest.TestCase):
    def test_eq_when_models_are_different_return_false(self):
        model_1 = BlockModel(["id", "x", "y", "z", "tons"], [Block(["id", "x", "y", "z", "tons"], [1, 2, 5, 4, 10]), Block(["id", "x", "y", "z", "tons"], [1, 2, 8, 4, 10])])
        model_2 = BlockModel(["id", "x", "y", "z", "tons"], [Block(["id", "x", "y", "z", "tons"], [1, 3, 5, 4, 10]), Block(["id", "x", "y", "z", "tons"], [1, 5, 8, 4, 10])])
        self.assertEqual(model_1.__eq__(model_2), False)

    def test_eq_when_models_are_not_different_return_true(self):
        model_1 = BlockModel(["id", "x", "y", "z", "tons"], [Block(["id", "x", "y", "z", "tons"], [1, 2, 5, 4, 10]), Block(["id", "x", "y", "z", "tons"], [1, 2, 8, 4, 10])])
        self.assertEqual(model_1.__eq__(model_1), True)

    def test_get_block_when_block_exist_return_block(self):
        block_1 = Block(["id", "x", "y", "z", "tons"], [1, 2, 5, 4, 10])
        block_2 = Block(["id", "x", "y", "z", "tons"], [1, 2, 8, 4, 10])
        block_model = BlockModel(["id", "x", "y", "z", "tons"], [block_1, block_2])
        self.assertEqual(block_model.getBlock(2, 5, 4), block_1)

    def test_get_block_when_block_do_not_exist_return_message(self):
        block_model = BlockModel(["id", "x", "y", "z", "tons"], [Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10]), Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, 10])])
        self.assertEqual(block_model.getBlock(2, 3, 5), "Block does not exist")