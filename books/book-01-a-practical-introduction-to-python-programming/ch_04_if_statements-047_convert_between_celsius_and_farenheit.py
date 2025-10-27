'''
Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in. Your program should convert the temperature to the other unit. The conversions are F = 9 / 5 * C + 32 and C = 5 / 9 * (F − 32).
'''


def main():
	original_temp = get_temp()
	original_temp_unit = get_temp_unit()
	if original_temp_unit == 'c':
		converted_temp = convert_celsius_to_farenheit(original_temp)
	elif original_temp_unit == 'f':
		converted_temp = convert_farenheit_to_celsius(original_temp)

	display_result(original_temp_unit, original_temp, converted_temp)


def get_temp() -> float:
	while True:
		try:
			original_temp = float(input('Enter the temperature: '))
			return original_temp
		except ValueError:
			print('Please enter a number.\n')


def get_temp_unit() -> str:
	valid_units = ['c', 'f']

	while True:
		try:
			unit = str(input('Enter the unit - Celsius (C) or Farenheit (F): '))
			unit_letter = unit[0].lower()
			if unit_letter in valid_units:
				return unit_letter
			else:
				raise ValueError
		except ValueError:
			print('Please enter a valid unit ("C" or "F")./n')


def convert_celsius_to_farenheit(original_temp: float) -> float:
	return 9 / 5 * original_temp + 32


def convert_farenheit_to_celsius(original_temp: float) -> float:
	return 5 / 9 * (original_temp - 32)


def display_result(original_temp_unit: str, original_temp: float, converted_temp: float) -> None:
	if original_temp_unit == 'c':
		print(f'{original_temp}°C = {converted_temp}°F')
	elif original_temp_unit == 'f':
		print(f'{original_temp}°F = {converted_temp}°C')


if __name__ == '__main__':
	main()
