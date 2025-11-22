'''
Let L be a list of strings. Write list comprehensions that create new lists from L for each of the following.

	(a) A list that consists of the strings of L with their first characters removed
	(b) A list of the lengths of the strings of L
	(c) A list that consists of only those strings of L that are at least three characters long
'''


WORDS = ['cat',
	'of',
	'a',
	'never',
	'fever',
	'pneumonoultramicroscopicsilicovolcanoconiosis'
	]


def main() -> None:
	words_without_first_char = [s[1:] for s in WORDS]
	words_lengths = [len(s) for s in WORDS]
	words_with_three_or_more_chars = [s for s in WORDS if len(s) >= 3]
	display_result(words_without_first_char, words_lengths, words_with_three_or_more_chars)


def display_result(words_without_first_char: list[str], words_lengths: list[str], words_with_three_or_more_chars: list[str]) -> None:
	print(f'Words: \n{WORDS}\n')
	print(f'Words without first char: \n{words_without_first_char}\n')
	print(f'Words lengths: \n{words_lengths}\n')
	print(f'Words with three or more chars: \n{words_with_three_or_more_chars}')


if __name__ == '__main__':
	main()