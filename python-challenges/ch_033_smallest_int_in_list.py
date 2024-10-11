'''
Find the smallest integer in the array

Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
'''


def main():
    user_int_list = get_user_int_list()
    # Ensure the list is not empty
    if user_int_list:
        smallest_int = find_smallest_int(user_int_list)
        print(f"The smallest integer is: {smallest_int}")
    else:
        print("No valid integers were entered.")


def get_user_int_list():
    '''
    Prompts the user to enter a list of integers separated by commas and returns the list.
    '''
    while True:
        try:
            user_input = input(
                'Please enter a list of integers separated by commas: ')
            user_list = user_input.split(',')
            list_of_ints = []
            for num in user_list:
                try:
                    list_of_ints.append(int(num.strip()))
                except ValueError:
                    print(
                        f"'{num.strip()}' is not a valid integer and will be skipped.")
            if list_of_ints:
                return list_of_ints
            else:
                print("No valid integers entered. Try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Try again.")


def find_smallest_int(list_of_ints):
    '''
    Finds and returns the smallest integer in the given list.
    '''
    return min(list_of_ints)


if __name__ == '__main__':
    main()


# Test
print(find_smallest_int([34, 15, 88, 2]) == 2)
print(find_smallest_int([34, -345, -1, 100]) == -345)
print(find_smallest_int([78, 56, 232, 12, 11, 43]) == 11)
print(find_smallest_int([78, 56, -2, 12, 8, -33]) == -33)
print(find_smallest_int([0, 1-2**64, 2**64]) == 1-2**64)
