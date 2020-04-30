import unittest
from reblock_functions import *

class TestReblockFunctions(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()