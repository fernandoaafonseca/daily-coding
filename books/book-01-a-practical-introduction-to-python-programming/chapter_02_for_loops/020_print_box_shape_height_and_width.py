'''
Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be.

*******************
*                 *
*                 *
*******************
'''


def main() -> None:
	box_height = int(input('Enter how high the box should be: '))
	box_width = int(input('Enter how wide the box should be: '))
	print()
	
	print_box(box_height, box_width)


def print_box(box_height: int, box_width:int) -> None:
	for i in range(box_height):
		current_line = i + 1

		if current_line == 1 or current_line == box_height:
			print('*' * box_width)
		else:
			empty_spaces = box_width - 2
			print('*', end='')
			print(' ' * empty_spaces, end='')
			print('*')


if __name__ == '__main__':
	main()