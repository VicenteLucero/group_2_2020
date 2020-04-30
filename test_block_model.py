import unittest
from block_model import BlockModel
from block import Block
from collections import defaultdict


class TestBlockModel(unittest.TestCase):
    def test_eq_when_models_are_different_return_false(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)
        block_2 = Block(columns, mass, minerals, [2, 2, 5, 5, 10, 4, 7, 1], classification)
        block_3 = Block(columns, mass, minerals, [1, 2, 6, 4, 10, 5, 6, 2], classification)
        block_4 = Block(columns, mass, minerals, [2, 2, 6, 5, 10, 4, 7, 1], classification)
        block_map1 = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        block_map1['2']['5']['4'] = block_1
        block_map1['2']['5']['5'] = block_2
        block_map2 = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        block_map1['2']['6']['4'] = block_3
        block_map1['2']['6']['5'] = block_4
        model_1 = BlockModel(columns, [block_1, block_2], block_map1)
        model_2 = BlockModel(columns, [block_3, block_4], block_map2)
        self.assertEqual(model_1.__eq__(model_2), False)

    def test_eq_when_models_are_not_different_return_true(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)
        block_2 = Block(columns, mass, minerals, [2, 2, 5, 5, 10, 4, 7, 1], classification)
        model_1 = BlockModel(columns, [block_1, block_2], {'2':{'5':{'4': block_1, '5': block_2}}})
        model_2 = BlockModel(columns, [block_1, block_2], {'2':{'5':{'4': block_1, '5': block_2}}})
        self.assertEqual(model_1.__eq__(model_2), True)

    def test_get_block_when_block_exist_return_block(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)
        block_2 = Block(columns, mass, minerals, [2, 2, 5, 5, 10, 4, 7, 1], classification)
        block_model = BlockModel(columns, [block_1, block_2], {'2':{'5':{'4': block_1, '5': block_2}}})
        self.assertEqual(block_model.getBlock(2, 5, 4), block_1)

    def test_get_block_when_block_do_not_exist_return_message(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)
        block_2 = Block(columns, mass, minerals, [2, 2, 5, 5, 10, 4, 7, 1], classification)
        block_map = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        block_map['2']['5']['4'] = block_1
        block_map['2']['5']['5'] = block_2
        block_model = BlockModel(columns, [block_1, block_2], block_map)
        self.assertEqual(block_model.getBlock(2, 3, 5), "Block does not exist")


if __name__ == '__main__':
    unittest.main()