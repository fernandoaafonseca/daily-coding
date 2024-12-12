'''
Guessing Game

I’m thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

Prompts the user for a level, "n". If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and "n", inclusive, using the random module.

Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

If the guess is smaller than that integer, the program should output Too small! and prompt the user again.

If the guess is larger than that integer, the program should output Too large! and prompt the user again.

If the guess is the same as that integer, the program should output Just right! and exit.

Hints
Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.
'''


import random
import sys


def main():
    level = get_level()
    generated_num = gen_random_num(level)
    is_game_over = False
    game_engine(is_game_over, generated_num)


def get_level() -> int:
    while True:
        try:
            level = int(input('Level: '))
            if level >= 1:
                return level
            else:
                continue
        except:
            continue


def gen_random_num(level: int) -> int:
    return random.randint(1, level)


def get_user_guess() -> int:
    while True:
        try:
            user_guess = int(input('Guess: '))
            break
        except:
            continue

    return user_guess


def check_user_guess(user_guess: int, generated_num: int, is_game_over: bool) -> list[bool, str]:
    if user_guess == generated_num:
        text = 'Just right!'
        is_game_over = True
    elif user_guess >= generated_num:
        text = 'Too large!'
        is_game_over = False
    else:
        text = 'Too small!'
        is_game_over = False

    return text, is_game_over


def game_engine(is_game_over: bool, generated_num: int) -> None:
    while True:
        if not is_game_over:
            user_guess = get_user_guess()
            text, is_game_over = check_user_guess(
                user_guess, generated_num, is_game_over)
            print(text)
        else:
            sys.exit()


if __name__ == '__main__':
    main()
