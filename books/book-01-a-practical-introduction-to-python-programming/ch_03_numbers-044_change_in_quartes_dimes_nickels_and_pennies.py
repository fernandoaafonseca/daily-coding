'''
Write a program that given an amount of change less than $1.00 will print out exactly how many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.

[Hint: the // operator may be useful.]
'''


def main():
	amount_of_change = get_amount_of_change()

	display_result()


def get_amount_of_change() -> float:
	while True:
		try:
			amount_of_change = float(input('Enter the amount of change (less than $1.00: $'))
			if 0.01 <= amount_of_change <= 1.00:
				return amount_of_change
			else:
				raise ValueError
		except ValueError:
			print('Please enter a valid number.\n')


def calculate_change(amount_of_change: float) -> None:


def display_result() -> None:
	print(f'')


if __name__ == '__main__':
	main()
