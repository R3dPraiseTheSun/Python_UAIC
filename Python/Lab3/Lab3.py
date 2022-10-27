import re

def ex1():
    def function(list_a, list_b):
            list_a = set(list_a)
            list_b = set(list_b)
            return [
                list_a.intersection(list_b),
                list_a.union(list_b),
                list_a.difference(list_b),
                list_b.difference(list_a)
            ]
    print(function(range(1,20,4), range(13,30,2)))

def ex2():
    def occur_dict(string):
        occurances_dict = {}
        for char in string:
            if occurances_dict.get(char):
                occurances_dict[char] = occurances_dict.get(char)+ 1
            else: occurances_dict[char] = 1
        occurances_dict = dict(sorted(occurances_dict.items()))
        print(occurances_dict)

    occur_dict("Ana has apples.")

def ex3(reccursive = False):
    # make a big list, sort it, find how many instances of one item we have
    def compare_dicts(dict_A: dict, dict_B: dict) -> bool:
        item_list = []
        for key in dict_A: item_list.append([key, dict_A[key]])
        for key in dict_B: item_list.append([key, dict_B[key]])
        item_list.sort(key= lambda x : x[0])
        for el in item_list[::2]: 
            if(not item_list.count(el)%2): print(el, 'is ok')
            else: 
                print(el, 'not ok')
                return False
        return True
    # raccursive way of iterating through dict
    def compare_dicts_reccursive(dict_A, dict_B):
        if type(dict_A) != type(dict_B): return False, f'first element is {type(dict_A)} while the second element is {type(dict_B)}'
        if type(dict_A) is dict:
            for label_1, label_2 in zip(sorted(dict_A.keys()), sorted(dict_B.keys())):
                if label_1 != label_2:
                    return False, f'{label_1} is different than {label_2}'
                verify_equal = compare_dicts_reccursive(dict_A[label_1], dict_B[label_2])
                if not verify_equal[0]: return False, f'{dict_A[label_1]} is different than {dict_B[label_2]}'
            return True, 'Dicts are equal'
        elif dict_A == dict_B: 
            return True, f'{dict_A} is ok'
        return False, f'{dict_A} is not ok'

    if reccursive :
        print(compare_dicts_reccursive({'A':10, 'B':11, 'C':12, 'D0':{'D1':1111, 'D2':22}}, {'A':10, 'B':11, 'C':12,'D0':{'D1':13, 'E':14, 'F':[15,16]}}))
        print(compare_dicts_reccursive({'A':10, 'B':11, 'C':12,'D0':{'D1':13, 'E':14, 'F':[15,16]}}, {'A':10, 'B':11, 'C':12,'D0':{'D1':13, 'E':14, 'F':[15,16]}}))
    else:
        print(compare_dicts({'A':10, 'B':11, 'C':12, 'D0':{'D1':1111, 'D2':22}}, {'A':10, 'B':11, 'C':12,'D0':{'D1':13, 'E':14, 'F':[15,16]}}))
        print(compare_dicts({'A':10, 'B':11, 'C':12,'D0':{'D1':13, 'E':14, 'F':[15,16]}}, {'A':10, 'B':11, 'C':12,'D0':{'D1':13, 'E':14, 'F':[15,16]}}))

def ex4():
    def build_xml_element(tag, content, **kwargs):
        href = kwargs.get("href")
        _class = kwargs.get("_class")
        id = kwargs.get("id")
        return f'<{tag} href={href}_class={_class}id={id}>{content}</{tag}>'
    
    print(build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))

def ex5():
    def validate_dict(validation_rules: set, targeted_dict: dict):
        rules_list = []
        for i in validation_rules: rules_list.append((i[0], i[1:]))
        rules_list.sort()

        for key, item in targeted_dict.items():
            key_found = False
            for rules in rules_list:
                if key == rules[0]: 
                    word_list = re.split(', | ', item)
                    if(
                        not rules[1][0] in word_list[0] or
                        not rules[1][-1] in word_list[-1] or
                        not rules[1][1] in word_list[1:-1]
                    ): return False, f'Rules broken for {key}'
                    key_found = True
                    break
            if not key_found: return False, 'Key not found in rule set'

        return True

    print(validate_dict(
        {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
        {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    ))
    print(validate_dict(
        {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
        {"key1": "inside, it's too cold out", "key3": "this is not valid"}
    ))
    print(validate_dict(
        {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
        {"key1": "come inside, it's too cold out", "key2": "start in the middle of winter"}
    ))

def ex6():
    def func(list_a):
        duplicate_set = set()
        duplicate_number = 0
        for el in set(list_a): 
            if (list_a.count(el)-1 > 0): 
                duplicate_set.add(el)
                duplicate_number += (list_a.count(el)-1)
        return len(set(list_a)), duplicate_set, duplicate_number
    print(func([1, 2, 3, 4, 1, 2, 5, 7, 10, 4, 10, 5, 1, 12]))

def ex7():
    def func(*sets):
        operation_dict = {}
        nr_o_sets = len(sets)
        for index in range(nr_o_sets):
            operation_dict[str(sets[index])+' & '+str(sets[(index+1)%nr_o_sets])] = sets[index].intersection(sets[(index+1)%nr_o_sets])
            operation_dict[str(sets[index])+' | '+str(sets[(index+1)%nr_o_sets])] = sets[index].union(sets[(index+1)%nr_o_sets])
            operation_dict[str(sets[index])+' - '+str(sets[(index+1)%nr_o_sets])] = sets[index].difference(sets[(index+1)%nr_o_sets])
            operation_dict[str(sets[(index+1)%nr_o_sets])+'-'+str(sets[index])] = sets[(index+1)%nr_o_sets].difference(sets[index])
        print(operation_dict)

    print(func({1,2}, {2,3,6}, {4,6,9,11}, {4,5,6}))

def ex8():
    def loop(mapping: dict):
        found_loop = False
        next_key = 'start'
        sequence = []
        while(not found_loop):
            if(not next_key == mapping.get(next_key) and not mapping.get(next_key) == 'start'):
                next_key = mapping.get(next_key)
                sequence.append(next_key)
            else: found_loop = True
        return sequence

    print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': 'x', '2': 'y', 'y': 'start'}))

def ex9():
    def my_function(*args, **kwargs):
        duplicates = []
        for key, value in kwargs.items():
            if value in args: duplicates.append(value)
        return len(duplicates)

    print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
