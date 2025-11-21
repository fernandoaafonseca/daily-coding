'''
Write a program that simulates drawing names out of a hat. In this drawing, the number of hat entries each person gets may vary. Allow the user to input a list of names and a list of how many entries each person has in the drawing, and print out who wins the drawing.
'''


import os, random


def main():
    names = get_names()
    entries = get_entries(names)
    hat = build_hat(names, entries)
    winner = draw_winner(hat)
    display_result(winner)


def press_any_key_to_continue() -> None:
    input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def get_names() -> list[str]:
    while True:
        try:
            press_any_key_to_continue()
            clear_terminal()

            raw_names = str(input('Enter a list of names separated by commas (like "John, Paul, George, Ringo"): '))
            # Generates a list of "names" splitting the string by "commas"
            names = [str(item).strip() for item in raw_names.split(',')]

            return names

        except ValueError:
            print('\nPlease enter names separated by commas.')


def get_entries(names: list[str]) -> list[int]:
    '''
    Ask the user how many entries each person has.
    '''
    entries = []

    for name in names:
        while True:
            try:
                press_any_key_to_continue()
                clear_terminal()

                new_entries = int(input(f'Enter how many entries for {name}: '))

                if new_entries > 0:
                    entries.append(new_entries)
                    break
                else:
                    raise ValueError

            except ValueError:
                print('\nPlease enter an integer.')

    return entries


def build_hat(names: list[str], entries: list[int]) -> list[str]:
    '''
    Build and return a list (the hat) where each name appears according to its number of entries.
    '''
    hat = []

    for index, name in enumerate(names):
        for i in range(entries[index]):
            hat.append(name)

    return hat


def draw_winner(hat: list[str]) -> str:
    '''
    Randomly select and return one name from the hat.
    '''
    return random.choice(hat)


def display_result(winner: str) -> None:
    print('And the winner is...')
    print(winner)


if __name__ == '__main__':
    main()