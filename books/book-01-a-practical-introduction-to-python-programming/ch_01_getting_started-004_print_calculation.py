'''
Write a program that computes and prints the result of

 512 − 282
-----------
47 · 48 + 5.

It is roughly .1017.
'''


def main() -> None:
	expected_result = 0.1017
	calc_result = (512 - 282) / (47 * 48 + 5)
	rounded_calc_result = round(calc_result, 4)

	print(calc_result)
	print(rounded_calc_result == expected_result)


if __name__ == '__main__':
	main()