import requests


NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = '4f9884b266db49f6a5e6829b2cca3d78'


class News:
    def get_latest_news_data(self, percentage_diff):
        if percentage_diff >= 3:
            news_params = {
                'q': 'tesla',
                'language': 'en',
                'apikey': NEWS_API_KEY
            }
            response = requests.get(NEWS_ENDPOINT, params=news_params)
            print(f'NEWS API RESPONSE: {response.status_code}')
            print()

            news_data = response.json()['articles']
            news_list = []
            for i in range(3):
                source = news_data[i]['source']['name']
                title = news_data[i]['title']
                description = news_data[i]['description'].replace('\r\n', '')
                url = news_data[i]['url']
                news_list.append({
                    'Source': source,
                    'Title': title,
                    'Description': description,
                    'URL': url
                })

            return news_list

    def print_summary(self, stock_name, change, percentage_diff, latest_news_data):
        if change == 'increased':
            print(f'{stock_name}: 🔺 {percentage_diff}%')
        else:
            print(f'{stock_name}: 🔻 {percentage_diff}%')
        if latest_news_data:
            for news in latest_news_data:
                print()
                print(f'SOURCE: {news["Source"]}')
                print(f'TITLE: {news["Title"]}')
                print(f'BRIEF: {news["Description"]}')
                print(f'LINK: {news["URL"]}')
        else:
            print()
            print('There was no significant price change in the last 24 hours.')
