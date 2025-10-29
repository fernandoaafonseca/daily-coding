'''
A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. Write a program that asks the user for a year and prints out whether it is a leap year or not.
'''


def main():
	year = get_year()
	is_leap_year = check_leap_year(year)
	display_result(year, is_leap_year)


def get_year() -> int:
	while True:
		try:
			year = int(input('Enter a year: '))
			if year > 0:
				return year
			else:
				raise ValueError
		except ValueError:
			print('Please enter a valid year after year 0.\n')


def check_leap_year(year: int) -> bool:
	if ((year % 400 == 0) and (year % 100 == 0)) or ((year % 100 != 0) and (year % 4 == 0)):
		is_leap_year = True
	else:
		is_leap_year = False

	return is_leap_year


def display_result(year: int, is_leap_year: bool) -> None:
	if is_leap_year:
		output = 'is'
	else:
		output = 'is not'
	print(f'\nThe year {year} {output} a leap year.')


if __name__ == '__main__':
	main()
