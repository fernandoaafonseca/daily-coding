'''
Write a program that asks the user for a weight in kilograms and converts it to pounds. There
are 2.2 pounds in a kilogram.
'''


def main() -> None:
	weight_kg = float(input('Enter your weight in Kg: '))
	weight_lbs = convert_kg_to_pounds(weight_kg)

	print(f'Your weight in pounds is: {weight_lbs} lbs.')


def convert_kg_to_pounds(weight_kg: float) -> float:
	conversion_factor = 2.20462
	weight_lbs = weight_kg * conversion_factor

	return weight_lbs



if __name__ == '__main__':
	main()