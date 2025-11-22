'''
When playing games where you have to roll two dice, it is nice to know the odds of each roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about 17%. You can compute these mathematically, but if you don’t know the math, you can write a program to do it. To do this, your program should simulate rolling two dice about 10,000 times and compute and print out the percentage of rolls that come out to be 2, 3, 4, ..., 12.
'''


import random


def main() -> None:
	DICE_VALUES = [1, 2, 3, 4, 5, 6]
	SIM_LENGTH = 10000

	dice_rolls_sim_results = run_simulation(DICE_VALUES, SIM_LENGTH)
	results_counts = count_results(dice_rolls_sim_results)
	results_perc = calc_percentage_results(results_counts, SIM_LENGTH)

	display_result(SIM_LENGTH, results_counts, results_perc)


def run_simulation(DICE_VALUES: list[int], SIM_LENGTH: int) -> list[int]:
	dice_rolls_sim_results = []

	for _ in range(SIM_LENGTH):
		new_result = roll_two_dice(DICE_VALUES)
		dice_rolls_sim_results.append(new_result)

	return dice_rolls_sim_results


def roll_two_dice(DICE_VALUES: list[int]) -> int:
	first_roll = random.choice(DICE_VALUES)
	second_roll = random.choice(DICE_VALUES)

	result = first_roll + second_roll

	return result


def count_results(dice_rolls_sim_results: list[int]) -> dict[int, int]:
	results_counts = {}

	for item in set(dice_rolls_sim_results):
		results_counts[item] = dice_rolls_sim_results.count(item)

	return results_counts


def calc_percentage_results(results_counts: dict[int, int], SIM_LENGTH: int) -> dict[int, float]:
	results_perc = {}

	for num in results_counts:
		results_perc[num] = results_counts[num] / SIM_LENGTH * 100

	return results_perc


def display_result(SIM_LENGTH: int, results_counts: dict[int, int], results_perc: dict[int, float]) -> None:
	print('DICE ROLLS SIMULATION')
	print('-' * 25)
	print(f'Simulation length: {SIM_LENGTH}')
	print('-' * 25)
	print('RESULTS:')
	print('-' * 25)

	for num in results_perc:
		if num < 10:
			# Adds an empty space to numbers < 10 to allign them
			print(' ', end='')
		print(f'{num}: {results_perc[num]:05.2f}% | {results_counts[num]} times')

	print('-' * 25)


if __name__ == '__main__':
	main()