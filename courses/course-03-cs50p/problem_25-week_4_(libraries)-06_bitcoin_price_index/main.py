'''
Bitcoin Price Index

    - As of Saturday, April 5, 2025 at 10:00 AM GMT-3, we are aware of the CoinCap v2 API deprecation that may affect students’ ability to complete this problem. We have now updated the problem to use the CoinCap v3 API instead. If you have already started working on this problem, you must update your code to use the CoinCap v3 API instead of the CoinCap v2 API. Importantly, you will need to sign up for a CoinCap account and obtain an API key. You can do this by visiting CoinCap. Once you have your API key, you can use it in your code to access the CoinCap v3 API.

Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:
    - Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
    - Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

        import requests

        try:
            ...
        except requests.RequestException:
            ...

Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.

Hints
    - Recall that the sys module comes with argv, per docs.python.org/3/library/sys.html#sys.argv.
    - Note that the requests module comes with quite a few methods, per requests.readthedocs.io/en/latest, among which are get, per requests.readthedocs.io/en/latest/user/quickstart.html#make-a-request, and json, per requests.readthedocs.io/en/latest/user/quickstart.html#json-response-content. You can install it with:

        pip install requests

    - Note that CoinCap’s API returns a JSON response like:

        {
          "data": {
            "id": "bitcoin",
            "rank": "1",
            "symbol": "BTC",
            "name": "Bitcoin",
            "supply": "19823321.0000000000000000",
            "maxSupply": "21000000.0000000000000000",
            "marketCapUsd": "1939613325892.4607145113457500",
            "volumeUsd24Hr": "12341417371.3505338276601668",
            "priceUsd": "97845.0243474572557500",
            "changePercent24Hr": "1.4324165997531723",
            "vwap24Hr": "96203.8859537212418977",
            "explorer": "https://blockchain.info/"
          },
          "timestamp": 1739399343596
        }

    - Recall that you can format USD to four decimal places with a thousands separator with code like:

        print(f"${amount:,.4f}")
'''


import random
import sys


def main():
    num_of_problems = 10
    level = get_level()
    problem_set = generate_problem_set(level, num_of_problems)
    game_engine(problem_set)


def get_level() -> int:
    accepted_levels = [1, 2, 3]
    while True:
        try:
            level = int(input('Level: '))
            if level in accepted_levels:
                return level
            else:
                raise ValueError
        except:
            continue


def generate_integer(level: int) -> tuple[int]:
    try:
        if level in [1, 2, 3]:
            match level:
                case 1:
                    min_num = 0
                    max_num = 9
                case 2:
                    min_num = 10
                    max_num = 99
                case 3:
                    min_num = 100
                    max_num = 999

            return random.randint(min_num, max_num)

    except:
        raise ValueError


def generate_problem_set(level: int, num_of_problems: int) -> list:
    problem_set = []

    for i in range(num_of_problems):
        problem_num = i + 1
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        problem_set.append({'Problem #': problem_num,
                           'x': x,
                            'y': y,
                            'Result': result})

    return problem_set


def get_user_guess() -> int:
    while True:
        try:
            user_guess = int(input('\nGuess: '))
            break
        except:
            continue

    return user_guess


def game_engine(problem_set: list) -> None:
    current_problem_num = 1
    qty_of_problems = len(problem_set)
    user_num_of_tries = 3
    user_score = 0

    while current_problem_num <= qty_of_problems:
        current_problem = problem_set[current_problem_num - 1]
        result = current_problem['Result']

        print(f'{current_problem['x']} + {current_problem['y']} = ')

        if user_num_of_tries > 0:
            user_guess = get_user_guess()
            if user_guess == result:
                user_score += 1
                current_problem_num += 1
            else:
                print('EEE')
                user_num_of_tries -= 1

        else:
            print(
                f'{current_problem['x']} + {current_problem['y']} = {result}')
            if current_problem_num <= qty_of_problems:
                user_num_of_tries = 3
                current_problem_num += 1
            else:
                break

    print(f'{user_score}')
    sys.exit()


if __name__ == '__main__':
    main()
