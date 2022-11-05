from utils import process_items


if __name__ == "__main__":
    print('Input a number and I will return the least prime number greater than your number\nOr input q to quit')
    while True:
        user_input = input("Input number: ")
        if user_input == "q":
            break
        try:
            x = int(user_input)
            print(process_items(x))
        except TypeError as e:
            print("Input is not integer", e)
        except Exception as e:
            print("Other error", e)
    print('Thank you, come again')