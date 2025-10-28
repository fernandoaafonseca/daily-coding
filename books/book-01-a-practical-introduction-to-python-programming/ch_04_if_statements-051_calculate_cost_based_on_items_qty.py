'''
A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99 items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a program that asks the user how many items they are buying and prints the total cost.
'''


def main():
	qty_items = get_quantity_of_items()
	total_cost = calculate_total_cost(qty_items)
	display_result(qty_items, total_cost)


def get_quantity_of_items() -> int:
	while True:
		try:
			qty_items = int(input('Enter how many items you are buying: '))
			if qty_items >= 1:
				return qty_items
			else:
				raise ValueError
		except ValueError:
			print('Please enter a positive integer number.\n')


def calculate_total_cost(qty_items: int) -> float:
	# Less than 10 items -> $12.00
	tier_1_price = 12
	# Between 10 and 99 items -> $10.00
	tier_2_price = 10
	# 100 or more items -> $7.00
	tier_3_price = 7

	if qty_items < 10:
		total_cost = qty_items * tier_1_price
	elif 10 <= qty_items < 100:
		total_cost = qty_items * tier_2_price
	else:
		total_cost = qty_items * tier_3_price

	return float(total_cost)


def display_result(qty_items: int, total_cost: float) -> None:
	print(f'\nItems bought: {qty_items}')
	print(f'Total cost: ${total_cost:.2f}')


if __name__ == '__main__':
	main()
