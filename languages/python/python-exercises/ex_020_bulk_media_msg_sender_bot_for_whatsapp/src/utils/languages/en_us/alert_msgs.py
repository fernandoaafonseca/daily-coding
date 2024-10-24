from time import sleep

from src.utils.constants import *
from src.utils.languages.en_us.screen_texts import ScreenTexts
from src.utils.terminal_utils import TerminalUtils


class AlertMsgs(TerminalUtils):
    '''
    Contém funções para exibir diferentes mensagens de aviso ou de erro no terminal. Herda de "TerminalPrints" para utilizar sua funcionalidade de impressão no terminal.
    '''

    def __init__(self):
        '''
        Invoca o construtor da superclasse "TerminalPrints".
        '''
        super().__init__()
        self.screen_texts = ScreenTexts()

    def unknown_error(self):
        '''
        Mensagem de erro desconhecido.
        '''
        self.screen_texts.app_title()
        self.terminal_fx.animate_text('[X] ERROR: Something went wrong! Try again!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.play_sound(ERROR_SOUND)
        self.screen_texts.press_enter_to_continue()

    def invalid_option(self):
        '''
        Mensagem de erro para opção inválida em menus.
        '''
        self.screen_texts.app_title()
        self.terminal_fx.animate_text('[X] ERROR: Invalid option!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.play_sound(ERROR_SOUND)
        self.screen_texts.press_enter_to_continue()

    def invalid_contact_list_format(self):
        '''
        Mensagem de erro para lista de contatos em formato inválido.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[⚠️] ERROr: Contact list in invalid format!', ALERT_COLOR)
        self.terminal_fx.animate_text(
            f'• Enter only names separated by commas.', WARNING_COLOR)
        self.terminal_fx.pretty_print()

        self.screen_texts.press_enter_to_continue()

    def list_has_duplicated_names(self, duplicated_names):
        '''
        Mensagem de aviso para quando existem nomes duplicados no lista digitada pelo usuário.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            f'[X] WARNING: List contains duplicate names!', ALERT_COLOR)
        self.terminal_fx.animate_text(
            f'• Duplicate names have been removed from the list.', WARNING_COLOR)
        self.terminal_fx.pretty_print(
            f'• Duplicate names:\n{NORMAL_COLOR}{duplicated_names}.', WARNING_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def max_amount_of_contacts_exceeded(self):
        '''
        Mensagem de aviso para quando o usuário tenta configurar o bot para enviar para uma quantidade maior que a quantidade máxima de contatos.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[⚠️] WARNING: Maximum number of contacts exceeded!', ALERT_COLOR)
        self.terminal_fx.animate_text(
            f'• The amount will be set to {MAX_AMOUNT}.', WARNING_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def file_not_found(self):
        '''
        Mensagem de erro para arquivo não encontrado no caminho enviado pelo usuário.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[X] ERROR: The file was not found in the specified path!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def invalid_file_type(self):
        '''
        Mensagem de erro para formato de arquivo inválido.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[X] ERROR: Invalid file type!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def file_size_exceeded(self):
        '''
        Mensagem de erro para arquivo maior que 16MB (tamanho máximo).
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[X] ERROR: Maximum file size exceeded!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def empty_text_msg(self):
        '''
        Mensagem de erro para quando o usuário pressiona ENTER sem digitar uma mensagem de texto.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[X] ERROR: Empty text message!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def whatsapp_web_not_loaded(self):
        '''
        Mensagem de erro para quando o driver não conseguir carregar a página inicial do WhatsApp Web.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[X] ERROR: WhatsApp Web did not load correctly!', ALERT_COLOR)
        self.terminal_fx.animate_text(
            '• Try again!', WARNING_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()
