'''
Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M. For instance, if L = [3, 1, 4] and M = [1, 5, 9], then N should equal [4, 6, 13].
'''


def main() -> None:
	L, M = get_two_lists_same_size()
	sums_L_M = sum_lists_elements(L, M)
	display_result(L, M, sums_L_M)


def get_two_lists_same_size() -> tuple[list[int], list[int]]:
	while True:
		try:
			print('Please enter two list of the same size.')
			L = get_list_of_ints(1)
			M = get_list_of_ints(2)

			if len(L) == len(M):
				return L, M
			else:
				raise ValueError
		except:
			print('\nThe two lists must have the same size.\n')


def get_list_of_ints(list_num: int) -> list[int]:
	while True:
		try:
			print(f'\nList #{list_num}')
			str_of_ints = str(input('Enter a list of integers separated by commas (like "1, 2, 3"): '))
			# Generates a list of "ints" splitting the string by "commas"
			list_of_ints = [int(item) for item in str_of_ints.split(',')]
			return list_of_ints
		except ValueError:
			print('\nPlease only enter integers separated by commas.\n')


def sum_lists_elements(L: list[int], M: list[int]) -> list[int]:
	sums_L_M = []

	for i in range(len(L)):
		sums_L_M.append(L[i] + M[i])

	return sums_L_M



def display_result(L: list[int], M: list[int], sums_L_M: list[int]) -> None:
	print()
	print(f'First list: \n{L}')
	print(f'\nSecond list: \n{M}')
	print(f'\nSums of corresponding elements of both lists: \n{sums_L_M}')


if __name__ == '__main__':
	main()