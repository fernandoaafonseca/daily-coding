'''
Outdated

In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

Hints
#string-methods, including split.
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html
#more-on-lists, among which is index.
Recall that a list comes with quite a few methods, per docs.python.org/3/tutorial/datastructures.html
Note that you can format an int with leading zeroes with code like
print(f"{n:02}")
#format-string-syntax.
wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html
'''


def main():
    months_names = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    raw_month, raw_day, raw_year = get_date()
    month, day, year = format_month_day_year(
        raw_month, raw_day, raw_year, months_names)
    print(generate_formatted_date(month, day, year))


def get_date() -> dict[int | str, int, int]:
    while True:
        try:
            user_input = input('Enter the date: ')
            if '/' in user_input:
                input_month, input_day, input_year = user_input.split('/')

                raw_month = int(input_month)
                raw_day = int(input_day)
                raw_year = int(input_year)

            elif ',' in user_input:
                input_month_and_day, input_year = user_input.split(',')

                try:
                    int(input_month_and_day[0])
                    continue
                except:
                    pass

                raw_day = [int(num)
                           for num in input_month_and_day.split() if num.isdigit()]
                raw_day = raw_day[0]

                raw_month = [char for char in input_month_and_day.split()
                             if char.isalpha()]
                raw_month = raw_month[0]

                raw_year = int(input_year)

            else:
                continue

            month_and_day_are_valid = validate_month_and_day(
                raw_month, raw_day)
            if month_and_day_are_valid:
                break
            else:
                continue

        except:
            continue

    return raw_month, raw_day, raw_year


def check_month_is_valid(raw_month: int | str) -> bool:
    if type(raw_month) is int:
        if raw_month > 12:
            return False
        else:
            return True
    else:
        return True


def check_day_is_valid(raw_day: int) -> bool:
    if raw_day > 31:
        return False
    else:
        return True


def validate_month_and_day(raw_month: int | str, raw_day: int) -> bool:
    month_is_valid = check_month_is_valid(raw_month)
    day_is_valid = check_day_is_valid(raw_day)
    if month_is_valid and day_is_valid:
        return True
    else:
        return False


def format_month_day_year(raw_month: int | str, raw_day: int, raw_year: int, months_names: list[str]) -> dict[str]:
    if raw_month in months_names:
        # If the "raw_month" is a string, get the index of the string on list +1 to find the number of the month
        month = str(months_names.index(raw_month) + 1).zfill(2)
    else:
        # The zfill(x) method fills the number with leading "zeros" until it has "x" digits
        month = str(raw_month).zfill(2)
    day = str(raw_day).zfill(2)
    year = str(raw_year)

    return month, day, year


def generate_formatted_date(month: str, day: str, year: str) -> str:
    return f'{year}-{month}-{day}'


if __name__ == '__main__':
    main()
