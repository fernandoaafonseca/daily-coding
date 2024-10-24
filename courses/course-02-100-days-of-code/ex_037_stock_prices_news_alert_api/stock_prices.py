import requests


STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = 'TX7J42MDSHGBZT3Z'


class StockPrices:
    def get_stock_prices_data(self, stock_name):
        stock_params = {
            'function': 'TIME_SERIES_DAILY_ADJUSTED',
            'symbol': stock_name,
            'outputsize': 'compact',
            'datatype': 'json',
            'apikey': STOCK_API_KEY
        }
        response = requests.get(STOCK_ENDPOINT, params=stock_params)
        print(f'STOCK API RESPONSE: {response.status_code}')
        print()

        stock_data = response.json()['Time Series (Daily)']
        stock_data_list = [value for (key, value) in stock_data.items()]

        return stock_data_list

    def get_price_change(self, stock_prices_data):
        yesterday_data = stock_prices_data[0]
        yesterday_closing_price = yesterday_data['4. close']
        day_before_yesterday_data = stock_prices_data[1]
        day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

        difference = abs(float(yesterday_closing_price) -
                         float(day_before_yesterday_closing_price))
        percentage_diff = round(
            (difference / float(yesterday_closing_price)) * 100, 2)

        if yesterday_closing_price > day_before_yesterday_closing_price:
            change = 'increased'
        else:
            change = 'decreased'

        return change, percentage_diff
