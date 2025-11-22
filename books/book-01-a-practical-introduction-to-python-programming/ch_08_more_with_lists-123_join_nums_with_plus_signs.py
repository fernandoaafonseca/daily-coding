'''
Write a program that allows the user to enter five numbers (read as strings). Create a string that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2, 5, 11, 33, and 55, then the string should be '2 + 5 + 11 + 33 + 55'.
'''


import os


def main() -> None:
	nums_list = get_nums()
	nums_string = add_plus_signs(nums_list)
	display_result(nums_list, nums_string)


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def get_nums() -> list[int]:
	while True:
		try:
			press_any_key_to_continue()
			clear_terminal()

			nums = str(input('Enter a list of integers separated by commas (like "1, 2, 3"): '))
			# Generates a list of "ints" splitting the string by "commas"
			nums_list = [int(item) for item in nums.split(',')]

			return nums_list

		except ValueError:
			print('\nPlease only enter integers separated by commas.')


def add_plus_signs(nums_list: list[int]) -> str:
	nums_string = ''

	for index, num in enumerate(nums_list):
		nums_string += str(num)

		if index < len(nums_list) - 1:
			nums_string += ' + '

	return nums_string


def display_result(nums_list: list[int], nums_string: str) -> None:
	press_any_key_to_continue()
	clear_terminal()

	print(f'Your list of numbers: {nums_list}')
	print(f'Adding plus signs: {nums_string}')


if __name__ == '__main__':
	main()