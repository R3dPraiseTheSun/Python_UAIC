from functools import reduce
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