'''
Little Professor

Source: https://www.youtube.com/watch?v=ZuJwzH9BIgs

One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level, 
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
    
Hints
Note that you can raise an exception like ValueError with code like:

raise ValueError

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
