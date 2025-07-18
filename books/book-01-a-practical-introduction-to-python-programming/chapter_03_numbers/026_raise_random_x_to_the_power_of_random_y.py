'''
Write a program that generates a random number, x , between 1 and 50, a random number y between 2 and 5, and computes x y .
'''


from random import randint


def main() -> None:
	X_LOWER_RANGE = 1
	X_HIGHER_RANGE = 50
	Y_LOWER_RANGE = 2
	Y_HIGHER_RANGE = 5

	x = generate_random_int(X_LOWER_RANGE, X_HIGHER_RANGE)
	y = generate_random_int(Y_LOWER_RANGE, Y_HIGHER_RANGE)
	x_to_the_y = x ** y
	print(f'{x} ^ {y} = {x_to_the_y}')


def generate_random_int(LOWER_RANGE: int, HIGHER_RANGE: int) -> int:
	random_int = randint(LOWER_RANGE, HIGHER_RANGE)

	return random_int


if __name__ == '__main__':
	main()