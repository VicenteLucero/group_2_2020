import unittest
from main import LoadBlockModel
import os
import csv
import sys, getopt

class TestLoadBlockModel(unittest.TestCase):
    def test_file(self):
        self.assertIsNotNone(open("kd.blocks", "r"))



    def test_model_input(self):
        model = open("kd.blocks", "r")
        for line in model.readlines():
            self.assertEqual(len(list(map(float, line.split()))), 9)


    def test_input_type(self):
        self.assertRegex("kd.blocks", ".blocks")



    # def test_output(self):
        # input = open("kd.blocks")
        # LoadBlockModel("kd.blocks", "kd.csv")
        # output = open("kd.csv", "r")
        # self.assertEqual(len(input.readlines()), len(output.readlines()))
        # for line in output.readlines():
        #    self.assertEqual(len(list(map(float, line.split(",")))), 9)
