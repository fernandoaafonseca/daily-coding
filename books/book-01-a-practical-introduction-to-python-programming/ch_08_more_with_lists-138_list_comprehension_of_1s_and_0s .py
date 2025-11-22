'''
Use a list comprehension to create the list below, which consists of ones separated by increasingly many zeroes. The last two ones in the list should be separated by ten zeroes.

	[1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, ...]
'''


def main() -> None:
	ones_and_zeros = [j for i in range(11) for j in ([1] if i == 0 else [*([0]*i), 1])]
	display_result(ones_and_zeros)


def display_result(ones_and_zeros: list[int]) -> None:
	print(ones_and_zeros)


if __name__ == '__main__':
	main()