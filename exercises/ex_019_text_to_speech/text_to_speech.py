import pyttsx3
import sys
import os
from time import sleep
from colorama import Fore, Back, Style


def animate(text, time=0.01):
  for letter in text:
    print(letter, end='')
    sys.stdout.flush()
    sleep(time)


def username(name):
    engine.say(f'Hello, {name}! What do you want me to say?')
    engine.runAndWait()
    input_text()


def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()


def input_text():
  os.system('cls' if os.name=='nt' else 'clear')
  animate(f'\n{Fore.BLUE}==================================================\n')
  animate(f'\n{Fore.YELLOW}Write something:\n\n')
  text = input(f'{Fore.GREEN}')
  animate(f'\n{Fore.BLUE}==================================================\n{Style.RESET_ALL}')
  text_to_speech(text)


def main():
  os.system('cls' if os.name=='nt' else 'clear')
  animate(f'\n{Fore.BLUE}==================================================\n')
  animate(f'\n{Fore.YELLOW}What is your name?\n\n')
  name = input(f'{Fore.GREEN}')
  animate(f'\n{Fore.BLUE}==================================================\n{Style.RESET_ALL}')
  username(name)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
try:
  engine.setProperty('voice', voices[2].id)
except:
  engine.setProperty('voice', voices[0].id)


if __name__ == '__main__':
  main()