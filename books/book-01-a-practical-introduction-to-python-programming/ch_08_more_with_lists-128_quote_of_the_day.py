'''
Write a simple quote-of-the-day program. The program should contain a list of quotes, and when the user runs the program, a randomly selected quote should be printed.
'''


import random


QUOTES = [
    '"He who has a why to live can bear almost any how." - Friedrich Nietzsche',
    '"There are no facts, only interpretations." - Friedrich Nietzsche',
    '"Somewhere, something incredible is waiting to be known." - Carl Sagan',
    '"Science is a way of thinking much more than it is a body of knowledge." - Carl Sagan',
    '"I may be a bit odd, but I am not mad." - Douglas Adams',
    '"I love the freedom of the press… and the freedom not to read it." - Douglas Adams',
    '"I won’t be a rock star. I will be a legend." - Freddie Mercury',
    '"Modern music bores me; I want emotion." - Roger Waters',
    '"Reality leaves a lot to the imagination." - John Lennon',
    '"Life is what happens while you are busy making other plans." - John Lennon'
    ]


def main():
    random_quote = get_random_quote()
    display_result(random_quote)


def get_random_quote() -> str:
    return random.choice(QUOTES)


def display_result(random_quote: str) -> None:
    print(random_quote)


if __name__ == '__main__':
    main()