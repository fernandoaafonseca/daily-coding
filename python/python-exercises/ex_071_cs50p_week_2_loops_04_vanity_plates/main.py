'''
Vanity Plates

In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

    - “All vanity plates must start with at least two letters.”
    
    - “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    
    - “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    
    - “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()

Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
Much like a list, a str is a “sequence” (of characters), which means it can be “sliced” into shorter strings with syntax like s[i:j]. For instance, if s is "CS50", then s[0:2] would be "CS".
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
            # If there's a letter after a number, the plate is "Invalid"
            return False

    return True

    return True


if __name__ == '__main__':
    main()


# Test:
print(is_valid('CS50') == True)

print(is_valid('CS05') == False)

print(is_valid('CS50P') == False)

print(is_valid('CS50P2') == False)

print(is_valid('PI3.14') == False)

print(is_valid('H') == False)

print(is_valid('OUTATIME') == False)

print(is_valid('50CS') == False)

print(is_valid('5CS') == False)
