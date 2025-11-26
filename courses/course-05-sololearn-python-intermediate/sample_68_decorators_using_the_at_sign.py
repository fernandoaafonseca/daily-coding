'''
You can apply a decorator to a function using the @ sign. It improves the code readability and provides a clean separation between the function and its decoration.

When a function with a decorator is called, it automatically includes the behavior defined in the decorator.

It's good practice to include 'decorator' in the name of a decorator function.
'''


def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message

    return wrapper


@uppercase
def greet():
    return 'Welcome!'


# Using the decorated function
print(greet())