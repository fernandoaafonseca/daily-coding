import requests

from news import News
from stock_prices import StockPrices


STOCK_NAME = "TSLA"


class Main:
    def __init__(self):
        self.stock_prices = StockPrices()
        self.news = News()

        self.stock_prices_data = self.stock_prices.get_stock_prices_data(
            STOCK_NAME)
        self.change, self.percentage_diff = self.stock_prices.get_price_change(
            self.stock_prices_data)

        self.latest_news_data = self.news.get_latest_news_data(
            self.percentage_diff)
        self.print_summary = self.news.print_summary(
            STOCK_NAME, self.change, self.percentage_diff, self.latest_news_data)


main = Main()
