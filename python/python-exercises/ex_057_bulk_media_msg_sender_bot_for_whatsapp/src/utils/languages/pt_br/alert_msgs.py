from time import sleep

from src.utils.constants import *
from src.utils.languages.pt_br.screen_texts import ScreenTexts
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
        self.terminal_fx.animate_text('[X] ERRO: Algo deu errado! Tente novamente!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.play_sound(ERROR_SOUND)
        self.screen_texts.press_enter_to_continue()

    def invalid_option(self):
        '''
        Mensagem de erro para opção inválida em menus.
        '''
        self.screen_texts.app_title()
        self.terminal_fx.animate_text('[X] ERRO: Opção inválida!', ALERT_COLOR)
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
            '[⚠️] ERRO: Lista de contatos em formato inválido!', ALERT_COLOR)
        self.terminal_fx.animate_text(
            f'• Insira apenas nomes (e sobrenomes, se houverem) separados por \nvírgulas.', WARNING_COLOR)
        self.terminal_fx.pretty_print()

        self.screen_texts.press_enter_to_continue()

    def list_has_duplicated_names(self, duplicated_names):
        '''
        Mensagem de aviso para quando existem nomes duplicados no lista digitada pelo usuário.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            f'[X] AVISO: A lista contém nomes duplicados!', ALERT_COLOR)
        self.terminal_fx.animate_text(
            f'• Os nomes duplicados foram removidos da lista.', WARNING_COLOR)
        self.terminal_fx.pretty_print(
            f'• Nomes duplicados:\n{NORMAL_COLOR}{duplicated_names}.', WARNING_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def max_amount_of_contacts_exceeded(self):
        '''
        Mensagem de aviso para quando o usuário tenta configurar o bot para enviar para uma quantidade maior que a quantidade máxima de contatos.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[⚠️] AVISO: Quantidade máxima de contatos excedida!', ALERT_COLOR)
        self.terminal_fx.animate_text(
            f'• A quantidade será configurada para {MAX_AMOUNT}.', WARNING_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def file_not_found(self):
        '''
        Mensagem de erro para arquivo não encontrado no caminho enviado pelo usuário.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[X] ERRO: O arquivo não foi encontrado no caminho especificado!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def invalid_file_type(self):
        '''
        Mensagem de erro para formato de arquivo inválido.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[X] ERRO: Formato de arquivo inválido!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def file_size_exceeded(self):
        '''
        Mensagem de erro para arquivo maior que 16MB (tamanho máximo).
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[X] ERRO: Tamanho máximo de arquivo excedido!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def empty_text_msg(self):
        '''
        Mensagem de erro para quando o usuário pressiona ENTER sem digitar uma mensagem de texto.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[X] ERRO: Mensagem de texto vazia!', ALERT_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()

    def whatsapp_web_not_loaded(self):
        '''
        Mensagem de erro para quando o driver não conseguir carregar a página inicial do WhatsApp Web.
        '''
        self.play_sound(ERROR_SOUND)
        self.screen_texts.app_title()
        self.terminal_fx.animate_text(
            '[X] ERRO: WhatsApp Web não foi carregado corretamente!', ALERT_COLOR)
        self.terminal_fx.animate_text(
            '• Tente novamente!', WARNING_COLOR)
        self.terminal_fx.pretty_print()
        self.screen_texts.press_enter_to_continue()
