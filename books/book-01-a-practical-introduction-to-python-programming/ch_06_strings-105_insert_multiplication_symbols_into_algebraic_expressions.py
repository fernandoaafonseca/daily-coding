'''
In algebraic expressions, the symbol for multiplication is often left out, as in 3x+4y or 3(x+5). Computers prefer those expressions to include the multiplication symbol, like 3*x+4*y or 3*(x+5). Write a program that asks the user for an algebraic expression and then inserts multiplication symbols where appropriate.
'''


import string


NUMBERS = [num for num in string.digits]
LETTERS = [letter for letter in string.ascii_letters]
OPERATORS = ['+', '-', '*', '/', '^', '%']
OPENING_SYMBOLS = ['(', '[', '{']
CLOSING_SYMBOLS = [')', ']', '}']
VALID_CHARS = NUMBERS + LETTERS + OPERATORS + OPENING_SYMBOLS + CLOSING_SYMBOLS


def main():
	expression = get_expression(VALID_CHARS)
	new_expression = insert_multiplication_symbols(expression, NUMBERS, LETTERS, OPERATORS, OPENING_SYMBOLS, CLOSING_SYMBOLS)

	display_result(expression, new_expression)


def get_expression(VALID_CHARS: list[str, ...]) -> str:
	while True:
		try:
			expression = str(input('Enter an algebraic expression (like "3(x+4y)"): '))

			# Removes empty spaces
			expression = expression.replace(' ', '')
			are_all_chars_valid = check_all_chars_are_valid(expression, VALID_CHARS)
			is_num_of_enclosure_symbols_correct = check_correct_num_of_enclosure_symbols(expression)

			if are_all_chars_valid and is_num_of_enclosure_symbols_correct and len(expression) > 0:
				return expression
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid algebraic expression (like "3(x+4y)".) \n')


def check_all_chars_are_valid(expression: str, VALID_CHARS: list[str, ...]):
    '''
    Checks if all characters in expression are present in VALID_CHARS using all() with a generator expression.
    '''
    return all(char in VALID_CHARS for char in expression)


def check_correct_num_of_enclosure_symbols(expression: str,) -> bool:
	'''
	Checks if the number of opening and closing parentheses, brackets and/or braces matches.
	'''
	is_num_of_parentheses_correct = expression.count('(') == expression.count(')')
	is_num_of_brackets_correct = expression.count('[') == expression.count(']')
	is_num_of_braces_correct = expression.count('{') == expression.count('}')

	return is_num_of_parentheses_correct and is_num_of_brackets_correct and is_num_of_braces_correct



def insert_multiplication_symbols(expression: str, NUMBERS: list[str, ...], LETTERS: list[str, ...], OPERATORS: list[str, ...], OPENING_SYMBOLS: list[str, ...], CLOSING_SYMBOLS: list[str, ...]) -> str:
	'''
	Checks for certain pairs of characters that imply multiplication.
	'''
	MULTIPLICATION_SYMBOL = '*'
	new_expression = ''

	for index in range(len(expression) - 1):
		current_char = expression[index]
		next_char = expression[index + 1]

		if current_char in OPERATORS or next_char in OPERATORS:
			# Checks whether the current or next character is an operator
			new_expression += current_char
		elif current_char in NUMBERS and next_char in LETTERS + OPENING_SYMBOLS:
			# Checks between number and letter: 3x → 3*x;
			# and between number and opening parenthesis, brackets or braces: 3(x+5) → 3*(x+5)
			new_expression += current_char + MULTIPLICATION_SYMBOL
		elif current_char in LETTERS and next_char in OPENING_SYMBOLS + LETTERS:
			# Checks between letter and opening parenthesis, brackets or braces: x(y+1) → x*(y+1);
			# and between letter and another letter: x(yz) → x*(y*z).
			new_expression += current_char + MULTIPLICATION_SYMBOL
		elif current_char in CLOSING_SYMBOLS and next_char in LETTERS + NUMBERS:
			# Checks between closing parenthesis, brackets or braces and letter: (x+1)y → (x+1)*y;
			# and between closing parenthesis, brackets or braces and number: (x+1)3 → (x+1)*3
			new_expression += current_char + MULTIPLICATION_SYMBOL
		else:
			# If the pair does not imply multiplication, it just adds the character of the current iteration
			new_expression += current_char

	# Adds the last character of the expression
	new_expression += expression[-1]

	return new_expression


def display_result(expression: str, new_expression: str) -> None:
	print()
	print(f'Original input expression: {expression}')
	print(f'Formatted expression: {new_expression}')


if __name__ == '__main__':
	main()