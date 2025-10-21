'''
Write a program that asks the user for their name and how many times to print it. The pro-
gram should print out the user’s name the specified number of times.
'''


def main() -> None:
	user_name = input('Enter your name: ')
	times = int(input('Times to print: '))
	
	for _ in range(times):
		print(user_name)


if __name__ == '__main__':
	main()