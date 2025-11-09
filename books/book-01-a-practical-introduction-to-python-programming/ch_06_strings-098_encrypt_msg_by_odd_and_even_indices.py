'''
A simple way of encrypting a message is to rearrange its characters. One way to rearrange the characters is to pick out the characters at even indices, put them first in the encrypted string, and follow them by the odd characters. For example, the string message would be encrypted as msaeesg because the even characters are m, s, a, e (at indices 0, 2, 4, and 6) and the odd characters are e, s, g (at indices 1, 3, and 5).

    (a) Write a program that asks the user for a string and uses this method to encrypt the string.
    (b) Write a program that decrypts a string that was encrypted with this method.
'''



def main() -> None:
    user_string = get_user_string()
    encrypted_str = encrypt_str(user_string)
    display_result(encrypted_str)


def get_user_string() -> str:
    while True:
        try:
            user_string = str(input('Enter a message to be encrypted: '))
            return user_string
        except ValueError:
            print('\nPlease enter a valid string.\n')


def encrypt_str(user_string: str) -> str:
    initial_chars = ''
    final_chars = ''

    for index, char in enumerate(user_string):
        if index % 2 == 0:
            initial_chars += char
        else:
            final_chars += char

    encrypted_str = initial_chars + final_chars

    return encrypted_str


def display_result(encrypted_str: str) -> None:
    print()
    print('Encrypted message:')
    print(encrypted_str)


if __name__ == "__main__":
    main()
