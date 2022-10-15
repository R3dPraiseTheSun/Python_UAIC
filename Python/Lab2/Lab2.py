
#Ex.1: List of the first n Fibonacci string
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

#Ex.3: Function with 2 lists a and b, return a intersected with b, a reunited etc.
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

#Ex.4: Given a list of musical notes and a list of order and a start position, return the music ordered by the order list
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

#Ex.5: Given a matrix return the same matrix with 0 under the main diagonal
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

#Ex.6: Given a function that receives a variable number of lists and a x, return a list of items that appear x times in lists
def ex6():
    def find_x_occurances(x, **items):
        appearances_dict = {}
        input_list = []
        for element in [item for listNo, item in items.items()]:
            input_list = input_list + element
        for element in input_list:
            appearances_dict[element]=input_list.count(element)
        print([element for element in appearances_dict if appearances_dict[element] == x])

    find_x_occurances(2, list1=[1,2,3], list2=[2,3,4], list3=[4,5,6], list4=[4,1, "test"])

#ex6()

#Ex.7: Write a function that receives a list of integers and returns a tuple like (number_of_palindromes, greatest_palindrome)
def ex7():
    def is_palindrome(number):
        if type(number) != str: number = str(number)
        if number == number[::-1]: return True
        return False

    def get_palindromes(input_list):
        palindrome_list = []
        for input in input_list:
            if is_palindrome(input):
                palindrome_list.append(input)
        palindrome_list.sort(reverse=True)
        return (palindrome_list.__len__(), palindrome_list[0])

    print(get_palindromes(range(0,1000,3)))

#ex7()

#Ex.8: Write a function that receives a list of strings and optional params x and a boolean, return a list of lists with elements ASCII divisible (or not) with x
def ex8():
    def func(x = 1, string_list = [], divisible = True):
        result_list = []
        for string in string_list:
            result_list.append([char for char in string if ord(char)%x != int(divisible)])
        return result_list

    print(func(2, ["test", "hello", "lab002"], divisible = False))

#ex8()

#Ex.9: Given a matrix with people heigths return the coordinates where one individual cannot see the #FIELD
def ex9():
    def get_shorter_people(matrix):
        prev_lines = []
        prev_lines.append(matrix[0])
        result_list = []
        for line in matrix[1:]:
            for index in range(line.__len__()):
                in_front = [p_line[index] for p_line in prev_lines]
                if(max(in_front) >= line[index]):
                    result_list.append([in_front.__len__(),index])
            prev_lines.append(line)
        return result_list
    matrix=[
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]
    print(get_shorter_people(matrix))

#ex9()

#Ex.10: Return in a list the index of multiple lists
def ex10():
    def order_lists(**lists):
        rezult_list = []
        maximum_length = max([item[1].__len__() for item in lists.items()])
        for element in [item[1] for item in lists.items() if item[1].__len__() < maximum_length]:
            for index in range(abs(maximum_length - element.__len__())):
                element.append(None)
        for index in range(maximum_length):
            rezult_list.append([item[index] for listName, item in lists.items()])
        return rezult_list

    print(order_lists(list1=[1,2,3], list2=[5,6,7], list3=["a", "b", "c"]))
    print(order_lists(list1=[1,2,3,4], list2=[5,6,7], list3=["a", "b", "c", "d", "e"]))

#ex10()

#Ex.11: Sort a list of strings based on the 3rd char of the 2nd element
def ex11():
    def sorter(input_string: list):
        input_string.sort(key= lambda x: x[1][2])
        return input_string

    print(sorter([('abc', 'bcd'), ('abc', 'zza')]))

#ex11()

#Ex.12: Given an input list with strings words, return grouped words based on their last 2 chars
def ex12():
    def group_by_rhyme(input_list):
        word_dict = {}
        for element in input_list:
            if element[-2:] not in word_dict: word_dict.update({element[-2:]: []})
            word_dict[element[-2:]].append(element)

        result_list = []
        for word in word_dict:
            result_list.append(word_dict[word])

        return result_list

    print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))

ex12()
