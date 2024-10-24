import os

from colorama import Fore, Back, Style


'''
Todas as constantes utilizadas pelo app.
'''
APP_TERMINAL_TITLE = 'WhatsApp Bot'

APP_NAME_PT_BR = '| Bot de envio automatizado de mensagens multimídia em massa para o WhatsApp |'
WIDTH_PT_BR = len(APP_NAME_PT_BR)
DIVIDER_LINE_TOP_PT_BR = '*' + '‾' * (len(APP_NAME_PT_BR) - 2) + '*'
DIVIDER_LINE_BOTTOM_PT_BR = '*' + '_' * (len(APP_NAME_PT_BR) - 2) + '*'

APP_NAME_EN_US = '| Automated bot for sending bulk multimedia messages on WhatsApp |'
WIDTH_EN_US = len(APP_NAME_EN_US)
DIVIDER_LINE_TOP_EN_US = '*' + '‾' * (len(APP_NAME_EN_US) - 2) + '*'
DIVIDER_LINE_BOTTOM_EN_US = '*' + '_' * (len(APP_NAME_EN_US) - 2) + '*'

SIGNATURE = 'Fernando Fonseca (https://github.com/fernandoaafonseca)'

URL_WHATSAPP_WEB = 'https://web.whatsapp.com/'
BYE_SOUND = 'sounds/bye.mp3'
ERROR_SOUND = 'sounds/error.mp3'

# 1: apenas texto; 2: texto + imagem/vídeo
MIN_MSG_TYPE = 1
MAX_MSG_TYPE = 2

# Selectores CSS e XPATH.
SEARCH_FIELD_XPATH = '//p[contains(@class,"selectable-text copyable-text")]'
MSG_FIELD_XPATH = '//p[contains(@class,"selectable-text copyable-text")]'
ATTACH_BUTTON_SELECTOR = '._1OT67'
IMG_INPUT_SELECTOR = '._1CGek input'
SEND_BUTTON_XPATH = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'

'''
Define as constantes para estilos de formatação e de cores do Colorama.
'''
BRIGHT = Style.BRIGHT
DIM = Style.DIM
NORMAL_STYLE = Style.NORMAL

APP_NAME_COLOR = f'{BRIGHT}{Back.LIGHTYELLOW_EX}{Fore.LIGHTBLACK_EX}'
ALERT_COLOR = Fore.RED
WARNING_COLOR = Fore.YELLOW
SUCCESS_COLOR = Fore.GREEN
NORMAL_COLOR = Fore.LIGHTYELLOW_EX
RESET_STYLES = Style.RESET_ALL

# Quantidade máxima de contatos.
MAX_AMOUNT = 50
'''
Velocidade em que o texto é animado pela função "animate_text()", do módulo "terminal_fx", em ms (milissegundos).
'''
TEXT_SPEED = 0.01
'''
Duração da contagem regressiva pra o carregamento da página inicial do WhatsApp Web.
'''
SLEEP_DURATION = 20
# Tempo de espera entre o envio de uma mensagem e outra.
TIME_BTW_MSGS = 15

# Todas as cores aceitas pelo Colorama para referência.
BLACK = Fore.BLACK
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
LIGHT_BLACK = Fore.LIGHTBLACK_EX
LIGHT_RED = Fore.LIGHTRED_EX
LIGHT_GREEN = Fore.LIGHTGREEN_EX
LIGHT_YELLOW = Fore.LIGHTYELLOW_EX
LIGHT_BLUE = Fore.LIGHTBLUE_EX
LIGHT_MAGENTA = Fore.LIGHTMAGENTA_EX
LIGHT_CYAN = Fore.LIGHTCYAN_EX
