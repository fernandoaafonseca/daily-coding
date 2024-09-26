'''
Coke Machine
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''


ACCEPTED_COINS = [5, 10, 25]


def main():
    amount_due = 50
    new_amount_due = add_coin(amount_due)
    change_owed_text = buy_coke(new_amount_due)
    print(change_owed_text)


def add_coin(amount_due):
    while amount_due > 0:
        print(f'Amount Due: {amount_due}')
        user_coin = int(input('Insert Coin: '))
        amount_due = check_user_coin(amount_due, user_coin)

    return amount_due


def check_user_coin(amount_due, user_coin):
    if user_coin in ACCEPTED_COINS:
        amount_due -= user_coin

    return amount_due


def buy_coke(amount_due):
    change_owed = abs(amount_due)
    return f'Change Owed: {change_owed}'


if __name__ == '__main__':
    main()


# Test:
amount_due = 50
test_amount_due = check_user_coin(amount_due, 5)
print(buy_coke(test_amount_due) == 'Change Owed: 45')

amount_due = 50
test_amount_due = check_user_coin(amount_due, 10)
print(buy_coke(test_amount_due) == 'Change Owed: 40')

amount_due = 50
test_amount_due = check_user_coin(amount_due, 25)
print(buy_coke(test_amount_due) == 'Change Owed: 25')

amount_due = 50
test_amount_due = check_user_coin(amount_due, 1)
print(buy_coke(test_amount_due) == 'Change Owed: 50')

amount_due = 50
test_amount_due = check_user_coin(amount_due, 25)
new_test_amount_due = check_user_coin(test_amount_due, 25)
print(buy_coke(new_test_amount_due) == 'Change Owed: 0')
