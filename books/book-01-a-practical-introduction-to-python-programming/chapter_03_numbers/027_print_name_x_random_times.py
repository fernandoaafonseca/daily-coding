'''
Write a program that generates a random number between 1 and 10 and prints your name that many times.
'''


from random import randint


def main() -> None:
	user_name = input('Enter you name: ')
	random_num = randint(1, 10)

	print(user_name * random_num)


if __name__ == '__main__':
	main()