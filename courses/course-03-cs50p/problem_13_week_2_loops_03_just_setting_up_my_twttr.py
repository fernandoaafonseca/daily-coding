'''
Just setting up my twttr

When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
Much like a list, a str is “iterable,” which means you can iterate over each of its characters in a loop. For instance, if s is a str, you could print each of its characters, one at a time, with code like:
for c in s:
    print(c, end="")
'''


def main():
    user_text: str = get_user_text()
    text_without_vowels: str = remove_vowels(user_text)
    print(text_without_vowels)


def get_user_text() -> str:
    user_text: str = str(input('Enter your text: '))

    return user_text


def remove_vowels(user_text: str) -> str:
    text_without_vowels: str = ''

    for letter in user_text:
        if letter.lower() not in 'aeiou':
            text_without_vowels += letter

    return text_without_vowels


if __name__ == '__main__':
    main()


# Test:
print(remove_vowels('Twitter') == 'Twttr')

print(remove_vowels('What\'s your name?') == 'Wht\'s yr nm?')

print(remove_vowels('CS50') == 'CS50')

print(remove_vowels('PYTHON') == 'PYTHN')
