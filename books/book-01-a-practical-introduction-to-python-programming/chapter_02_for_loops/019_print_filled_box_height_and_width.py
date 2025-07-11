'''
Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be. [Hint: print('*'*10) prints ten asterisks.]

*******************
*******************
*******************
*******************
'''


def main() -> None:
	box_height = int(input('Enter how high the box should be: '))
	box_width = int(input('Enter how wide the box should be: '))
	print()
	
	print_box(box_height, box_width)


def print_box(box_height: int, box_width:int) -> None:
	for _ in range(box_height):
		print('*' * box_width)


if __name__ == '__main__':
	main()