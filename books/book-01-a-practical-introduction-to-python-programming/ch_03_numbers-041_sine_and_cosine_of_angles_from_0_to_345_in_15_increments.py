'''
Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦in 15◦increments. Each result should be rounded to 4 decimal places. Sample output is shown below:

0 --- 0.0 1.0
15 --- 0.2588 0.9659
30 --- 0.5 0.866
...
345 --- -0.2588 0.9659
'''


import math


def main() -> None:
	print(f'xxx° ---  Sine  --- Cosine')
	generate_angles_sines_and_cosines()

def generate_angles_sines_and_cosines():
	for angle_in_degrees in range(0, 345 + 1, 15):
		angle_in_radians = convert_degrees_to_radians(angle_in_degrees)
		sine, cosine = calculate_sin_cos(angle_in_radians)
		display_result(angle_in_degrees, sine, cosine)


def convert_degrees_to_radians(degrees: float) -> float:
	return math.radians(degrees)


def calculate_sin_cos(angle_in_radians: float) -> tuple[float, float]:
	sine = math.sin(angle_in_radians)
	cosine = math.cos(angle_in_radians)

	return sine, cosine


def display_result(angle_in_degrees: float, sine: float, cosine: float) -> None:
	# ":03d" puts zeroes to the left until the number has 3 digits
	print(f'{angle_in_degrees:03d}° --- {sine:.4f} --- {cosine:.4f}')


if __name__ == '__main__':
	main()
