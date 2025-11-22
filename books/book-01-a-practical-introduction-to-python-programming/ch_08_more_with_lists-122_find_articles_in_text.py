'''
Write a program that asks the user to enter some text and then counts how many articles are in the text. Articles are the words 'a', 'an', and 'the'.
'''


import os, string


ARTICLES = ['a', 'an', 'the']


def main() -> None:
	text = get_text()
	qty_articles = find_articles(text)
	display_result(text, qty_articles)


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


def find_articles(text: str) -> int:
	raw_words = text.split()
	words = [word.strip(string.punctuation) for word in raw_words]
	qty_articles = 0

	for word in words:
		if word.lower() in ARTICLES:
			qty_articles += 1

	return qty_articles


def display_result(text: str, qty_articles: int) -> None:
	press_any_key_to_continue()
	clear_terminal()

	if qty_articles == 1:
		output = 'article'
	else:
		output = 'articles'

	print(f'Your text: "{text}" has {qty_articles} {output}.')


if __name__ == '__main__':
	main()