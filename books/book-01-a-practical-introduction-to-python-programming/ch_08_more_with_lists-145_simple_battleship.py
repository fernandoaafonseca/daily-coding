'''
The following is useful as part of a program to play Battleship. Suppose you have a 5 × 5 list that consists of zeroes and ones. Ask the user to enter a row and a column. If the entry in the list at that row and column is a one, the program should print Hit and otherwise it should print Miss.
'''


import os, random


def main() -> None:
	matrix_board = generate_matrix(5, 5)
	row_guess, col_guess = get_row_and_column(5, 5)
	user_hit = check_hit_or_miss(matrix_board, row_guess, col_guess)
	display_result(matrix_board, row_guess, col_guess, user_hit)


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def generate_matrix(rows: int, cols: int) -> list[list[int]]:
	matrix = []

	for row in range(rows):
		matrix.append([random.randint(0, 1) for _ in range(cols)])

	return matrix


def get_row_and_column(rows: int, cols: int) -> tuple[int, int]:
	possible_rows = [row + 1 for row in range(rows)]
	possible_cols = [col + 1 for col in range(cols)]

	while True:
		try:
			clear_terminal()

			row_and_col = str(input(f'Enter a row ({possible_rows}) and a column ({possible_cols}) separated by commas (like "1, 3"): '))
			# Generates a list of "ints" splitting the string by "commas"
			row_and_col = [int(item) for item in row_and_col.split(',')]

			if len(row_and_col) != 2:
				raise ValueError

			row_guess = row_and_col[0]
			col_guess = row_and_col[1]

			are_all_nums_valid = row_guess in possible_rows and col_guess in possible_cols

			if are_all_nums_valid:
				return row_guess, col_guess
			else:
				raise ValueError

		except ValueError:
			print(f'\nPlease only enter two integers - a row ({possible_rows}) and a column ({possible_cols}) - separated by commas.')
			press_any_key_to_continue()


def check_hit_or_miss(matrix_board: list[list[int]], row_guess: int, col_guess: int) -> bool:
	# It returns the index of the list, that is, row or column "1" becomes "0"
	row_guess = row_guess - 1
	col_guess = col_guess - 1
	user_guess = matrix_board[row_guess][col_guess]

	return user_guess == 1


def display_result(matrix_board: list[list[int]], row_guess: int, col_guess: int, user_hit: bool) -> None:
	press_any_key_to_continue()
	clear_terminal()

	print('SIMPLE BATTLESHIP BOARD:')
	for row in matrix_board:
		print(row)

	print(f'\nYour row guess: {row_guess}')
	print(f'Your col guess: {col_guess}')

	if user_hit:
		print(f'\nHIT!')
	else:
		print(f'\nMISS!')


if __name__ == '__main__':
	main()