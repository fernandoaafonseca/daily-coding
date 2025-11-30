'''
(a) Write a program that uses a while loop (not a for loop) to read through a string and print the characters of the string one-by-one on separate lines.
(b) Modify the program above to print out every second character of the string.
'''


import os


def main() -> None:
    user_str = get_string()
    display_result(user_str)


def press_any_key_to_continue() -> None:
    input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def get_string() -> str:
    while True:
        try:
            clear_terminal()

            user_str = str(input('Enter a string: '))

            if len(user_str.replace(' ', '')) > 0:
                return user_str
            else:
                raise ValueError

        except ValueError:
            print('\nPlease enter a non-empty string.')
            press_any_key_to_continue()


def display_result(user_str: str) -> None:
    for index, char in enumerate(user_str):
        if index % 2 != 0:
            print(char)


if __name__ == '__main__':
    main()