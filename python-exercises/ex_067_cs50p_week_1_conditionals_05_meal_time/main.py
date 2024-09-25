'''
Meal Time
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    ...


def convert(time):
    ...


if __name__ == "__main__":
    main()

Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split, which separates a str into a sequence of values, all of which can be assigned to variables at once. For instance, if time is a str like "7:30", then
hours, minutes = time.split(":")
will assign "7" to hours and "30" to minutes.

Keep in mind that there are 60 minutes in 1 hour.
'''


def main():
    user_time = get_user_time()
    time = convert(user_time)
    meal_time = check_meal_time(time)

    print(meal_time)


def get_user_time():
    user_time = input('Type the current time: ')

    return user_time


def convert(user_time):
    raw_hours, raw_minutes = user_time.split(':')
    hours = float(raw_hours)
    minutes = float(raw_minutes)

    if minutes > 0:
        minutes_in_hours = 1 / (60 / minutes)
    else:
        minutes_in_hours = 0
    time = hours + minutes_in_hours

    return time


def check_meal_time(time):
    if 7 <= time <= 8:
        meal_time = 'breakfast time'
    elif 12 <= time <= 13:
        meal_time = 'lunch time'
    elif 18 <= time <= 19:
        meal_time = 'dinner time'
    else:
        meal_time = ''

    return meal_time


if __name__ == '__main__':
    main()


# Test:
test_time = convert('7:00')
print(check_meal_time(test_time) == 'breakfast time')

test_time = convert('7:30')
print(check_meal_time(test_time) == 'breakfast time')

test_time = convert('8:01')
print(check_meal_time(test_time) == '')

test_time = convert('18:01')
print(check_meal_time(test_time) == 'dinner time')

test_time = convert('18:59')
print(check_meal_time(test_time) == 'dinner time')

test_time = convert('12:42')
print(check_meal_time(test_time) == 'lunch time')

test_time = convert('18:32')
print(check_meal_time(test_time) == 'dinner time')

test_time = convert('11:11')
print(check_meal_time(test_time) == '')
