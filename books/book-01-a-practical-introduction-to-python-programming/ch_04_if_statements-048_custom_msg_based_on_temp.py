'''
Ask the user to enter a temperature in Celsius. The program should print a message based on the temperature:

	- If the temperature is less than -273.15, print that the temperature is invalid because it is below absolute zero.
	- If it is exactly -273.15, print that the temperature is absolute 0.
	- If the temperature is between -273.15 and 0, print that the temperature is below freezing.
	- If it is 0, print that the temperature is at the freezing point.
	- If it is between 0 and 100, print that the temperature is in the normal range.
	- If it is 100, print that the temperature is at the boiling point.
	- If it is above 100, print that the temperature is above the boiling point.
'''


def main():
	temp_in_celsius = get_temp()
	display_result(temp_in_celsius)


def get_temp() -> float:
	while True:
		try:
			temp = float(input('Enter the temperature in Celsius: '))
			return temp
		except ValueError:
			print('Please enter a number.\n')


def display_result(temp_in_celsius: float) -> None:
	print(f'\n{temp_in_celsius:.2f}°C')

	if temp_in_celsius < -273.15:
		print('The temperature is invalid because it is below absolute zero.')
	elif temp_in_celsius == -273.15:
		print('The temperature is absolute zero.')
	elif -273.15 < temp_in_celsius < 0:
		print('The temperature is below freezing.')
	elif temp_in_celsius == 0:
		print('The temperature is at the freezing point.')
	elif 0 < temp_in_celsius < 100:
		print('The temperature is in the normal range.')
	elif temp_in_celsius == 100:
		print('The temperature is at the boiling point.')
	else:
		print('The temperature is above the boiling point.')


if __name__ == '__main__':
	main()
