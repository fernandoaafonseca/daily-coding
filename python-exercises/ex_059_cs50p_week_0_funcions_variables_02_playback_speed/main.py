'''
Playback Speed
Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

Hints
Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
'''


def replace_spaces_with_three_periods(text):
    slower_text = str(text).replace(' ', '...')
    return slower_text


text = input()
print(replace_spaces_with_three_periods(text))

# Test:
print(replace_spaces_with_three_periods('This is CS50') == 'This...is...CS50')
print(replace_spaces_with_three_periods('This is our week on functions')
      == 'This...is...our...week...on...functions')
print(replace_spaces_with_three_periods('Let\'s implement a function called hello')
      == 'Let\'s...implement...a...function...called...hello')
