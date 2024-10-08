'''
Factorial of a Number
Write a function that calculates the factorial of a given number. The factorial of a number n is the product of all the integers from 1 to n. For example, the factorial of 5 (5!) is 5 x 4 x 3 x 2 x 1 = 120.
'''


def main():
    display_title()
    n = get_num()
    list_of_nums = create_list_of_nums(n)
    result = factorial(n)
    display_result(n, list_of_nums, result)


def display_title():
    print('=' * 24)
    print('  Factorial Calculator  ')
    print('=' * 24)
    print()


def get_num():
    while True:
        try:
            n = int(input('Please enter a positive integer number: '))
            if n >= 0:
                break
            else:
                print()
                print('The number must be positive! Try again.')
                print()
        except:
            print()
            print('Please enter a valid positive integer number! Try again!')
            print()

    return n


def factorial(n):
    result = n

    if n != 0:
        for i in range(n-1, 1, -1):
            result *= i
    else:
        result = 1

    return result


def create_list_of_nums(n):
    list_of_nums = []

    if n != 0:
        for i in range(n, 1, -1):
            list_of_nums.append(i)
    else:
        list_of_nums = [0]

    return list_of_nums


def display_result(n, list_of_nums, result):
    print()
    print('-' * 32)
    print(f'The factorial of {n} is: ')
    print(f'{n}! = ', end='')

    if n != 0:
        # Print the numbers with 'x' between them, but not after the last one
        for i, num in enumerate(list_of_nums):
            if i < len(list_of_nums) - 1:
                print(f'{num} x ', end='')
            else:
                print(f'{num} =', end='')

    print(f' {result}')
    print('-' * 32)
    print()


if __name__ == '__main__':
    main()


# Test:
print(factorial(0) == 1)
print(factorial(1) == 1)
print(factorial(2) == 2)
print(factorial(5) == 120)
print(factorial(7) == 5040)
print(factorial(11) == 39916800)
