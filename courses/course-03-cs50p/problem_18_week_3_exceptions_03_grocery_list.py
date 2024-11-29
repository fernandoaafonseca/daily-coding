'''
Grocery List

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

Hints
Note that you can detect when the user has inputted control-d by catching an EOFError with code like:
try:
    item = input()
except EOFError:
    ...
Odds are you’ll want to store your grocery list as a dict.
Note that a dict comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#mapping-types-dict, among them get, and supports operations like:
d[key]
and

if key in d:
    ...
wherein d is a dict and key is a str.

Be sure to avoid or catch any KeyError.
Note that you can sort a dictionary’s keys alphabetically by passing that dictionary as an argument to sorted.
'''


import sys


def main():
    grocery_list: dict[str, int] = {}

    while True:
        try:
            user_item = get_user_item()
        except EOFError:
            sorted_grocery_list = sort_grocery_list(grocery_list)
            display_list_of_items(sorted_grocery_list)
            sys.exit()

        if user_item.lower() == 'exit':
            sorted_grocery_list = sort_grocery_list(grocery_list)
            display_list_of_items(sorted_grocery_list)
            sys.exit()

        grocery_list = add_item(user_item, grocery_list)


def get_user_item() -> str:
    return input()


def add_item(user_item: str, grocery_list: dict[str, int]) -> dict[str, int]:
    if user_item in grocery_list:
        grocery_list[user_item] += 1
    else:
        grocery_list[user_item] = 1

    return grocery_list


def display_list_of_items(sorted_grocery_list: dict[str, int]) -> None:
    for item in sorted_grocery_list:
        print(f'{sorted_grocery_list[item]} {item.upper()}')


def sort_grocery_list(grocery_list: dict[str, int]):
    sorted_grocery_list = {}
    for item, number in sorted(grocery_list.items()):
        sorted_grocery_list[item] = number

    return sorted_grocery_list


if __name__ == '__main__':
    main()
