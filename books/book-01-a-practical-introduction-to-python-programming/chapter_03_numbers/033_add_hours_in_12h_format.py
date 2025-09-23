'''
Write a program that asks the user for an hour between 1 and 12 and for how many hours in the future they want to go. Print out what the hour will be that many hours into the future. An example is shown below.

Enter hour: 8
How many hours ahead? 5
New hour: 1 o'clock
'''


def main() -> None:
	hour = get_hour()
	hours_ahead = get_hours_ahead()
	display_result(hour, hours_ahead)


def get_hour() -> int:
	while True:
		try:
			hour = int(input('Enter hour: '))
		except ValueError:
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