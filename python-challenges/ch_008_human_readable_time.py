'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
You can find some examples in the test fixtures.
'''


def make_readable(seconds):
    hours = str(seconds // 3600)
    mins = str((seconds % 3600) // 60)
    secs = str(seconds % 60)
    f_hours = '0' + hours if len(hours) == 1 else hours
    f_mins = '0' + mins if len(mins) == 1 else mins
    f_secs = '0' + secs if len(secs) == 1 else secs
    readable_time = f'{f_hours}:{f_mins}:{f_secs}'
    return readable_time


print(make_readable(359999))
