'''
Write a program that asks the user for a large integer and inserts commas into it according to the standard American convention for commas in large numbers. For instance, if the user enters 1000000, the output should be 1,000,000.
'''


def main() -> None:
	user_int = get_user_int()
	formatted_with_commas = format_int_to_commas(user_int)
	display_result(user_int, formatted_with_commas)


def get_user_int() -> int:
	while True:
		try:
			user_int = int(input(f'Enter a large integer (bigger than 1,000): '))
			if user_int >= 1000:
				return user_int
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid integer larger than 1,000.\n')


def format_int_to_commas(user_int: int) -> str:
	user_int_in_str = str(user_int)
	# Empty values before and after the colon default to start (0) and end (len(string)) respectively.
	reversed_string = user_int_in_str[::-1]
	# [i:i+3] slices the reversed string into groups of three characters.
	chunks_of_three = [reversed_string[i:i+3] for i in range(0, len(reversed_string), 3)]
	with_commas = ",".join(chunks_of_three)
	formatted_with_commas = with_commas[::-1]

	return formatted_with_commas


def display_result(user_int: int, formatted_with_commas: str) -> None:
	print()
	print(f'Formatting "{user_int}" according to the standard American convention for commas in large numbers:')
	print(formatted_with_commas)


if __name__ == '__main__':
	main()