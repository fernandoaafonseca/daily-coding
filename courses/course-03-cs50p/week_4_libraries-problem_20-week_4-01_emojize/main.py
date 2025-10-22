'''
Emojize

Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, for instance, :thumbs_up:, which will be automatically converted to 👍. Some programs additionally support aliases, whereby you can more succinctly type, for instance, :thumbsup:, which will also be automatically converted to 👍.

See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.

In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

Hints
Note that the emoji module comes with two functions, per pypi.org/project/emoji, one of which is emojize, which takes an optional, named parameter called language. You can install it with:
pip install emoji
'''


from emoji import emojize


def main():
    emoji_alias_input = get_emoji_alias_input()
    emoji = convert_alias_to_emoji(emoji_alias_input)
    print(emoji)


def get_emoji_alias_input() -> str:
    return input('Enter an emoji alias: ')


def convert_alias_to_emoji(emoji_alias_input: str) -> str:
    return emojize(emoji_alias_input, language='alias')


if __name__ == '__main__':
    main()


# Test:
emoji = convert_alias_to_emoji(':1st_place_medal:')
expected_result = '🥇'
print(emoji == expected_result)

emoji = convert_alias_to_emoji(':money_bag:')
expected_result = '💰'
print(emoji == expected_result)

emoji = convert_alias_to_emoji(':smile_cat:')
expected_result = '😸'
print(emoji == expected_result)

emoji = convert_alias_to_emoji(':thumbs_up:')
expected_result = '👍'
print(emoji == expected_result)

emoji = convert_alias_to_emoji(':thumbsup:')
expected_result = '👍'
print(emoji == expected_result)
