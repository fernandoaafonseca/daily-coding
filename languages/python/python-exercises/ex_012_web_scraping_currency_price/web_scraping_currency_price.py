import os
import pandas as pd
import requests
import urllib
from bs4 import BeautifulSoup
from time import sleep
from unidecode import unidecode


# Inspect -> Network -> select any -> Request Headers -> 'user-agent'
USER_AGENT = {'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
WIKI_URL = 'https://pt.wikipedia.org/wiki/Lista_de_moedas'


def get_currency_names():
    wiki_html = pd.read_html(WIKI_URL, match='Moeda')
    currency_df = wiki_html[0]
    names = currency_df['Moeda[2]']

    names_list_raw = []
    for i in range(len(names)):
        name = unidecode(str(names[i]).split('[')[0].lower())
        names_list_raw.append(name)

    for i in range(len(names)):
        name = unidecode(str(names[i]).split()[0].lower())
        names_list_raw.append(name)

    currency_names = list(set(names_list_raw))
    return currency_names


def get_user_input(currency_names):
    input_currency = None
    print('Digite o nome da moeda: ')
    while input_currency not in currency_names:
        try:
            input_currency = unidecode(input()).lower()
            if input_currency == 'dolar':
                input_currency = 'dolar dos estados unidos'
            elif input_currency == 'dolar canadense':
                input_currency = 'dolar canadiano'
            elif input_currency == 'franco':
                input_currency = 'franco suico'
            elif input_currency == 'libra':
                input_currency = 'libra esterlina'
            elif input_currency == 'peso':
                input_currency = 'peso mexicano'
            elif input_currency == 'rupia':
                input_currency = 'rupia indiana'
            elif input_currency == 'yuan' or input_currency == 'renminbi':
                input_currency = 'iuane'
        except:
            break

    return input_currency


def get_result(input_currency):
    query_raw = f'cotação {input_currency}'
    query = urllib.parse.quote(query_raw)
    url = f'https://www.google.com/search?q={query}'
    get_search_result = requests.get(url, headers=USER_AGENT)
    search_result_html = BeautifulSoup(get_search_result.text, 'html.parser')

    price_html = search_result_html.find('span', class_='DFlfde SwHCTb')
    price = price_html.get_text()
    full_price = price_html["data-value"].replace('.', ',')

    return get_search_result, price, full_price


def print_header():
    app_name = 'COTAÇÃO ATUAL'
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=' * len(app_name))
    print(app_name)
    print('=' * len(app_name))
    print()


def print_results(price, full_price):
    success = 'COTAÇÃO OBTIDA COM SUCESSO!'
    print()
    print('=' * len(success))
    print(success)
    print('=' * len(success))
    print()
    print(f'- Preço:')
    print(f'R$ {price}')
    print()
    print('- Preço completo:')
    print(f'R$ {full_price}')


def main():
    continue_running = True
    while continue_running:
        print_header()
        currency_names = get_currency_names()
        input_currency = get_user_input(currency_names)
        get_search_result, price, full_price = get_result(input_currency)
        if get_search_result.ok:
            print_results(price, full_price)
        
        user_input_str = 'Deseja saber a cotação de outra moeda? (s/n)'
        print()
        print('=' * len(user_input_str))
        print()
        print(user_input_str)
        valid_options = ['s', 'n']
        user_option = None
        while user_option not in valid_options:
            user_option = input().lower()[0]
        if user_option == 's':
            continue
        elif user_option == 'n':
            print()
            print('Até mais!')
            sleep(3)
            continue_running = False


if __name__ == '__main__':
    main()