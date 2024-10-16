import random


def set_difficulty():
    difficulty = ''
    valid_difficulties = ['easy', 'hard']
    while difficulty not in valid_difficulties:
        difficulty = input(f'Choose a difficulty. Type "easy" or "hard":\n').lower()
        if difficulty == 'easy':
            attempts = EASY_LEVEL
            return attempts
        elif difficulty == 'hard':
            attempts = HARD_LEVEL
            return attempts


def game(attempts):
    game_over = False
    while not game_over:
        guess = ''
        while type(guess) != int:
            try:
                guess = int(guess)
                break
            except:
                guess = input('\nMake a guess:\n')

        if guess == number:
            print(f'\nYou win! The number was: {number}.')
            game_over = True
        elif guess < number:
            print('\nToo low!')
            attempts -= 1
        else:
            print('\nToo high!')
            attempts -= 1
        
        if attempts > 0 and not game_over:
            print('Try again!')
            print(f'You have {attempts} attempts left to guess the number.')
        elif attempts == 0:
            print('\nYou lose!')
            print(f'The number was: {number}.')
            game_over = True

HARD_LEVEL = 5
EASY_LEVEL = 10
print('Number guessing game!')
print('I\'m thinking of a number between 1 and 100.')
number = random.randint(1, 100)
attempts = set_difficulty()
game(attempts)