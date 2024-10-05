'''
Rules:
"Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are."

Source: Wikipedia article "Leap year"
https://en.wikipedia.org/wiki/Leap_year
'''


def main():
    # Display the title of the program.
    display_title()

    # Get a valid year from the user.
    year = get_year()

    # Determine if the year is a leap year.
    is_leap_year = check_leap_year(year)

    # Display the result based on the leap year check.
    display_result(year, is_leap_year)


def display_title():
    '''
    Displays the program's title formatted with separators.
    '''
    print('=' * 20)
    print(' Leap Year Checker ')
    print('=' * 20)
    print()


def get_year():
    '''
    Prompts the user to input a valid year. 
    It keeps asking until the input is a valid integer greater than 0.
    '''
    while True:
        try:
            year = int(input('Please enter a year: '))
            if year > 0:
                break
            else:
                if year == 0:
                    # Special message for the non-existent year 0.
                    print(f'The year {year} never existed!')
                # This block handles values less than or equal to 0.
                print('Please enter a valid year greater than 0.')
                print()
        except ValueError:
            # This block handles invalid input (non-integer values).
            print('That was not a valid year. Try again!')
            print()

    return year


def check_leap_year(year):
    '''
    Determines if the given year is a leap year based on the rules:
        1. A year is a leap year if it is divisible by 400;
        2. If not divisible by 400, it is a leap year if divisible by 4 but not by 100.
    '''
    if year % 400 == 0:
        # The year is divisible by 400, so it's a leap year.
        is_leap_year = True
    elif year % 4 == 0 and year % 100 != 0:
        # The year is divisible by 4 but not divisible by 100, so it's a leap year.
        is_leap_year = True
    else:
        # The year is not divisible by 400, and either divisible by 100 or not by 4, so not a leap year.
        is_leap_year = False

    return is_leap_year


def display_result(year, is_leap_year):
    '''
    Displays the result based on whether the year is a leap year or not.
    '''
    if is_leap_year:
        print(f'The year {year} is a leap year.')
    else:
        print(f'The year {year} is not a leap year.')


if __name__ == '__main__':
    main()
