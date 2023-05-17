import os
import sys
from time import sleep
from colorama import Fore, Back, Style

def animate(text, time=0.01):
  for letter in text:
    print(letter, end="")
    sys.stdout.flush()
    sleep(time)

def check_int(num):
    valid_int = False
    number = 0

    while True:
        n = str(input(num))

        if n.isdigit():
            number = int(n)
            valid_int = True
        else:
            print(f'\n{Fore.RED}ERROR!\nEnter a valid integer!\n')

        if valid_int:
            break

    return prime_checker(number)

def prime_checker(number):
    prime = True

    for n in range(2, number):
        if number % n == 0:
            prime = False
    
    if prime:
        animate(f'\n{Fore.GREEN}{number} is a prime number.{Style.RESET_ALL}\n')
    else:
        animate(f'\n{Fore.RED}{number} is not a prime number.{Style.RESET_ALL}\n')

os.system('cls')
animate(f'{Fore.MAGENTA}=========== PRIME NUMBER CHECKER ===========\n\n')
n = check_int(f'{Fore.BLUE}Enter an integer:\n')