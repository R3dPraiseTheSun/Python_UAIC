import sys

#Ex2: Anonymous function:
anonymous_function = lambda *args, **kwargs: sum(kwargs.values())

#Ex2: Traditional function:
def Ex2(*args, **kwargs):
    return sum(kwargs.values())

#Ex3: v1
def Ex3(input_string):
    return [el for el in input_string if el in "aeiou"]

#Ex3: (anonymous) v2:
anonymous_ex3 = lambda input_string: list(filter(lambda x: x in "aeiou", input_string))

#Ex3: (anonymous) v3:
anonymous_ex3_v2 = lambda input_string: [el for el in input_string if el in "aeiou"]

#Ex4:
def Ex4(*args, **kwargs) -> list:
    return [
               arg for arg in args
               if isinstance(arg, dict) and len(arg) >= 2 and max([0] + [len(key) for key in arg.keys() if type(key) == str]) >= 3
           ] + [
               kwarg for kwarg in kwargs.values()
               if isinstance(kwarg, dict) and len(kwarg) >= 2 and max([0] + [len(key) for key in kwarg.keys() if type(key) == str]) >= 3
           ]

#Ex5: anonymous
anon_ex5 = lambda input_list: [el for el in input_list if isinstance(el, (int, float))]

#Ex6:
anon_ex6 = lambda input_list: list(zip([el for el in input_list if not el%2],[el for el in input_list if el%2]))

#Ex7:
def get_fibonacci_1000():
    fibonacci_list = []
    def fibonacci_1000(**kwargs):
        a = kwargs.get('a', 0)
        b = kwargs.get('b', 1)
        current_limit = kwargs.get('current_limit', 0)

        if current_limit >= 1000:
            return fibonacci_list
        fibonacci_list.append(a)
        return(fibonacci_1000(a=b, b=a+b, current_limit= current_limit+1))
    return fibonacci_1000()

def sum_digits(x):
    return sum(map(int, str(x)))

#Set recursion because python has ~1000 limit by default and I require more
sys.setrecursionlimit(1005)

def process(**kwargs):
    fibonacci_sequence = get_fibonacci_1000()
    try:
        if "filters" in kwargs.keys():
            for f in kwargs["filters"]:
                fibonacci_sequence = list(filter(f, fibonacci_sequence))
        if "offset" in kwargs.keys():
            fibonacci_sequence = fibonacci_sequence[kwargs["offset"]:]
        if "limit" in kwargs.keys():
            fibonacci_sequence = fibonacci_sequence[:kwargs["limit"]]
    except Exception as e:
        print("Error at processing:", e)
    return fibonacci_sequence

#Ex8: a)
def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

def print_arguments(function):
    if function.__name__ == 'multiply_by_two':
        result_function = lambda *args, **kwargs: print(f'Arguments are: {args}, {kwargs} and will return {function(args[0])}')
    else:
        result_function = lambda *args, **kwargs: print(f'Arguments are: {args}, {kwargs} and will return {function(args[0], args[1])}')
    return result_function

#Ex8: b)
def multiply_by_three(x):
    return x * 3

def multiply_output(function):
    return lambda *args: print(2*function(args[0]))

#Ex8: c)
def augment_function(function, decorators):
    for decorator in decorators:
        result_function = lambda *args, **kwargs: print(f'Arguments are: {args}, {kwargs} and will return {decorator(function)}')
    return result_function

summ = lambda a,b:a+b
prod = lambda a,b:a*b
pow = lambda a,b:a**b

#Ex9:
def f9(**kwargs):
    tuples_list = kwargs.get('pairs')
    result_list = []
    for tuple in tuples_list:
        res_dict = {
            'sum': summ(tuple[0], tuple[1]),
            'prod': prod(tuple[0], tuple[1]),
            'pow': pow(tuple[0], tuple[1])
        }
        result_list.append(res_dict)
    return result_list
