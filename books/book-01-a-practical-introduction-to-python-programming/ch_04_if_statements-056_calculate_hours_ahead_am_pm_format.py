'''
Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm, and asks them how many hours into the future they want to go. Print out what the hour will be that many hours into the future, printing am or pm as appropriate. An example is shown below.

Enter hour: 8
am (1) or pm (2)? 1
How many hours ahead? 5
New hour: 1 pm
'''


def main():
	hour = get_hour()
	am_pm = get_am_pm()
	hours_ahead = get_hours_ahead()
	new_hour, new_am_pm = calculate_new_hour(hour, am_pm, hours_ahead)
	display_result(new_hour, new_am_pm)


def get_hour() -> int:
	while True:
		try:
			hour = int(input('Enter hour: '))
			if 1 <= hour <= 12:
				return hour
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid hour between 1 and 12.\n')


def get_am_pm() -> int:
	while True:
		try:
			am_pm = int(input('\na.m. (1) or p.m. (2)? '))
			if am_pm in [1, 2]:
				return am_pm
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter "1" for "a.m." or "2" for "p.m.".\n')


def get_hours_ahead() -> int:
	while True:
		try:
			hours_ahead = int(input('\nHow many hours ahead? '))
			if 0 <= hours_ahead <= 24:
				return hours_ahead
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid hour amount between 0 and 24 (included).\n')


def invert_am_pm(am_pm: int) -> int:
	'''
	If am_pm == 1, then: 3 - 1 = 2.
	If am_pm == 2, then: 3 - 2 = 1
	'''
	return 3 - am_pm


def calculate_new_hour(hour: int, am_pm: int, hours_ahead: int) -> tuple[int, int]:
	# Add and subtract to the 12-hour cycle
	new_hour = (hour + hours_ahead - 1) % 12 + 1

	# Count how many times it passed through 12 → 1
	flips = (hour - 1 + hours_ahead) // 12

	# Invert a.m./p.m. if the number of revolutions is odd
	if flips % 2 == 1:
		am_pm = invert_am_pm(am_pm)

	return new_hour, am_pm


def display_result(new_hour: int, new_am_pm: int) -> None:
	if new_am_pm == 1:
		period = 'a.m.'
	else:
		period = 'p.m.'

	print(f'\nNew hour: {new_hour} {period}')


if __name__ == '__main__':
	main()