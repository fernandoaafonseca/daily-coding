'''
Write a program that asks the user to enter a value n, and then computes (1 + 1/2 + 1/3 + ··· + 1/n) − ln(n). The ln function is log in the math module.
'''


import math


def main():
	num = get_num()
	result = calc_harmonic_num_minus_ln(num)
	display_result(num, result)


def get_num() -> int:
	while True:
		try:
			num = int(input('Enter a positive integer: '))
			if num > 0:
				return num
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid positive integer.\n')


def calc_harmonic_num_minus_ln(num: int) -> float:
	result = 1

	for i in range(2, num + 1):
		# 1/2 + 1/3 + ... + 1/num
		result += 1 / i

	# result - ln(num)
	result -= math.log(num)

	return result


def display_result(num: int, result: float) -> None:
	print(f'\nThe result of the Euler–Mascheroni formula approximation: \nharmonic number - ln, or \n(1 + 1/2 + 1/3 + ··· + 1/n) − ln(n), \nwith "n = {num}" is: \n{result}')


if __name__ == '__main__':
	main()