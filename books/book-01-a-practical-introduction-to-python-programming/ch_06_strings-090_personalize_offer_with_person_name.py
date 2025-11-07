'''
Companies often try to personalize their offers to make them more attractive. One simple way to do this is just to insert the person’s name at various places in the offer. Of course, companies don’t manually type in every person’s name; everything is computer-generated. Write a program that asks the user for their name and then generates an offer like the one below. For simplicity’s sake, you may assume that the person’s first and last names are one word each.

	Enter name: George Washington

	Dear George Washington,

	I am pleased to offer you our new Platinum Plus Rewards card at a special introductory APR of 47.99%. George, an offer like this does not come along every day, so I urge you to call now toll-free at 1-800-314-1592. We cannot offer such a low rate for long, George, so call right away.
'''


def main() -> None:
	user_name = get_user_name()
	user_name_capitalized = user_name.title()
	display_result(user_name_capitalized)


def get_user_name() -> str:
	while True:
		try:
			user_name = str(input(f'Enter your name: '))
			return user_name
		except ValueError:
			print('\nPlease enter a valid string.\n')


def display_result(user_name_capitalized: str) -> None:
	user_first_name = user_name_capitalized.split()[0]

	print()
	print(f'Dear {user_name_capitalized},\nI am pleased to offer you our new Platinum Plus Rewards card at a special introductory APR of 47.99%. {user_first_name}, an offer like this does not come along every day, so I urge you to call now toll-free at 1-800-314-1592. We cannot offer such a low rate for long, {user_first_name}, so call right away.')


if __name__ == '__main__':
	main()