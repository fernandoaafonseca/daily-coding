'''
Find the sum of all even elements of the Fibonacci sequence with values less than 1,000,000 (1 million).

Present the solution in the form of a function called "calculate()". In response, call "calculate()" function and print the result to the console.

Expected result: 1,089,154.
'''


def main():
    upper_bound = 100
    expected_result = 1089154

    fibonacci_even_numbers = even_numbers_fibonacci_sequence(upper_bound)
    sum_even_elements = calculate(fibonacci_even_numbers)

    print(
        f'Sum of all even elements of the Fibonacci sequence with values less than {upper_bound}: {sum_even_elements}.')

    print(check_result(sum_even_elements, expected_result))


def even_numbers_fibonacci_sequence(upper_bound: int) -> list[int]:
    fibonacci_even_numbers = []
    last_number = 0
    current_number = 1

    while current_number < upper_bound:
        next_number = last_number + current_number

        if next_number % 2 == 0 and next_number <= upper_bound:
            fibonacci_even_numbers.append(next_number)

        last_number = current_number
        current_number = next_number
        

    return fibonacci_even_numbers


def calculate(fibonacci_even_numbers: list[int]) -> int:
    sum_even_elements = 0
    for num in fibonacci_even_numbers:
        sum_even_elements += num

    return sum_even_elements


def check_result(sum_even_elements: int, expected_result: int) -> bool:
    return sum_even_elements == expected_result


if __name__ == '__main__':
    main()
