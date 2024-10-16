'''
Making Faces

Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

Hints
Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
An emoji is actually just a character, so you can quote it like any str, a la "😐". And you can copy and paste the emoji from this page into your own code as needed.
'''


def convert(text):
      text_with_emojis = str(text).replace(':)', '🙂').replace(':(', '🙁')
      return text_with_emojis


text_input = convert(input())
print(convert(text_input))


# Test:
print(convert('Hello :)') == 'Hello 🙂')
print(convert('Goodbye :(') == 'Goodbye 🙁')
print(convert('Hello :) Goodbye :(') == 'Hello 🙂 Goodbye 🙁')
