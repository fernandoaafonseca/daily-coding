'''
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

Examples:
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"

- don't worry about uppercase vowels
- "y" is not considered a vowel for this kata
'''


VOWELS = ['a', 'e', 'i', 'o', 'u']


def main():
    word = str(input('Enter the word: '))
    new_word = shortcut(word)
    print(new_word)


def shortcut(word):
    word_without_lowercase_vowels = ''
    for letter in word:
        if letter not in VOWELS:
            word_without_lowercase_vowels += letter
    return word_without_lowercase_vowels


if __name__ == '__main__':
    main()

# Test:
print(shortcut('hello') == 'hll')
print(shortcut('codewars') == 'cdwrs')
print(shortcut('goodbye') == 'gdby')
print(shortcut('HELLO') == 'HELLO')
print(shortcut("how are you today?") == "hw r y tdy?")
print(shortcut('complain') == 'cmpln')
print(shortcut('never') == 'nvr')
