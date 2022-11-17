def is_prime(x: int) -> bool:
    if x < 2 or x != 2 and x % 2 == 0 or x != 3 and x % 3 == 0:
        return False
    for d in range(5, 1 + int(x ** 0.5), 6):
        if x % d == 0 or x % (d + 2) == 0:
            return False
    return True


def process_items(x: int) -> int:
    while not is_prime(x + 1):
        x += 1
    return x + 1

if __name__ == "__main__":
    print(process_items(int(input('Give number: '))))