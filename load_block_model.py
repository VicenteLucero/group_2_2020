import os
import csv
import sys, getopt
from block import Block
from block_model import BlockModel


def loadModelArguments(argv):
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

def printModelArguments(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"i:",["ifile="])
    except getopt.GetoptError:
        print('main.py -P -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfile = arg
    
    blockModel = CreateBlockModel(inputfile)
    PrintBlockModel(blockModel)


def numberOfBlocksArguments(argv):
    block_model_name = ""

    try:
        opts, args = getopt.getopt(argv, "b:", ["bname="])
    except getopt.GetoptError:
        print('main.py -N -b <block_model_name>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-b", "--bname"):
            block_model_name = arg

    block_model = CreateBlockModel(block_model_name)
    printNumberOfBlocks(block_model)

def massInKilogramsArgument(argv):
    block_model_name = ""
    x = 0
    y = 0
    z = 0

    try:
        opts, args = getopt.getopt(argv, "b:x:y:z:", ["bname=", "xcoord=", "ycoord=", "zcoord="])
    except getopt.GetoptError:
        print('main.py -M <block_model_name> <block_x> <block_y> <block_z>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-b", "--bname"):
            block_model_name = arg
        elif opt in ("-x", "--xcoord"):
            x = int(arg)
        elif opt in ("-y", "--ycoord"):
            y = int(arg)
        elif opt in ("-z", "--zcoord"):
            z = int(arg)

    block_model = CreateBlockModel(block_model_name)
    printMassInKilograms(block_model, x, y, z)

def gradeInPercentageArguments(argv):
    block_model_name = ""
    model_name = ""
    x = 0
    y = 0
    z = 0
    mineral_name = ""

    try:
        opts, args = getopt.getopt(argv, "n:b:x:y:z:m:", ["nnams=", "bname=", "xcoord=", "ycoord=", "zcoord=", "mname="])
    except getopt.GetoptError:
        print('main.py -G -n <model_name> -b <block_model_name> -x <block_x> -y <block_y> -z <block_z> -m <mineral_name>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-n", "--nname"):
            model_name = arg
        elif opt in ("-b", "--bname"):
            block_model_name = arg
        elif opt in ("-x", "--xcoord"):
            x = int(arg)
        elif opt in ("-y", "--ycoord"):
            y = int(arg)
        elif opt in ("-z", "--zcoord"):
            z = int(arg)
        elif opt in ("-m", "--mname"):
            mineral_name = arg

    blocks = CreateBlockModel(block_model_name)
    GetGradeOfMineral(blocks, model_name, x, y, z, mineral_name)

def attributeArguments(argv):
    block_model_name = ""
    x = 0
    y = 0
    z = 0
    attribute_name = ""

    try:
        opts, args = getopt.getopt(argv, "b:x:y:z:n:", ["bname=", "xcoord=", "ycoord=", "zcoord=", "aname="])
    except getopt.GetoptError:
        print('main.py -A -b <block_model_name> -x <block_x> -y <block_y> -z <block_z> -n <attribute_name>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-b", "--bname"):
            block_model_name = arg
        elif opt in ("-x", "--xcoord"):
            x = int(arg)
        elif opt in ("-y", "--ycoord"):
            y = int(arg)
        elif opt in ("-z", "--zcoord"):
            z = int(arg)
        elif opt in ("-n", "--aname"):
            attribute_name = arg

    blocks = CreateBlockModel(block_model_name)
    GetAttribute(blocks, x, y, z, attribute_name)

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
        wr.writerow(columns.split(','))
        for line in lines:
            csv_line = line.split()
            for i in range(len(csv_line)):
                try:
                    csv_line[i] = int(csv_line[i])
                except:
                    try:
                        csv_line[i] = float(csv_line[i])
                    except:
                        csv_line[i] = str(csv_line[i])
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
    if type(block) is str:
        print(block)
    else:
        print(block.getValue(attribute_name))

def GetGradeOfMineral(block_model, block_model_name, X, Y, Z, mineral_name):
    block = block_model.getBlock(X, Y, Z)
    if type(block) is str:
        print(block)
    else:
        print(block.getMineralGrade(mineral_name, block_model_name))

def printNumberOfBlocks(block_model):
    number_of_blocks = len(block_model.blocks)

    print(number_of_blocks)

def printMassInKilograms(block_model, x, y, z):
    block = block_model.getBlock(x, y, z)
    if type(block) is str:
        print(block)
        return
    possible_names = ["<tonn>", "ton", "tonns", "tons", "rock_tonnes"]
    
    for name in possible_names:
        if name in block_model.columns:
            mass = float(block.getValue(name))*1000
            print(str(mass), "kg")
            return
    

