'''
You can assign a function to a variable.

After assigning a function to a variable, you can use the variable to call the function.
'''


def shout(text):
    return text.upper()


yell = shout

print(yell("Hello"))