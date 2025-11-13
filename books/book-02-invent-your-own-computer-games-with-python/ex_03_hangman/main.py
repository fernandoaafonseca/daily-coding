'''
python3 -m venv .venv
source .venv/bin/activate
pip install colorama
'''

import os, random, string, unicodedata
from colorama import Fore, Back, Style
from assets.ascii_hangman_drawings import STAGES
from assets.ascii_hangman_logo import LOGO
from assets import en_words, pt_words


ALPHABET = string.ascii_lowercase


def main() -> None:
    game_loop()


def game_loop() -> None:
    player_lives, language, list_of_words, word = game_setup()
    game_over = False

    clear_terminal()
    display_logo()
    display_hangman_drawing(player_lives)

    print(word)

    guessed_letters = []

    display_word_board(word, guessed_letters)

    while not game_over:
        player_letter = get_player_letter(player_lives)
        is_player_letter_in_word = check_letter_in_word(player_letter, word)

        if is_player_letter_in_word:
            # If the player guesses a letter correctly, it is added to the list of guessed letters.
            guessed_letters.append(player_letter)
        else:
            # If the player gets a letter wrong, he loses a life.
            player_lives -= 1

        game_over = check_player_won(guessed_letters, word)

        if game_over or player_lives == 0:
            break

        clear_terminal()
        display_logo()
        display_hangman_drawing(player_lives)
        display_word_board(word, guessed_letters)

    clear_terminal()
    display_logo()
    display_hangman_drawing(player_lives)
    display_word_board(word, guessed_letters)
    print('GAME OVER!')


def game_setup() -> tuple[int, int, list[str], str]:
    clear_terminal()
    display_logo()

    player_lives = 6
    language = get_words_language()
    list_of_words = get_words_list(language)
    word = get_random_word(list_of_words).lower()
    word = remove_accents(word)

    return player_lives, language, list_of_words, word


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def press_any_key_to_continue() -> None:
    input('\nPRESS ANY KEY TO CONTINUE...')


def display_logo() -> None:
    '''
    Displays an ASCII art of the word "hangman".
    '''
    print(f'{Fore.BLUE}{LOGO}{Style.RESET_ALL}')


def display_hangman_drawing(player_lives: int) -> None:
    '''
    The STAGES list contains 7 Hangman drawings, with index 0 being the starting point (when the player has 7 lives) and index 6 being the end point (when the player loses the game).
    '''
    print(f'{Fore.YELLOW}{STAGES[player_lives]}{Style.RESET_ALL}')


def display_word_board(word: str, guessed_letters: list[str]) -> None:

    word_board = ''

    for index, letter in enumerate(word):
        current_letter = word[index]
        if current_letter in guessed_letters:
            # Adds the letter if the player has already guessed it.
            word_board += current_letter
        else:
            # Adds an empty space where the player has not yet guessed the letter.
            word_board += '_.'

    print(f'{Fore.GREEN}{word_board}{Style.RESET_ALL}\n\n')


def get_words_language() -> int:
    while True:
        try:
            print('Choose your language:\n')
            print('1 - English')
            print('2 - Português')
            language = int(input())

            if language in [1, 2]:
                return language
            else:
                raise ValueError
        except ValueError:
            print('\nPlease enter 1 or 2.\n')


def get_words_list(language: str):
    '''
    Returns the list of words according to the chosen language.
    1 -> English
    2 -> Brazilian Portuguese
    '''
    if language == 1:
        return en_words.WORDS
    elif language == 2:
        return pt_words.WORDS
    else:
        raise ValueError(f'"{language}" language not available.')


def get_random_word(list_of_words: list[str]) -> str:
    return random.choice(list_of_words)


def get_player_letter(player_lives: int) -> str:
    pt_chars = ['á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'ô', 'ã', 'õ', 'à']

    while True:
        try:
            user_string = str(input('Guess a letter:\n')).strip().lower()
            player_letter = remove_accents(user_string)
            if player_letter in ALPHABET:
                return player_letter
            else:
                raise ValueError
        except ValueError:
            print('\nPlease enter a letter.')
            press_any_key_to_continue()
            clear_terminal()
            display_logo()
            display_hangman_drawing(player_lives)


def remove_accents(user_string: str) -> str:
    '''
    Remove accents and normalize uppercase/lowercase letters.
    '''
    normalized = unicodedata.normalize('NFD', user_string)
    return ''.join(ch for ch in normalized if unicodedata.category(ch) != 'Mn')


def check_letter_in_word(player_letter: str, word: str) -> bool:
    normalized_word = remove_accents(word.lower())
    normalized_letter = remove_accents(player_letter.lower())

    return normalized_letter in normalized_word


def check_player_won(guessed_letters: list[str], word: str) -> bool:
    '''
    Checks if all elements of "guessed_letters" are in "word"
    '''
    return all(letter in guessed_letters for letter in word)


def tchururum():
    # initializes some variables to keep track of the game state
    lives = 6
    position = 0
    right_letters = 0
    track = 0

    while lives > 0:
    # prints the number of lives left
        if lives > 1:
            print(f'You have {lives} lives left.')
        else:
            print(f'You have {lives} live left.')

    # prints the ASCII art for the player's current lives
        print(f'{Fore.YELLOW}{stages[lives]}{Style.RESET_ALL}')

    # asks the user to write a letter
        guess = input('Guess a letter:\n').lower()
        position = 0
        track = 0
        os.system('cls')

    # checks if the letter is in the chosen word
        for letter in chosen_word:
            if letter == guess:
                display[position] = letter
                right_letters += 1
                track += 1
            position += 1

    # displays the current state of the game with the letters filled in
        print(f'{Fore.BLUE}{logo}{Style.RESET_ALL}\n\n')
        print(f'{Fore.GREEN}{" ".join(display)}{Style.RESET_ALL}\n\n')

    # if the word does not contain that letter,
    # it will give -1 to the life of the player
        if track == 0:
            print(f'{Fore.RED}You lost a live!{Style.RESET_ALL}')
            lives -= 1

    # if all the letters are filled, the user wins the game
        if right_letters == len(display):
            print('You won!\n')
            print(f'{Fore.BLUE}The word was: {Back.WHITE}{chosen_word}.{Style.RESET_ALL}')
            break

    # if the user runs out of lives, game over
        if lives == 0:
            print(stages[0])
            print(f'{Fore.RED}You lose!{Style.RESET_ALL}\n')
            print(f'{Fore.BLUE}The word was: {Back.WHITE}{chosen_word}{Back.RESET}.{Style.RESET_ALL}')
            break




if __name__ == '__main__':
    main()