import os
import random

from src.controllers.user_input_validator import UserInputValidator
from src.utils.constants import *


class UserInputHandler:
    '''
    Contém funções que obtêm e manipulam os inputs do usuário.
    '''

    def __init__(self, user_language):
        if user_language == 'pt-br':
            from src.utils.languages.pt_br.screen_texts import ScreenTexts
            from src.utils.languages.pt_br.alert_msgs import AlertMsgs
        elif user_language == 'en-us':
            from src.utils.languages.en_us.screen_texts import ScreenTexts
            from src.utils.languages.pt_br.alert_msgs import AlertMsgs

        self.alert_msgs = AlertMsgs()
        self.screen_texts = ScreenTexts()
        self.user_input_validator = UserInputValidator()

    def get_contact_list(self):
        '''
        Recebe os inputs dos nomes dos contatos para os quais o usuário irá enviar a mensagem.
        '''
        while True:
            self.screen_texts.get_contact_list_screen()
            try:
                contact_list_input = input()
            except:
                self.alert_msgs.unknown_error()
                continue
            contact_list_is_valid = self.user_input_validator.check_contact_list(
                contact_list_input)

            if contact_list_is_valid:
                contact_list = self.create_contact_list(contact_list_input)
                break
            else:
                self.alert_msgs.invalid_contact_list_format()
                continue

        return contact_list

    def create_contact_list(self, contact_list_input):
        '''
        Se o usuário digitar uma lista de contatos válida, uma lista de contatos será criada.
        '''
        # Transforma a string em lista.
        contact_list_raw = [contact_name.strip().title()
                            for contact_name in contact_list_input.split(',')]

        # Pega a lista de nomes duplicados.
        duplicated_names = list(
            set([name for name in contact_list_raw if contact_list_raw.count(name) > 1]))

        # Pega apenas os nomes únicos da lista.
        contact_list = list(set(contact_list_raw))

        # Verifica se há nomes duplicados na lista. Se sim, mostra uma mensagem de aviso.
        if duplicated_names:
            self.alert_msgs.list_has_duplicated_names(duplicated_names)

        return contact_list

    def get_msg_type(self):
        '''
        Obtém o tipo de mensagem que o usuário quer enviar, dentre: 1 - Apenas texto; 2 - Mídia + texto.
        '''
        while True:
            self.screen_texts.get_msg_type_screen()
            try:
                msg_type = int(input())
            except:
                self.alert_msgs.invalid_option()
                continue

            if msg_type not in range(MIN_MSG_TYPE, MAX_MSG_TYPE + 1):
                self.alert_msgs.invalid_option()
                continue
            else:
                break

        return msg_type

    def get_text_msg(self):
        '''
        Obtém a mensagem de texto que o usuário quer enviar.
        '''
        while True:
            self.screen_texts.get_text_msg_screen()
            try:
                msg = str(input())
            except:
                self.alert_msgs.unknown_error()
                continue

            if msg == '':
                # Se o usuário enviar uma mensagem vazia, exibe uma mensagem de erro.
                self.alert_msgs.empty_text_msg()
                continue
            else:
                # Se o usuário inseriu uma quebra de linha, ela virá salva como '\\n' na string.
                fixed_msg = msg.replace('\\n', '\n')
                msg = fixed_msg
                break

        return msg

    def get_media_file_path(self):
        while True:
            self.screen_texts.get_media_file_path_screen()
            try:
                media_path_input = str(input())
            except:
                self.alert_msgs.unknown_error()
                continue

            # Caso o caminho do arquivo possua aspas simples ou duplas, elas serão deletadas.
            media_file_path = media_path_input.replace(
                '"', '').replace("'", '')

            # Obtém o caminho absoluto do arquivo.
            media_file_path = os.path.abspath(media_file_path)
            media_path_exists = self.user_input_validator.check_media_path_exists(
                media_file_path)

            if media_path_exists:
                # Checa se o arquivo existe.
                media_type_is_valid = self.user_input_validator.check_media_type(
                    media_file_path)
                if media_type_is_valid:
                    # Se o arquivo existe, checa se o tipo do arquivo é válido.
                    media_size_exceeded = self.user_input_validator.check_media_size_exceeded(
                        media_file_path)
                    if not media_size_exceeded:
                        # Se o tipo do arquivo for vâlido, checa se o tamanho excede 16MB. Se não, sai do loop.
                        break
                    else:
                        # Se o tamanho do arquivo excede 16MB, mostra uma mensagem de erro e retorna ao início do loop.
                        self.alert_msgs.file_size_exceeded()
                        continue
                else:
                    # Se o tipo do arquivo é inválido, mostra uma mensagem de erro e retorna ao início do loop.
                    self.alert_msgs.invalid_file_type()
                    continue
            else:
                # Se o arquivo não existe, mostra uma mensagem de erro e retorna ao início do loop.
                self.alert_msgs.file_not_found()
                continue

        return media_file_path

    def generate_final_msgs(self, contact_list, msg):
        '''
        Gera uma mensagem personalizada utilizando o nome do contato.
        '''
        final_msgs = []
        for contact_name in contact_list:
            if '-NOME-' in msg:
                new_msg = msg.replace('-NOME-', contact_name)
            elif '-NAME-' in msg:
                new_msg = msg.replace('-NAME-', contact_name)
            else:
                new_msg = msg
            final_msgs.append(new_msg)

        return final_msgs

    def review_data(self, contact_list, final_msgs, media_file_path):
        '''
        Mostra todos os dados enviados para que o usuário revise.
        '''
        random_sample_msg = random.choice(final_msgs)
        min_confirm_answer = 0
        if media_file_path != None:
            max_confirm_answer = 6
        else:
            max_confirm_answer = 4

        while True:
            self.screen_texts.review_data_scren(
                contact_list, random_sample_msg, media_file_path)
            try:
                user_review = int(input())
            except:
                self.alert_msgs.invalid_option()
                continue

            if user_review not in range(min_confirm_answer, max_confirm_answer + 1):
                self.alert_msgs.invalid_option()
                continue
            else:
                break

        return user_review
