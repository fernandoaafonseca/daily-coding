'''
Write a program that asks the user to enter a word and determines whether the word is a palindrome or not. A palindrome is a word that reads the same backwards as forwards.
'''


def main() -> None:
	user_word = get_user_word().lower()
	reversed_user_word = user_word[::-1]
	is_palindrome = check_palindrome(user_word, reversed_user_word)

	display_result(user_word, reversed_user_word, is_palindrome)


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


def check_palindrome(user_word: str, reversed_user_word: str) -> bool:
	return user_word == reversed_user_word


def display_result(user_word: str, reversed_user_word: str, is_palindrome: bool) -> None:
	print(f'\nOriginal input string: {user_word}')
	print(f'Reversed string: {reversed_user_word}\n')

	if is_palindrome:
		print(f'✔️ Yes! "{user_word}" is a palindrome!')
		print(f'"{user_word}" = "{reversed_user_word}"')
	else:
		print(f'❌ No! "{user_word}" is not a palindrome.')
		print(f'"{user_word}" ≠ "{reversed_user_word}"')


if __name__ == '__main__':
	main()