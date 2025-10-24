'''
A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator, determine how many leap years there have been between 1600 and that year.
'''


def main():
	year = get_year()
	leap_years_count = count_leap_years(year)
	display_result(year, leap_years_count)


def get_year() -> int:
	while True:
		try:
			year = int(input('Enter a year after 1600: '))
			if year > 1600:
				return year
			else:
				raise ValueError
		except ValueError:
			print('Please enter a valid year.\n')


def count_leap_years(year: int) -> int:
	leap_years_count = 0
	second_count = 0

	for new_year in range(1600, year + 1, 1):
		if (new_year % 4 == 0 and new_year % 100 != 0) or (new_year % 400 == 0):
			leap_years_count += 1

	return leap_years_count


def display_result(year: int, leap_years_count) -> None:
	print(f'There have been {leap_years_count} leap years between 1600 and {year} (included).')


if __name__ == '__main__':
	main()
