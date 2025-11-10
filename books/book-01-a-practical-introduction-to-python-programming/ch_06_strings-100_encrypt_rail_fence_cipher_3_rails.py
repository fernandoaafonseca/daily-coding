'''
A more general version of the above technique is the "rail fence cipher", where instead of breaking things into evens and odds, they are broken up by threes, fours or something larger. For instance, in the case of threes, the string "secret message" would be broken into three groups. The first group is "sr sg", the characters at indices 0, 3, 6, 9 and 12. The second group is "eemse", the characters at indices 1, 4, 7, 10, and 13. The last group is "ctea", the characters at indices 2, 5, 8, and 11. The encrypted message is "sr sgeemsectea".

    (a) Write a program the asks the user for a string and uses the rail fence cipher in the threes case to encrypt the string.
    (b) Write a decryption program for the threes case.
    (c) Write a program that asks the user for a string, and an integer determining whether to break things up by threes, fours, or whatever. Encrypt the string using the rail-fence cipher.
    (d) Write a decryption program for the general case.
'''


def main() -> None:
    user_string = get_user_string()
    encrypted_str = encrypt_rail_fence_three(user_string)
    display_result(encrypted_str)


def get_user_string() -> str:
    while True:
        try:
            user_string = str(input('Enter a message to be decrypted: '))
            if len(user_string.replace(' ', '')) > 0:
                return user_string
            else:
                raise ValueError
        except ValueError:
            print('\nPlease enter a non-empty string.\n')


def encrypt_rail_fence_three(user_string: str) -> str:
    first_part = user_string[0::3]
    second_part = user_string[1::3]
    third_part = user_string[2::3]

    return first_part + second_part + third_part


def display_result(encrypted_str: str) -> None:
    print()
    print('Encrypted message:')
    print(encrypted_str)


if __name__ == "__main__":
    main()