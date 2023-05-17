import os
import string

alphabet = list(string.ascii_lowercase) + list(string.ascii_lowercase)

def caesar(direction, text, shift):
    final_text = ''

    for letter in text:
        position = alphabet.index(letter)

        if direction == 'decode':
            shift *= -1

        new_position = position + shift
        final_text += alphabet[new_position]

    print(f'\nThe {direction}d message is:\n{final_text}')

os.system('cls')

direction = input('Type "encode" to encrypt or "decode" do decrypt:\n').lower()
text = input('\nType your message:\n').lower()
shift = int(input('\nType the shift number:\n'))

caesar(direction, text, shift)