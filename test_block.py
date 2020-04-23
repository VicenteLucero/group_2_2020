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
        self.assertEqual(Block(["id", "x", "y", "z", "tons"], [1, 2, 3, 4, [1, 2, 3]]).getValue("ore tons"), "Column does not exist")

    def test_get_mineral_grade_when_model_or_mineral_not_exist_return_text(self):
        columns = ["id", "x", "y", "z", "type", "grade", "tonns", "min_caf", "value_extracc", "value_proc", "apriori_process"]
        values = [0, 0, 1, 20, "FRWS", 0.077065843, 2192.93, 1.02, -2236.7886, -36475.56586, 0]
        block = Block(columns, values)
        self.assertEqual(block.getMineralGrade("PKMN", "newman1"), "Model or Mineral not valid")
        self.assertEqual(block.getMineralGrade("FRWS", "Arkham"), "Model or Mineral not valid")

    def test_get_mineral_grade_when_model_or_mineral_not_exist_return_grade(self):
        columns = ["id", "x", "y", "z", "type", "grade", "tonns", "min_caf", "value_extracc", "value_proc", "apriori_process"]
        values = [0, 0, 1, 20, "FRWS", 0.077065843, 2192.93, 1.02, -2236.7886, -36475.56586, 0]
        block = Block(columns, values)
        self.assertEqual(block.getMineralGrade("mineral", "newman1"), 0.077065843)