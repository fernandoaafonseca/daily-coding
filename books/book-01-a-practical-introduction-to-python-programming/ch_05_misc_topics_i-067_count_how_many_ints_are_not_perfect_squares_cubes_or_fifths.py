'''
Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect cubes, or perfect fifth powers.
'''


def main():
	higher_bound = 1000
	list_of_squares = generate_list_of_squares(higher_bound)
	list_of_cubes = generate_list_of_cubes(higher_bound)
	list_of_fifths = generate_list_of_fifths(higher_bound)
	forbidden_numbers = set(list_of_squares + list_of_cubes + list_of_fifths)
	non_perfect_numbers = find_ints_not_perfect_squares_cubes_or_fifth_powers(higher_bound, forbidden_numbers)
	display_result(higher_bound, non_perfect_numbers)


def find_ints_not_perfect_squares_cubes_or_fifth_powers(higher_bound: int, forbidden_numbers: set[int]) -> set[int]:
	all_numbers = set(i for i in range(1, higher_bound + 1))
	non_perfect_numbers = set(all_numbers - forbidden_numbers)

	return non_perfect_numbers


def generate_list_of_squares(higher_bound: int) -> list[int]:
	list_of_squares = []

	for i in range(1, higher_bound + 1):
		is_a_perfect_square = check_is_a_perfect_square(i)
		if is_a_perfect_square:
			list_of_squares.append(i)

	return list_of_squares


def generate_list_of_cubes(higher_bound: int) -> list[int]:
	list_of_cubes = []

	for i in range(1, higher_bound + 1):
		is_a_perfect_cube = check_is_a_perfect_cube(i)
		if is_a_perfect_cube:
			list_of_cubes.append(i)

	return list_of_cubes


def generate_list_of_fifths(higher_bound: int) -> list[int]:
	list_of_fifths = []

	for i in range(1, higher_bound + 1):
		is_a_perfect_fifth = check_is_a_perfect_fifth_power(i)
		if is_a_perfect_fifth:
			list_of_fifths.append(i)

	return list_of_fifths


def check_is_a_perfect_square(number: int) -> bool:
	return round(number ** (1/2)) ** 2 == number


def check_is_a_perfect_cube(number: int) -> bool:
	return round(number ** (1/3)) ** 3 == number


def check_is_a_perfect_fifth_power(number: int) -> bool:
	return round(number ** (1/5)) ** 5 == number


def display_result(higher_bound: int, non_perfect_numbers: set[int]) -> None:
	quantity_of_non_perfect_numbers = len(non_perfect_numbers)

	print(f'There are {quantity_of_non_perfect_numbers} integers from 1 to {higher_bound} that are not perfect squares, cubes, or fifth powers.')
	print(f'\nList of non_perfect_numbers: {non_perfect_numbers}')


if __name__ == '__main__':
	main()