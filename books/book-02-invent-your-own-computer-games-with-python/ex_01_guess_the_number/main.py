import os, random


def main() -> None:
    game_loop()


def game_loop() -> None:
    MIN_NUM = 1
    MAX_NUM = 20
    MAX_ATTEMPTS = 5
    attempts = 0
    generated_num = random.randint(MIN_NUM, MAX_NUM)

    clear_terminal()
    display_hud(attempts, MAX_ATTEMPTS)
    player_name = get_player_name(attempts, MAX_ATTEMPTS)

    clear_terminal()
    display_hud(attempts, MAX_ATTEMPTS)
    print(f'Well, {player_name}, I am thinking of a number between {MIN_NUM} and {MAX_NUM}.')
    press_any_key_to_continue()

    while attempts < MAX_ATTEMPTS:
        clear_terminal()
        display_hud(attempts, MAX_ATTEMPTS)
        player_guess = int(input('Take a guess.\n'))
        attempts += 1

        if player_guess == generated_num:
            break
        else:
            if player_guess < generated_num:
                print('\nYour guess is too low.')
                press_any_key_to_continue()
            elif player_guess > generated_num:
                print('\nYour guess is too high.')
                press_any_key_to_continue()

        clear_terminal()
        display_hud(attempts, MAX_ATTEMPTS)

    clear_terminal()
    display_hud(attempts, MAX_ATTEMPTS)
    if attempts == MAX_ATTEMPTS and player_guess != generated_num:
        print('GAME OVER! YOU LOSE!')
        print(f'\nNope. The number I was thinking of was {generated_num}.')
    else:
        print('GAME OVER! YOU WON!')
        print(f'\nGood job, {player_name}! You guessed my number in {attempts} guesses!')


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def press_any_key_to_continue() -> None:
    input('\nPRESS ANY KEY TO CONTINUE...')


def display_hud(attempts: int, MAX_ATTEMPTS: int) -> None:
    print('=' * 10, end='')
    print(' GUESS THE NUMBER ', end='')
    print('=' * 10)
    print(f'Attempts left: {MAX_ATTEMPTS - attempts}')
    print('-' * 38)


def get_player_name(attempts: int, MAX_ATTEMPTS: int) -> str:
    while True:
        try:
            player_name = str(input('Hello! What is your name?\n'))
            if player_name:
                return player_name
            else:
                raise ValueError
        except ValueError:
            clear_terminal()
            display_hud(attempts, MAX_ATTEMPTS)
            print('Please enter your name.\n')


if __name__ == '__main__':
    main()