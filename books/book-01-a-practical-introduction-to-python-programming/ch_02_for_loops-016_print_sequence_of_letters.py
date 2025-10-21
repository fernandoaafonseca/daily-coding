'''
Write a program that uses exactly four for loops to print the sequence of letters below.

AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
'''


def main() -> None:
	for _ in range(10):
		print('A', end='')

	for _ in range(7):
		print('B', end='')

	for _ in range(4):
		print('CD', end='')

	for _ in range(5):
		print('F', end='')

	print('G')


if __name__ == '__main__':
	main()