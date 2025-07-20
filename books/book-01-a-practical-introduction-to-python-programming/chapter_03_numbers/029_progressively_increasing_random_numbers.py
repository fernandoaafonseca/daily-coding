'''
Write a program that generates 50 random numbers such that the first number is between 1 and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
1 and 51.
'''


from random import randint


def main() -> None:
	AMOUNT = 50
	LOWER_BOUND = 1
	random_nums = generate_prog_increasing_random_nums(AMOUNT, LOWER_BOUND)

	print(random_nums)


def generate_prog_increasing_random_nums(AMOUNT: int, LOWER_BOUND:int) -> list[int]:
	random_nums = []

	for i in range(LOWER_BOUND, AMOUNT + 1):
		new_num = randint(LOWER_BOUND, i + 1)
		random_nums.append(new_num)

	return random_nums



if __name__ == '__main__':
	main()