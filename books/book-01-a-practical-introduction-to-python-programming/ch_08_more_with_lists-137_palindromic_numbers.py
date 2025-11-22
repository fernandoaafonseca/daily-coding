'''
Use a list comprehension to produce a list that consists of all palindromic numbers between 100 and 1000.
'''


def main() -> None:
	palindromic_nums = [num for num in range(100, 1000) if str(num)[0] == str(num)[-1]]
	display_result(palindromic_nums)


def display_result(palindromic_nums: list[int]) -> None:
	print('Palindromic nums from 100 to 1000:')
	print(palindromic_nums)


if __name__ == '__main__':
	main()