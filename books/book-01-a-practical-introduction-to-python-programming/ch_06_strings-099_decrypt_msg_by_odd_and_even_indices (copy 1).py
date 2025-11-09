'''
A simple way of encrypting a message is to rearrange its characters. One way to rearrange the characters is to pick out the characters at even indices, put them first in the encrypted string, and follow them by the odd characters. For example, the string message would be encrypted as msaeesg because the even characters are m, s, a, e (at indices 0, 2, 4, and 6) and the odd characters are e, s, g (at indices 1, 3, and 5).

    (a) Write a program that asks the user for a string and uses this method to encrypt the string.
    (b) Write a program that decrypts a string that was encrypted with this method.
'''


def main() -> None:
    user_string = get_user_string()
    decrypted_str = decrypt_str(user_string)
    display_result(decrypted_str)


def get_user_string() -> str:
    while True:
        try:
            user_string = str(input('Enter a message to be decrypted: '))
            return user_string
        except ValueError:
            print('\nPlease enter a valid string.\n')


def decrypt_str(user_string: str) -> str:
    even_chars = ''
    odd_chars = ''
    mid_char = len(user_string) // 2

    for index, char in enumerate(user_string):
        if index <= mid_char:
            even_chars += char
        else:
            odd_chars += char

    decrypted_str = ''

    length = mid_char if mid_char % 2 == 0 else mid_char + 1
    for i in range(length):
        if i != length - 1:
            decrypted_str += even_chars[i] + odd_chars[i]
        else:
            decrypted_str += even_chars[i]

    return decrypted_str


def display_result(decrypted_str: str) -> None:
    print()
    print('Decrypted message:')
    print(decrypted_str)


if __name__ == "__main__":
    main()