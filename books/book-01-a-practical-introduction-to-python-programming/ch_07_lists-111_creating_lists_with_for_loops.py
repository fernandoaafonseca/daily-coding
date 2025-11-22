'''
Create the following lists using a for loop.

	(a) A list consisting of the integers 0 through 49
	(b) A list containing the squares of the integers 1 through 50.
	(c) The list ['a', 'bb', 'ccc', 'dddd', ...] that ends with 26 copies of the letter z.
'''


import string


ALPHABET = string.ascii_lowercase


def main() -> None:
	list_of_ints = generate_list_of_ints()
	list_of_squares = generate_list_of_squares()
	list_of_letters = generate_list_of_letters(ALPHABET)
	display_result(list_of_ints, list_of_squares, list_of_letters)


def generate_list_of_ints() -> list[int]:
	return [num for num in range(0, 50)]


def generate_list_of_squares() -> list[int]:
	return [num**2 for num in range(1, 51)]


def generate_list_of_letters(ALPHABET) -> list[str]:
	list_of_letters = []

	for index, letter in enumerate(ALPHABET):
		list_of_letters.append(letter * (index + 1))

	return list_of_letters


def display_result(list_of_ints: list[int], list_of_squares: list[int], list_of_letters: list[str]) -> None:
	print(f'List of integers: \n{list_of_ints}')
	print(f'\nList of squares: \n{list_of_squares}')
	print(f'\nList of letters: \n{list_of_letters}')


if __name__ == '__main__':
	main()