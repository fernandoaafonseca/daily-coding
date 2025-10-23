'''
Write a program that asks the user to enter an angle in degrees and prints out the sine of that angle.
'''


import math


def main() -> None:
	angle_in_degrees = get_angle_in_degrees()
	angle_in_radians = convert_degrees_to_radians(angle_in_degrees)
	sine = calculate_sin(angle_in_radians)
	display_result(angle_in_degrees, angle_in_radians, sine)


def get_angle_in_degrees() -> float:
	while True:
		try:
			angle_in_degrees = float(input('Enter an angle in degrees (°): '))
			return angle_in_degrees
		except ValueError:
			print('Please enter a valid number.\n')


def convert_degrees_to_radians(degrees: float) -> float:
	return math.radians(degrees)


def calculate_sin(angle_in_radians: float) -> float:
	return math.sin(angle_in_radians)


def display_result(angle_in_degrees: float, angle_in_radians: float, sine: float) -> None:
	print(f'The angle {angle_in_degrees:.2f}° is {angle_in_radians:.4f} rad.')
	print(f'Sine: {sine:.6f}')


if __name__ == '__main__':
	main()
