'''
This exercise is about the well-known Monty Hall problem. In the problem, you are a contestant on a game show. The host, Monty Hall, shows you three doors. Behind one of those doors is a prize, and behind the other two doors are goats. You pick a door. Monty Hall, who knows behind which door the prize lies, then opens up one of the doors that doesn’t contain the prize. There are now two doors left, and Monty gives you the opportunity to change your choice. Should you keep the same door, change doors, or does it not matter?

	(a) Write a program that simulates playing this game 10000 times and calculates what percentage of the time you would win if you switch and what percentage of the time you would win by not switching.
	b) Try the above but with four doors instead of three. There is still only one prize, and Monty still opens up one door and then gives you the opportunity to switch.
'''


import random


def main():
	game_loop()


def game_loop() -> None:
	possible_doors = [1, 2, 3]
	right_door = generate_random_right_door()

	user_guess = get_user_guess(possible_doors)
	possible_doors.remove(user_guess)

	monty_hall_choice = get_monty_hall_choice(possible_doors, right_door)
	possible_doors.remove(monty_hall_choice)

	user_guess = ask_user_wants_change_door(possible_doors, user_guess, monty_hall_choice)
	is_user_right = check_result(user_guess, right_door)

	display_result(is_user_right, user_guess, right_door)


def generate_random_right_door() -> int:
	return random.randint(1, 3)


def get_user_guess(possible_doors: list[int]) -> int:
	while True:
		try:
			user_guess = int(input('Choose the door (1, 2 or 3): '))
			if user_guess in possible_doors:
				return user_guess
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid door (1, 2 or 3).\n')


def get_monty_hall_choice(possible_doors: list[int, int], right_door: int) -> int:
	for door in possible_doors:
		# possible_doors doesn't have the user chosen door right now
		if door != right_door:
			return door


def ask_user_wants_change_door(possible_doors: list[int], user_guess: int, monty_hall_choice: int) -> int:
	print()
	print(f'You chose the door #{user_guess}.')
	print(f'Monty Hall chose the door #{monty_hall_choice}.')
	while True:
		try:
			user_choice = str(input('Do you want to change your door? Enter Y or N: '))
			if user_choice.lower()[0] == 'y':
				user_guess = possible_doors[0]
				return user_guess
			elif user_choice.lower()[0] == 'n':
				return user_guess
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter Y or N.\n')


def check_result(user_guess: int, right_door: int) -> bool:
	return user_guess == right_door


def display_result(is_user_right: bool, user_guess: int, right_door: int) -> None:
	print()
	if is_user_right:
		print(f'YOU WON!')
	else:
		print(f'YOU LOSE! Your guess was {user_guess} but the right door was {right_door}.')


if __name__ == '__main__':
	main()