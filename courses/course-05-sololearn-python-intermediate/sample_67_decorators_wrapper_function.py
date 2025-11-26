'''
Imagine you have a function that generates a message. Your goal is to create another function that takes this original function as an argument and converts the original message into uppercase, without altering the original function's code.

These functions are known as decorators. In the code below, the uppercase() function acts as a decorator, and the wrapper() function represents the modified (or decorated) version of the greet() function.
'''


def greet():
    return 'Welcome!'


# Takes a function as an argument
def uppercase(func):
    # Wrapper function to keep the original function code unchanged
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message

    return wrapper


greet_upper = uppercase(greet)

print(greet_upper())