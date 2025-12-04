'''
Write a program that allows the user to enter any number of test scores. The user indicates they are done by entering in a negative number. Print how many of the scores are A’s (90 or above). Also print out the average.
'''


import os


def main():
	test_scores = get_test_scores()
	a_scores = find_a_scores(test_scores)
	if test_scores:
		average_score = sum(test_scores) / len(test_scores)
	else:
		average_score = 0
	display_result(test_scores, a_scores, average_score)


def clear_terminal() -> None:
	os.system('cls' if os.name == 'nt' else 'clear')


def press_any_key_to_continue() -> None:
	input('\nPRESS ANY KEY TO CONTINUE...')


def get_test_scores() -> list[int]:
	test_scores = []

	while True:
		new_score = get_score_input()
		if new_score >= 0:
			test_scores.append(new_score)
		else:
			break

	return test_scores


def get_score_input() -> int:
	while True:
		try:
			clear_terminal()
			new_score = int(input(f'Enter the test score or enter a negative number to exit: '))
			if 0 <= new_score <= 100:
				return new_score
			elif new_score <= 0:
				return -1
			else:
				raise ValueError

		except ValueError:
			print('\nPlease enter a valid score between 0 and 100 or a negative number to exit.')
			press_any_key_to_continue()


def find_a_scores(test_scores: list[int]) -> int:
	a_scores = 0

	for score in test_scores:
		if score >= 90:
			a_scores += 1

	return a_scores


def display_result(test_scores: list[int], a_scores: int, average_score: float) -> None:
	print(f'\nList of scores: \n{test_scores}')
	print(f'Total of A scores: {a_scores}')
	print(f'Average score: {average_score:.2f}')


if __name__ == '__main__':
	main()