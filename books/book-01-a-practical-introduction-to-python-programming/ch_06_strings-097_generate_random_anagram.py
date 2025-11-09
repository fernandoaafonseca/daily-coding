'''
An anagram of a word is a word that is created by rearranging the letters of the original. For instance, two anagrams of idle are deli and lied. Finding anagrams that are real words is beyond our reach until Chapter 12. Instead, write a program that asks the user for a string and returns a random anagram of the string — in other words, a random rearrangement of the letters of that string.
'''


import itertools, random


def main() -> None:
    user_word = get_user_word()
    anagrams = create_anagrams(user_word)
    random_anagram = random.choice(anagrams)
    display_result(random_anagram)


def get_user_word() -> str:
    while True:
        try:
            user_word = str(input('Enter a word: '))
            if user_word.isalpha():
                return user_word
            else:
                raise ValueError
        except ValueError:
            print('\nPlease enter a single word.\n')


def create_anagrams(user_word: str) -> list[str, ...]:
    '''
    Generates all possible anagrams (permutations) of a word.
    '''
    permutations = set(itertools.permutations(user_word.lower()))
    anagrams = list(''.join(p) for p in permutations)

    return anagrams


def display_result(random_anagram: str) -> None:
    print()
    print(f'Random anagram: "{random_anagram}"')


if __name__ == "__main__":
    main()
