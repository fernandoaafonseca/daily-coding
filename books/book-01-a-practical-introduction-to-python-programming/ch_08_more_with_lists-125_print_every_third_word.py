'''
(a) Ask the user to enter a sentence and print out the third word of the sentence.
(b) Ask the user to enter a sentence and print out every third word of the sentence.
'''


import os, string


def main():
	text = get_text()
	every_third_word = find_every_third_word(text)
	display_result(text, every_third_word)


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def get_text() -> str:
	while True:
		try:
			press_any_key_to_continue()
			clear_terminal()

			text = str(input('Enter some text: '))

			if len(text.replace(' ', '')) > 0:
				return text
			else:
				raise ValueError

		except ValueError:
			print('\nPlease enter a non-empty string of text.')


def find_every_third_word(text: str) -> list[str] | str:
	raw_words = text.split()
	words = [word.strip(string.punctuation) for word in raw_words]

	every_third_words = []

	if len(words) >= 3:
		for num in range(len(words)):
			if (num + 1) % 3 == 0:
				every_third_words.append(words[num])
	else:
		return 'you entered less than 3 words'

	return every_third_words


def display_result(text: str, every_third_word: list[str] | str) -> None:
	press_any_key_to_continue()
	clear_terminal()

	print(f'YOur text: {text}')
	print(f'Every third word: {every_third_word}')


if __name__ == '__main__':
	main()