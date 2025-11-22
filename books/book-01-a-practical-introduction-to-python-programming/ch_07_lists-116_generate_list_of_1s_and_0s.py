'''
Using a for loop, create the list below, which consists of ones separated by increasingly many zeroes. The last two ones in the list should be separated by ten zeroes.

	[1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, ...]
'''


def main() -> None:
	ones_and_zeros = generate_list_of_ones_and_zeros()
	display_result(ones_and_zeros)


def generate_list_of_ones_and_zeros() -> list[int]:
	ones_and_zeros = []

	for i in range(11):
		ones_and_zeros.append(1)

		if i > 0:
			for _ in range(i):
				ones_and_zeros.append(0)

	ones_and_zeros.append(1)

	return ones_and_zeros


def display_result(ones_and_zeros: list[int]) -> None:
	print(ones_and_zeros)


if __name__ == '__main__':
	main()