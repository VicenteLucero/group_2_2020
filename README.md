# group_2_2020

# To Build:

Just clone this repository into your computer.
Be sure to have your kb.blocks in the same folder as your main.py and test_main.py files.
All modules required (os, unittest, csv, sys, getopt) should come with python 3.


# To Test:

There are 3 files that have tests created (test_block, test_block_model, test_load_block_model).
To run this tests just type in the command console the following command (be sure to have your console in the correct directory):

run all the tests: python -m unittest
run a specific test: python -m unittest test_name 

# To Use:

There are 6 main console commands that can be used in this program.

1. Load Block Model:

    The following command is used to load the block model and saves it into a csv file (be sure to use a .csv as the outputFile name, also columns.txt must be a one line file with the column_names of the model separated by commas):

    main.py -L -i [inputFile] -c [columnsFile.txt] -o [outputFile.csv]

    i.e.

    main.py -L -i kd.blocks -c columns.txt -o kd_blocks.csv

2. Print a previously saved block model:

    The following command is used to print a previously saved block model in a .csv file:

    main.py -P -i [blockModelFile.csv]

    i.e.

    main.py -P -i kd_blocks.csv

3. Print number of blocks in a previously saved model:

    The following command is used to print the number of blocks in a block model that was prevoiusly loaded:

    main.py -N -b [blockModelFile.csv]

    i.e.

    main.py -N -b kd_blocks.csv

4. Print mass in Kilograms of one block in a stored block model:

    The following command is used to print the mass in kilograms of a block stored in a block model previously loaded in a specific coordinate:

    main.py -M -b [blockModelFile.csv] -x [xCoordinate] -y [yCoordinate] -z [zCoordinate]

    i.e.

    main.py -M -b kd_blocks.csv -x 11 -y 0 -z 18

5. Print grade in percentage for each mineral of one block in a stored block model:

    The following command is used to print the grade in percentage for a mineral in a block of a previously loaded block model in a specific coordinate:

    main.py -G -n[blockModelName] -b [blockModelFile.csv] -x [xCoordinate] -y [yCoordinate] -z [zCoordinate] -m [mineralName]

    i.e.

    main.py -G -n kd -n kd_blocks.csv -x 11 -y 0 -z 18 -m copper

6. Print value of attribute of one block in a stored block model:

    The following command is used to print the value of any attribute in a previously stored block model in a specific coordinate:

    main.py -A -b [blockModelFile.csv] -x [xCoordinate] -y [yCoordinate] -z [zCoordinate] -n "[attributeName]"

    i.e.

    main.py -A -b kd_blocks.csv -x 11 -y 0 -z 12 -n "destination"

The mineral names for each model are (file column name -> commandline parameter)

1. newman1: 
    - grade -> mineral

2. zuck:
    - ore_tonnes -> ore

3. kd:
    - Cu % -> copper

4. p4hd:
    - Au (oz/ton) -> gold
    - Ag (oz/ton) -> silver
    - Cu % -> copper

5. marvin:
    - au [ppm] -> gold
    - Cu % -> copper

6. w23:
    - Au -> gold

7. mclaughlin:
    - Au (oz/ton) -> gold
