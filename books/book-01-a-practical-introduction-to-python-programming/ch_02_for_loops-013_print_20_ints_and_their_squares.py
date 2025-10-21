'''
Write a program that prints out a list of the integers from 1 to 20 and their squares. The output
should look like this:

1 --- 1
2 --- 4
3 --- 9
...
20 --- 400
'''


def main() -> None:
	for i in range(20):
		new_int = i + 1
		new_square = new_int ** 2
		print(f'{new_int} --- {new_square}')


if __name__ == '__main__':
	main()