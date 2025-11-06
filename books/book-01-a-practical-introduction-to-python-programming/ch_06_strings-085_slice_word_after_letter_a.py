'''
Write a program that asks the user to enter a word that contains the letter a. The program should then print the following two lines: On the first line should be the part of the string up to and including the first a, and on the second line should be the rest of the string. Sample output is shown below:

	Enter a word: buffalo
	buffa
	lo
'''


def main() -> None:
	user_word = get_user_word()
	word_1st_part, word_2nd_part = slice_str_after_first_letter_a(user_word)
	display_result(user_word, word_1st_part, word_2nd_part)


def get_user_word() -> str:
	while True:
		try:
			user_word = str(input('Enter a word containing the letter "a": '))
			if user_word.isalpha() and 'a' in user_word:
				return user_word
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a single word containing the letter "a".\n')


def slice_str_after_first_letter_a(user_word: str) -> tuple[str, str]:
	# The find() method finds the first occurrence of the specified value.
	index_letter_a = user_word.find('a')
	word_1st_part = user_word[0:index_letter_a + 1]
	word_2nd_part = user_word[index_letter_a + 1:]

	return word_1st_part, word_2nd_part


def display_result(user_word: str, word_1st_part: str, word_2nd_part:str) -> None:
	print()
	print(f'Slicing the word "{user_word}" after the first letter "a":')
	print(word_1st_part)
	print(word_2nd_part)


if __name__ == '__main__':
	main()