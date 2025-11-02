'''
Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000.
'''


def main():
	higher_bound = 2000

	# Method 1:
	total_sum = calculate_sum_alternating_signs(higher_bound)
	print(total_sum)

	# Method 2:
	total_sum = calculate_by_grouping_the_terms(higher_bound)
	print(total_sum)


def calculate_sum_alternating_signs(higher_bound: int) -> int:
	total_sum = 0
	for i in range (1, higher_bound + 1):
		if i % 2 == 0:
			total_sum -= i
		else:
			total_sum += i

	return total_sum


def calculate_by_grouping_the_terms(higher_bound: int) -> int:
	'''
	The series can be grouped into pairs of consecutive numbers:
	(1 - 2) + (3 - 4) + ... + (1999 - 2000)

	Each pair in the series has a sum of -1.
	(1 - 2) = -1
	(3 - 4) = -1
	...
	(1999 - 2000) = -1

	The series contains numbers from 1 to 2000, for a total of 2000 terms. Since the terms are grouped into pairs, there are 2000 / 2 pairs.
	Number of pairs = 2000 / 2 = 1000

	The total sum is the number of pairs multiplied by the sum of each pair:
	Total sum = 1000 * (-1) = -1000

	If there is an odd number of terms, simply add the last one to the end. So, if the series ended in 2001, we would have:
	Total sum = (2000 / 2) * (-1) + 2001 = 1001
	'''
	num_of_pairs = higher_bound // 2

	total_sum = num_of_pairs * -1

	if higher_bound % 2 != 0:
		total_sum += higher_bound

	return total_sum


if __name__ == '__main__':
	main()