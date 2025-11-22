'''
Write a program that gets a string from the user containing a potential telephone number. The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise. A phone number is considered valid as long as it is written in the form abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number should contain only numbers and dashes, and the number of digits in each group must be correct. Test your program with the output shown below.

	Enter a phone number: 1-301-447-5820
	Valid
	Enter a phone number: 301-447-5820
	Valid
	Enter a phone number: 301-4477-5820
	Invalid
	Enter a phone number: 3X1-447-5820
	Invalid
	Enter a phone number: 3014475820
	Invalid
'''


import os


VALID_CHARS = '0123456789-'


def main() -> None:
	phone_number = get_phone_number()
	is_valid = is_valid_phone(phone_number)
	display_result(is_valid)
	run_tests()


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def get_phone_number() -> str:
	while True:
		try:
			clear_terminal()

			phone_number = str(input('Enter a phone number: '))

			all_chars_are_valid = all(char in VALID_CHARS for char in phone_number)

			if len(phone_number.replace(' ', '')) > 0 and all_chars_are_valid:
				return phone_number
			else:
				raise ValueError

		except ValueError:
			print('\nPlease enter a phone number.')
			press_any_key_to_continue()


def is_valid_standard_format(phone_number: str) -> bool:
    '''
    Return True if the number matches the form abc-def-hijk.
    '''
    chars = [char for char in phone_number]
    nums_indices = [0, 1, 2, 4, 5, 6, 8, 9, 10, 11]
    dashes_indices = [3, 7]

    if len(phone_number) != 12:
    	return False

    for index, char in enumerate(chars):
    	if index in nums_indices and char.isdigit():
    		continue
    	elif index in dashes_indices and char == '-':
    		continue
    	else:
    		return False

    return True


def is_valid_with_country_code(phone_number: str) -> bool:
    '''
    Return True if the number matches the form 1-abc-def-hijk.
    '''
    chars = [char for char in phone_number]
    nums_indices = [2, 3, 4, 6, 7, 8, 10, 11, 12, 13]
    dashes_indices = [1, 5, 9]

    if len(phone_number) != 14:
    	return False

    for index, char in enumerate(chars):
    	if index == 0 and char == '1':
    		continue
    	elif index in nums_indices and char.isdigit():
    		continue
    	elif index in dashes_indices and char == '-':
    		continue
    	else:
    		return False

    return True


def is_valid_phone(phone_number: str) -> bool:
    '''
    Return True if the number is a valid phone number according to the rules.
    '''
    if is_valid_standard_format(phone_number) or is_valid_with_country_code(phone_number):
    	return True
    else:
    	return False


def display_result(is_valid: bool) -> None:
	if is_valid:
		print('Valid')
	else:
		print('Invalid')


def run_tests() -> None:
	press_any_key_to_continue()
	clear_terminal()

	print('TESTS RESULTS:\n')

	print(is_valid_phone('1-301-447-5820') == True)
	print(is_valid_phone('301-447-5820') == True)
	print(is_valid_phone('301-4447-5820') == False)
	print(is_valid_phone('3X1-447-5820') == False)
	print(is_valid_phone('3014475820') == False)
	print(is_valid_phone('2-301-447-5820') == False)
	print(is_valid_phone('1-3-0-447-5820') == False)


if __name__ == '__main__':
	main()