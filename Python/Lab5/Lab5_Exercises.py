import Lab5_Functions as lb5

print('Ex2: Anonymous_function: ',lb5.anonymous_function(1, 2, c=3, d=4))
print('Ex2: Traditional function', lb5.Ex2(1, 2, c=3, d=4))

print('Ex3: Traditional function', lb5.Ex3('Programming in Python is fun'))
print('Ex3: Anonymous function: ',lb5.anonymous_ex3('Programming in Python is fun'))
print('Ex3: Anonymous function v2: ',lb5.anonymous_ex3_v2('Programming in Python is fun'))

print('Ex4:', lb5.Ex4(
    {1: 2, 3: 4, 5: 6}, 
    {'a': 5, 'b': 7, 'c': 'e'}, 
    {2: 3}, 
    [1, 2, 3],
    {'abc': 4, 'def': 5},
    3764,
    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    test={1: 1, 'test': True}
))

print('Ex5: anonymous:', lb5.anon_ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
print('Ex6: anonymous:', lb5.anon_ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

print(
    'Ex7:',
    lb5.process(
        filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= lb5.sum_digits(item) <= 20],
        limit=2,
        offset=2
    ))

print('Ex8: a)')
augmented_multiply_by_two = lb5.print_arguments(lb5.multiply_by_two)
x = augmented_multiply_by_two(10)

augmented_add_numbers = lb5.print_arguments(lb5.add_numbers)
x = augmented_add_numbers(3, 4)

print('Ex8: b)')
augmented_multiply_by_three = lb5.multiply_output(lb5.multiply_by_three)
x = augmented_multiply_by_three(10)

print('Ex8: c)')
decorated_function = lb5.augment_function(lb5.add_numbers, [lb5.print_arguments, lb5.multiply_output]) 
x = decorated_function(3, 4)
