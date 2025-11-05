'''
People often forget closing parentheses when entering formulas. Write a program that asks the user to enter a formula and prints out whether the formula has the same number of opening and closing parentheses.
'''


def main():
	user_formula = get_user_formula()
	is_num_parentheses_correct = check_correct_num_of_parentheses(user_formula)
	display_result(user_formula, is_num_parentheses_correct)


def get_user_formula() -> str:
	while True:
		try:
			user_formula = str(input('Enter a formula: '))
			return user_formula
		except ValueError:
			print('\nPlease enter a valid string.\n')


def check_correct_num_of_parentheses(user_formula: str) -> bool:
	'''
	Checks if the number of opening and closing parentheses matches.
	'''
	return user_formula.count('(') == user_formula.count(')')


def display_result(user_formula: str, is_num_parentheses_correct: bool) -> None:
	correct_or_incorrect = 'correct'

	if is_num_parentheses_correct:
		correct_or_incorrect = 'correct'
	else:
		correct_or_incorrect = 'incorrect'

	print()
	print(f'Your formula is {correct_or_incorrect}.')

	if not is_num_parentheses_correct:
		print(f'Your formula "{user_formula}"" is missing one or more opening or closing parentheses.')
	else:
		print(f'Your formula "{user_formula}" has the correct number of opening and closing parentheses.')


if __name__ == '__main__':
	main()