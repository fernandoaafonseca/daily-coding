'''
Using a for loop, create the list below, which consists of ones separated by increasingly many zeroes. The last two ones in the list should be separated by ten zeroes.

	[1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, ...]
'''


def main():
	ones_and_zeroes = generate_list_of_ones_and_zeroes()
	display_result(ones_and_zeroes)


def generate_list_of_ones_and_zeroes() -> list[int]:
	ones_and_zeroes = []

	for i in range(11):
		ones_and_zeroes.append(1)

		if i > 0:
			for _ in range(i):
				ones_and_zeroes.append(0)

	ones_and_zeroes.append(1)

	return ones_and_zeroes


def display_result(ones_and_zeroes: list[int]) -> None:
	print(ones_and_zeroes)


if __name__ == '__main__':
	main()