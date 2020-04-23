import os
import csv
import sys, getopt
from load_block_model import loadModelArguments, printModelArguments, numberOfBlocksArguments, massInKilogramsArgument, gradeInPercentageArguments, attributeArguments

if __name__ == "__main__":
    if sys.argv[1] == '-L':
        print(loadModelArguments(sys.argv[2:]))
    elif sys.argv[1] == '-P':
        printModelArguments(sys.argv[2:])
    elif sys.argv[1] == '-N':
        print(numberOfBlocksArguments(sys.argv[2:]))
    elif sys.argv[1] == '-M':
        print(massInKilogramsArgument(sys.argv[2:]))
    elif sys.argv[1] == '-G':
        print(gradeInPercentageArguments(sys.argv[2:]))
    elif sys.argv[1] == '-A':
        print(attributeArguments(sys.argv[2:]))
    else:
        print('\nAvailable commands:\n')
        print('main.py -L -i <inputfile> -c <columnsFile> -o <outputfile>')
        print('Load file. Needs input file name and output file name.')
        print('----')
        print('main.py -P -i <inputfile>')
        print('Print file. Needs input file name.')
        print('----')
        print('main.py -N  -b <block_model_name>')
        print('Number of Blocks of a stored block model. Needs block model name and number of blocks.')
        print('----')
        print('main.py -M -b <block_model_name> -x <block_x> -y <block_y> -z <block_z>')
        print('Mass in Kilograms of one block in a stored block model. Needs block model name and coordinates.')
        print('----')
        print('main.py -G -n <model_name> -b <block_model_name> -x <block_x> -y <block_y> -z <block_z> -m <mineral_name>')
        print('Grade in Percentage for each Mineral of one block in a stored block model. Needs block model name, coordinates and mineral name.')
        print('----')
        print('main.py -A -b <block_model_name> -x <block_x> -y <block_y> -z <block_z> -n <attribute_name>')
        print('Search attribute of one block in a stored block model. Needs block model name, coordinates and attribute name.')