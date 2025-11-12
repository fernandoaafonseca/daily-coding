'''
Write a program that asks the user to enter a list of integers. Do the following:

	(a) Print the total number of items in the list.
	(b) Print the last item in the list.
	(c) Print the list in reverse order.
	(d) Print Yes if the list contains a 5 and No otherwise.
	(e) Print the number of fives in the list.
	(f) Remove the first and last items from the list, sort the remaining items, and print the result.
	(g) Print how many integers in the list are less than 5.
'''


def main():
	list_of_ints = get_list_of_ints()
	num_items = len(list_of_ints)
	last_item = list_of_ints[-1]
	reversed_list = list_of_ints[::-1]
	contains_a_five = 'Yes' if 5 in list_of_ints else 'No'
	num_of_fives = list_of_ints.count(5)
	list_of_ints_removing_first_and_last_items = list_of_ints[1:-1]
	num_of_ints_less_than_5 = len([item for item in list_of_ints if item < 5])

	display_result(list_of_ints, num_items, last_item, reversed_list, contains_a_five, num_of_fives, list_of_ints_removing_first_and_last_items, num_of_ints_less_than_5)


def get_list_of_ints() -> list[int]:
	while True:
		try:
			str_of_ints = str(input('Enter a list of integers separated by commas (like "1, 2, 3": '))
			# Generates a list of "ints" splitting the string by "commas""
			list_of_ints = [int(item) for item in str_of_ints.split(',')]
			return list_of_ints
		except ValueError:
			print('\nPlease only enter integers separated by commas.\n')


def display_result(list_of_ints: list[int], num_items: int, last_item: int, reversed_list: list[int], contains_a_five: bool, num_of_fives: int, list_of_ints_removing_first_and_last_items: list[int], num_of_ints_less_than_5: int) -> None:
	print()
	print(f'Original list: {list_of_ints}')
	print(f'Total number of items: {num_items}')
	print(f'Last item: {last_item}')
	print(f'Reversed list: {reversed_list}')
	print(f'List contains a 5: {contains_a_five}')
	print(f'Number of fives: {num_of_fives}')
	print(f'List without first and last items: {list_of_ints_removing_first_and_last_items}')
	print(f'Number of integers less than 5: {num_of_ints_less_than_5}')


if __name__ == '__main__':
	main()