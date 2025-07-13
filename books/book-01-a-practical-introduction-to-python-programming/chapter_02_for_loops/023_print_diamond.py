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

	print_diamond(diamond_height)


def print_diamond(diamond_height: int) -> None:
	# 5 de altura, 3 é a linha do meio
	middle_line = (diamond_height + 1) // 2

	# Top lines
	for amount in range(1, middle_line + 1):
		# Print empty spaces to the left
		for _ in range(middle_line - amount):
			print(' ', end = '')
		# Print asterisks
		for _ in range((amount * 2) - 1):
			print('*', end = '')
		print()

	# Bottom lines
	for amount in range(middle_line + 1, diamond_height + 1):
		# Print empty spaces to the left
		for _ in range(amount - middle_line):
			print(' ', end = '')
		# Print asterisks
		for _ in range((diamond_height + 1 - amount)*2 - 1):
			print('*', end = '')
		print()


if __name__ == '__main__':
	main()