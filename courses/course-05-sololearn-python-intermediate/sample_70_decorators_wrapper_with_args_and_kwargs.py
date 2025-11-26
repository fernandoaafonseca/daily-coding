'''
It's  a good practice to use *args and **kwargs in the signature of a wrapper function within a decorator. This approach ensures that the decorator is versatile and can be applied to any function, regardless of the number and type of its arguments.
'''


def some_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before the function runs')
        result = func(*args, **kwargs)
        print('After the function runs')
        return result
    return wrapper


@some_decorator
def greet(name):
    print(f'Hello, {name}!')


greet('Fernando')