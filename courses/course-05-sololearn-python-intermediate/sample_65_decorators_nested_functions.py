'''
Functions are a fundamental concept in programming, greatly enhancing the efficiency and flexibility of your code. Up until now, you've focused on defining and calling functions. However, Python offers advanced techniques to make your code even more powerful and adaptable.

In this lesson, we'll learn about decorators, special functions that modify or enhance other functions.

In Python, functions can be nested. This means you can define a function inside another function's body.
'''


# Outer/parent function
def outer_function():
    print('Hello from the outer function')

    # Inner/child function
    def inner_function():
        print('Hello from the inner function')

    inner_function()


outer_function()