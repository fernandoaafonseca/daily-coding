'''
Felipe’s Taqueria
Note that, as of Wednesday, October 25, 2023 at 12:59 PM GMT-3, the prices of Felipe’s have been updated!

Felipe's Taqueria
One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

Hints
Note that you can detect when the user has inputted control-d by catching an EOFError with code like:
try:
    item = input()
except EOFError:
    ...
You might want to print a new line so that the user’s cursor (and subsequent prompt) doesn’t remain on the same line as your program’s own prompt.

Inputting control-d does not require inputting Enter as well, and so the user’s cursor (and subsequent prompt) might thus remain on the same line as your program’s own prompt. You can move the user’s cursor to a new line by printing \n yourself!
Note that a dict comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#mapping-types-dict, among them get, and supports operations like:
d[key]
and

if key in d:
    ...
wherein d is a dict and key is a str.

Be sure to avoid or catch any KeyError.
'''


def main():
    food_menu: dict[str, float] = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total_price: float = 0

    while True:
        try:
            user_item: str = get_item()
        except EOFError:
            exit()

        if user_item.lower() == 'exit':
            exit()

        total_price = update_total_price(food_menu, user_item, total_price)
        display_total_price(total_price)


def get_item() -> str:
    return input('Item: ').title()


def update_total_price(food_menu: dict[str, float], user_item: str, total_price: float) -> float:
    if user_item in food_menu:
        total_price += food_menu[user_item]
    return total_price


def display_total_price(total_price: float) -> str:
    print(f'Total: ${total_price:.2f}')


if __name__ == '__main__':
    main()
