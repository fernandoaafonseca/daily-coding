'''
A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly how much candy is in the bowl, then you win all the candy. You ask the person in charge the following:

	- If the candy is divided evenly among 5 people, how many pieces would be left over? The answer is 2 pieces.
	- You then ask about dividing the candy evenly among 6 people, and the amount left over is 3 pieces.
	- Finally, you ask about dividing the candy evenly among 7 people, and the amount left over is 2 pieces.
	- By looking at the bowl, you can tell that there are less than 200 pieces.

Write a program to determine how many pieces are in the bowl.
'''


def main():
	qty_of_candies = calculate_amount_of_candies()
	display_result(qty_of_candies)


def calculate_amount_of_candies() -> int:
	'''
	x mod 5 = 2
	x mod 6 = 3
	x mod 7 = 2
	x < 200
	'''
	for qty_of_candies in range(1, 200):
		if (qty_of_candies % 5 == 2) and (qty_of_candies % 6 == 3) and (qty_of_candies % 7 == 2):
			return qty_of_candies


def display_result(qty_of_candies: int) -> None:
	print(f"There are {qty_of_candies} pieces of candy in the bowl.")


if __name__ == '__main__':
	main()