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
	if diamond_height % 2 == 0:
		is_height_even = True
	else:
		is_height_even = False

	# 5 de altura, 3 é a linha do meio
	if is_height_even:
		middle_line = int((diamond_height + 1) / 2)
	else:
		middle_line = int((diamond_height + 1) // 2)

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
	if not is_height_even:
		for amount in range(middle_line + 1, diamond_height + 1):
			# Print empty spaces to the left
			for _ in range(amount - middle_line):
				print(' ', end = '')
			# Print asterisks
			for _ in range((diamond_height + 1 - amount) * 2 - 1):
				print('*', end = '')
			print()

	else:
		for amount in range(middle_line, diamond_height):
			# Print empty spaces to the left
			for _ in range(amount - middle_line):
				print(' ', end = '')
			# Print asterisks
			for _ in range((diamond_height - amount) * 2 - 1):
				print('*', end = '')
			print()


if __name__ == '__main__':
	main()