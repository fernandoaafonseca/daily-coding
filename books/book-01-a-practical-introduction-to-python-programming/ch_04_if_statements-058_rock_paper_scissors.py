'''
Write a program that lets the user play Rock-Paper-Scissors against the computer. There should be five rounds, and after those five rounds, your program should print out who won and lost or that there is a tie.
'''


import os
import random


def main():
	game_loop()


def game_loop():
	player_points = 0
	cpu_points = 0

	for game_round in range(1, 6):
		clear_terminal()

		current_round = game_round
		display_logo_and_current_round_num(current_round)

		cpu_choice = generate_random_cpu_choice()
		player_choice = get_player_choice(current_round)

		round_result = check_round_result(cpu_choice, player_choice)
		cpu_choice_str = generate_string_from_choice(cpu_choice)
		player_choice_str = generate_string_from_choice(player_choice)

		if round_result == 'player_won':
			player_points += 1
		elif round_result == 'cpu_won':
			cpu_points += 1

		display_round_result(cpu_choice_str, player_choice_str, round_result, cpu_points, player_points)

	final_result = check_final_result(cpu_points, player_points)
	clear_terminal()
	display_result(final_result, cpu_points, player_points)


def clear_terminal() -> None:
	input('PLEASE ANY KEY TO CONTINUE...')
	os.system('cls' if os.name == 'nt' else 'clear')


def display_logo_and_current_round_num(current_round: int) -> None:
	print('--- ROCK, PAPER, SCISSORS ---\n')
	print('=' * 20)
	print(f'- ROUND {current_round} -')
	print('=' * 20)


def generate_random_cpu_choice() -> int:
	return random.randint(1, 3)


def get_player_choice(current_round: int) -> int:
	while True:
		try:
			print('Enter your choice: ')
			player_choice = int(input('1 - Rock\n2 - Paper\n3 - Scissors\n\n'))
			if player_choice in [1, 2, 3]:
				return player_choice
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid option (1, 2 or 3).\n')
			clear_terminal()
			display_logo_and_current_round_num(current_round)


def check_round_result(cpu_choice: int, player_choice: int) -> str:
	'''
	1 = Rock
	2 = Paper
	3 = Scissors
	'''
	if player_choice == cpu_choice:
		round_result = 'tie'
	elif player_choice == 1:
		if cpu_choice == 2:
			round_result = 'cpu_won'
		else:
			round_result = 'player_won'
	elif player_choice == 2:
		if cpu_choice == 1:
			round_result = 'player_won'
		else:
			round_result = 'cpu_won'
	elif player_choice == 3:
		if player_choice == 1:
			round_result = 'player_won'
		else:
			round_result = 'cpu_won'

	return round_result


def generate_string_from_choice(choice: int) -> str:
	if choice == 1:
		choice_str = 'rock'
	elif choice == 2:
		choice_str = 'paper'
	else:
		choice_str = 'scissors'

	return choice_str


def display_round_result(cpu_choice_str: str, player_choice_str: str, round_result: str, cpu_points: int, player_points: int) -> None:
	print()
	print('-' * 20)
	print(f'You chose {player_choice_str}.')
	print(f'The CPU chose {cpu_choice_str}.\n')

	if round_result == 'player_won':
		print('You won!')
	elif round_result == 'cpu_won':
		print('The CPU won!')
	else:
		print('It was a tie.')

	print('\nTotal points:')
	print(f'You: {player_points}')
	print(f'CPU: {cpu_points}')
	print('-' * 20)


def check_final_result(cpu_points: int, player_points: int) -> str:
	if cpu_points > player_points:
		final_result = 'cpu'
	elif cpu_points < player_points:
		final_result = 'player'
	else:
		final_result = 'tie'

	return final_result


def display_result(final_result: str, cpu_points: int, player_points: int) -> None:
	print('-' * 20)
	print(f'FINAL SCORE:\n')
	print(f'You: {player_points}')
	print(f'CPU: {cpu_points}\n')
	print('-' * 20)

	if final_result == 'player':
		print('CONGRATULATIONS! YOU WON THE GAME!')
	elif final_result == 'cpu':
		print('YOU LOSE! The CPU won the game!')
	else:
		print('The game ended in a tie.')


if __name__ == '__main__':
	main()