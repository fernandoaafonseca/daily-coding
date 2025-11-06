'''
Write a program that asks the user to enter a word and then capitalizes every other letter of that word. So if the user enters rhinoceros, the program should print:

	rHiNoCeRoS
'''


def main() -> None:
	user_word = get_user_word()
	formatted_word = capitalize_every_other_letter(user_word)
	display_result(user_word, formatted_word)


def get_user_word() -> str:
	while True:
		try:
			user_word = str(input('Enter a word: '))
			if user_word.isalpha():
				return user_word
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a single word.\n')


def capitalize_every_other_letter(user_word: str) -> str:
	formatted_word = ''

	for index, char in enumerate(user_word):
		if index % 2 == 0:
			# The even indices will be lowercase. "0 % 2 == 0" returns True, so "0" is considered pair.
			formatted_word += char.lower()
		else:
			# The odd indices will be uppercase
			formatted_word += char.upper()

	return formatted_word


def slice_str_after_first_letter_a(user_word: str) -> tuple[str, str]:
	# The find() method finds the first occurrence of the specified value.
	index_letter_a = user_word.find('a')
	word_1st_part = user_word[0:index_letter_a + 1]
	word_2nd_part = user_word[index_letter_a + 1:]

	return word_1st_part, word_2nd_part


def display_result(user_word: str, formatted_word:str) -> None:
	print()
	print(f'Capitalizing every other letter in the word "{user_word}":')
	print(formatted_word)


if __name__ == '__main__':
	main()