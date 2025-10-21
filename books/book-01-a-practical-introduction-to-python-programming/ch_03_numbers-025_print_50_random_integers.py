'''
Write a program that generates and prints 50 random integers, each between 3 and 6.
'''


from random import randint


def main() -> None:
	AMOUNT = 50
	LOWER_RANGE = 3
	HIGHER_RANGE = 6

	random_ints = generate_random_ints(50, 3, 6)
	print(random_ints)


def generate_random_ints(AMOUNT: int, LOWER_RANGE: int, HIGHER_RANGE: int) -> tuple[int]:
	random_ints = []

	for _ in range(AMOUNT):
		new_random_int = randint(LOWER_RANGE, HIGHER_RANGE)
		random_ints.append(new_random_int)

	return random_ints


if __name__ == '__main__':
	main()