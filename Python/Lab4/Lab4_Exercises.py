import os
import sys
import Lab4_Functions as l4

print("Ex1:")
print(l4.ex_1(os.getcwd()+ '\\Test_Directory'))

print("\nEx2: See New Text Document(2).txt from Test_Directory")
l4.ex_2(
    os.getcwd() + '\\Test_Directory',
    os.getcwd() + '\\Test_Directory\\New Text Document(2).txt'
    )

print("\nEx.3: Folder input")
print(l4.ex_3(os.getcwd()))

print("\nEx.3: File input")
print(l4.ex_3(os.getcwd() + '/Test_Directory/New Text Document(2).txt'))

if len(sys.argv) > 1:
    print("\nEx4:")
    print(l4.ex_4())
else: print("\nEx4: argument required!")

print("\nEx5: Folder input")
print(l4.ex_5(os.getcwd(), 'ananas'))
print("\nEx5: File input")
print(l4.ex_5(os.getcwd() + '/Test_Directory/New Text Document(2).txt', 'ananas'))

print("\nEx6:")
l4.ex_6(os.getcwd() + '/Test_Dire', 'ananas', l4.error_callback)

print("\nEx7")
print(l4.ex_7(os.getcwd() + '/Test_Directory/New Text Document(2).txt'))

print("\nEx8")
print(l4.ex_8(os.getcwd()))
