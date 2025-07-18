'''
Write a program that generates a random decimal number between 1 and 10 with two decimal places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.
'''


import random


def main() -> None:
	LOWER_BOUND = 1.00
	UPPER_BOUND = 10.00
	DECIMAL_PLACES = 2
	
	random_decimal_number = generate_random_decimal_number(LOWER_BOUND, UPPER_BOUND, DECIMAL_PLACES)

	print(random_decimal_number)


def generate_random_decimal_number(LOWER_BOUND: float, UPPER_BOUND: float, DECIMAL_PLACES: int) -> float:
	random_decimal_number = round(random.uniform(LOWER_BOUND, UPPER_BOUND), DECIMAL_PLACES)

	return random_decimal_number


if __name__ == '__main__':
	main()