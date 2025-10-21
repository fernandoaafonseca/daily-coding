'''
A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included.
'''


def main():
	price, percent_tip = get_price_and_percent_tip()
	tip, total = calculate_tip_and_total(price, percent_tip)

	print()
	print(f'Tip amount ({percent_tip} %): {tip}')
	print(f'Total bill: $ {total}')


def get_price_and_percent_tip() -> tuple[float]:
	price = float(input(f'Enter the price of the meal: $'))
	percent_tip = float(input(f'Enter the % tip you want to leave: '))

	return price, percent_tip


def calculate_tip_and_total(price: float, percent_tip: float) -> tuple[float]:
	tip = price * percent_tip / 100
	total = format(price + tip, '.2f')

	return tip, total

if __name__ == '__main__':
	main()