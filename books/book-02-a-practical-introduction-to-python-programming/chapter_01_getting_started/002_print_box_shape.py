'''
Print a box like the one below.

*******************
*                 *
*                 *
*******************
'''


def main() -> None:
	for row in range(4):
		if row in [0, 3]:
			print('*' *19)
		else:
			for column in range(19):
				#print(column)
				if column in [0, 18]:
					print('*', end='')
				else:
					print(' ', end='')
			print()


if __name__ == '__main__':
	main()