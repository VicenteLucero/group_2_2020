import os
import csv
import sys, getopt
from block import Block
from block_model import BlockModel

def mainLoad(argv):
   inputfile = ''
   outputfile = ''
   columnsfile = ''
   try:
      opts, args = getopt.getopt(argv,"i:c:o:",["ifile=", "cfile=", "ofile="])
   except getopt.GetoptError:
      print('main.py -L -i <inputfile> -c <columnsFile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-c", "--cfile"):
         columnsfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   LoadBlockModel(inputfile, columnsfile, outputfile)

def mainPrint(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"i:",["ifile="])
   except getopt.GetoptError:
      print('main.py -P -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         inputfile = arg
         
   block_model = CreateBlockModel(inputfile)
   PrintBlockModel(block_model)

def CreateBlockModel(input_name):
    blocks = []
    columns = []

    with open(input_name, 'r') as csv_block_file:
        lines = csv_block_file.readlines()
        for line in range(len(lines)):  
            if line == 0:
                columns = lines[line].strip().split(',')
            else:
                block = Block(columns, lines[line].strip().split(','))
                blocks.append(block)
    return BlockModel(columns, blocks)


def LoadBlockModel(input_name, columns_name, output_name):

    block_file = open(input_name, "r")
    lines = block_file.readlines()
    block_file.close()

    columns_file = open(columns_name, "r")
    columns = columns_file.readline()
    columns_file.close()

    with open(output_name, 'w', newline='') as csv_block_file:
        wr = csv.writer(csv_block_file, quoting=csv.QUOTE_MINIMAL)
        wr.writerow(columns.split())
        for line in lines:
            csv_line = line.split()
            for i in range(len(csv_line)):
                try:
                    csv_line[i] = int(csv_line[i])
                except:
                    csv_line[i] = float(csv_line[i])
            wr.writerow(csv_line)

def PrintBlockModel(block_model):

    elements = []
    max_element_length = []

    elements.append(block_model.columns)

    for x in range(len(block_model.blocks)):
        elements.append(block_model.blocks[x].values)

    for n in range(len(elements[0])):
        max_element_length.append(0)

    for i in range(len(elements)):
        for j in range(len(elements[0])):
            if len(elements[i][j]) > max_element_length[j]:
                max_element_length[j] = len(str(elements[i][j]))

    print(' ' + '-'*(sum(max_element_length) + len(max_element_length) - 1))

    for i in range(len(elements)):
        values = '|'
        for j in range(len(elements[0])):
            element = elements[i][j].strip()

            values += str(element) + (" "*int(max_element_length[j]-len(str(element)))) + '|'
        print(values)
        print(' ' + '-'*(sum(max_element_length) + len(max_element_length) - 1))


def GetAttribute(block_model, X, Y, Z, attribute_name):
    block = block_model.getBlock(X, Y, Z)
    return block.getValue(attribute_name)

