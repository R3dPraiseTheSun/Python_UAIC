
#Ex.1: list of the first n Fibonacci string
def ex1():
    fibonacci_list = []
    def fibonacci(**kwargs):
        a = kwargs.get('a', 0)
        b = kwargs.get('b', 1)
        current_limit = kwargs.get('current_limit', 0)
        limit = kwargs.get('limit', 10)

        if current_limit >= limit:
            print(fibonacci_list)
            return
        fibonacci_list.append(a)
        return(fibonacci(a=b, b=a+b, current_limit= current_limit+1, limit = limit))

    limit = int(input('limit: '))
    fibonacci(limit = limit)
              
#ex1()

#Ex.2: Find prime numbers inside a list
def ex2():
    def is_prime(number):
        if number > 1:
            for div in range(2, number):
                if number%div == 0:
                    return False
        return True

    primes_list = []
    def find_primes(number_list):
        for number in number_list:
            if is_prime(number):
                primes_list.append(number)
        print(primes_list)

    find_primes(range(1,100))

#ex2()

#Ex.3: function with 2 lists a and b, return a intersected with b, a reunited etc.
def ex3():
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

#ex3()

#Ex.4: given a list of musical notes and a list of order and a start position, return the music ordered by the order list
def ex4():
    def compose(music_list, order_list, start_pos):
        final_music_list = []
        current_pos = start_pos
        note_len = music_list.__len__()
        final_music_list.append(music_list[current_pos])
        for index in range(order_list.__len__()):
            current_pos = (current_pos + order_list[index])%note_len
            final_music_list.append(music_list[current_pos])
        print(final_music_list)

    compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)

#ex4()

#Ex.5: given a matrix return the same matrix with 0 under the main diagonal
def ex5():
    def replace_matrix(matrix):
        for line in range(matrix.__len__()):
            for element in range(matrix[line].__len__()):
                if(line > element): matrix[line][element] = 0
        for line in matrix: print(line)
        
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    replace_matrix(matrix)

#ex5()

import random
#Ex.6: Given a function that receives a variable number of lists and a x, return a list of items that appear x times in lists
def ex6():
    def find_x_occurances(x, **items):
        appearances_dict = {'element': {}}
        for listNo, item in items.items():
            for element in item:
                appearances_dict['element'].append(element)
        print(appearances_dict)

    find_x_occurances(2, list1=[1,2,3], list2=[2,3,4], list3=[4,5,6], list4=[4,1, "test"])

ex6()
