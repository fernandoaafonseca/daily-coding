'''
Use a for loop to print a triangle like the one below. Allow the user to specify how high the
triangle should be.

*
**
***
****
'''


def main() -> None:
	triangle_height = int(input('Enter how high the triangle should be: '))
	print()
	
	print_triangle(triangle_height)


def print_triangle(triangle_height: int) -> None:
	for i in range(triangle_height):
		size = i + 1
		print('*' * size)


if __name__ == '__main__':
	main()