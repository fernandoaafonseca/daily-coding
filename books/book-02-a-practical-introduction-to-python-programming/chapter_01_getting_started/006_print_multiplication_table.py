'''
Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,
and 5x, each separated by three dashes, like below.

Enter a number: 7
7---14---21---28---35.
'''


def main() -> None:
	x = int(input('Enter a number: '))

	for i in range (5):
		if i != 4:
			print(x * (i + 1), end='')
			print('---', end='')
		else:
			print(x * (i + 1), end='')
			print('.')


if __name__ == '__main__':
	main()