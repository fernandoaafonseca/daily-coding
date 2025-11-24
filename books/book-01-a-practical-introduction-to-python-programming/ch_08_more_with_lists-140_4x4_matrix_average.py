'''
Write a program that finds the average of all of the entries in a 4 × 4 list of integers.
'''


def main() -> None:
	matrix = [
	[3, 8, 2, 5],
	[7, 1, 9, 4],
	[6, 3, 2, 8],
	[5, 5, 7, 1]
	]
	average = matrix_average(matrix)
	display_result(matrix, average)


def matrix_average(matrix: list[list[int]]) -> float:
	total = 0
	count = 0

	for row in matrix:
		for num in row:
			total += num
			count += 1

	return total / count


def display_result(matrix: list[list[int]], average: float) -> None:
	print('Matrix:')
	print(matrix)
	print(f'\nThe average of the matrix is: {average:.2f}')


if __name__ == '__main__':
	main()