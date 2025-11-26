'''
You can also return the result of the nested function directly from within the body of the parent function.
'''


def greet(name):
    print(f'Hey {name}')

    def account():
        return 'Your account is created!'

    message = account()
    return message


print(greet('Bob'))