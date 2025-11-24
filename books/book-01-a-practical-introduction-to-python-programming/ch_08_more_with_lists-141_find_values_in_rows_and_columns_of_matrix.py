'''
Write a program that creates a 10×10 list of random integers between 1 and 100. Then do the following:

	(a) Print the list.
	(b) Find the largest value in the third row.
	(c) Find the smallest value in the sixth column.
'''


import random


def main() -> None:
	matrix = generate_matrix(10, 10)
	largest_value_third_row = find_largest_value_in_a_row(matrix, 3)
	smallest_value_sixth_col = find_smallest_value_in_a_col(matrix, 6)
	display_result(matrix, largest_value_third_row, smallest_value_sixth_col)


def generate_matrix(rows: int, cols: int) -> list[list[int]]:
	matrix = []

	for row in range(rows):
		matrix.append([random.randint(1, 100) for _ in range(cols)])

	return matrix


def find_largest_value_in_a_row(matrix: list[list[int]], row: int) -> int:
	largest_value = matrix[row - 1][0]

	for num in matrix[row - 1]:
		if num > largest_value:
			largest_value = num

	return largest_value


def find_smallest_value_in_a_col(matrix: list[list[int]], col: int) -> int:
	smallest_value = matrix[0][col - 1]

	for row in matrix:
		value = row[col - 1]
		if value < smallest_value:
			smallest_value = value

	return smallest_value


def display_result(matrix: list[list[int]], largest_value_third_row: int, smallest_value_sixth_col: int) -> None:
	print('Matrix:')
	for row in matrix:
		print(row)

	print(f'\nThe largest value in the third row is: {largest_value_third_row}')
	print(f'\nThe smallest value in the sixth column is: {smallest_value_sixth_col}')


if __name__ == '__main__':
	main()