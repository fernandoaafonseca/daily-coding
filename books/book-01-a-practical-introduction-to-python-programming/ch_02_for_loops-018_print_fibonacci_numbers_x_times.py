'''
The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .
'''


def main() -> None:
	amount = int(input('Enter how many Fibonacci numbers to print: '))
	print_fibonacci_numbers(amount)


def print_fibonacci_numbers(amount: int) -> None:
	last_number = 0
	current_number = 1
	next_number = last_number + current_number

	for i in range(amount):
		print(f'{current_number}', end='')

		if i + 1 != amount:
			print(', ', end='')
		else:
			print('.')

		current_number = next_number
		next_number = last_number + current_number
		last_number, current_number = current_number, next_number


if __name__ == '__main__':
	main()