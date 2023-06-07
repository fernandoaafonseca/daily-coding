'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
'''


import string
alphabet = string.ascii_lowercase


def alphabet_position(text):
    positions_list = []
    for char in text:
        new_position = alphabet.find(char.lower()) + 1
        if new_position != 0:
            positions_list.append(str(new_position))
    positions_string = ' '.join(positions_list)
    return positions_string


print(alphabet_position("The sunset sets at twelve o' clock."))
