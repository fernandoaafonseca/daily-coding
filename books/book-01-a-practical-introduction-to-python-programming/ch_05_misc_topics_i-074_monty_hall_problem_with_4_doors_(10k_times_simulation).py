'''
This exercise is about the well-known Monty Hall problem. In the problem, you are a contestant on a game show. The host, Monty Hall, shows you three doors. Behind one of those doors is a prize, and behind the other two doors are goats. You pick a door. Monty Hall, who knows behind which door the prize lies, then opens up one of the doors that doesn’t contain the prize. There are now two doors left, and Monty gives you the opportunity to change your choice. Should you keep the same door, change doors, or does it not matter?

	(a) Write a program that simulates playing this game 10000 times and calculates what percentage of the time you would win if you switch and what percentage of the time you would win by not switching.
	b) Try the above but with four doors instead of three. There is still only one prize, and Monty still opens up one door and then gives you the opportunity to switch.
'''


import random


def main() -> None:
	simulation_1_changing_choice()
	simulation_2_not_changing_choice()


def simulation_1_changing_choice() -> None:
	simulation_length = 10000
	cpu_will_change_choice = True

	cpu_guess_right, cpu_guess_wrong = simulation(simulation_length, cpu_will_change_choice)
	display_result(simulation_length, cpu_will_change_choice, cpu_guess_right, cpu_guess_wrong)


def simulation_2_not_changing_choice() -> None:
	simulation_length = 10000
	cpu_will_change_choice = False

	cpu_guess_right, cpu_guess_wrong = simulation(simulation_length, cpu_will_change_choice)
	display_result(simulation_length, cpu_will_change_choice, cpu_guess_right, cpu_guess_wrong)


def simulation(simulation_length: int, cpu_will_change_choice: bool) -> tuple[int, int]:
	cpu_guess_right = 0
	cpu_guess_wrong = 0

	for i in range(simulation_length):
		is_cpu_right = game_loop(cpu_will_change_choice)

		if is_cpu_right:
			cpu_guess_right += 1
		else:
			cpu_guess_wrong += 1

	return cpu_guess_right, cpu_guess_wrong


def game_loop(cpu_will_change_choice: bool) -> bool:
	possible_doors = [1, 2, 3, 4]
	right_door = generate_random_door()

	cpu_guess = generate_random_door()
	possible_doors.remove(cpu_guess)

	monty_hall_choice = get_monty_hall_choice(possible_doors, right_door)
	possible_doors.remove(monty_hall_choice)

	if cpu_will_change_choice:
		# CPU will change its choice, choosing one of the remaining closed doors
		cpu_guess = random.choice(possible_doors)

	return check_result(cpu_guess, right_door)


def generate_random_door() -> int:
	return random.randint(1, 4)


def get_monty_hall_choice(possible_doors: list[int, int], right_door: int) -> int:
	while True:
		# possible_doors doesn't have the user chosen door right now
		possible_choice = random.choice(possible_doors)

		if possible_doors != right_door:
			# Checks if the randomly selected door is not the right door
			return possible_choice
		else:
			continue


def check_result(cpu_guess: int, right_door: int) -> bool:
	return cpu_guess == right_door


def display_result(simulation_length: int, cpu_will_change_choice: bool, cpu_guess_right: int, cpu_guess_wrong: int) -> None:
	print('=' * 30)
	print('SIMULATION SETTINGS')
	print(f'Simulation lenght: {simulation_length}')

	if cpu_will_change_choice:
		cpu_change = 'ALWAYS'
	else:
		cpu_change = 'NEVER'
	print(f'CPU will {cpu_change} change its choice.')

	print('-' * 30)
	print('SIMULATION RESULTS')
	print(f'CPU won: {cpu_guess_right} times')
	print(f'CPU lost: {cpu_guess_wrong} times')

	cpu_accuracy = (cpu_guess_right / simulation_length) * 100
	print()
	print(f'Accuracy of choosing the right door:')
	print(f'{cpu_accuracy:.2f}%')

	print('=' * 30)


if __name__ == '__main__':
	main()