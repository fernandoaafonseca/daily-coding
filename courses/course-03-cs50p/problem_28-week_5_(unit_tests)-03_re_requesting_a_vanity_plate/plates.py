'''
Re-requesting a Vanity Plate

In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

    def main():
        ...


    def is_valid(s):
        ...


    if __name__ == "__main__":
        main()

Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

    pytest test_plates.py

Hints
Be sure to include

    import plates

    or

    from plates import is_valid

atop test_plates.py so that you can call is_valid in your tests.

Take care to return, not print, a bool in is_valid. Only main should call print
'''


def main():
    plate: str = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(user_plate: str) -> bool:
    if not is_plate_length_valid(user_plate):
        # If the length is below 2 characters, or above 6 characters, the plate is "Invalid"
        return False
    elif not is_plate_alphanumeric(user_plate):
        # If the plate has any non-alphanumeric character, the plate is "Invalid"
        return False
    elif is_using_numbers(user_plate):
        # Check if the plate contains any number
        if is_there_any_number_in_first_two_chars(user_plate):
            # If any of the first 2 characters are numbers, the plate is "Invalid"
            return False
        elif is_first_number_a_0(user_plate):
            # If the first number is a "0", the plate is "Invalid"
            return False
        elif not are_numbers_at_the_end(user_plate):
            # If there is any letter after a number, the plate is "Invalid"
            return False
        else:
            # If all conditions with using numbers are met, the plate is "Valid"
            return True

    else:
        # If all conditions are met, the plate is "Valid"
        return True


def is_plate_length_valid(user_plate: str) -> bool:
    '''
    Checks if the plate contains a minimum of 2 and a maximum of 6 characters.
    '''
    if len(user_plate) < 2 or len(user_plate) > 6:
        return False
    else:
        return True


def is_plate_alphanumeric(user_plate: str) -> bool:
    '''
    Checks if the plate contains any non-alphanumeric character.
    '''
    if not user_plate.isalnum():
        return False
    else:
        return True


def is_there_any_number_in_first_two_chars(user_plate: str) -> bool:
    '''
    Checks if the first two characters are numbers.
    '''
    if user_plate[:2].isdigit():
        return True
    else:
        return False


def is_using_numbers(user_plate: str) -> bool:
    '''
    Checks if the plate contains numbers.
    '''
    if any(char.isdigit() for char in user_plate):
        return True
    else:
        return False


def is_first_number_a_0(user_plate: str) -> bool:
    '''
    Finds the first number in the plate. If it's a "0", the plate is "Invalid".
    '''
    first_num = None
    for _, char in enumerate(user_plate):
        if char.isdigit():
            # Find the first number and exit the loop
            first_num = int(char)
            break

    if first_num == 0:
        # Check if the first number is a "0"
        return True
    else:
        return False


def are_numbers_at_the_end(user_plate: str) -> bool:
    '''
    Checks if the numbers are at the end of the plate.
    '''
    found_number = False
    
    for char in user_plate:
        if char.isdigit():
            found_number = True
        elif found_number:
            # If the char is not a digit and "found_number" was set to "True" before, i.e. if there's a letter after a number
            return False

    # If there's no letter after a number
    return True


if __name__ == '__main__':
    main()