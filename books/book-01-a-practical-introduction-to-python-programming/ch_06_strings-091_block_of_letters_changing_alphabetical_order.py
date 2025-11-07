'''
Write a program that generates the 26-line block of letters partially shown below. Use a loop containing one or two print statements.

	abcdefghijklmnopqrstuvwxyz
	bcdefghijklmnopqrstuvwxyza
	cdefghijklmnopqrstuvwxyzab
	...
	yzabcdefghijklmnopqrstuvwx
	zabcdefghijklmnopqrstuvwxy
'''


import string


def main() -> None:
	alphabet_doubled = string.ascii_lowercase + string.ascii_lowercase
	display_result(alphabet_doubled)


def display_result(alphabet_doubled: list[str, ...]) -> None:
	num_lines = 26
	line_length = 26
	starting_char = 0

	for line in range(num_lines):
		for char_index in range(line_length):
			print(alphabet_doubled[char_index + starting_char], end='')
		starting_char += 1
		print()


if __name__ == '__main__':
	main()