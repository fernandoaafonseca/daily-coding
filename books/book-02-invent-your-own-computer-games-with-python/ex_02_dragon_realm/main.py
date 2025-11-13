import os, random, time


def main() -> None:
    game_loop()


def game_loop() -> None:
    clear_terminal()
    display_hud()
    display_intro()
    press_any_key_to_continue()

    play_again = True

    while play_again:
        clear_terminal()
        display_hud()

        chosen_cave = choose_cave()
        friendly_cave = random.randint(1, 2)
        check_cave(chosen_cave, friendly_cave)

        press_any_key_to_continue()
        play_again = want_to_play_again()
        clear_terminal()


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def press_any_key_to_continue() -> None:
    input('\nPRESS ANY KEY TO CONTINUE...')


def display_hud() -> None:
    print('=' * 14, end='')
    print(' DRAGON REALM ', end='')
    print('=' * 14)


def display_intro() -> None:
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.\n')


def choose_cave() -> int:
    while True:
        try:
            cave = int(input('Which cave will you go into? (1 or 2)\n'))
            if cave in [1, 2]:
                return cave
            else:
                raise ValueError
        except ValueError:
            clear_terminal()
            display_hud()


def check_cave(chosen_cave: int, friendly_cave: int) -> None:
    clear_terminal()
    display_hud()

    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...\n')
    time.sleep(2)

    if chosen_cave == friendly_cave:
        print('💎 Gives you his treasure!')
    else:
        print('☠️  Gobbles you down in one bite!')


def want_to_play_again() -> bool:
    while True:
        try:
            clear_terminal()
            display_hud()
            play_again = str(input('Do you want to play again? (Yes or No)\n'))
            if play_again:
                if play_again[0].lower() == 'y':
                    return True
                elif play_again[0].lower() == 'n':
                    return False
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            clear_terminal()
            display_hud()
            print('Please enter "Y" or "N".\n')


if __name__ == '__main__':
    main()