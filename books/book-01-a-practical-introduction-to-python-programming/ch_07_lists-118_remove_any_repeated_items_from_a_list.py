'''
Write a program that removes any repeated items from a list so that each item appears at most once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
'''


import random


def main():
	list_of_ints = generate_random_int_list()
	unique_items_list = get_unique_items_list(list_of_ints)
	display_result(list_of_ints, unique_items_list)


def generate_random_int_list() -> list[int]:
	'''
	Generates a list of random integers within the given range.
	'''
	list_of_ints = []

	for _ in range(10):
		list_of_ints.append(random.randint(0, 4))

	return list_of_ints


def get_unique_items_list(list_of_ints: list[int]) -> list[int]:
	'''
	Builds a new list containing only the first occurrence of each item.
	Duplicate elements are ignored as the list is scanned from left to right.
	'''
	unique_items_list = []

	for item in list_of_ints:
		if item not in unique_items_list:
			unique_items_list.append(item)

	return unique_items_list


def display_result(list_of_ints: list[int], unique_items_list: list[int]) -> None:
	print('Original list:')
	print(list_of_ints)
	print()
	print('Unique items in the list:')
	print(unique_items_list)


if __name__ == '__main__':
	main()