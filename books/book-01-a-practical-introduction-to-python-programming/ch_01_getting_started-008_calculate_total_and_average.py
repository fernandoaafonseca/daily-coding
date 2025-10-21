'''
Write a program that asks the user to enter three numbers (use three separate input state-
ments). Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average.
'''


def main():
	user_numbers = get_user_numbers()
	total, average = calc_total_and_average(user_numbers)

	print(f'The total is {total}.')
	print(f'The average is {average}.')


def get_user_numbers() -> list[int]:
	user_numbers = []

	for i in range(3):
		new_number = int(input(f'Enter number {i + 1}: '))
		user_numbers.append(new_number)

	return user_numbers


def calc_total_and_average(user_numbers: list[int]) -> tuple[int]:
	total = sum(user_numbers)
	average = total / len(user_numbers)

	return total, average


if __name__ == '__main__':
	main()