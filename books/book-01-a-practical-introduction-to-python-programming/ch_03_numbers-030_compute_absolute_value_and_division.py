'''
Write a program that asks the user to enter two numbers, x and y , and computes (|x + y|) / (x + y).
'''


def main() -> None:
	x = int(input('Enter the value of X: '))
	y = int(input('Enter the value of Y: '))

	result = compute_sum_abs_values_divided_by_sum_of_values(x, y)
	print(f'(|x + y|) / (x + y) = {result}')


def compute_sum_abs_values_divided_by_sum_of_values(x: int, y: int) -> float:
	result = (abs(x) + abs(y)) / (x + y)

	return result


if __name__ == '__main__':
	main()