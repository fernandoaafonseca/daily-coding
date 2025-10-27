'''
Write a program that draws “modular rectangles” like the ones below. The user specifies the width and height of the rectangle, and the entries start at 0 and increase typewriter fashion from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 × 5 rectangle and a 4 × 8.

0 1 2 3 4
5 6 7 8 9
0 1 2 3 4

0 1 2 3 4 5 6 7
8 9 0 1 2 3 4 5
6 7 8 9 0 1 2 3
4 5 6 7 8 9 0 1
'''


def main():
	horizontal_lines, vertical_lines = get_rectangle_size()
	print_modular_rectangle(horizontal_lines, vertical_lines)


def get_rectangle_size() -> tuple[int, int]:
	while True:
		try:
			horizontal_lines = int(input('Enter the amount of horizontal lines: '))
		except ValueError:
			print('Please enter a valid number.\n')

		try:
			vertical_lines = int(input('Enter the amount of vertical lines: '))
		except ValueError:
			print('Please enter a valid number.\n')

		return horizontal_lines, vertical_lines


def print_modular_rectangle(horizontal_lines: int, vertical_lines: int) -> None:
	current_number = 0

	for _ in range(horizontal_lines):
		for _ in range(vertical_lines):
			if current_number > 9:
				current_number = 0
				print(f'{current_number} ', end='')
				current_number += 1
			else:
				print(f'{current_number} ', end='')
				current_number += 1
		print()


if __name__ == '__main__':
	main()
