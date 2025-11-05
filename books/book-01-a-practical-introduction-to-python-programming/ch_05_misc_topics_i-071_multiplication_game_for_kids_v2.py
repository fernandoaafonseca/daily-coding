'''
In the last chapter there was an exercise that asked you to create a multiplication game for kids. Improve your program from that exercise to keep track of the number of right and wrong answers. At the end of the program, print a message that varies depending on how many questions the player got right.
'''


import os
import random


def main():
	game_loop()


def game_loop() -> None:
	game_counter = 10
	user_points = 0

	for i in range(1, game_counter + 1):
		question_num = i
		x, y, result = generate_multiplication()
		display_hud(question_num, x, y, user_points)
		user_answer = get_user_answer()
		is_user_answer_right = check_question_answer(user_answer, result)
		display_question_answer(result, is_user_answer_right)
		clear_terminal()
		if is_user_answer_right:
			user_points += 1
		print()

	display_result(user_points)


def clear_terminal() -> None:
	input('PLEASE ANY KEY TO CONTINUE...')
	os.system('cls' if os.name == 'nt' else 'clear')


def display_hud(question_num: int, x: int, y: int, user_points: int) -> None:
	print('=' * 27)
	print('--- MULTIPLICATION GAME ---')
	print('=' * 27)
	print(f'RIGHT ANSWERS: {user_points}')
	print('-' * 27)
	print('-' * 7, end='')
	print(f' Question #{question_num} ', end='')
	if question_num < 10:
		print('-' * 7)
	else:
		print('-' * 6)
	print('-' * 27)
	print(f'{x} * {y} = ?')
	print('=' * 27)


def generate_random_int() -> int:
	return random.randint(1, 10)


def generate_multiplication() -> tuple[int, int, int]:
	x = generate_random_int()
	y = generate_random_int()
	result = x * y

	return x, y, result


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
		print(f'\nWrong. The correct answer is {result}.\n')


def display_result(user_points: int) -> None:
	print('=' * 27)
	print('GAME OVER!')
	if user_points == 10:
		print(f'CONGRATULATIONS! You answered all questions correctly!')
	elif user_points >= 7:
		print(f'GOOD JOB! You answered {user_points}/10 questions correctly. Can you get them all right on your next try?')
	elif user_points >= 1:
		print(f'GOOD! You answered {user_points}/10 questions correctly. You need to improve.')
	else:
		print(f'BAD! You got all the answers wrong. Study more!')


if __name__ == '__main__':
	main()