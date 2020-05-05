import unittest
from block_model import BlockModel
from block import Block
from collections import defaultdict
from load_block_model import CreateBlockModel


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

    def test_reblock_when_valid_parameters(self):
        columns = ['<id>', '<x>', '<y>', '<z>', '<tonn>', '<destination>', '<Au (oz/ton)>', '<Ag [ppm]>', '<Cu %>']
        classification = [0, 0, 0, 0, 0, 2, 1, 1, 1]
        mass = "<tonn>"
        minerals = {'copper': ['%', '<Cu %>'], 'gold': ['oz/ton', '<Au (oz/ton)>'], 'silver': ['ppm', '<Ag [ppm]>']}
        
        block_1 = Block(columns, mass, minerals, [0, 0, 0, 0, 5300, 1, 0.1, 0.0009999999999999998, 10.0], classification)
        block_2 = Block(columns, mass, minerals, [2, 0, 0, 2, 1700, 1, 0.1, 0.001, 10.0], classification)
        block_3 = Block(columns, mass, minerals, [8, 0, 2, 0, 4400, 1, 0.1, 0.001, 10.0], classification)
        block_4 = Block(columns, mass, minerals, [10, 0, 2, 2, 6200, 2, 0.1, 0.0009999999999999998, 10.0], classification)
        block_5 = Block(columns, mass, minerals, [32, 2, 0, 0, 4400, 2, 0.1, 0.0009999999999999998, 10.0], classification)
        block_6 = Block(columns, mass, minerals, [34, 2, 0, 2, 4400, 2, 0.1, 0.001, 10.0], classification)
        block_7 = Block(columns, mass, minerals, [40, 2, 2, 0, 2600, 1, 0.1, 0.001, 10.0], classification)
        block_8 = Block(columns, mass, minerals, [42, 2, 2, 2, 2600, 1, 0.1, 0.001, 10.0], classification)

        block_model = CreateBlockModel("test_data.csv")
        mockup_result = [[[block_1, block_2],[block_3, block_4]],
                         [[block_5, block_6],[block_7, block_8]]]
        
        result = block_model.reBlock(2, 2, 2)
        x = 0
        while x < len(result):
            y = 0
            while y < len(result[0]):
                z = 0
                while z < len(result[0][0]):
                    self.assertEqual(result[x][y][z].__eq__(mockup_result[x][y][z]), True)
                    z += 1
                y += 1
            x += 1

    def test_reblock_return_correct_tonns_when_reblock(self):
        block_model = CreateBlockModel("test_data.csv")
        result = block_model.reBlock(2, 2, 2)
        self.assertEqual(result[0][0][0].getValue('<tonn>'), 5300)

    def test_reblock_return_correct_destination_when_reblock(self):
        block_model = CreateBlockModel("test_data.csv")
        result = block_model.reBlock(2, 2, 2)
        self.assertEqual(result[0][0][0].getValue('<destination>'), 1)

    def test_reblock_return_correct_Au_when_reblock(self):
        block_model = CreateBlockModel("test_data.csv")
        result = block_model.reBlock(2, 2, 2)
        self.assertEqual(result[0][0][0].getValue('<Au (oz/ton)>'), 0.1)

    def test_reblock_return_correct_Ag_when_reblock(self):
        block_model = CreateBlockModel("test_data.csv")
        result = block_model.reBlock(2, 2, 2)
        self.assertEqual(result[0][0][0].getValue('<Ag [ppm]>'), 0.0009999999999999998)

    def test_reblock_return_correct_Cu_when_reblock(self):
        block_model = CreateBlockModel("test_data.csv")
        result = block_model.reBlock(2, 2, 2)
        self.assertEqual(result[0][0][0].getValue('<Cu %>'), 10.0)

    def test_reblock_when_resizing_by_1(self):
        block_model = CreateBlockModel("test_data.csv")
        blocks = block_model.blocks
        mockup_result = []

        count = 0
        for x in range(4):
            x_list = []
            for y in range(4):
                y_list = []
                for z in range(4):
                    y_list.append(blocks[count])
                    count += 1
                x_list.append(y_list)
            mockup_result.append(x_list)

        result = block_model.reBlock(1, 1, 1)
        x = 0
        while x < len(result):
            y = 0
            while y < len(result[0]):
                z = 0
                while z < len(result[0][0]):
                    self.assertEqual(result[x][y][z].__eq__(mockup_result[x][y][z]), True)
                    z += 1
                y += 1
            x += 1

    def test_reblock_when_resizing_by_original_length(self):
        columns = ['<id>', '<x>', '<y>', '<z>', '<tonn>', '<destination>', '<Au (oz/ton)>', '<Ag [ppm]>', '<Cu %>']
        classification = [0, 0, 0, 0, 0, 2, 1, 1, 1]
        mass = "<tonn>"
        minerals = {'copper': ['%', '<Cu %>'], 'gold': ['oz/ton', '<Au (oz/ton)>'], 'silver': ['ppm', '<Ag [ppm]>']}
        values = [0, 0, 0, 0, 31600, 1, 0.1, 0.0010000000000000009, 10.0]
        mockup_result = [[[Block(columns, mass, minerals, values, classification)]]]

        block_model = CreateBlockModel("test_data.csv")

        result = block_model.reBlock(4, 4, 4)
        x = 0
        while x < len(result):
            y = 0
            while y < len(result[0]):
                z = 0
                while z < len(result[0][0]):
                    self.assertEqual(result[x][y][z].__eq__(mockup_result[x][y][z]), True)
                    z += 1
                y += 1
            x += 1

    def test_reblock_when_model_is_empty(self):
        columns = ['<id>', '<x>', '<y>', '<z>', '<tonn>', '<destination>', '<Au (oz/ton)>', '<Ag [ppm]>', '<Cu %>']
        block_map = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        block_model = BlockModel(columns, [], block_map)

        result = block_model.reBlock(1, 1, 1)
        self.assertEqual(result, [[[None]]])
        
    def test_reblock_when_invalid_rx(self):
        block_model = CreateBlockModel("test_data.csv")
        
        result = block_model.reBlock(None, 2, 2)
        self.assertEqual(result, "Invalid parameters")

    def test_reblock_when_invalid_ry(self):
        block_model = CreateBlockModel("test_data.csv")
        
        result = block_model.reBlock(2, None, 2)
        self.assertEqual(result, "Invalid parameters")
    
    def test_reblock_when_invalid_rz(self):
        block_model = CreateBlockModel("test_data.csv")
        
        result = block_model.reBlock(2, 2, None)
        self.assertEqual(result, "Invalid parameters")

if __name__ == '__main__':
    unittest.main()