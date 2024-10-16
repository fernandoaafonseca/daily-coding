import os
import sys
from time import sleep

from src.controllers.bot import Bot
from src.controllers.user_input_handler import UserInputHandler
from src.utils.constants import *
from src.utils.terminal_fx import TerminalFX
from src.utils.terminal_utils import TerminalUtils


class App():
    '''
    Módulo com todas as funções principais para a configuração do bot. Ele vai obter a língua do usuário e todar as variáveis que o usuário digitar, perguntar ao usuário se todos os dados estão corretos e, por fim, vai passar todas os dados para o módulo "bot".
    '''

    def __init__(self):
        '''
        Método construtor da classe. Inicializa as variáveis que serão utilizadas e, por fim, chama a função "perform_tasks()", que inicializará todas as funções do bot.
        '''
        self.terminal_fx = TerminalFX()
        self.terminal_utils = TerminalUtils()
        self.user_language = self.get_language()
        if self.user_language == 'pt-br':
            from src.utils.languages.pt_br.screen_texts import ScreenTexts
        elif self.user_language == 'en-us':
            from src.utils.languages.en_us.screen_texts import ScreenTexts
        self.screen_texts = ScreenTexts()
        self.user_input = UserInputHandler(self.user_language)
        self.perform_tasks()

    def get_language(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.terminal_fx.animate_text(
                '-> Selecione sua língua / Select your language:', NORMAL_COLOR, new_line=False)
            self.terminal_fx.animate_text('\n\
        1 - Português\n\
        2 - English', NORMAL_COLOR)
            try:
                user_language = int(input())
                if user_language == 1:
                    user_language = 'pt-br'
                    break
                elif user_language == 2:
                    user_language = 'en-us'
                    break
                else:
                    self.invalid_language_option()
                    continue
            except:
                self.invalid_language_option()
                pass
        return user_language

    def invalid_language_option(self):
        self.terminal_fx.pretty_print()
        self.terminal_fx.pretty_print(
            '[X] ERRO / ERROR: Opção inválida / Invalid option!', ALERT_COLOR)
        self.terminal_utils.play_sound(ERROR_SOUND)
        sleep(3)

    def perform_tasks(self):
        '''
        Invoca todas as funções necessárias na ordem certa para que o bot realize suas tarefas.
        '''
        # Tela inicial de boas-vindas.
        self.screen_texts.main_screen()
        # Obtém todos os inputs necessários do usuário.
        self.get_all_user_inputs()
        # Tela para que o usuário o usuário cheque e confirme todos os dados enviados.
        self.check_user_data_confirmation()
        # Inicializa o módulo de envio de mensagens.
        self.msg_sender = Bot(self.user_language)
        self.msg_sender.init_data(
            self.contact_list, self.final_msgs, self.media_file_path)
        self.msg_sender.start()
        # Finaliza o app.
        self.exit_app()

    def get_all_user_inputs(self):
        '''
        Invoca todas as funções para obter os inputs necessários do usuário, salvando os retornos em suas respectivas variáveis.
        '''
        self.msg_type = self.user_input.get_msg_type()
        self.contact_list = self.user_input.get_contact_list()
        self.msg = self.user_input.get_text_msg()
        self.final_msgs = self.user_input.generate_final_msgs(
            self.contact_list, self.msg)
        # Se o tipo de mensagem não for apenas texto (já que a opção 1 é "Apenas texto"), vai obter cominho para a mídia do usuário.
        if self.msg_type > 1:
            self.media_file_path = self.user_input.get_media_file_path()
        else:
            self.media_file_path = None

    def open_media(self, media_file_path):
        '''
        Visualiza o arquivo de mídia em uma nova janela.
        '''
        if os.name == 'nt':
            # Windows.
            os.system('start "" "' + media_file_path + '"')
        elif os.name == 'posix':
            # Linux ou macOS,
            os.system('xdg-open "" "' + media_file_path + '"')

    def check_user_data_confirmation(self):
        '''
        Checa se o usuário confirmou os dados atuais na tela de review.
        '''
        while True:
            self.user_confirm = self.user_input.review_data(
                self.contact_list, self.final_msgs, self.media_file_path)
            match self.user_confirm:
                case 1:
                    # Usuário revisou os dados enviados, o  app irá começar os envios das mensagens.
                    break
                case 2:
                    self.contact_list = self.user_input.get_contact_list()
                    self.final_msgs = self.user_input.generate_final_msgs(
                        self.contact_list, self.msg)
                case 3:
                    self.msg = self.user_input.get_text_msg()
                    self.final_msgs = self.user_input.generate_final_msgs(
                        self.contact_list, self.msg)
                case 4:
                    self.media_file_path = self.user_input.get_media_file_path()
                case 5:
                    self.open_media(self.media_file_path)
                case 6:
                    self.media_file_path = None
                case 0:
                    self.exit_app()

    def exit_app(self):
        '''
        Exibe a mensagem final e finaliza o programa.
        '''
        self.screen_texts.exit_app_screen()
        sys.exit()
