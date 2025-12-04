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


Before You Begin
    - Create a CoinCap account at CoinCap Sign Up (https://pro.coincap.io/signup) and obtain an API key by clicking the “Add New Key” button in your CoinCap Dashboard (https://pro.coincap.io/dashboard). You will need to use this API key in your program. You can read more about the API usage in the CoinCap API documentation (https://pro.coincap.io/api-docs/).
'''


import requests
import sys


def main() -> None:
    num_of_btc = get_num_of_btc()
    btc_in_usd = get_btc_value_in_usd(num_of_btc)
    print(f'${btc_in_usd:,.4f}')


def get_num_of_btc() -> float:
    if len(sys.argv) == 2:
        try:
            # The index 0 is the first argument (the name of the file), so index 1 is the second argument received from the user.
            num_of_btc = float(sys.argv[1])
            return num_of_btc
        except ValueError:
            print('command-line argument is not a number')
            sys.exit(1)
    else:
        print('Missing command-line argument')
        sys.exit(1)


def get_btc_value_in_usd(num_of_btc: float) -> None:
    API_KEY = 'e8e08229bcdc6d53b6cf6062d76783aa70116c5aea6acee5f9288c6e1efe59e2'
    try:
        response = requests.get(f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}')
        btc_price = float(response.json()['data']['priceUsd'])
        result = num_of_btc * btc_price
        return result
    except requests.RequestException:
        print('API error')
        sys.exit(1)


if __name__ == '__main__':
    main()