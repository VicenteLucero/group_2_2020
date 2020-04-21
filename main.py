import os
import csv
import sys, getopt
from load_block_model import *

if __name__ == "__main__":
    if sys.argv[1] == '-L':
        mainLoad(sys.argv[2:])
    elif sys.argv[1] == '-P':
        mainPrint(sys.argv[2:])
    else:
        print('\nAvailable commands:\n')
        print('main.py -L -i <inputfile> -o <outputfile>')
        print('main.py -P -i <inputfile>')