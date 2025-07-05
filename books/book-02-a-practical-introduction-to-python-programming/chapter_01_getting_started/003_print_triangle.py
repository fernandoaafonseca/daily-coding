'''
Print a triangle like the one below.

*
**
***
****
'''


def main() -> None:
	for i in range(4):
		print('*' * (i+1))


if __name__ == '__main__':
	main()