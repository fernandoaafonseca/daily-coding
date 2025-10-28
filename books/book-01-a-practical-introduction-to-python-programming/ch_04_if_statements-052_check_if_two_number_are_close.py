'''
Write a program that asks the user for two numbers and prints Close if the numbers are within .001 of each other and Not close otherwise.
'''


def main():
	user_num_1 = get_user_num()
	user_num_2 = get_user_num()
	are_nums_close = check_if_nums_are_close(user_num_1, user_num_2)
	display_result(user_num_1, user_num_2, are_nums_close)


def get_user_num() -> float:
	while True:
		try:
			num = float(input('Enter the number: '))
			return num
		except ValueError:
			print('Please enter a number.\n')


def check_if_nums_are_close(user_num_1: float, user_num_2: float) -> bool:
	result = user_num_1 - user_num_2
	if abs(round(result, 4)) <= 0.001:
		return True
	else:
		return False


def display_result(user_num_1: float, user_num_2: float, are_nums_close: bool) -> None:
	if are_nums_close:
		output = 'close'
	else:
		output = 'not close'

	print(f'\nThe numbers {user_num_1} and {user_num_2} are {output} within .001 of each other.')


if __name__ == '__main__':
	main()
