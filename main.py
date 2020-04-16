import os
import csv
import sys, getopt

def mainLoad(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('main.py -L -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   LoadBlockModel(inputfile, outputfile)

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
         
   PrintBlockModel(inputfile)

def LoadBlockModel(input_name, output_name):

    block_file = open(input_name, "r")
    lines = block_file.readlines()

    with open(output_name, 'w', newline='') as csv_block_file:
        wr = csv.writer(csv_block_file, quoting=csv.QUOTE_MINIMAL)
        for line in lines:
            csv_line = line.split()
            for i in range(len(csv_line)):
                try:
                    csv_line[i] = int(csv_line[i])
                except:
                    csv_line[i] = float(csv_line[i])
            wr.writerow(csv_line)

def PrintBlockModel(input_name):

    elements = []
    max_element_length = [2, 1, 1, 1, 4, 11, 11, 4, 14]

    with open(input_name, 'r') as csv_block_file:
        lines = csv_block_file.readlines()
        for line in lines:
            elements.append(line.split(','))

    for i in range(len(elements)):
        for j in range(len(elements[0])):
            if len(elements[i][j]) > max_element_length[j]:
                max_element_length[j] = len(str(elements[i][j]))

    id_print = (" "*int((max_element_length[0]-2)//2)) + "ID" + (" "*int((max_element_length[0]-2) - ((max_element_length[0]-2)//2)))
    x_print = (" "*int((max_element_length[1]-1)//2)) + "X" + (" "*int((max_element_length[1]-1) - ((max_element_length[1]-1)//2)))
    y_print = (" "*int((max_element_length[2]-1)//2)) + "Y" + (" "*int((max_element_length[2]-1) - ((max_element_length[2]-1)//2)))
    z_print = (" "*int((max_element_length[3]-1)//2)) + "Z" + (" "*int((max_element_length[3]-1) - ((max_element_length[3]-1)//2)))
    tonn_print = (" "*int((max_element_length[4]-4)//2)) + "TONN" + (" "*int((max_element_length[4]-4) - ((max_element_length[4]-4)//2)))
    block_value_print = (" "*int((max_element_length[5]-11)//2)) + "BLOCK VALUE" + (" "*int((max_element_length[5]-11) - ((max_element_length[5]-11)//2)))
    destination_print = (" "*int((max_element_length[6]-11)//2)) + "DESTINATION" + (" "*int((max_element_length[6]-11) - ((max_element_length[6]-11)//2)))
    cu_print = (" "*int((max_element_length[7]-4)//2)) + "CU %" + (" "*int((max_element_length[7]-4) - ((max_element_length[7]-4)//2)))
    process_print = (" "*int((max_element_length[8]-14)//2)) + "PROCESS PROFIT" + (" "*int((max_element_length[8]-14) - ((max_element_length[8]-14)//2)))

    print(' ' + '-'*(sum(max_element_length) + len(max_element_length) - 1))
    print('|' + id_print + '|' + x_print + '|' + y_print + '|' + z_print + '|' + tonn_print + '|' + block_value_print + '|' + destination_print + '|' + cu_print + '|' + process_print + '|')
    print(' ' + '-'*(sum(max_element_length) + len(max_element_length) - 1))

    for i in range(len(elements)):
        values = '|'
        for j in range(len(elements[0])):
            element = 0

            try:
                element = int(elements[i][j])
            except:
                element = float(elements[i][j])

            values += str(element) + (" "*int(max_element_length[j]-len(str(element)))) + '|'
        print(values)
        print(' ' + '-'*(sum(max_element_length) + len(max_element_length) - 1))

if __name__ == "__main__":
    if sys.argv[1] == '-L':
        mainLoad(sys.argv[2:])
    elif sys.argv[1] == '-P':
        mainPrint(sys.argv[2:])
    else:
        print('\nAvailable commands:\n')
        print('main.py -L -i <inputfile> -o <outputfile>')
        print('main.py -P -i <inputfile>')