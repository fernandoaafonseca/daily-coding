'''
Below is described how to find the date of Easter in any year. Despite its intimidating appearance, this is not a hard problem. Note that ⌊x⌋ is the floor function, which for positive numbers just drops the decimal part of the number. For instance ⌊3.14⌋ = 3. The floor function is part of the math module.

C = century (1900’s → C = 19)
Y = year (all four digits)
m = (15 + C − ⌊(C / 4)⌋ − ⌊(8C + 13) / 25⌋) mod 30
n = (4 + C − ⌊C / 4⌋) mod 7
a = Y mod 4
b = Y mod 7
c = Y mod 19
d = (19c + m) mod 30
e = (2a + 4b + 6d + n) mod 7

Easter is either March (22 + d + e) or April (d + e − 9). There is an exception if d = 29 and e = 6. In this case, Easter falls one week earlier on April 19. There is another exception if d = 28, e = 6, and m = 2, 5, 10, 13, 16, 21, 24, or 39. In this case, Easter falls one week earlier on April 18. Write a program that asks the user to enter a year and prints out the date of Easter in that year. (See Tattersall, Elementary Number Theory in Nine Chapters, 2nd ed., page 167)
'''


import math


def main():
	year = get_year()
	m, d, e = easter_formula(year)
	day, month = calculate_day_and_month(m, d, e)
	display_result(year, month, day)


def get_year() -> int:
	while True:
		try:
			year = int(input('Enter a year: '))
			if year > 0:
				return year
			else:
				raise ValueError
		except ValueError:
			print('Please enter a valid year.\n')


def easter_formula(year: int) -> tuple[int, int, int]:
	'''
	-> m: century-based correction for the lunar cycle (determines the approximate date of the Paschal full moon)
	-> n: century-based correction for the weekday offset (aligns the lunar date with the solar calendar)
	-> a: remainder when the year is divided by 4 (represents the leap-year cycle)
	-> b: remainder when the year is divided by 7 (represents the weekly cycle)
	-> c: remainder when the year is divided by 19 (represents the Metonic cycle — alignment of Sun and Moon every 19 years)
	-> d: intermediate value combining c and m, gives the moon phase adjustment
	-> e: final correction combining all cycles (used to determine the Sunday following the Paschal full moon)
	'''
	century = year // 100

	m = (15 + century - math.floor(century / 4) - math.floor((8 * century + 13) / 25)) % 30
	n = (4 + century - math.floor(century / 4)) % 7
	a = year % 4
	b = year % 7
	c = year % 19
	d = (19 * c + m) % 30
	e = (2 * a + 4 * b + 6 * d + n) % 7

	return m, d, e


def calculate_day_and_month(m:int, d: int, e: int) -> tuple[int, str]:
	day = 22 + d + e
	month = 'March'

	if day > 31:
		day = d + e - 9
		month = 'April'

	if d == 29 and e == 6:
		day = 19
		month = 'April'
	elif d == 28 and e == 6 and m in [2, 5, 10, 13, 16, 21, 24, 29]:
		day = 18
		month = 'April'

	return day, month


def display_result(year: int, month: int, day: int) -> None:
	if day in [1, 21, 31]:
		day_suffix = 'st'
	elif day in [2, 22]:
		day_suffix = 'nd'
	elif day == 3:
		day_suffix = 'rd'
	else:
		day_suffix = 'th'

	print(f'Easter in {year} falls on {month} {day}{day_suffix}.')


if __name__ == '__main__':
	main()
