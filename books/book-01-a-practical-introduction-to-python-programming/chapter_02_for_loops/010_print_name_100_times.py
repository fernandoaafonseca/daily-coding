'''
Write a program that prints your name 100 times.
'''


def main() -> None:
	user_name = input('Enter your name: ')
	
	for _ in range (100):
		print(user_name)



if __name__ == '__main__':
	main()