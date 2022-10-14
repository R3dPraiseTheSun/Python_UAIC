import math
import sys

#Ex.1: GCD of multiple numbers
def ex1():
    # GCD computation from an array
    def gcd_of_array(arr, **kwargs):
        idx = kwargs.get('index', 0)
        if idx == len(arr)-1:
            return arr[idx]
        a = arr[idx]
        b = gcd_of_array(arr, index=idx+1)
        
        return math.gcd(a, b)

    var_list = []
    # Look for terminal args, if not found use keyboard input
    if (len(sys.argv) <= 1):
        while True:
            x = input("x= ")
            try:
                var_list.append(int(x))
            except ValueError:
                break
    else:
        # If terminal args are found try to convert args from string to int and append them to var_list
        try:
            for arg in sys.argv[1:]:
                var_list.append(int(arg))
        except ValueError:
            print('Error in string to int conversion, I think you\'ve put a word in that list')
            return
    print(var_list)
    print(gcd_of_array(var_list))

#ex1()

#tested commands: python .\Lab2.py 10 20 30 (expected result: [10,20,30] \n 10)
#tested commands: python .\Lab2.py 10 12 14 (expected result: [10,12,14] \n 2)

#Ex.2: Find vowels in string
def ex2():
    def find_vowels(string):
        #define a result tuple to include found vowels in order and vowel count
        vowel_found = []
        vowel_count = 0

        #define vowel list
        vowel_list = {'a','e','i','o','u'}

        for index in range(0,len(string)):
            if string[index] in vowel_list:
                vowel_found.append(string[index])
                vowel_count = vowel_count + 1
        
        return (vowel_found, vowel_count)

    input_string = ''
    if (len(sys.argv) <= 1):
        input_string = input("input: ")
    elif (len(sys.argv) == 1):
        # If terminal args are found try to convert args from string to int and append them to var_list
        input_string = sys.argv[1]
    else:
        for arg in sys.argv[1:]: input_string = input_string + arg
    print(find_vowels(input_string))

#ex2()

#tested commands: python .\Lab2.py input string (expected result: (['i', 'u', 'i'], 3))
#tested commands: python .\Lab2.py uluai benglades (['u', 'u', 'a', 'i', 'e', 'a', 'e'], 7)

#Ex.3: Find a substring in a bigger string and count how many times it appears
def ex3():
    def substring_search(substring: str, string_to_check: str) -> int:
        """ 
        # classinc method
        # Find substring in the bigger string, if found then slice the bigger string and search
        # again for the substring until string is empty

        occurances = 0
        while string_to_check:
            if string_to_check.find(substring) != -1:
                string_to_check = string_to_check[string_to_check.find(substring)+1:]
                occurances = occurances + 1
            else: break
        return occurances
        """
        # split returns the list of the remaining string_to_check without the substring 
        # and it has separate entries in the list for each occurance of the substring
        # if we get the length of the split and remove the first entry we are left
        # with the number of substring instances

        return len(string_to_check.split(substring)) - 1

    substring = ''
    string_to_check = ''
    if (len(sys.argv) < 3):
        print('\nNot enough args!\n')
        substring = input('substring: ')
        string_to_check = input('string to check: ')
    elif (len(sys.argv) == 3):
        substring = sys.argv[1]
        string_to_check = sys.argv[2]
    else:
        substring = sys.argv[1]
        for arg in sys.argv[2:]:
            string_to_check = string_to_check + ' ' + arg

    print(substring_search(substring, string_to_check))

#ex3()

# tested commands: python .\Lab2.py lad lets go drinking lads (expected result: 1)
# tested commands: python .\Lab2.py ab abasssabaafabababffsafggasabab (expected result: 7)

#Ex.4: Convert UpperCamelCase into lower_snake_case
def ex4():
    # save every uppercase letter in a dictionary (because a list would repeat letters)
    # and then replace every uppercase letter with a '_' 
    # before the letter and then make the whole string lowercase
    def convert(string: str) -> str:
        letters_dict = {char for char in string[1:] if char.isupper()}
        for letter in letters_dict:
            string = string.replace(letter, '_'+letter)
        return string.lower()

    input_string = ''
    if (len(sys.argv) <= 1):
        input_string = input("input: ")
        print(convert(input_string))
    else:
        for arg in sys.argv[1:]: print(convert(arg))

#ex4()

# tested commands: python .\Lab2.py AlaMamaBaNaNa (expected result: ala_mama_ba_na_na)
# tested commands: python .\Lab2.py AlaMamaBaNaNa BaNana (expected result: ala_mama_ba_na_na \n ba_nana)

#Ex.5: spiral matrix
def ex5():
    def read_matrix(matrix: list[list[str]]):
        # read matrix border while saving the inner matrix for reccursive use

        spiral_order = []
        new_matrix = []
        for index in range(0,len(matrix[0])):
            spiral_order.append(matrix[0][index])
        for line in matrix[1:len(matrix)-1]:
            spiral_order.append(line[len(line)-1])
            new_matrix.append([char for char in line[1:len(line)-1]])
        matrix[len(matrix)-1].reverse()
        for index in range(0,len(matrix[len(matrix)-1])):
            spiral_order.append(matrix[len(matrix)-1][index])
        for line in matrix[len(matrix)-2:0:-1]:
            spiral_order.append(line[0])

        if new_matrix.__len__() > 0:
            spiral_order2 = read_matrix(new_matrix)
            for char in spiral_order2:
                spiral_order.append(char)
        return spiral_order

    matrix = [
        ['f','i','r','s'],
        ['n','_','l','t'],
        ['o','b','a','_'],
        ['h','t','y','p']
        ]

    matrix_order_list = read_matrix(matrix)
    rez = ''
    for char in matrix_order_list:
        rez = rez + char
    print(rez)

#ex5()

# (input already defined) expected result: first_python_lab

#Ex.6: function that validates if a number is palindrome
def ex6():
    def is_palindrome(number):
        if type(number) != str: number = str(number)
        if number == number[::-1]: return True
        return False

    if (len(sys.argv) <= 1):
        input_string = input("input: ")
        print(is_palindrome(input_string))
    else:
        for arg in sys.argv[1:]: print(is_palindrome(arg))

#ex6()

# tested commands: python .\Lab2.py 1001 1002 (expected result: True \n False)

#Ex.7: extract number from a string (only the first one)
def ex7():
    def exctract_first_number(string):
        number_list = ['0','1','2','3','4','5','6','7','8','9']
        for index in range(len(string)):
            if string[index] in number_list:
                for j_index in range(index, len(string)):
                    if string[j_index] not in number_list: return string[index:j_index]
        return False

    if (len(sys.argv) <= 1):
        input_string = input("input: ")
        print(exctract_first_number(input_string))
    else:
        for arg in sys.argv[1:]: print(exctract_first_number(arg))

#ex7()

# tested commands: python .\Lab2.py 'An apple is 123 USD and orange is 321 USD' (expected result: 123)
# tested commands: python .\Lab2.py abc123def (expected result: 123)

#Ex.8: Find out how many '1'.s are in a number transformed into its binary form
def ex8():
    def bits(number: int):
        return number.bit_count()

    if (len(sys.argv) <= 1):
        input_string = int(input("input: "))
        print(bits(input_string))
    else:
        for arg in sys.argv[1:]: print(bits(int(arg)))

#ex8()

# tested commands: python .\Lab2.py 24 (expected result: 2)

#Ex.9: Find the most common letter in a string
def ex9():
    def common_letter(string):
        string = string.lower()
        letters_dict = {char for char in string if char != ' '}
        letter_count = []
        for letter in letters_dict:
            letter_count.append({'letter': letter, 'count': string.count(letter)})

        return sorted(letter_count, key=lambda i: i['count'], reverse=True)[0]
        
    if (len(sys.argv) <= 1):
        input_string = input("input: ")
        print(common_letter(input_string))
    else:
        for arg in sys.argv[1:]: print(common_letter(arg))

#ex9()

# tested commands: python .\Lab2.py 'An apple is not a Tomato' (expected result: {'letter': 'a', 'count': 4})

#Ex.10: Count how many words are in a string
def ex10():
    def find_words(string: str) -> int:
        return string.split().__len__()

    if (len(sys.argv) <= 1):
        input_string = input("input: ")
        print(find_words(input_string))
    else:
        for arg in sys.argv[1:]: print(find_words(arg))

#ex10()

# tested commands: python .\Lab2.py 'An apple is not a Tomato' (expected result: 6)
