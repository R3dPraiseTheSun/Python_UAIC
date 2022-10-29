from genericpath import isdir
import os
import sys
import numpy as np

def ex_1(given_path):
    return sorted({os.path.splitext(f)[-1] for f in os.listdir(given_path) if os.path.splitext(f)[-1] != ''})

def ex_2(directory_path, file_path):
    with open(file_path, "w") as fd:
        [fd.write(os.path.abspath(f) + '\n') for f in os.listdir(directory_path) if f.startswith("a") and os.path.splitext(f)[-1] != '']

file_list = []
def ex_3(my_path):
    if(os.path.isdir(my_path)):
        extensions_list = []
        for file in os.listdir(my_path):
            if(os.path.splitext(file)[-1] != ''):
                extensions_list.append(os.path.splitext(file)[-1])
            else: ex_3(my_path + '/' + file)
        for ext in np.unique(extensions_list):
            #print(f'In path {my_path} the extension {ext} appears {extensions_list.count(ext)} times')
            file_list.append((ext, extensions_list.count(ext)))
            file_list.sort(key= lambda x: x[1], reverse=True)
    else:
        with open(my_path, "r") as fd:
            return fd.read()[-20:]
    return file_list

def ex_4():
    directory_path = sys.argv[1]
    return {os.path.splitext(f)[-1][1:] for f in os.listdir(directory_path) if not os.path.isdir(f)}

file_list5 = []
def ex_5(target, to_search):
    if(os.path.isdir(target)):
        for file in os.listdir(target):
            if(os.path.splitext(file)[-1] != ''):
                if to_search in str(file):
                    #print(f'{file} found')
                    file_list5.append(file)
                else: ex_5(target + '/' + file, to_search)
            elif('__pycache__' not in file): ex_5(target + '/' + file, to_search)
    elif(os.path.isfile(target)):
        with open(target, "r") as fd:
            if to_search in fd.read():
                return os.path.abspath(target)
    else: raise ValueError(target + ': is not valid')
    return file_list5

def error_callback(exception: Exception):
    print(exception)

def ex_6(target, to_search, callback):
    try:
        ex_5(target, to_search)
    except Exception as e:
        callback(e)

def ex_7(file_path):
    try:
        if os.path.isdir(file_path):
            raise Exception("Path should point to a file")
        return {
            "full_path": os.path.abspath(file_path),
            "file_size": os.path.getsize(file_path),
            "file_extension": os.path.splitext(file_path)[-1][1:],
            "can_read": os.access(file_path, os.R_OK),
            "can_write": os.access(file_path, os.W_OK),
        }
    except Exception as e:
        print(e)

def ex_8(dir_path):
    try:
        if os.path.isfile(dir_path):
            raise Exception("Path should point to a directory")
        return [os.path.abspath(f) for f in os.listdir(dir_path)]
    except Exception as e:
        print(e)

