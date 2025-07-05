'''
Ask the user to enter a number. Print out the square of the number, but use the sep optional
argument to print it out in a full sentence that ends in a period. Sample output is shown
below.

Enter a number: 5
The square of 5 is 25.
'''


def main() -> None:
	user_number = int(input('Enter a number: '))
	square_user_number = user_number * user_number

	print(f'The square of {user_number} is {square_user_number}.')


if __name__ == '__main__':
	main()