'''
Section 8.3 described how to use the shuffle method to create a random anagram of a string. Use the choice method to create a random anagram of a string.
'''


import os, random


def main() -> None:
    word = get_user_word()
    anagram = create_anagram(word)
    display_result(word, anagram)


def press_any_key_to_continue() -> None:
    input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_word() -> str:
    while True:
        try:
            clear_terminal()
            user_word = str(input('Enter a word: '))
            if user_word.isalpha():
                return user_word
            else:
                raise ValueError
        except ValueError:
            print('\nPlease enter a single word.\n')
            press_any_key_to_continue()


def create_anagram(word: str) -> str:
    '''
    Return a random anagram of the string using random.choice().
    '''
    letters = [char for char in word]
    anagram = ''

    for _ in range(len(letters)):
        new_letter = random.choice(letters)
        anagram += new_letter.lower()
        letters.remove(new_letter)

    return anagram


def display_result(word: str, anagram: str) -> None:
    press_any_key_to_continue()
    clear_terminal()

    print(f'Your original word: {word}')
    print(f'Random anagram: {anagram}')


if __name__ == '__main__':
    main()