'''
Use for loops to print a diamond like the one below. Allow the user to specify how high the
diamond should be.

   *
  ***
 *****
*******
 *****
  ***
   *
'''


def main() -> None:
	diamond_height = int(input('Enter how high the diamond should be: '))
	print()
	
	print_triangle_upside_down(triangle_height)


def print_diamond(diamond_height: int) -> None:
	for i in range(triangle_height, 0, -1):
		size = i
		print('*' * size)


if __name__ == '__main__':
	main()