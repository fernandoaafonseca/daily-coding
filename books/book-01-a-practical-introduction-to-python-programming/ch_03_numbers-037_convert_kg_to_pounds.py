'''
Write a program that asks the user to enter a weight in kilograms. The program should convert it to pounds, printing the answer rounded to the nearest tenth of a pound.
'''


def main() -> None:
	kg = get_kg()
	pounds = convert_kg_to_pounds(kg)
	display_result(kg, pounds)


def get_kg() -> float:
	while True:
		try:
			return float(input('Enter a weight in kilograms: '))
		except ValueError:
			print('Please enter a number.\n')


def convert_kg_to_pounds(kg: float) -> float:
	pounds = kg * 2.20462262185
	return round(pounds, 1)


def display_result(kg: float, pounds: float) -> None:
	print(f'{kg} kg = {pounds} lb')


if __name__ == '__main__':
	main()