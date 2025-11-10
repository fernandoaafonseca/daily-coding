'''
A more general version of the above technique is the "rail fence cipher", where instead of breaking things into evens and odds, they are broken up by threes, fours or something larger. For instance, in the case of threes, the string "secret message" would be broken into three groups. The first group is "sr sg", the characters at indices 0, 3, 6, 9 and 12. The second group is "eemse", the characters at indices 1, 4, 7, 10, and 13. The last group is "ctea", the characters at indices 2, 5, 8, and 11. The encrypted message is "sr sgeemsectea".

    (a) Write a program the asks the user for a string and uses the rail fence cipher in the threes case to encrypt the string.
    (b) Write a decryption program for the threes case.
    (c) Write a program that asks the user for a string, and an integer determining whether to break things up by threes, fours, or whatever. Encrypt the string using the rail-fence cipher.
    (d) Write a decryption program for the general case.
'''


def main() -> None:
    user_string = get_user_string()
    num_rails = get_num_rails(user_string)
    decrypted_str = decrypt_rail_fence_three(user_string, num_rails)
    display_result(decrypted_str)


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


def get_num_rails(user_string: str) -> int:
    while True:
        try:
            num_rails = int(input('Enter the number of rails: '))
            if len(user_string) > num_rails:
                return num_rails
            else:
                raise ValueError
        except ValueError:
            print('\nPlease enter a value smaller than the length of the message.\n')


def decrypt_rail_fence_three(user_string: str, num_rails: int) -> str:
    '''
    Generalized Rail Fence Cipher decryption for any number of rails.
    It reconstructs each rail based on the number of characters per rail,
    then reassembles the message in the original order.
    '''
    length = len(user_string)
    rail_len = [length // num_rails + (1 if i < length % num_rails else 0) for i in range(num_rails)]

    rails = []
    index = 0
    for l in rail_len:
        rails.append(user_string[index:index + l])
        index += l

    decrypted_str = ''
    for i in range(max(rail_len)):
        for r in range(num_rails):
            if i < len(rails[r]):
                decrypted_str += rails[r][i]

    return decrypted_str


def display_result(decrypted_str: str) -> None:
    print()
    print('Decrypted message:')
    print(decrypted_str)


if __name__ == "__main__":
    main()