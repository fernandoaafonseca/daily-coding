'''
An integer is called "squarefree" if it is not divisible by any perfect squares other than 1. For instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is divisible by 9, which is a perfect square. Write a program that asks the user for an integer and tells them if it is squarefree or not.
'''


def main():
	num = get_num()
	divisors = get_divisors(num)
	is_squarefree = check_is_squarefree(divisors)
	display_result(num, is_squarefree)

	# TESTS
	run_simple_tests()
	run_brute_force_tests()


def get_num() -> int:
	while True:
		try:
			num = int(input('Enter an integer: '))
			return num
		except ValueError:
			print('\nPlease enter a valid integer.\n')


def get_divisors(number: int) -> list[int]:
	# To get all the divisors for negative integers too
	number = abs(number)
	divisors = []

	for i in range(1, number + 1):
		if number % i == 0:
			divisors.append(i)

	return divisors


def check_is_squarefree(divisors: list[int]) -> bool:
	'''
	An integer is called "squarefree" if it is not divisible by any perfect squares other than 1.
	'''
	if divisors:
		# Checks if the number is not "0", i.e., the list of divisors is not empty
		for i in range(1, len(divisors)):
			# Starts at index "1" because we want to ignore the number 1 (the first divisor)
			divisor = divisors[i]
			is_a_perfect_square = check_is_a_perfect_square(divisor)
			if is_a_perfect_square:
				return False

		return True

	else:
		return False


def check_is_a_perfect_square(x: int) -> bool:
	'''
	A perfect square is an integer that is the product of an integer multiplied by itself, or n**2.
	'''
	for i in range(2, x + 1):
		if i ** 2 == x:
			return True

	return False


def display_result(num: int, is_squarefree: bool) -> None:
	output = 'is' if is_squarefree else 'is not'
	print(f'\nThe number {num} {output} squarefree.')


def run_simple_tests() -> None:
	input('\n⏳ PRESS ANY KEY TO START THE SIMPLE TESTS...')

	print('📝 ===== BASIC TESTS ===== 📝')

	test_num_1 = 42
	print(f'\nTest number: {test_num_1}')
	divisors = get_divisors(test_num_1)
	is_squarefree = check_is_squarefree(divisors)
	print(is_squarefree == True)

	test_num_2 = 45
	print(f'\nTest number: {test_num_2}')
	divisors = get_divisors(test_num_2)
	is_squarefree = check_is_squarefree(divisors)
	print(is_squarefree == False)

	test_num_3 = -2
	print(f'\nTest number: {test_num_3}')
	divisors = get_divisors(test_num_3)
	is_squarefree = check_is_squarefree(divisors)
	print(is_squarefree == True)

	test_num_4 = -6
	print(f'\nTest number: {test_num_4}')
	divisors = get_divisors(test_num_4)
	is_squarefree = check_is_squarefree(divisors)
	print(is_squarefree == True)

	test_num_5 = 0
	print(f'\nTest number: {test_num_5}')
	divisors = get_divisors(test_num_5)
	is_squarefree = check_is_squarefree(divisors)
	print(is_squarefree == False)

	test_num_6 = 998
	print(f'\nTest number: {test_num_6}')
	divisors = get_divisors(test_num_6)
	is_squarefree = check_is_squarefree(divisors)
	print(is_squarefree == True)

	test_num_7 = -998
	print(f'\nTest number: {test_num_7}')
	divisors = get_divisors(test_num_7)
	is_squarefree = check_is_squarefree(divisors)
	print(is_squarefree == True)

	print('=' * 20)


def run_brute_force_tests() -> None:
	'''
	Up to 1000, there are 608 squarefree numbers.
	'''
	input('\n⏳ PRESS ANY KEY TO START THE BRUTE FORCE TESTS...')

	HIGHER_BOUND = 1000
	quantity_of_squarefree_numbers = 0
	list_of_squarefree_numbers = []

	EXPECTED_LIST_OF_SQUAREFREE_NUMBERS = [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 46, 47, 51, 53, 55, 57, 58, 59, 61, 62, 65, 66, 67, 69, 70, 71, 73, 74, 77, 78, 79, 82, 83, 85, 86, 87, 89, 91, 93, 94, 95, 97, 101, 102, 103, 105, 106, 107, 109, 110, 111, 113, 114, 115, 118, 119, 122, 123, 127, 129, 130, 131, 133, 134, 137, 138, 139, 141, 142, 143, 145, 146, 149, 151, 154, 155, 157, 158, 159, 161, 163, 165, 166, 167, 170, 173, 174, 177, 178, 179, 181, 182, 183, 185, 186, 187, 190, 191, 193, 194, 195, 197, 199, 201, 202, 203, 205, 206, 209, 210, 211, 213, 214, 215, 217, 218, 219, 221, 222, 223, 226, 227, 229, 230, 231, 233, 235, 237, 238, 239, 241, 246, 247, 249, 251, 253, 254, 255, 257, 258, 259, 262, 263, 265, 266, 267, 269, 271, 273, 274, 277, 278, 281, 282, 283, 285, 286, 287, 290, 291, 293, 295, 298, 299, 301, 302, 303, 305, 307, 309, 310, 311, 313, 314, 317, 318, 319, 321, 322, 323, 326, 327, 329, 330, 331, 334, 335, 337, 339, 341, 345, 346, 347, 349, 353, 354, 355, 357, 358, 359, 362, 365, 366, 367, 370, 371, 373, 374, 377, 379, 381, 382, 383, 385, 386, 389, 390, 391, 393, 394, 395, 397, 398, 399, 401, 402, 403, 406, 407, 409, 410, 411, 413, 415, 417, 418, 419, 421, 422, 426, 427, 429, 430, 431, 433, 434, 435, 437, 438, 439, 442, 443, 445, 446, 447, 449, 451, 453, 454, 455, 457, 458, 461, 462, 463, 465, 466, 467, 469, 470, 471, 473, 474, 478, 479, 481, 482, 483, 485, 487, 489, 491, 493, 494, 497, 498, 499, 501, 502, 503, 505, 506, 509, 510, 511, 514, 515, 517, 518, 519, 521, 523, 526, 527, 530, 533, 534, 535, 537, 538, 541, 542, 543, 545, 546, 547, 551, 553, 554, 555, 557, 559, 561, 562, 563, 565, 566, 569, 570, 571, 573, 574, 577, 579, 581, 582, 583, 586, 587, 589, 590, 591, 593, 595, 597, 598, 599, 601, 602, 606, 607, 609, 610, 611, 613, 614, 615, 617, 618, 619, 622, 623, 626, 627, 629, 631, 633, 634, 635, 638, 641, 642, 643, 645, 646, 647, 649, 651, 653, 654, 655, 658, 659, 661, 662, 663, 665, 667, 669, 670, 671, 673, 674, 677, 678, 679, 681, 682, 683, 685, 687, 689, 690, 691, 694, 695, 697, 698, 699, 701, 703, 705, 706, 707, 709, 710, 713, 714, 715, 717, 718, 719, 721, 723, 727, 730, 731, 733, 734, 737, 739, 741, 742, 743, 745, 746, 749, 751, 753, 754, 755, 757, 758, 759, 761, 762, 763, 766, 767, 769, 770, 771, 773, 777, 778, 779, 781, 782, 785, 786, 787, 789, 790, 791, 793, 794, 795, 797, 798, 799, 802, 803, 805, 806, 807, 809, 811, 813, 814, 815, 817, 818, 821, 822, 823, 826, 827, 829, 830, 831, 834, 835, 838, 839, 842, 843, 849, 851, 853, 854, 857, 858, 859, 861, 862, 863, 865, 866, 869, 870, 871, 874, 877, 878, 879, 881, 883, 885, 886, 887, 889, 890, 893, 894, 895, 897, 898, 899, 901, 902, 903, 905, 906, 907, 910, 911, 913, 914, 915, 917, 919, 921, 922, 923, 926, 929, 930, 933, 934, 935, 937, 938, 939, 941, 942, 943, 946, 947, 949, 951, 953, 955, 957, 958, 959, 962, 965, 966, 967, 969, 970, 971, 973, 974, 977, 978, 979, 982, 983, 985, 986, 987, 989, 991, 993, 994, 995, 997, 998]
	EXPECTED_QUANTITY_OF_SQUAREFREE_NUMBERS = len(EXPECTED_LIST_OF_SQUAREFREE_NUMBERS)

	for i in range(HIGHER_BOUND + 1):
		test_num = i
		divisors = get_divisors(test_num)
		is_squarefree = check_is_squarefree(divisors)
		if is_squarefree:
			quantity_of_squarefree_numbers += 1
			list_of_squarefree_numbers.append(test_num)

	print('\n\n💪 ===== BRUTE FORCE TEST ===== 💪')
	print(f'The expected quantity of squarefree numbers from 1 to {HIGHER_BOUND} is: {EXPECTED_QUANTITY_OF_SQUAREFREE_NUMBERS}.')
	print(f'The calculated amount of squarefree numbers was: {quantity_of_squarefree_numbers}')

	if EXPECTED_QUANTITY_OF_SQUAREFREE_NUMBERS == quantity_of_squarefree_numbers:
		print('✅ SUCCESS! The calculated quantity is correct.')
	else:
		print('⚠️ FAILURE! The calculated quantity differs from the expected one.')

	print(f'\nChecking if the generated list of squarefree numbers is equal to the expected list...')
	if list_of_squarefree_numbers == EXPECTED_LIST_OF_SQUAREFREE_NUMBERS:
		print('✅ SUCCESS! The program generated exactly the expected list of squarefree numbers')
	else:
		print('⚠️ FAILURE! The program generated a different list than expected.')
		# Elements in list1 but not in list2
		unique_to_generated_list = list(set(list_of_squarefree_numbers) - set(EXPECTED_LIST_OF_SQUAREFREE_NUMBERS))
		print(f"Elements unique to the generated list: {unique_to_generated_list}")
		print(f'Quantity of unique elements: {len(unique_to_generated_list)}')

		# Elements in list2 but not in list1
		unique_to_expected_list = list(set(EXPECTED_LIST_OF_SQUAREFREE_NUMBERS) - set(list_of_squarefree_numbers))
		print(f"Elements unique to the expected list: {unique_to_expected_list}")
		print(f'Quantity of unique elements: len(unique_to_expected_list)')

		print('=' * 20)


if __name__ == '__main__':
	main()