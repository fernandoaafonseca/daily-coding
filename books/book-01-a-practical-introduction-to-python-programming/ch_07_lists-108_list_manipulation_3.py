'''
Start with the list [8, 9, 10]. Do the following:

	(a) Set the second entry (index 1) to 17
	(b) Add 4, 5, and 6 to the end of the list
	(c) Remove the first entry from the list
	(d) Sort the list
	(e) Double the list
	(f) Insert 25 at index 3 The final list should equal [4, 5, 6, 25, 10, 17, 4, 5, 6, 10, 17]
'''


import random


def main() -> None:
	EXPECTED_FINAL_LIST = [4, 5, 6, 25, 10, 17, 4, 5, 6, 10, 17]

	l = [8, 9, 10]
	l[1] = 17
	l += [4, 5, 6]
	l.pop(0)
	l = sorted(l)
	l *= 2
	l.insert(3, 25)

	display_result(l, EXPECTED_FINAL_LIST)


def display_result(l: list[int], EXPECTED_FINAL_LIST: list[int]) -> None:
	print(f'Original manipulated list: \n{l}')
	print(f'\nExpected final list: \n{EXPECTED_FINAL_LIST}')
	print(f'\nAre they equal: \n{l == EXPECTED_FINAL_LIST}')


if __name__ == '__main__':
	main()