'''
This was a pretty tough one.
I tried not to look at the solution video so I could write the code in my own way.
I also used the "colorama" module for the very first time.
It was a really fun challenge to do.
'''

import os
import random
from colorama import Fore, Back, Style

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

words_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

# list of the words for the game import from the "hangman.py" module
words_list = words_list

# choose a word from the list
chosen_word = random.choice(words_list)

display = []

# creates empty spaces in the lenght of the chosen word
for _ in range(len(chosen_word)):
    display.append('_')

# prints the "Hangman" logo
os.system('cls')
print(f'{Fore.BLUE}{logo}{Style.RESET_ALL}\n\n')

# prints the empty spaces with the lenght of the chosen word
print(f'{Fore.GREEN}{" ".join(display)}{Style.RESET_ALL}\n\n')

# initializes some variables to keep track of the game state
lives = 6
position = 0
right_letters = 0
track = 0

while lives > 0:
# prints the number of lives left
    if lives > 1:
        print(f'You have {lives} lives left.')
    else:
        print(f'You have {lives} live left.')

# prints the ASCII art for the player's current lives
    print(f'{Fore.YELLOW}{stages[lives]}{Style.RESET_ALL}')

# asks the user to write a letter
    guess = input('Guess a letter:\n').lower()
    position = 0
    track = 0
    os.system('cls')

# checks if the letter is in the chosen word
    for letter in chosen_word:
        if letter == guess:
            display[position] = letter
            right_letters += 1
            track += 1
        position += 1

# displays the current state of the game with the letters filled in
    print(f'{Fore.BLUE}{logo}{Style.RESET_ALL}\n\n')
    print(f'{Fore.GREEN}{" ".join(display)}{Style.RESET_ALL}\n\n')
    
# if the word does not contain that letter,
# it will give -1 to the life of the player
    if track == 0:
        print(f'{Fore.RED}You lost a live!{Style.RESET_ALL}')
        lives -= 1

# if all the letters are filled, the user wins the game
    if right_letters == len(display):
        print('You won!\n')
        print(f'{Fore.BLUE}The word was: {Back.WHITE}{chosen_word}.{Style.RESET_ALL}')
        break
    
# if the user runs out of lives, game over
    if lives == 0:
        print(stages[0])
        print(f'{Fore.RED}You lose!{Style.RESET_ALL}\n')
        print(f'{Fore.BLUE}The word was: {Back.WHITE}{chosen_word}{Back.RESET}.{Style.RESET_ALL}')
        break