'''
Write a program that asks the user to guess a random number between 1 and 10. If they guess right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give the user five numbers to guess and print their score after all the guessing is done.
'''


import os
import random


def main() -> None:
	game_loop()


def game_loop() -> None:
	player_score = 0
	player_lives = 15
	is_game_over = False

	while not is_game_over:
		for game_round in range(1, 6):
			is_player_guess_correct = False
			current_round = game_round
			generated_num = generate_random_num()

			while not is_player_guess_correct and player_lives >= 1:
				clear_terminal()
				display_hud(current_round, player_lives, player_score)

				player_guess = get_player_guess(current_round, player_lives, player_score)
				is_player_guess_correct = check_player_guess(player_guess, generated_num)

				if is_player_guess_correct:
					player_score += 10
				else:
					player_score -= 1
					player_lives -= 1

			# Break the for loop at the current round when player lives reaches 0
			if player_lives <= 0:
				break

		is_game_over = True

		display_final_screen(current_round, player_score, player_lives)


def clear_terminal() -> None:
	input('PLEASE ANY KEY TO CONTINUE...')
	os.system('cls' if os.name == 'nt' else 'clear')


def display_hud(current_round: int, player_lives: int, player_score: int) -> None:
	if player_lives > 0:
		lives_emoji = '❤️'
	else:
		lives_emoji = '☠️'

	print('--- GUESS THE NUMBER ---\n')
	print('=' * 24)
	print(' ' * 6, end='')
	print(f'- ROUND {current_round}/5 -', end='')
	print(' ' * 7)
	print('=' * 24)
	print(f'{lives_emoji}  # LIVES: {player_lives}')
	print('=' * 24)
	print(f'🧮 # SCORE: {player_score}')
	print('=' * 24)


def generate_random_num() -> int:
	return random.randint(1, 10)


def get_player_guess(current_round: int, player_lives: int, player_score: int) -> int:
	while True:
		try:
			num = int(input('Guess the generated number bewtween 1 and 10: '))
			if 1 <= num <= 10:
				return num
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid number bewteen 1 and 10.\n')
			clear_terminal()
			display_hud(current_round, player_lives, player_score)


def check_player_guess(player_guess: int, generated_num: int) -> bool:
	if player_guess == generated_num:
		points_output = '➕ 10 points'
	else:
		points_output = '➖ 1 point'

	if player_guess > generated_num:
		print(f'\n❌ WRONG! TOO HIGH! ⬇️\n')
	elif player_guess < generated_num:
		print(f'\n❌ WRONG! TOO LOW! ⬆️ \n')
	else:
		print(f'\n✔️  RIGHT! 📌\n')

	print(points_output)
	print('-' * 24)

	return player_guess == generated_num


def display_final_screen(final_round: int, player_score: int, player_lives: int) -> None:
	clear_terminal()
	display_hud(final_round, player_lives, player_score)

	print(' ' * 7, end='')
	print('GAME OVER', end='')
	print(' ' * 7)

	if final_round < 5 or player_lives == 0:
		print('\nTOO BAD!')
		print('You didn\'t manage to complete all 5 rounds.')
	else:
		print('\nCONGRATULATIONS!')
		print(f'You managed to complete all 5 rounds with {player_lives} lives remaining!')


if __name__ == '__main__':
	main()