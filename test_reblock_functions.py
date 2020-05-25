import unittest
from reblock_functions import *
from load_block_model import CreateBlockModel

class TestReblockFunctions(unittest.TestCase):
    def test_invalid_parameters_when_is_None(self):
        standard_input = [0, 0, None, "10"]
        self.assertEqual(invalidParameters(standard_input), True)

    def test_invalid_parameters_when_is_not_None(self):
        standard_input = [0, 0, False, "10"]
        self.assertEqual(invalidParameters(standard_input), False)

    def test_empty_blocks_when_valid_paramenters(self):
        test_new_blocks =   [[[None, None],[None, None]],
                             [[None, None],[None, None]]]
        self.assertEqual(emptyblocks(2, 2, 2), test_new_blocks)
    
    def test_empty_blocks_when_x_is_None(self):
        self.assertEqual(emptyblocks(None, 2, 2), "Invalid parameters")
    
    def test_empty_blocks_when_y_is_None(self):
        self.assertEqual(emptyblocks(2, None, 2), "Invalid parameters")
    
    def test_empty_blocks_when_z_is_None(self):
        self.assertEqual(emptyblocks(2, 2, None), "Invalid parameters")

    def test_new_block_values_when_valid_parameters(self):
        values = [0, 2, 2, 2, 31600, 1, 0.1, 0.0010000000000000009, 10.0]
        columns = ['<id>', '<x>', '<y>', '<z>', '<tonn>', '<destination>', '<Au (oz/ton)>', '<Ag [ppm]>', '<Cu %>']
        classification = [0, 0, 0, 0, 0, 2, 1, 1, 1]
        mass = "<tonn>"
        minerals = {'copper': ['%', '<Cu %>'], 'gold': ['oz/ton', '<Au (oz/ton)>'], 'silver': ['ppm', '<Ag [ppm]>']}
        mockup_block = Block(columns, mass, minerals, values, classification)

        block_model = CreateBlockModel("test_data.csv")

        block = newBlockValues(block_model.columns, block_model.blocks, 2, 2, 2)
        self.assertEqual(block.__eq__(mockup_block), True)

    def test_new_block_values_when_columns_is_None(self):
        block_model = CreateBlockModel("test_data.csv")
        
        block = newBlockValues(None, block_model.blocks, 2, 2, 2)
        self.assertEqual(block, "Invalid parameters")

    def test_new_block_values_when_blocks_is_None(self):
        block_model = CreateBlockModel("test_data.csv")
        
        block = newBlockValues(block_model.columns, None, 2, 2, 2)
        self.assertEqual(block, "Invalid parameters")

    def test_new_block_values_when_x_is_None(self):
        block_model = CreateBlockModel("test_data.csv")
        
        block = newBlockValues(block_model.columns, block_model.blocks, None, 2, 2)
        self.assertEqual(block, "Invalid parameters")

    def test_new_block_values_when_y_is_None(self):
        block_model = CreateBlockModel("test_data.csv")
        
        block = newBlockValues(block_model.columns, block_model.blocks, 2, None, 2)
        self.assertEqual(block, "Invalid parameters")

    def test_new_block_values_when_z_is_None(self):
        block_model = CreateBlockModel("test_data.csv")
        
        block = newBlockValues(block_model.columns, block_model.blocks, 2, 2, None)
        self.assertEqual(block, "Invalid parameters")
    
    def test_reblock_arround_blocks_when_valid_parameters(self):
        values = [42, 2, 2, 2, 2600, 1, 0.1, 0.001, 10.0]
        columns = ['<id>', '<x>', '<y>', '<z>', '<tonn>', '<destination>', '<Au (oz/ton)>', '<Ag [ppm]>', '<Cu %>']
        classification = [0, 0, 0, 0, 0, 2, 1, 1, 1]
        mass = "<tonn>"
        minerals = {'copper': ['%', '<Cu %>'], 'gold': ['oz/ton', '<Au (oz/ton)>'], 'silver': ['ppm', '<Ag [ppm]>']}
        mockup_block = Block(columns, mass, minerals, values, classification)

        block_model = CreateBlockModel("test_data.csv")
        block = reblockAroundBlocks(block_model, 2, 2, 2, 4, 4, 4)

        self.assertEqual(block.__eq__(mockup_block), True)

    def test_reblock_arround_blocks_when_invalid_block_model(self):
        block = reblockAroundBlocks(None, 2, 2, 2, 4, 4, 4)

        self.assertEqual(block, "Invalid parameters")

    def test_reblock_arround_blocks_when_invalid_block_x(self):
        block_model = CreateBlockModel("test_data.csv")
        block = reblockAroundBlocks(block_model, None, 2, 2, 4, 4, 4)

        self.assertEqual(block, "Invalid parameters")

    def test_reblock_arround_blocks_when_invalid_block_y(self):
        block_model = CreateBlockModel("test_data.csv")
        block = reblockAroundBlocks(block_model, 2, None, 2, 4, 4, 4)

        self.assertEqual(block, "Invalid parameters")

    def test_reblock_arround_blocks_when_invalid_block_z(self):
        block_model = CreateBlockModel("test_data.csv")
        block = reblockAroundBlocks(block_model, 2, 2, None, 4, 4, 4)

        self.assertEqual(block, "Invalid parameters")

    def test_reblock_arround_blocks_when_invalid_block_rx(self):
        block_model = CreateBlockModel("test_data.csv")
        block = reblockAroundBlocks(block_model, 2, 2, 2, None, 4, 4)

        self.assertEqual(block, "Invalid parameters")

    def test_reblock_arround_blocks_when_invalid_block_ry(self):
        block_model = CreateBlockModel("test_data.csv")
        block = reblockAroundBlocks(block_model, 2, 2, 2, 4, None, 4)

        self.assertEqual(block, "Invalid parameters")

    def test_reblock_arround_blocks_when_invalid_block_rz(self):
        block_model = CreateBlockModel("test_data.csv")
        block = reblockAroundBlocks(block_model, 2, 2, 2, 4, 4, None)

        self.assertEqual(block, "Invalid parameters")

if __name__ == '__main__':
    unittest.main()