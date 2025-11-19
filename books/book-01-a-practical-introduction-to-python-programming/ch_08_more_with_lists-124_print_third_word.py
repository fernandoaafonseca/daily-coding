'''
(a) Ask the user to enter a sentence and print out the third word of the sentence.
(b) Ask the user to enter a sentence and print out every third word of the sentence.
'''


import os, string


def main():
	text = get_text()
	third_word = find_third_word(text)
	display_result(text, third_word)


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


def find_third_word(text: str) -> str:
	raw_words = text.split()
	words = [word.strip(string.punctuation) for word in raw_words]

	if len(words) >= 3:
		return words[2]
	else:
		return 'you entered less than 3 words'


def display_result(text: str, third_word: str) -> None:
	press_any_key_to_continue()
	clear_terminal()

	print(f'YOur text: {text}')
	print(f'Third word: {third_word}')


if __name__ == '__main__':
	main()