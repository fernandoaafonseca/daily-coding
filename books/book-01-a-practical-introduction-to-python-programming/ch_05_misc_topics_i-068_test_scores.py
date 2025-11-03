'''
Ask the user to enter 10 test scores. Write a program to do the following:

(a) Print out the highest and lowest scores.
(b) Print out the average of the scores.
(c) Print out the second largest score.
(d) If any of the scores is greater than 100, then after all the scores have been entered, print a message warning the user that a value over 100 has been entered.
(e) Drop the two lowest scores and print out the average of the rest of them.
'''


def main():
	test_scores = get_test_scores()
	highest_score = max(test_scores)
	lowest_score = min(test_scores)
	average_score = sum(test_scores) / len(test_scores)
	sorted_test_scores = sorted(test_scores)
	second_highest_score = sorted_test_scores[-2]
	dropped_lowest_scores = sorted_test_scores[2:]
	average_dropping_lowest_scores = sum(dropped_lowest_scores) / len(dropped_lowest_scores)
	display_result(test_scores, highest_score, lowest_score, average_score, second_highest_score, average_dropping_lowest_scores)


def get_test_scores() -> list[int]:
	test_scores = []

	for i in range(1, 11):
		test_num = i
		new_score = get_score_input(test_num)
		test_scores.append(new_score)

	return test_scores


def get_score_input(test_num: int) -> int:
	while True:
		try:
			new_score = int(input(f'Enter the test score no. {test_num}: '))
			if 0 <= new_score <= 100:
				return new_score
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid score between 0 and 100.\n')


def display_result(test_scores: list[int], highest_score: int, lowest_score: int, average_score: float, second_highest_score: int, average_dropping_lowest_scores: float) -> None:
	print(f'\nList of scores: {test_scores}')
	print(f'Highest score: {highest_score}')
	print(f'Second highest score: {second_highest_score}')
	print(f'Lowest score: {lowest_score}')
	print(f'Average score: {average_score:.2f}')
	print(f'Average score dropping the two lowest scores: {average_dropping_lowest_scores:.2f}')


if __name__ == '__main__':
	main()