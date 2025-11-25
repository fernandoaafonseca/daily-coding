'''
Write a program that checks to see if a 4 × 4 list is a magic square. In a magic square, every row, column, and the two diagonals add up to the same value.
'''


def main() -> None:
	matrix = [
		[16, 2, 3, 13],
		[5, 11, 10, 8],
		[9, 7, 6, 12],
		[4, 14, 15, 1]
		]
	is_magic_square = check_is_magic_square(matrix)
	display_result(matrix, is_magic_square)


def check_is_magic_square(matrix: list[list[int]]) -> bool:
	# Base sum = sum of the first row
	target = sum_row(matrix, 0)

	if not check_rows(matrix, target):
		return False

	if not check_cols(matrix, target):
		return False

	if not check_diagonals(matrix, target):
		return False

	return True


def check_rows(matrix: list[list[int]], target: int) -> bool:
	for row_index in range(len(matrix)):
		if sum_row(matrix, row_index) != target:
			return False
	return True


def check_cols(matrix: list[list[int]], target: int) -> bool:
	for col_index in range(len(matrix[0])):
		if sum_col(matrix, col_index) != target:
			return False
	return True


def check_diagonals(matrix: list[list[int]], target: int) -> bool:
	# Nain diagonal
	total_main = 0
	for i in range(len(matrix)):
		total_main += matrix[i][i]

	if total_main != target:
		return False

	# Secondary diagonal
	total_secondary = 0
	size = len(matrix)
	for i in range(size):
		total_secondary += matrix[i][size - 1 - i]

	if total_secondary != target:
		return False

	return True


def sum_row(matrix: list[list[int]], row: int) -> int:
	total = 0
	for num in matrix[row]:
		total += num
	return total


def sum_col(matrix: list[list[int]], col: int) -> int:
	total = 0
	for row in matrix:
		total += row[col]
	return total


def display_result(matrix: list[list[int]], is_magic_square: bool) -> None:
	print('Matrix:')
	for row in matrix:
		print(row)
	print()

	if is_magic_square:
		print('This is a magic square.')
	else:
		print('This is NOT a magic square.')


if __name__ == '__main__':
    main()
