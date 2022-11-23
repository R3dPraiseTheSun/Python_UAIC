import re
import sys

def function(file_path_in, file_path_out):
    element_dict = {}
    with open(file_path_in, 'r') as fd:
        for line in fd.readlines():
            element_dict[line.split()[0]] = line.split()[2]
        fd.close()
    with open(file_path_out, 'w') as fd:
        for key in sorted(element_dict.keys()):
            # print(type(element_dict[key]))
            to_write = ''.join([key, '\t= ' , element_dict[key], '\n'])
            fd.write(to_write)
        fd.close()

function(sys.argv[1], sys.argv[2])
    