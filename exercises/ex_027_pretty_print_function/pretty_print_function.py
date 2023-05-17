import os
import sys
from time import sleep
from colorama import Fore, Back, Style


def animate(text, time=0.01):
  for letter in text:
    print(letter, end="")
    sys.stdout.flush()
    sleep(time)


def write(text):
    os.system('cls' if os.name=='nt' else 'clear')
    size = len(text) + 4

    animate(f'{Fore.YELLOW}=' * size)
    print()
    animate(f' ' * 2)
    animate(f'{Fore.BLUE}{text}')
    print()
    animate(f'{Fore.YELLOW}=' * size)
    print(f'{Style.RESET_ALL}')


text = input('Write something:\n')
write(text)