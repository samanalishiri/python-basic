# Saman Alishiri samanalishiri@gmail.com


def print_range(lower, upper):
    if upper < lower:
        print('invalid range')
        return

    for number in range(lower, upper + 1):
        print(number, end=' ')


if __name__ == '__main__':
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    print_range(lower, upper)
