# group_2_2020

# To Build:

Just clone this repository into your computer.
Be sure to have your kb.blocks in the same folder as your main.py and test_main.py files.
All modules required (os, unittest, csv, sys, getopt) should come with python 3.


# To Test:

There are 4 tests implemented in test_main.py.
To run this tests just type in the command console the following command (be sure to have your console in the correct directory):

python -m unittest


# To Use:

There are 2 main console commands that can be used in this program.

1. Load Block Model:

    The following command is used to load the block model and saves it into a csv file (be sure to use a .csv as the outputFile name, also columns.txt must be a one line file with the column_names of the model separated by commas):

    main.py -L -i [inputFile] -c [columnsFile.txt] -o [outputFile.csv]

    i.e.

    main.py -L -i kd.blocks -c columns.txt -o kd_blocks.csv

2. Print a previosly saved block model:

    The following command is used to print a previously saved block model in a .csv file:

    main.py -P -i [blockModel.csv]

    i.e.

    main.py -P -i kd_blocks.csv
