'''
Write a censoring program. Allow the user to enter some text and your program should print out the text with all the curse words starred out. The number of stars should match the length of the curse word. For the purposes of this program, just use the“curse” words darn, dang, freakin, heck, and shoot. Sample output is below:

    Enter some text: Oh shoot, I thought I had the dang problem figured out. Darn it. Oh well, it was a heck of a freakin try.

    Oh *****, I thought I had the **** problem figured out. it. Oh well, it was a **** of a ****** try.
'''


import os, string


CURSE_WORDS = ['darn', 'dang', 'freakin', 'heck', 'shoot']


def main():
    text = get_text()
    censored_text = censor_text(text)
    display_result(censored_text)


def press_any_key_to_continue() -> None:
    input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def get_text() -> str:
    while True:
        try:
            press_any_key_to_continue()
            clear_terminal()

            text = input('Enter some text: ')

            if len(text.replace(' ', '')) > 0:
                return text
            else:
                raise ValueError

        except ValueError:
            print('\nPlease enter a non-empty sentence.')


def censor_text(text: str) -> str:
    words = text.split()
    #words = [word.strip(string.punctuation) for word in text]
    censored_text = ''

    for word in words:
        # Check for a final period
        has_period = word.endswith('.')
        if has_period:
            # Remove the period
            word = word[:-1]

        # Check for a comma
        has_comma = word.endswith(',')
        if has_comma:
            # Remove the comma
            word = word[:-1]

        if word.lower() in CURSE_WORDS:
            censored_text += '*' * len(word)
        else:
            censored_text += word

        if has_period:
            # Add back the period
            censored_text += '. '

        elif has_comma:
            # Add back the comma
            censored_text += ', '

        else:
            censored_text += ' '

    return censored_text


def display_result(censored_text: str) -> None:
    press_any_key_to_continue()
    clear_terminal()

    print('Censored text:')
    print(censored_text)


if __name__ == '__main__':
    main()