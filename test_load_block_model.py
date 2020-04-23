import unittest
from block import Block
from block_model import BlockModel
from load_block_model import *

class TestLoadBlockModel(unittest.TestCase):

    # test para obtener el grade de algun mineral es el mismo que en test_block ya que llama a dicha funcion para un
    # bloque en especifico
    # La mayoria de las funciones llaman a funciones propias de block y block model por lo que sus respectivos test
    # estan en sus respectivos archivos
    def test_create_block_model_when_csv_exists_return_block_model(self):
        columns = ["id", "x", "y", "z", "type", "grade", "tonns", "min_caf", "value_extracc", "value_proc", "apriori_process"]
        block_1 = Block(columns, ["0", "0", "1", "20", "FRWS", "0.077065843", "2192.93", "1.02", "-2236.7886", "-36475.56586", "0"])
        block_2 = Block(columns, ["1", "1", "1", "15", "FROR", "1.375353107", "5664","1.04","-5890.56", "24829.116", "1"])
        block_3 = Block(columns, ["2", "1", "1", "16", "OXOR", "0.913001543", "5184", "1.03", "-5339.52", "34347.213", "0"])
        block_4 = Block(columns, ["3", "1", "1", "17", "OXOR", "0.60628858", "5184", "1.03", "-5339.52", "6743.223", "0"])
        block_model_1 = BlockModel(columns, [block_1, block_2, block_3, block_4])
        block_model_2 = CreateBlockModel("test_model_file.csv")
        self.assertEqual(block_model_2.__eq__(block_model_1), True)