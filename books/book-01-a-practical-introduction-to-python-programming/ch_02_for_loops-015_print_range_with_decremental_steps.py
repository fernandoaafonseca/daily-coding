'''
Write a program that uses a for loop to print the numbers 100, 98, 96, . . . , 4, 2.
'''


def main() -> None:
	for i in range(100, 1, -2):
		print(i)


if __name__ == '__main__':
	main()