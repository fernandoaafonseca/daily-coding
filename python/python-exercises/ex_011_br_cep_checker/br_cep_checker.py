import os
import re
import requests
from colorama import Fore, Back, Style
from time import sleep


BOLD = '\x1B[1m'
ITALIC = '\x1B[3m'
BOLD_ITALIC = '\x1B[1;3m'
CLOSING_TAG = '\x1B[0m'


class App:
    def __init__(self):
        self.header_type = 1
        screen = Screen(self.header_type)
        self.validate_cep_number()


    def animate(self, text, speed=0.01):
        for letter in text:
            print(letter, end='', flush=True)
            sleep(speed)


    def validate_cep_number(self):
        header_type = 2
        while True:
            cep_number = self.get_cep_number()
            if len(cep_number) != 8:
                header = Screen(header_type)
            else:
                response = requests.get(f'http://www.viacep.com.br/ws/{cep_number}/json/')
                address_data = response.json()

                self.print_cep_info(address_data, cep_number)
                break


    def get_cep_number(self):
        cep_input_prompt = 'Enter the CEP number: '
        self.animate(f'{Fore.YELLOW}{cep_input_prompt}{Style.RESET_ALL}')
        cep_input = input()
        cep_number = ''.join(re.findall('\d+', cep_input))
        return cep_number


    def print_cep_info(self, address_data, cep_number):
        header_type = 3
        header = Screen(header_type, cep_number)
        speed = 0.02

        if 'erro' not in address_data:
            separator_line = '=' * 19
            cep_found = f'{BOLD}{Fore.GREEN}{separator_line} CEP number found! {separator_line}{Style.RESET_ALL}{CLOSING_TAG}'

            masks = ['CEP number', 'Street', 'Neighborhood', 'City', 'State']
            data = [address_data["cep"], address_data["logradouro"], address_data["bairro"], address_data["localidade"], address_data["uf"]]

            self.animate(cep_found, speed)

            print()
            for i in range(0, len(masks)):
                line = f'{BOLD}{Fore.GREEN}{masks[i]:<14}|{Style.RESET_ALL}{CLOSING_TAG} {data[i]:>41}\n'
                self.animate(line, speed)
            separator_line = '=' * 57
            self.animate(f'{BOLD}{Fore.GREEN}{separator_line}{Style.RESET_ALL}{CLOSING_TAG}', speed)
            print()

        else:
            separator_line = '=' * 17
            cep_not_found = f'{BOLD}{Fore.RED}{separator_line} CEP number not found! {separator_line}{Style.RESET_ALL}{CLOSING_TAG}'
            cep_not_valid = f'{BOLD}{Fore.WHITE}{cep_number} is not a valid CEP number!{Style.RESET_ALL}{CLOSING_TAG}'
            separator_line = '=' * 57

            self.animate(cep_not_found, speed)
            print()
            self.animate(cep_not_valid, speed)
            print()
            self.animate(f'{BOLD}{Fore.RED}{separator_line}{Style.RESET_ALL}{CLOSING_TAG}', speed)
            print()


class Screen(App):
    def __init__(self, header_type, cep_number=None):
        self.set_terminal_title()
        self.header_type = header_type
        self.cep_number = cep_number
        self.clear_screen()
        self.print_header()


    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def set_terminal_title(self):
        title = 'Brazilian CEP checker'
        title_unix = f'"\\033]0;{title}\\007"'

        if os.name == 'nt':
            os.system(f'title {title}')
        elif os.name == 'posix':
            os.system(f'echo -n {title_unix}')


    def print_header(self):
        separator_line = '=-' * 28 + '='
        separator_blank = ' ' * 18
        header_text = f'''{BOLD}{Fore.WHITE}{Back.BLUE}
{separator_line}
{separator_blank}Brazilian CEP checker{separator_blank}
{separator_line}
{Style.RESET_ALL}{CLOSING_TAG}'''

        separator_line = '-' * 24
        status_title_ok = (f'{BOLD}{Fore.GREEN}{separator_line} STATUS: {separator_line}{Style.RESET_ALL}')
        status_title_error = (f'{BOLD}{Fore.RED}{separator_line} STATUS: {separator_line}{Style.RESET_ALL}{CLOSING_TAG}')
        
        match self.header_type:
            case 1:
                self.animate(header_text)
                print(status_title_ok)
                status_msg = f'{BOLD}{Fore.GREEN}Waiting for an input...{Style.RESET_ALL}{CLOSING_TAG}'
                print(status_msg)
                print()
            case 2:
                print(header_text, end='')
                print(status_title_error)
                status_msg = f'{BOLD}{Fore.RED}ERROR: CEP number must contain 8 digits!{Style.RESET_ALL}{CLOSING_TAG}'
                print(status_msg)
                print()
            case 3:
                print(header_text, end='')
                print(status_title_ok)
                status_msg = f'{BOLD}{Fore.GREEN}You\'ve entered: {Style.RESET_ALL}{Fore.WHITE}{self.cep_number}{Style.RESET_ALL}{CLOSING_TAG}'
                print(status_msg)
                print()


def main():
    # this_file_path = os.path.abspath(__file__)
    # this_file_path_unix = this_file_path.replace('\\', '/')

    # if not os.environ.get('PYTHONSTARTUP'):
    #     os.environ['PYTHONSTARTUP'] = '1'
    #     if os.name == 'nt':
    #         os.system(f'start powershell.exe "python {this_file_path}"')
    #     elif os.name == 'posix':
    #         os.system(f'gnome-terminal --working-directory=/path/to/script --command=\"bash -c \'{this_file_path_unix}; $SHELL\'\"')
    #     else:
    #         pass

    continue_running = True
    while continue_running:
        app = App()
        valid_options = ['y', 'n']
        print('\n')
        app.animate('Do you want to check another CEP number? (y/n)\n', speed=0.02)
        option = input().lower()[0]
        while option not in valid_options:
            print(f'\n{BOLD}{Fore.RED}Please enter "y" or "n"!{Style.RESET_ALL}{CLOSING_TAG}')
            option = input().lower()[0]
        if option == 'y':
            continue
        elif option == 'n':
            print()
            print(f'{BOLD}{Fore.GREEN}BYE! :){Style.RESET_ALL}{CLOSING_TAG}')
            sleep(3)
            continue_running = False


if __name__ == '__main__':
    main()