'''
Testing my twttr

In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

    def main():
        ...


    def shorten(word):
        ...


    if __name__ == "__main__":
        main()

Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

    pytest test_twttr.py

Hints
Be sure to include

    import twttr

    or

    from twttr import shorten

atop test_twttr.py so that you can call shorten in your tests.

Take care to return, not print, a str in shorten. Only main should call print.
'''


def main() -> None:
    user_text: str = get_user_text()
    text_without_vowels: str = shorten(user_text)
    print(text_without_vowels)


def get_user_text() -> str:
    user_text: str = str(input('Enter your text: '))

    return user_text


def shorten(user_text: str) -> str:
    text_without_vowels: str = ''

    for letter in user_text:
        if letter.lower() not in 'aeiou':
            text_without_vowels += letter

    return text_without_vowels


if __name__ == '__main__':
    main()