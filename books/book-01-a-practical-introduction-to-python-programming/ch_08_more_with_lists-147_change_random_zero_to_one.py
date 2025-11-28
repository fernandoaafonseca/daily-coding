'''
The following is useful in implementing computer players in a number of different games. Write a program that creates a 5 × 5 list consisting of zeroes and ones. Your program should then pick a random location in the list that contains a zero and change it to a one. If all the entries are one, the program should say so. [Hint: one way to do this is to create a new list whose items are the coordinates of all the ones in the list and use the choice method to randomly select one. Use a two-element list to represent a set of coordinates.]
'''


import copy
import os
import random


BOARD_ROWS = 5
BOARD_COLS = 5


def main() -> None:
	matrix = generate_binary_matrix()
	zero_positions = get_zero_positions(matrix)

	display_matrix('INITIAL MATRIX', matrix)

	if not zero_positions:
		print('\nAll entries are already 1.')
	else:
		new_matrix = flip_random_zero_to_one(matrix, zero_positions)

	display_matrix('UPDATED MATRIX', new_matrix)


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def generate_binary_matrix() -> list[list[int]]:
	'''
	Generates a BOARD_ROWS×BOARD_COLS matrix containing randomly chosen 0s and 1s.
	'''
	return [[random.choice([0, 1]) for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]


def get_zero_positions(matrix: list[list[int]]) -> list[list[int]]:
	'''
	Returns a list of [row, col] pairs identifying every cell that contains 0.
	'''
	return [[row, col] for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if matrix[row][col] == 0]


def flip_random_zero_to_one(matrix: list[list[int]], positions: list[list[int]]) -> None:
	'''
	Randomly selects one of the zero positions and flips it to 1.
	'''
	row, col = random.choice(positions)

	# Creates a completely independent copy of the list and all its nested mutable objects. Changes to the deep copy will not affect the original list, even for nested elements
	new_matrix = copy.deepcopy(matrix)
	new_matrix[row][col] = 1

	return new_matrix


def display_matrix(title: str, matrix: list[list[int]]) -> None:
	'''
	Clears the terminal and prints a matrix with a title header.
	'''
	print('=' * 14)
	print(title)
	print('=' * 14)

	for row in matrix:
		print(' '.join(str(x) for x in row))


if __name__ == '__main__':
    main()