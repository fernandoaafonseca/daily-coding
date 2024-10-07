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
    text = str(input('Enter the text: '))
    shortcut_text = shortcut(text)
    print(shortcut_text)


def shortcut(text):
    text_without_lowercase_vowels = ''
    for char in text:
        if char not in VOWELS:
            text_without_lowercase_vowels += char
    return text_without_lowercase_vowels


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
