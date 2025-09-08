'''
(a) One way to find out the last digit of a number is to mod the number by 10. Write a program that asks the user to enter a power. Then find the last digit of 2 raised to that power.

(b) One way to find out the last two digits of a number is to mod the number by 100. Write a program that asks the user to enter a power. Then find the last two digits of 2 raised to that power.

(c) Write a program that asks the user to enter a power and how many digits they want. Find the last that many digits of 2 raised to the power the user entered.
'''


def main() -> None:
	hour = get_hour()
	hours_ahead = get_hours_ahead()
	display_result(hour, hours_ahead)


def get_hour() -> int:
	while True:
		try:
			hour = int(input('Enter hour: '))
		except:
			print('Please enter a number (1 - 12).')
			print()
			continue

		if 1 <= hour <= 12:
			break
		else:
			print('Hour must be between 1 and 12.\n')

	return hour


def get_hours_ahead() -> int:
	while True:
		try:
			hours_ahead = int(input('How many hours ahead? '))
			break
		except:
			print('Please enter an integer number.')
			print()

	return hours_ahead


def display_result(hour: int, hours_ahead:int) -> None:
	new_hour = hour + hours_ahead

	if new_hour != 12:
		new_hour_am_pm_format = new_hour % 12
	else:
		new_hour_am_pm_format = 12
	
	print(f'New hour: {new_hour_am_pm_format} o\'clock')


if __name__ == '__main__':
	main()