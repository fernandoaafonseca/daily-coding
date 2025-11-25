'''
Write a program that creates and prints an 8 × 8 list whose entries alternate between 1 and 2 in a checkerboard pattern, starting with 1 in the upper left corner.
'''


def main() -> None:
	matrix = generate_checkerboard_matrix(8, 8)
	display_result(matrix)


def generate_checkerboard_matrix(rows: int, cols: int) -> list[list[int]]:
	matrix = []

	for row in range(rows):
		new_row = []
		for col in range(cols):
			if (row + col) % 2 == 0:
				new_row.append(1)
			else:
				new_row.append(2)
		matrix.append(new_row)

	return matrix


def display_result(matrix: list[list[int]]) -> None:
	print('Checkerboard matrix:')
	for row in matrix:
		print(row)


if __name__ == '__main__':
	main()