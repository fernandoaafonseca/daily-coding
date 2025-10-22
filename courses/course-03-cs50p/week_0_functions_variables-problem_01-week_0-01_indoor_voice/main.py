'''
Indoor Voice

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

Hints
Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
'''


def convert_to_lowercase(text):
    text = str(str(text).lower())
    return text


text = input()
print(convert_to_lowercase(text))

# Test:
print(convert_to_lowercase('HELLO') == 'hello')
print(convert_to_lowercase('THIS IS CS50') == 'this is cs50')
print(convert_to_lowercase(50) == '50')
