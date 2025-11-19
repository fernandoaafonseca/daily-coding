'''
(a) Write a program that asks the user to enter a sentence and then randomly rearranges the words of the sentence. Don’t worry about getting punctuation or capitalization correct.
(b) Do the above problem, but now make sure that the sentence starts with a capital, that the original first word is not capitalized if it comes in the middle of the sentence, and that the period is in the right place.
'''


import os, random, string


def main():
	text = get_text()
	randomized_text = randomize_words_order(text)
	display_result(text, randomized_text)


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


def randomize_words_order(text: str) -> str:
	# Split into words
	words = text.split()

	# Shuffle the words list
	random.shuffle(words)

	# Put back together
	return ' '.join(words)


def display_result(text: str, randomized_text: str) -> None:
	press_any_key_to_continue()
	clear_terminal()

	print(f'Your text: {text}')
	print(f'Your text randomized: {randomized_text}')


if __name__ == '__main__':
	main()