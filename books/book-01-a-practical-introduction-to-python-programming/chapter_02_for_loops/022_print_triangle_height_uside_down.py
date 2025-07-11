'''
Use a for loop to print an upside down triangle like the one below. Allow the user to specify
how high the triangle should be.

****
***
**
*
'''


def main() -> None:
	triangle_height = int(input('Enter how high the triangle should be: '))
	print()
	
	print_triangle_upside_down(triangle_height)


def print_triangle_upside_down(triangle_height: int) -> None:
	for i in range(triangle_height, 0, -1):
		size = i
		print('*' * size)


if __name__ == '__main__':
	main()