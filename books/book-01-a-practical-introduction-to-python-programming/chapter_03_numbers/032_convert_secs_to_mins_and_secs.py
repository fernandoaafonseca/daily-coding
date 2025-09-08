'''
Write a program that asks the user for a number of seconds and prints out how many minutes and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds.

[Hint: Use the // operator to get minutes and the % operator to get seconds.]
'''


def main() -> None:
	secs = get_secs()
	total_mins, remaining_secs = convert_secs_to_mins(secs)
	display_result(total_mins, remaining_secs)


def get_secs() -> int:
	while True:
		try:
			secs = int(input('Enter the number of seconds: '))
			break
		except:
			print('Please enter an integer number.')
			print()

	return secs


def convert_secs_to_mins(secs: int) -> tuple[int, int]:
	total_mins = secs // 60
	remaining_secs = secs % 60

	return total_mins, remaining_secs


def display_result(total_mins, remaining_secs) -> None:
	print()

	if remaining_secs > 0:
		print(f'{total_mins}m, {remaining_secs}s')
	else:
		print(f'{total_mins}m')


if __name__ == '__main__':
	main()