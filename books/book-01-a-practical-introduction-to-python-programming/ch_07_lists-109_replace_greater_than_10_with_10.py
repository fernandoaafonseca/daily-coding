'''
Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the entries in the list that are greater than 10 with 10.
'''


def main() -> None:
	user_list = get_list_of_ints()
	new_list = replace_greater_than_10_with_10(user_list)
	display_result(user_list, new_list)


def get_list_of_ints() -> list[int]:
	while True:
		try:
			str_of_ints = str(input('Enter a list of integers between 1 and 12: '))
			# Generates a list of "ints" splitting the string by "commas"
			list_of_ints = [int(item) for item in str_of_ints.split(',')]

			# Check if all values in my_list are within the range [lower_bound, upper_bound]
			all_in_range = all(1 <= x <= 12 for x in list_of_ints)
			if all_in_range:
				return list_of_ints
			else:
				raise ValueError
		except ValueError:
			print('\nPlease only enter integers between 1 and 12 separated by commas.\n')


def replace_greater_than_10_with_10(user_list: list[int]) -> list[int]:
	return [num if num <= 10 else 10 for num in user_list]


def display_result(user_list: list[int], new_list: list[int]) -> None:
	print()
	print(f'Original list: \n{user_list}')
	print(f'\nReplacing values greater than 10 with 10: \n{new_list}')


if __name__ == '__main__':
	main()