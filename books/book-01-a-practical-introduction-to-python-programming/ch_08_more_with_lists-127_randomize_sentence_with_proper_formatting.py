'''
(a) Write a program that asks the user to enter a sentence and then randomly rearranges the words of the sentence. Don’t worry about getting punctuation or capitalization correct.
(b) Do the above problem, but now make sure that the sentence starts with a capital, that the original first word is not capitalized if it comes in the middle of the sentence, and that the period is in the right place.
'''


import os, random


def main():
    text = get_text()
    randomized = randomize_words_order_proper(text)
    display_result(text, randomized)


def press_any_key_to_continue() -> None:
    input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def get_text() -> str:
    while True:
        try:
            press_any_key_to_continue()
            clear_terminal()

            text = input('Enter a sentence: ').strip()

            if len(text.replace(' ', '')) > 0:
                return text
            else:
                raise ValueError

        except ValueError:
            print('\nPlease enter a non-empty sentence.')


def randomize_words_order_proper(text: str) -> str:
    '''
    Randomly rearrange the words of a sentence while ensuring:
    - The sentence starts with a capital letter.
    - The original first word is not capitalized if it appears elsewhere.
    - The final period is placed at the end.
    '''

    text = text.strip()

    # Check for a final period
    has_period = text.endswith('.')
    if has_period:
        text = text[:-1]  # remove the period

    # Convert all to lowercase first
    words = text.split()
    original_first = words[0].lower()
    words = [w.lower() for w in words]

    # Shuffle words
    random.shuffle(words)

    # Capitalize the new first word
    words[0] = words[0].capitalize()

    # Rebuild sentence
    randomized = " ".join(words)

    # Add back the period
    if has_period:
        randomized += "."

    return randomized


def display_result(original: str, randomized: str) -> None:
    press_any_key_to_continue()
    clear_terminal()

    print(f'Original sentence: {original}')
    print(f'Randomized sentence: {randomized}')


if __name__ == '__main__':
    main()