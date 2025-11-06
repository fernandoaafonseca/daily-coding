'''
Write a program that asks the user to enter two strings of the same length. The program should then check to see if the strings are of the same length. If they are not, the program should print an appropriate message and exit. If they are of the same length, the program should alternate the characters of the two strings. For example, if the user enters abcde and ABCDE the program should print out AaBbCcDdEe.
'''


def main() -> None:
	user_string_1 = get_user_string(1)
	user_string_2 = get_user_string(2)
	are_two_str_same_length = check_two_str_lenghts_are_equal(user_string_1, user_string_2)
	display_result(user_string_1, user_string_2, are_two_str_same_length)


def get_user_string(str_num: int) -> str:
	while True:
		try:
			user_string = str(input(f'Enter the string #{str_num}: '))
			return user_string
		except ValueError:
			print('\nPlease enter a valid string.\n')


def check_two_str_lenghts_are_equal(user_string_1: str, user_string_2: str) -> bool:
	return len(user_string_1) == len(user_string_2)


def generate_alternating_chars_between_two_str(user_string_1: str, user_string_2: str) -> str:
	alternating_string = ''

	for index, char in enumerate(user_string_1):
		alternating_string += user_string_2[index] + user_string_1[index]

	return alternating_string


def simple_test():
	test_string_1 = 'abcde'
	test_string_2 = 'ABCDE'
	expected_alternating_string = 'AaBbCcDdEe'

	test_alternating_string = generate_alternating_chars_between_two_str(test_string_1, test_string_2)

	return expected_alternating_string == test_alternating_string


def display_result(user_string_1: str, user_string_2: str, are_two_str_same_length: bool) -> None:
	print()

	if are_two_str_same_length:
		alternating_string = generate_alternating_chars_between_two_str(user_string_1, user_string_2)
		print(f'Alternating the characters of the two strings:')
		print(alternating_string)
	else:
		print('The two given strings are not the same lenght.')

	test_result = simple_test()
	print()
	print(f'Simple test result: {test_result}.')


if __name__ == '__main__':
	main()