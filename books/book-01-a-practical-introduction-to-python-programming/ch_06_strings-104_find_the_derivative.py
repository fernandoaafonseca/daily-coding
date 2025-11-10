'''
In calculus, the derivative of x^4 is 4x^3. The derivative of x^5 is 5x^4. The derivative of x^6 is 6x^5. This pattern continues. Write a program that asks the user for input like x^3 or x^25 and prints the derivative. For example, if the user enters x^3, the program should print out 3x^2.
'''


def main():
	expression = get_expression()
	derivative = find_derivative(expression)
	display_result(expression, derivative)


def get_expression() -> str:
	while True:
		try:
			expression = str(input('Enter an expression (like "x^n") to find the derivative: '))
			if expression[0].lower() == 'x' and expression[1] == '^' and int(expression[2:]):
				return expression
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid expression (like "x^n".) \n')


def find_derivative(expression: str) -> str:
	coefficient = int(expression[2:])
	if coefficient > 2:
		power = f'^{coefficient - 1}'
	else:
		power = ''

	return f'{coefficient}x{power}'


def display_result(expression: str, derivative: str) -> None:
	print()
	print(f'The derivative of {expression} is: {derivative}.')


if __name__ == '__main__':
	main()