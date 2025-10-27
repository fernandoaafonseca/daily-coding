'''
Write a program that given an amount of change less than $1.00 will print out exactly how many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.

[Hint: the // operator may be useful.]
'''


def main():
	amount_of_change = get_amount_of_change()
	quarters, dimes, nickels, pennies = calculate_change(amount_of_change)
	display_result(amount_of_change, quarters, dimes, nickels, pennies)


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


def calculate_change(amount_of_change: float) -> tuple[int, int, int, int]:
	quarters, dimes, nickels, pennies = 0, 0, 0, 0

	remaining_change = amount_of_change
	while remaining_change >= 0.25:
		quarters += 1
		remaining_change -= 0.25

	while remaining_change >= 0.10:
		dimes += 1
		remaining_change -= 0.10

	while remaining_change >= 0.05:
		nickels += 1
		remaining_change -= 0.05

	while remaining_change >= 0.01:
		pennies += 1
		remaining_change -= 0.01

	return quarters, dimes, nickels, pennies


def display_result(amount_of_change: float, quarters: int, dimes: int, nickels: int, pennies: int) -> None:
	print(f'Change: ${amount_of_change}')
	print(f'Quarters ($0.25): {quarters}')
	print(f'Dimes ($0.10): {dimes}')
	print(f'Nickels ($0.05): {nickels}')
	print(f'Pennies ($0.01): {quarters}')


if __name__ == '__main__':
	main()
