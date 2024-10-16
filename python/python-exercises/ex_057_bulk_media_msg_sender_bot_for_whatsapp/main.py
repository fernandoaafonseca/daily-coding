import os

from src.utils.constants import APP_TERMINAL_TITLE
from src.controllers.app import App


def main():
    '''
    Inicializa o app.
    '''
    app = App()


if __name__ == '__main__':
    title_unix = f'"\\033]0;{APP_TERMINAL_TITLE}\\007"'

    if os.name == 'nt':
        os.system(f'title {APP_TERMINAL_TITLE}')
    elif os.name == 'posix':
        os.system(f'echo -n {title_unix}')
    main()
