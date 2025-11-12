'''
Write a program that asks the user for an integer and creates a list that consists of the factors of that integer.
'''


def main():
	user_num = get_user_num()
	factors = get_factors(user_num)
	display_result(user_num, factors)


def get_user_num() -> int:
	while True:
		try:
			num = int(input('Enter an integer number: '))
			return num
		except ValueError:
			print('Please enter a valid integer number.\n')


def get_factors(user_num: int) -> list[int]:
	factors = []

	if user_num >= 0:
		for i in range(1, user_num + 1):
			if user_num % i == 0:
				factors.append(i)
	else:
		for i in range(user_num, abs(user_num) + 1):
			if i == 0:
				continue
			elif user_num % i == 0:
				factors.append(i)
	return factors


def display_result(user_num: int, factors: list[int]) -> None:
	print()
	print(f'Factors of {user_num}: {factors}')


if __name__ == '__main__':
	main()