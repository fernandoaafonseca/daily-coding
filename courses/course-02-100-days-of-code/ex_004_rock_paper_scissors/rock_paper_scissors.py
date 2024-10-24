'''
Jokenpo (Rock, Paper and Scissors) game running in the terminal.
I played around with the code a bit, adding colors, ASCII art and animations for the strings.
'''

import os
import random
import sys
from time import sleep
from colorama import Fore, Back, Style


def animate(text, time=0.01):
  for letter in text:
    print(letter, end="")
    sys.stdout.flush()
    sleep(time)


def jokenpo(user_choice):
    os.system('cls' if os.name=='nt' else 'clear')
    sleep(0.1)
    animate(f'\n{Fore.YELLOW}==================================================\n')
    sleep(0.5)
    print('JO!')
    sleep(0.5)
    print('KEN!')
    sleep(0.5)
    print('PO!')
    sleep(0.5)
    animate(f'{Fore.YELLOW}==================================================\n\n')
    sleep(0.1)

    cpu_choice = random.randint(0,2)

    if user_choice == 0:
        animate(f'{Fore.GREEN}You chose ROCK{Style.RESET_ALL}')
        animate(f'{Fore.GREEN}{rock}')
    elif user_choice == 1:
        animate(f'{Fore.GREEN}You chose PAPER{Style.RESET_ALL}')
        animate(f'{Fore.GREEN}{paper}')
    else:
        animate(f'{Fore.GREEN}You chose SCISSORS{Style.RESET_ALL}')
        animate(f'{Fore.GREEN}{scissors}')

    if cpu_choice == 0:
        animate(f'\n\n\n{Fore.RED}Computer chose ROCK{Style.RESET_ALL}')
        animate(f'{Fore.RED}{rock}')
    elif cpu_choice == 1:
        animate(f'\n\n\n{Fore.RED}Computer chose PAPER{Style.RESET_ALL}')
        animate(f'{Fore.RED}{paper}')
    else:
        animate(f'\n\n\n{Fore.RED}Computer chose SCISSORS{Style.RESET_ALL}')
        animate(f'{Fore.RED}{scissors}')

    compare(user_choice, cpu_choice)

def compare(user_choice, cpu_choice):
    if user_choice == cpu_choice:
        animate(f'\n{Fore.BLUE}\nIT\'S A TIE!\n')
    elif user_choice == 0 and cpu_choice == 1:
        animate(f'\n\n{Fore.RED}\nPaper covers rock.')
        animate(f'\n{Fore.RED}\nYOU LOSE!\n')
    elif user_choice == 0 and cpu_choice == 2:
        animate(f'\n\n{Fore.GREEN}\nRock smashes scissors.')
        animate(f'\n{Fore.GREEN}\nYOU WIN!\n')
    elif user_choice == 1 and cpu_choice == 0:
        animate(f'\n\n{Fore.GREEN}\nPaper covers rock.')
        animate(f'\n{Fore.GREEN}\nYOU WIN!\n')
    elif user_choice == 1 and cpu_choice == 2:
        animate(f'\n{Fore.RED}\nScissors cuts paper.')
        animate(f'\n{Fore.RED}\nYOU LOSE!\n')
    elif user_choice == 2 and cpu_choice == 1:
        animate(f'\n{Fore.GREEN}\nScissors cuts paper.')
        animate(f'\n{Fore.GREEN}\nYOU WIN!\n')
    else:
        animate(f'\n{Fore.RED}\nRock smashes scissors.')
        animate(f'\n{Fore.RED}\nYOU LOSE!\n')
    animate(f'\n{Fore.YELLOW}==================================================\n{Style.RESET_ALL}')


def main():
    os.system('cls' if os.name=='nt' else 'clear')
    user_choice = ''
    valid_choices = [0, 1, 2]
    while user_choice not in valid_choices:
        os.system('cls' if os.name=='nt' else 'clear')
        print(f'{Fore.YELLOW}{logo}{Style.RESET_ALL}')
        user_choice = int(input('What do you choose?\n\
            0 - Rock\n\
            1 - Paper\n\
            2 - Scissors\n'))
        if user_choice in valid_choices:
            jokenpo(user_choice)


rock = '''
    _______
---'   ____)
    (_____)
    (_____)
    (____)
---.(___)'''

paper = '''
    _______
---'   ____)__
        ______)
        _______)
        _______)
---.__________)'''

scissors = '''
    ________
---'   ______)
        ______)
    ______)
    (____)
---.(___)'''

logo = '''
    ⠀⠀⠀⠀⠀⣠⡴⠖⠒⠲⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠖⠒⢶⣄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⡾⠁⠀⣀⠔⠁⠀⠀⠈⠙⠷⣤⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀
    ⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠈⢿⡀⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⣰⠏⠀⢀⣤⣤⣄⡀⠀⠀
    ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠛⠛⠃⠸⡇⠈⣇⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀⠈⠹⡆⠀
    ⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀⢠⣤⡤⠶⠖⠛⠀⣿⠀⣿⠀⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⢀⣠⡾⠃⠀
    ⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠖⠋⢀⣿⣠⠏⠀⠀⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀
    ⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄
    ⠀⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀⠀⢀⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣠⠼⠃
    ⠀⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⣀⣤⠶⠛⠉⠀⠀⠀
    ⠀⠀⠀⠀⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀⠀⠀⠀⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀⠀⠙⣄⠀⠙⢷⡀⠀⠀⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀⢀⣠⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢀⡾⠁⣴⠋⠰⣤⣄⡀⠀⠀⠀⠀⠈⠳⢤⣼⣇⣀⣀⠀⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⠃⢰⠇⠰⢦⣄⡈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠸⣧⣿⠀⠻⣤⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠈⠹⣆⠀⠈⠛⠂⠀⠀⠀⠀⠀⠀⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀⠀⠀⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠦⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    '''


if __name__ == '__main__':
    main()