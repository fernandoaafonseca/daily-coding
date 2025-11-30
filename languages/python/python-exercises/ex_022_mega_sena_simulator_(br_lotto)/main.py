'''
Official Mega Sena Rules (Brazil) — explained in English

Number range:
You choose 6 to 15 distinct integers.
Each number must be between 1 and 60.

Winning condition:
To win the Jackpot (Sena), you must match all 6 numbers.

Price per bet:
Price varies depending on how many numbers you choose (6–15),
but the cheapest ticket (6 numbers) costs:

💰 R$ 5,00 (as of 2025)
'''

import time
from mega_sena_utils import (
	generate_official_draw,
	generate_random_ticket,
	check_win,
	count_matches,
	TICKET_PRICE_SIX_NUMBERS,
)


def main() -> None:
	print('\nMEGA SENA SIMULATOR')
	print('------------------------------------')

	while True:
		choice = choose_simulation()

		if choice == 1:
			run_simulation_one()
		elif choice == 2:
			run_simulation_two()
		elif choice == 3:
			run_simulation_three()
		elif choice == 0:
			print('\nExiting program...')
			return

		print('\nSimulation finished!')
		print('------------------------------------\n')


def choose_simulation() -> int:
	'''
	Asks the user which simulation they want to run.
	Returns an integer representing the chosen option.
	'''
	while True:
		print('\nChoose a simulation:')
		print('1 - Simulation 1 (Fixed official draw)')
		print('2 - Simulation 2 (New draw for each ticket)')
		print('3 - Simulation 3 (Mega da Virada)')
		print('0 - Exit program')

		user_input = input('Your choice: ').strip()

		if user_input.isdigit():
			choice = int(user_input)
			if choice in (0, 1, 2, 3):
				return choice

		print('Invalid input! Please enter 0, 1, 2, or 3.')


def run_simulation_one() -> None:
	'''
	Simulation 1:
	One fixed official draw. Generate tickets until jackpot is hit.

	FIRST SIMULATION
	'Fixed official draw + generate tickets until you win'
	--------------------------------------------
	Logic:
	- Generate one official draw
	- Generate random (cheap) tickets repeatedly
	- Stop only when you match all 6 numbers
	- Display attempts, total spent, and winning ticket
	'''
	official_draw = generate_official_draw()
	attempts = 0
	total_spent = 0.0

	start_time = time.time()
	last_time_check = start_time

	while True:
		attempts += 1
		total_spent += TICKET_PRICE_SIX_NUMBERS

		# print every 100k attempts
		if attempts % 100000 == 0:
			print(f'ATTEMPTS: {attempts:,}')

		# print elapsed time every 30 seconds
		current_time = time.time()
		if current_time - last_time_check >= 30:
			elapsed = current_time - start_time
			print(f'Elapsed time: {elapsed:.2f} seconds')
			last_time_check = current_time

		ticket = generate_random_ticket()

		if check_win(ticket, official_draw):
			total_spent = TICKET_PRICE_SIX_NUMBERS * attempts
			total_time = time.time() - start_time

			print('\nJACKPOT HIT!')
			print(f'Official draw: {official_draw}')
			print(f'Winning ticket: {ticket}')
			print(f'Attempts: {attempts:,}')
			print(f'Total spent: R$ {total_spent:.2f}')
			print(f'Total time: {total_time:.2f} seconds')
			break


def run_simulation_two() -> None:
	'''
	Simulation 2:
	Each ticket receives its own brand-new official draw.

	SECOND SIMULATION
	'New official draw for each ticket'
	--------------------------------------------
	Logic:
	- Each time you generate a random ticket,
	  also generate a new official draw
	- Check if ticket == draw
	- Stop when jackpot is hit
	- Display attempts and total spent
	'''
	attempts = 0
	total_spent = 0.0

	start_time = time.time()
	last_time_check = start_time

	while True:
		attempts += 1

		# print every 100k attempts
		if attempts % 100000 == 0:
			print(f'ATTEMPTS: {attempts:,}')

		# print elapsed time every 30 seconds
		current_time = time.time()
		if current_time - last_time_check >= 30:
			elapsed = current_time - start_time
			print(f'Elapsed time: {elapsed:.2f} seconds')
			last_time_check = current_time

		ticket = generate_random_ticket()
		official_draw = generate_official_draw()

		if check_win(ticket, official_draw):
			total_spent = TICKET_PRICE_SIX_NUMBERS * attempts
			total_time = time.time() - start_time

			print('\nJACKPOT HIT!')
			print(f'Official draw: {official_draw}')
			print(f'Winning ticket: {ticket}')
			print(f'Attempts: {attempts}')
			print(f'Total spent: R$ {total_spent:.2f}')
			print(f'Total time: {total_time:.2f} seconds')
			break


def run_simulation_three(num_players: int = 5_000_000) -> None:
	'''
	Simulation 3 – Mega da Virada:
	Many players, one official draw.
	The prize is awarded to whoever gets the most matches (at least 4).

	THIRD SIMULATION
	‘Mega da Virada’ — New Year’s special lottery
	--------------------------------------------
	Characteristics:
	- It must have a winner
	- The draw is identical to a normal Mega Sena
	- What guarantees a winner is:
	  If nobody hits 6 numbers, the prize rolls down
	  to 5-number winners, then 4-number winners.

	Simulation logic:
	- Generate one official draw
	- Generate millions of tickets
	- Track the best match count
	- Declare the best ticket
	'''
	official_draw = generate_official_draw()

	best_ticket = None
	best_match_count = -1

	for _ in range(num_players):
		ticket = generate_random_ticket()
		matches = count_matches(ticket, official_draw)

		if matches > best_match_count:
			best_match_count = matches
			best_ticket = ticket

	print('\nMEGA DA VIRADA SIMULATION COMPLETE')
	print(f'Official draw: {official_draw}')
	print(f'Best ticket: {best_ticket}')
	print(f'Best match count: {best_match_count}')

	if best_match_count == 6:
		print('Jackpot winner exists!')
	else:
		print('No jackpot winner — prize rolled down.')


if __name__ == '__main__':
	main()
