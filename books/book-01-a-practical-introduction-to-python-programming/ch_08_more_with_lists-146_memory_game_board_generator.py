'''
This exercise is useful in creating a Memory game. Randomly generate a 6 × 6 list of assorted characters such that there are exactly two of each character. An example is shown below.

    @ 5 # A A !
    5 0 b @ $ z
    $ N x ! N z
    0 - + # b :
    - : + c c x
'''


import os, random, string


# At least one of the two values (rows or columns) MUST be even, since even * even = even, just as even * odd = even
# "BOARD_ROWS * BOARD_COLS" must not exceed "len(CHARS_POOL) * 2"
BOARD_ROWS = 6
BOARD_COLS = 6
LOWERCASE_LETTERS = string.ascii_lowercase
UPPERCASE_LETTERS = string.ascii_uppercase
DIGITS = string.digits
# Remove problematic punctuation characters (quotes, backslashes, etc.) that could interfere with printing or string interpretation.
PUNCTUATION_CHARS_TO_REMOVE = '"\'\\()_`|'
PUNCTUATION_MARKS= ''.join(char for char in string.punctuation if char not in PUNCTUATION_CHARS_TO_REMOVE)
CHARS_POOL = LOWERCASE_LETTERS + UPPERCASE_LETTERS + DIGITS + PUNCTUATION_MARKS


def main() -> None:
	game_board = generate_game_board()
	display_result(game_board)


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def generate_game_board() -> list[list[str]]:
	selected_chars = select_characters()
	paired_chars = create_pairs(selected_chars)
	shuffled_chars = shuffle_pairs(paired_chars)
	game_board = create_board(shuffled_chars)

	return game_board


def select_characters() -> list[str]:
	'''
	Randomly selects the exact number of unique characters needed for the board.
	Uses random.sample() to ensure all chosen characters are distinct.
    '''
	num_of_chars = int(BOARD_ROWS * BOARD_COLS / 2)
	return random.sample(CHARS_POOL, num_of_chars)


def create_pairs(selected_chars: list[str]) -> list[str]:
	'''
	Duplicate each selected character so that every symbol appears exactly twice.
	'''
	return [item for item in selected_chars for _ in range(2)]


def shuffle_pairs(paired_chars: list[str]) -> list[str]:
	'''
	Shuffles the list of paired characters in-place, ensuring random placement of each pair on the final board.
    '''
	random.shuffle(paired_chars)
	return paired_chars


def create_board(shuffled_chars: list[str]) -> list[list[str]]:
	'''
	Builds the 6×6 board by sequentially filling each row with characters from the shuffled list. Produces a 2D list representing the game grid.
	'''
	board = []
	current_char_index = 0

	for _ in range(BOARD_ROWS):
		# Fill the BOARD_ROWSxBOARD_COLS board row by row using characters from the shuffled list
		new_row = []
		for _ in range(BOARD_COLS):
			new_row.append(shuffled_chars[current_char_index])
			# "current_char_index" tracks our position as we consume the flat list
			current_char_index += 1
		board.append(new_row)

	return board


def display_result(game_board: list[list[str]]) -> None:
	'''
	Clears the terminal and prints the final memory board in a human-readable grid format.
	'''
	clear_terminal()

	print('MEMORY GAME BOARD')
	print()

	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			print(game_board[row][col], end=' ')
		print()


if __name__ == '__main__':
	main()