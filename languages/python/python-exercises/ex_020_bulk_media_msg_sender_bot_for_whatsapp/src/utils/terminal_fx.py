import os
import sys
from time import sleep

from colorama import AnsiToWin32
from colorama import init as colorama_init

from src.utils.constants import *


class TerminalFX:
    '''
    Contém as funções de impressão e animação do texto no terminal.
    '''

    def __init__(self):
        '''
        Inicializa uma nova instância da classe. Configura o módulo Colorama para redefinir automaticamente a formatação e as cores do texto após a saída de cada comando de impressão "(autoreset=True)".
        Define o fluxo de saída padrão de texto do terminal, dependendo do OS em que o código está sendo executado. Se o sOS for Windows, utiliza o objeto "AnsiToWin32", que permite o uso de códigos ANSI no prompt de comando do Windows. Caso contrário, utiliza o objeto "sys.stderr".
        '''
        colorama_init(autoreset=True)

        if os.name == 'nt':
            self.stream = AnsiToWin32(sys.stderr).stream
        else:
            self.stream = sys.stderr

    def animate_text(self, text, style=Style.RESET_ALL, new_line=True, TEXT_SPEED=0.01):
        '''
        Anima o texto recebido usando a formatação e as cores recebidas como argumentos após a string. Se o argumento "style" não for passado, serão usadas a formatação e a cor padrão do terminal.
        Também é possível passar mais de um argumento, como por exemplo as cors de fundo e da fonte, além da formatação, usando uma f-string. Não use formatação no meio da string! Exemplo:
        animate_text('Texto animado em opaco (dim) com fundo vermelho e fonte branca.', f'{Back.RED}{Fore.WHITE}{DIM}')
        '''
        for letter in text:
            self.pretty_print(letter, style=style, end='')
            sleep(TEXT_SPEED)
        if new_line:
            # Insere uma quebra de linha ao final do texto por padrao,a não ser que seja passado o argumento "new_line=False".
            self.pretty_print()

    def pretty_print(self, text='', style=Style.RESET_ALL, end='\n'):
        '''
        Substitui a função print() padrão para que possa usar a formatação e as cores recebidas como parâmetros após a string. Se o argumento "style" não for passado, serão usadas a formatação e a cor padrão do terminal.
        Também é possível inserir vários parâmetros por meio de uma f-string, sendo: as cores de fundo e da fonte, além da formatação. Exemplo:
        pretty_print('Texto impresso em opaco (dim) com fundo vermelho e fonte branca. {MAGENTA}Aqui a fonte é magenta.', f'{DIM}Back.RED}{Fore.WHITE}')
        '''
        print(f'{style}{text}', end=end, flush=True, file=self.stream)
