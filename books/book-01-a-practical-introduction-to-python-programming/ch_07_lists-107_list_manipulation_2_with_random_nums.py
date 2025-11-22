'''
Write a program that generates a list of 20 random numbers between 1 and 100.

	(a) Print the list.
	(b) Print the average of the elements in the list.
	(c) Print the largest and smallest values in the list.
	(d) Print the second largest and second smallest entries in the list.
	(e) Print how many even numbers are in the list.
'''


import random


def main() -> None:
	random_nums = generate_list_random_nums()
	average = sum(random_nums) / len(random_nums)
	smallest_value = min(random_nums)
	largest_value = max(random_nums)
	sorted_random_nums = sorted(random_nums)
	second_smallest_value = sorted_random_nums[1]
	second_largest_value = sorted_random_nums[-2]
	qty_even_nums = len([num for num in random_nums if num % 2 == 0])

	display_result(random_nums, average, smallest_value, largest_value, second_smallest_value, second_largest_value, qty_even_nums)


def generate_list_random_nums() -> list[int]:
	random_nums = []

	for _ in range(20):
		random_nums.append(random.randint(1, 100))

	return random_nums


def display_result(random_nums: list[int], average: float, smallest_value: int, largest_value: int, second_smallest_value: int, second_largest_value: int, qty_even_nums: int) -> None:
	print(f'Original list: {random_nums}')
	print(f'Average: {average}')
	print(f'Smallest value: {smallest_value}')
	print(f'Largest value: {largest_value}')
	print(f'Second smallest value: {second_smallest_value}')
	print(f'Second largest value: {second_largest_value}')
	print(f'Quantity of even numbers: {qty_even_nums}')


if __name__ == '__main__':
	main()