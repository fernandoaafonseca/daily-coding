import random

computer = random.randint(0, 10)
guessed = False
attempts = 0

while not guessed:
    player = int(input('Guess the number between 0 and 10:\n'))
    attempts += 1

    if player == computer:
        guessed = True
        print('You won!')
        break
    else:
        if player < computer:
            print('My number is higher than that!')
        elif player > computer:
            print('My number is lower than that!')

print(f'You guessed the right number with {attempts} tries.')