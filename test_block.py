import unittest
from block import Block


class TestBlock(unittest.TestCase):
    def test_check_eq_when_blocks_equals_returns_true(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)
        
        self.assertEqual((block_1).__eq__(block_1), True)

    def test_check_eq_when_blocks_not_equals_returns_false(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)
        block_2 = Block(columns, mass, minerals, [2, 2, 5, 5, 10, 4, 7, 1], classification)
        self.assertEqual((block_1).__eq__(block_2), False)

    def test_get_value_when_column_exist_return_values(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)

        self.assertEqual(block_1.getValue("tonn"), 10)

    def test_get_value_when_column_not_exist_return_message(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)

        self.assertEqual(block_1.getValue("ore tons"), "Column does not exist")

    def test_get_mineral_grade_when_mineral_not_exist_return_text(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)
        
        self.assertEqual(block_1.getMineralGrade("lithium"), "Mineral does not exist in this model")

    def test_get_mineral_grade_when_mineral_does_not_match_any_column(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %'], "lithium": ["%", "l%"]}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)

        self.assertEqual(block_1.getMineralGrade("lithium"), "Column of the mineral does not match any of the existing columns")

    def test_get_mineral_grade_when_mineral_unit_is_percentage(self):
        columns = ["id","x","y","z","tonn","Au (oz/ton)","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['oz/ton', 'Au (oz/ton)'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)

        self.assertEqual(block_1.getMineralGrade("copper"), 2.0)

    def test_get_mineral_grade_when_mineral_unit_is_oz_ton(self):
        columns = ["id","x","y","z","tonn","Au [ppm]","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['ppm', 'Au [ppm]'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)
        
        self.assertEqual(block_1.getMineralGrade("silver"), 0.0170097)

    def test_get_mineral_grade_when_mineral_unit_is_ppm(self):
        columns = ["id","x","y","z","tonn","Au [ppm]","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['ppm', 'Au [ppm]'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)

        self.assertEqual(block_1.getMineralGrade("gold"), 0.0005)

    def test_get_mineral_grade_when_mineral_unit_is_tonn(self):
        columns = ["id","x","y","z","tonn","Au tonn","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['tonn', 'Au tonn'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)
        
        self.assertEqual(block_1.getMineralGrade("gold"), 50.0)

    def test_get_value_classification_pair_when_column_exists(self):
        columns = ["id","x","y","z","tonn","Au tonn","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['tonn', 'Au tonn'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)

        self.assertEqual(block_1.getValueClassificationPair("tonn"), (10, 0))

    
    def test_get_value_classification_pair_when_column_does_not_exists(self):
        columns = ["id","x","y","z","tonn","Au tonn","Ag (oz/ton)","Cu %"]
        mass = "tonn"
        minerals = {"gold": ['tonn', 'Au tonn'], "silver": ['oz/ton', 'Ag (oz/ton)'], "copper": ['%', 'Cu %']}
        classification = [0, 0, 0, 0, 0, 1, 1, 1]
        block_1 = Block(columns, mass, minerals, [1, 2, 5, 4, 10, 5, 6, 2], classification)

        self.assertEqual(block_1.getValueClassificationPair("columna"), "Column does not exist")

if __name__ == '__main__':
    unittest.main()