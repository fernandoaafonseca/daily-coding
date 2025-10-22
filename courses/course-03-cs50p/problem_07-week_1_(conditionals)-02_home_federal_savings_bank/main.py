'''
Home Federal Savings Bank

In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.
'''


def main():
    user_greeting = input('Greeting: ')
    amount = check_greeting(user_greeting)
    print(f'${amount}')


def check_greeting(user_greeting):
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


main()


# Test:
print(check_greeting('Hello, Newman') == 0)
print(check_greeting('Hey') == 20)
print(check_greeting('How you doing?') == 20)
print(check_greeting('What\'s happening?') == 100)
print(check_greeting('What\'s up?') == 100)
print(check_greeting('How\'s it going?') == 20)
