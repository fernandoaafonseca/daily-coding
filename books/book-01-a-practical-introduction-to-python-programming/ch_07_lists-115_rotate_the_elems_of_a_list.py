'''
Write a program that rotates the elements of a list so that the element at the first index moves to the second index, the element in the second index moves to the third index, etc., and the element in the last index moves to the first index.
'''


def main():
	original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	rotated_list = rotate_elements(original_list)
	display_result(original_list, rotated_list)


def rotate_elements(original_list: list[int]) -> list[int]:
	# Initiates with the index 0 filled with an element, so the for loop can insert at the next index.
	rotated_list = [0]

	for index, item in enumerate(original_list):
		# If it's the last item, insert it at index 0.
		if index == len(original_list) - 1:
			rotated_list[0] = item
		else:
			# Inserts the item at index 0 of original_list in the index 1 of rotated_list and so on.
			rotated_list.insert(index + 1, item)

	return rotated_list


def display_result(original_list: list[int], rotated_list: list[int]) -> None:
	print(f'Original list: \n{original_list}')
	print(f'Rotated list: \n{rotated_list}')


if __name__ == '__main__':
	main()