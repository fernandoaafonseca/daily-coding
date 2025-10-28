'''
Write a program that asks the user how many credits they have taken. If they have taken 23 or less, print that the student is a freshman. If they have taken between 24 and 53, print that they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.
'''


def main():
	student_credits = get_student_credits()
	display_result(student_credits)


def get_student_credits() -> int:
	while True:
		try:
			credits = int(input('Enter how many credits you have taken: '))
			if credits >= 0:
				return credits
			else:
				raise ValueError
		except ValueError:
			print('Please enter a positive integer number.\n')


def display_result(student_credits: int) -> None:
	print(f'\nCredits taken: {student_credits}')

	if student_credits <= 23:
		print('You\'re a freshman.')
	elif 24 <= student_credits <= 53:
		print('You\'re a sophomore.')
	elif 54 <= student_credits <= 83:
		print('You\'re a junior.')
	else:
		print('You\'re a senior.')


if __name__ == '__main__':
	main()
