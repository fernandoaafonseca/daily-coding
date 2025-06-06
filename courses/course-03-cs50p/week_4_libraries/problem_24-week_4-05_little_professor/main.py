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
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integereger returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    ...


def get_level():
    ...


def generate_integereger(level):
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
    num_of_problems = 10
    level = get_level()
    problem_set = generate_problem_set(level, num_of_problems)
    game_engine(problem_set)


def get_level() -> int:
    accepted_levels = [1, 2, 3]
    while True:
        try:
            level = int(input('Level: '))
            if level in accepted_levels:
                return level
            else:
                raise ValueError
        except:
            continue


def generate_integer(level: int) -> tuple[int]:
    try:
        if level in [1, 2, 3]:
            match level:
                case 1:
                    min_num = 0
                    max_num = 9
                case 2:
                    min_num = 10
                    max_num = 99
                case 3:
                    min_num = 100
                    max_num = 999

            return random.randint(min_num, max_num)

    except:
        raise ValueError


def generate_problem_set(level: int, num_of_problems: int) -> list:
    problem_set = []

    for i in range(num_of_problems):
        problem_num = i + 1
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        problem_set.append({'Problem #': problem_num,
                           'x': x,
                            'y': y,
                            'Result': result})

    return problem_set


def get_user_guess() -> int:
    while True:
        try:
            user_guess = int(input('\nGuess: '))
            break
        except:
            continue

    return user_guess


def game_engine(problem_set: list) -> None:
    current_problem_num = 1
    qty_of_problems = len(problem_set)
    user_num_of_tries = 3
    user_score = 0

    while current_problem_num <= qty_of_problems:
        current_problem = problem_set[current_problem_num - 1]
        result = current_problem['Result']

        print(f'{current_problem['x']} + {current_problem['y']} = ')

        if user_num_of_tries > 0:
            user_guess = get_user_guess()
            if user_guess == result:
                user_score += 1
                current_problem_num += 1
            else:
                print('EEE')
                user_num_of_tries -= 1

        else:
            print(
                f'{current_problem['x']} + {current_problem['y']} = {result}')
            if current_problem_num <= qty_of_problems:
                user_num_of_tries = 3
                current_problem_num += 1
            else:
                break

    print(f'{user_score}')
    sys.exit()


if __name__ == '__main__':
    main()
