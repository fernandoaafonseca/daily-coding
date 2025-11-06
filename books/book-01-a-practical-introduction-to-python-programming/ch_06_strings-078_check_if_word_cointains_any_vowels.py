'''
Write a program that asks the user to enter a word and prints out whether that word contains any vowels.
'''


def main():
	VOWELS = ['a', 'e', 'i', 'o', 'u']

	user_word = get_user_word()
	contains_any_vowels = check_for_vowels(VOWELS, user_word)
	display_result(user_word, contains_any_vowels)


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


def check_for_vowels(VOWELS: list[str], user_word: str) -> bool:
	for char in user_word:
		if char.lower() in VOWELS:
			return True
	return False


def display_result(user_word: str, contains_any_vowels: bool) -> None:
	if contains_any_vowels:
		output = 'CONTAINS'
	else:
		output = 'DOES NOT CONTAIN'

	print()
	print(f'The word "{user_word}" {output} at least one vowel.')


if __name__ == '__main__':
	main()