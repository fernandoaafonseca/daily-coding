'''
A simple way to estimate the number of words in a string is to count the number of spaces in the string. Write a program that asks the user for a string and returns an estimate of how many words are in the string.
'''


def main():
	user_string = get_user_string()
	num_of_words = estimate_num_of_words(user_string)
	display_result(user_string, num_of_words)


def get_user_string() -> str:
	while True:
		try:
			user_string = str(input('Enter a string: '))
			return user_string
		except ValueError:
			print('\nPlease enter a valid string.\n')


def estimate_num_of_words(user_string: str) -> int:
	num_of_words = user_string.count(' ') + 1

	if user_string[-1] == ' ':
		# Removes possible counting error if the last character is an empty space
		num_of_words -= 1

	return num_of_words


def display_result(user_string: str, num_of_words: int) -> None:
	print('=' * 20)
	print(f'Estimation of the number of words in the string "{user_string}": {num_of_words}')
	print('=' * 20)


if __name__ == '__main__':
	main()