'''
Let L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]. Use a list comprehension to produce a list of the gaps between consecutive entries in L. Then find the maximum gap size and the percentage of gaps that have size 2.
'''


def main() -> None:
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
	gaps = [primes[i + 1] - primes[i] for i in range(len(primes) - 1)]
	max_gap = max(gaps)
	perc_of_gaps_size_2 = len([gap for gap in gaps if gap == 2]) / len(gaps) * 100
	display_result(primes, gaps, max_gap, perc_of_gaps_size_2)


def display_result(primes: list[int], gaps: list[int], max_gap: int, perc_of_gaps_size_2: float) -> None:
	print(f'Original list: \n{primes}\n')
	print(f'Gaps between consecutive entries: \n{gaps}\n')
	print(f'Max gap: \n{max_gap}\n')
	print(f'Percentage of gaps that have the size 2: \n{perc_of_gaps_size_2:.2f}%')


if __name__ == '__main__':
	main()