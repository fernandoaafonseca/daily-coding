'''
A number is called a "perfect number" if it is equal to the sum of all of its divisors, not including the number itself. For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6 and 6 = 1 + 2 + 3. As another example, 28 is a perfect number because its divisors are 1, 2, 4, 7, 14, 28 and 28 = 1 + 2 + 4 + 7 + 14. However, 15 is not a perfect number because its divisors are 1, 3, 5, 15 and 15 ≠ 1 + 3 + 5. Write a program that finds all four of the perfect numbers that are less than 10000.
'''


def main():
	higher_bound = 10000
	perfect_numbers = find_perfect_numbers(higher_bound)
	display_result(higher_bound, perfect_numbers)


def find_perfect_numbers(higher_bound: int) -> tuple[int]:
	perfect_numbers = []

	for i in range(1, higher_bound + 1):
		divisors_of_i = get_divisors(i)
		sum_of_all_divisors_of_i = calc_sum_all_divisors(divisors_of_i)
		is_i_perfect = check_is_a_perfect_num(i, sum_of_all_divisors_of_i)
		if is_i_perfect:
			perfect_numbers.append(i)

	return perfect_numbers



def get_divisors(number: int) -> list[int]:
	divisors = []

	for i in range(1, number + 1):
		if number % i == 0:
			divisors.append(i)

	return divisors


def calc_sum_all_divisors(divisors: list[int]) -> int:
	total_sum = 0

	for i in range(len(divisors)):
		total_sum += divisors[i]

	return total_sum


def check_is_a_perfect_num(number: int, sum_of_all_divisors: int) -> bool:
	return (sum_of_all_divisors - number) == number


def display_result(higher_bound: int, perfect_numbers: list[int]) -> None:
	print(f'The perfect numbers from 1 to {higher_bound} are:')
	print(perfect_numbers)


if __name__ == '__main__':
	main()