'''
Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. The
output should look like the output below.
1 Your name
2 Your name
3 Your name
4 Your name
...
100 Your name
'''


def main() -> None:
	user_name = input('Enter your name: ')

	for i in range(100):
		print(f'{i + 1} {user_name}')


if __name__ == '__main__':
	main()