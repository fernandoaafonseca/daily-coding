'''
Write a program that swaps the values of three variables x, y, and z, so that x gets the value of y, y gets the value of z, and z gets the value of x.
'''


def main():
	x, y, z = 'x', 'y', 'z'
	x, y, z = swap_variables(x, y, z)
	display_result(x, y, z)


def swap_variables(x: str, y: str, z: str) -> tuple[str, str, str]:
	x, y, z = y, z, x

	return x, y, z


def display_result(x: str, y: str, z: str) -> None:
	print(f'New value of x: {x}')
	print(f'New value of y: {y}')
	print(f'New value of z: {z}')


if __name__ == '__main__':
	main()