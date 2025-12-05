'''
Back to the Bank

In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns an int, namely 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. You can assume that the string passed to the value function will not contain any leading spaces. Only main should call print.

    def main():
        ...


    def value(greeting):
        ...


    if __name__ == "__main__":
        main()

Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

    pytest test_bank.py

Hints
Be sure to include

    import bank

    or

    from bank import value

atop test_bank.py so that you can call value in your tests.

Take care to return, not print, an int in value. Only main should call print.

'''


def main() -> None:
    user_greeting: str = input('Greeting: ')
    amount: int = value(user_greeting)
    print(f'${amount}')


def value(user_greeting: str) -> int:
    # Removes blank spaces and lower the characters.
    user_greeting = user_greeting.strip().lower()
    # Returns only the first word.
    user_greeting = user_greeting.split()[0]
    # Checks if the first 5 letters are exactly "hello".
    if user_greeting[0:5] == 'hello':
        return 0
    elif user_greeting[0] == 'h':
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()