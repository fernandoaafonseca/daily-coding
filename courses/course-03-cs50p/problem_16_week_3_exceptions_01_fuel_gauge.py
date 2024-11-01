'''
Fuel Gauge

Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split.
Note that you can handle two exceptions separately with code like:
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...
Or you can handle two exceptions together with code like:

try:
    ...
except (ValueError, ZeroDivisionError):
    ...
'''


def main():
    while True:
        try:
            user_input = get_user_input()
            numerator, denominator = get_numerator_denominator(user_input)
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction.")
            continue
    remaining_fuel = calculate_remaining_fuel(numerator, denominator)
    print(generate_result(remaining_fuel))


def get_user_input() -> str:
    return input('Enter the remaining fuel fraction (e.g., "1/2"): ')


def get_numerator_denominator(user_input: str) -> tuple[int, int]:
    numbers = user_input.split('/')
    if len(numbers) != 2:
        raise ValueError(
            "Input must be in the format 'numerator/denominator'.")

    numerator = int(numbers[0])
    denominator = int(numbers[1])

    if denominator == 0:
        raise ZeroDivisionError("The denominator must not be zero.")

    elif numerator > denominator:
        raise ValueError(
            "The numerator must not be greater than the denominator.")

    return numerator, denominator


def calculate_remaining_fuel(numerator: int, denominator: int) -> str | int:
    remaining_fuel = round(numerator / denominator * 100)
    if remaining_fuel <= 1:
        return "E"
    elif remaining_fuel >= 99:
        return "F"
    return remaining_fuel


def generate_result(remaining_fuel: str | int) -> str:
    if isinstance(remaining_fuel, int):
        return f'{remaining_fuel}%'
    else:
        return f'{remaining_fuel}'


'''
if __name__ == '__main__':
    main()
'''

# Test:
numerator, denominator = get_numerator_denominator('3/4')
remaining_fuel = calculate_remaining_fuel(numerator, denominator)
result = generate_result(remaining_fuel)
print(result == '75%')

numerator, denominator = get_numerator_denominator('1/3')
remaining_fuel = calculate_remaining_fuel(numerator, denominator)
result = generate_result(remaining_fuel)
print(result == '33%')

numerator, denominator = get_numerator_denominator('2/3')
remaining_fuel = calculate_remaining_fuel(numerator, denominator)
result = generate_result(remaining_fuel)
print(result == '67%')

numerator, denominator = get_numerator_denominator('0/100')
remaining_fuel = calculate_remaining_fuel(numerator, denominator)
result = generate_result(remaining_fuel)
print(result == 'E')

numerator, denominator = get_numerator_denominator('1/100')
remaining_fuel = calculate_remaining_fuel(numerator, denominator)
result = generate_result(remaining_fuel)
print(result == 'E')

numerator, denominator = get_numerator_denominator('100/100')
remaining_fuel = calculate_remaining_fuel(numerator, denominator)
result = generate_result(remaining_fuel)
print(result == 'F')

numerator, denominator = get_numerator_denominator('99/100')
remaining_fuel = calculate_remaining_fuel(numerator, denominator)
result = generate_result(remaining_fuel)
print(result == 'F')

try:
    get_numerator_denominator('100/0')
except Exception as e:
    print(type(e) == ZeroDivisionError)

try:
    get_numerator_denominator('3/4')
except Exception as e:
    print(type(e) == ValueError)

try:
    get_numerator_denominator('1.5/4')
except Exception as e:
    print(type(e) == ValueError)

try:
    get_numerator_denominator('3/5.5')
except Exception as e:
    print(type(e) == ValueError)

try:
    get_numerator_denominator('10/3')
except Exception as e:
    print(type(e) == ValueError)

try:
    get_numerator_denominator('three/four')
except Exception as e:
    print(type(e) == ValueError)

try:
    get_numerator_denominator('5-10')
except Exception as e:
    print(type(e) == ValueError)
