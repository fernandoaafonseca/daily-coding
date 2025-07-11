'''
Write a program to fill the screen horizontally and vertically with your name. [Hint: add the
option end='' into the print function to fill the screen horizontally.]
'''


def main() -> None:
	user_name = input('Enter your name: ')
	
	for _ in range (100):
		print(user_name, end='')



if __name__ == '__main__':
	main()