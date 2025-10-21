'''
Write a program that asks the user for a number and then prints out the sine, cosine, and tangent of that number.
'''


import math


def main() -> None:
	angle_in_degrees = get_angle_in_degrees()
	angle_in_radians = convert_degrees_to_radians(angle_in_degrees)
	sine, cosine, tangent = calculate_sin_cos_tan(angle_in_radians)
	display_result(angle_in_degrees, angle_in_radians, sine, cosine, tangent)


def get_angle_in_degrees() -> float:
	while True:
		try:
			angle_in_degrees = float(input('Enter an angle in degrees (°): '))
			return angle_in_degrees
		except ValueError:
			print('Please enter a valid number.\n')


def convert_degrees_to_radians(degrees: float) -> float:
	return math.radians(degrees)


def calculate_sin_cos_tan(angle_in_radians: float) -> tuple[float, float, float | str]:
	sine = math.sin(angle_in_radians)
	cosine = math.cos(angle_in_radians)

	if abs(cosine) < 1e-12:
		tangent = 'undefined'
	else:
		tangent = sine / cosine

	return sine, cosine, tangent


def display_result(angle_in_degrees: float, angle_in_radians: float, sine: float, cosine: float, tangent: float) -> None:
	print(f'The angle {angle_in_degrees:.2f}° is {angle_in_radians:.4f} rad.')
	print(f'Sine: {sine:.6f}')
	print(f'Cosine: {cosine:.6f}')
	if isinstance(tangent, float):
		print(f'Tangent: {tangent:.6f}')
	else:
		print(f'Tangent: {tangent}')


if __name__ == '__main__':
	main()
