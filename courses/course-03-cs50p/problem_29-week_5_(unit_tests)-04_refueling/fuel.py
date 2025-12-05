'''
Refueling

In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

    - "convert" expects a str in X/Y format as input, wherein each of X and Y is a positive integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.

    - "gauge" expects an int and returns a str that is:
        - "E" if that int is less than or equal to 1,
        - "F" if that int is greater than or equal to 99,
        - and "Z%" otherwise, wherein Z is that same int.


    def main():
        ...


    def convert(fraction):
        ...


    def gauge(percentage):
        ...


    if __name__ == "__main__":
        main()

Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

    pytest test_fuel.py

Hints
    - Be sure to include

        import fuel

        or

        from fuel import convert, gauge

    atop test_fuel.py so that you can call convert and gauge in your tests.

    - Take care to return, not print, an int in convert and a str in gauge. Only main should call print.

    - Note that you can raise an exception like ValueError with code like:

        raise ValueError

    - Note that you can check with pytest whether a function has raised an exception, per docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions.
'''


def main():
    user_input = get_user_input()
    remaining_fuel = convert(user_input)
    gauge_output = gauge(remaining_fuel)
    print(gauge_output)


def get_user_input() -> str:
    while True:
        try:
            user_input = input('Enter the remaining fuel fraction (e.g., "1/2"): ')
            numbers = user_input.split('/')
            if len(numbers) != 2:
                raise ValueError('Input must be in the format "numerator/denominator".')
            else:
                return user_input

        except ValueError:
            print('Invalid input. Please enter a valid fraction.')


def convert(user_input: str) -> tuple[int, int]:
    numbers = user_input.split('/')
    numerator = int(numbers[0])
    denominator = int(numbers[1])

    if denominator == 0:
        raise ZeroDivisionError('The denominator must not be zero.')
    elif numerator > denominator:
        raise ValueError('The numerator must not be greater than the denominator.')
    elif numerator < 0 or denominator < 0:
        raise ValueError('The fraction must not have negative numbers.')

    return round(numerator / denominator * 100)


def gauge(remaining_fuel: int) -> str:
    if remaining_fuel <= 1:
        return 'E'
    elif remaining_fuel >= 99:
        return 'F'
    else:
        return f'{remaining_fuel}%'


if __name__ == '__main__':
    main()