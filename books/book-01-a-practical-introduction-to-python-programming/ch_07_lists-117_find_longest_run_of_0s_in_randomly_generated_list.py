'''
Write a program that generates 100 random integers that are either 0 or 1. Then find the longest run of zeros, the largest number of zeros in a row. For instance, the longest run of zeros in [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0] is 4.
'''


import random


def main():
	ones_and_zeros = generate_list_of_ones_and_zeros()
	longest_run = find_longest_run_of_zeros(ones_and_zeros)
	display_result(ones_and_zeros, longest_run)


def generate_list_of_ones_and_zeros() -> list[int]:
	ones_and_zeros = []

	for _ in range(100):
		ones_and_zeros.append(random.randint(0, 1))

	return ones_and_zeros


def find_longest_run_of_zeros(ones_and_zeros: list[int]) -> int:
	current_run = 0
	longest_run = 0

	for num in ones_and_zeros:
		if num == 0:
			current_run += 1
		elif num == 1:
			# If the current number is a 1, the possible run of 0s has ended.
			if current_run > longest_run:
				longest_run = current_run
			current_run = 0

		if current_run > longest_run:
	    	# After finishing the list, compare one last time, in the case where the last number is a 0 and it is also the longest sequence.
			longest_run = current_run

	return longest_run


def display_result(ones_and_zeros: list[int], longest_run: int) -> None:
	print('The longest run of zeros in the list:')
	print(ones_and_zeros)
	print(f'is {longest_run} zeros.')


if __name__ == '__main__':
	main()