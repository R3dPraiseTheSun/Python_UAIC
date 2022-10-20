#Ex.1:
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
# ex1()

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
#ex2()

def ex3():
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
    print(compare_dicts({'A':10, 'B':11, 'C':12, 'D0':{'D1':1111, 'D2':22}}, {'A':10, 'B':11, 'C':12,'D0':{'D1':13, 'E':14, 'F':[15,16]}}))
    print(compare_dicts({'A':10, 'B':11, 'C':12,'D0':{'D1':13, 'E':14, 'F':[15,16]}}, {'A':10, 'B':11, 'C':12,'D0':{'D1':13, 'E':14, 'F':[15,16]}}))
ex3()

def ex4():
    print("Work in progress")
# ex4()

def ex5():
    print("Work in progress")
# ex5()

def ex6():
    print("Work in progress")
# ex6()

def ex7():
    print("Work in progress")
# ex7()

def ex8():
    print("Work in progress")
# ex8()

def ex9():
    print("Work in progress")
# ex9()
