'''
Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them whether they got it right or wrong and what the correct answer is.

Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong.
The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right.
'''


import random


def main():
	game_loop()


def game_loop() -> None:
	game_counter = 10
	user_points = 0

	for i in range(1, game_counter + 1):
		question_num = i
		x, y, result = generate_multiplication()
		display_question(question_num, x, y)
		user_answer = get_user_answer()
		is_user_answer_right = check_question_answer(user_answer, result)
		display_question_answer(result, is_user_answer_right)
		if is_user_answer_right:
			user_points += 1
		print()

	display_result(user_points)


def generate_random_int() -> int:
	return random.randint(1, 10)


def generate_multiplication() -> tuple[int, int, int]:
	x = generate_random_int()
	y = generate_random_int()
	result = x * y

	return x, y, result


def display_question(question_num: int, x: int, y: int) -> None:
	print(f'Question {question_num}: {x} * {y} = ?')


def get_user_answer() -> int:
	while True:
		try:
			user_answer = float(input('Enter your answer: '))
			return user_answer
		except ValueError:
			print('\nPlease enter a valid number!\n')


def check_question_answer(user_answer: int, result: int) -> bool:
	return user_answer == result


def display_question_answer(result: int, is_user_answer_right: bool) -> None:
	if is_user_answer_right:
		print('\nRIGHT!')
	else:
		print(f'\nWrong. The correct answer is {result}.')


def display_result(user_points: int) -> None:
	print('GAME OVER!')
	print(f'You answered {user_points}/10 questions correctly.')


if __name__ == '__main__':
	main()