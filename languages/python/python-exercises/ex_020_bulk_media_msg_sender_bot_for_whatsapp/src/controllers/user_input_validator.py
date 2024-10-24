import mimetypes
import os
import re


class UserInputValidator():
    '''
    Contém funções que checam a validade dos inputs do usuário.
    '''

    def __init__(self):
        pass

    def check_contact_list(self, contact_list_input):
        '''
        Checa se a lista de nomes segue o padrão correto.
        '''
        # Padrão para um nome, com apenas letras e um sobrenome opcional.
        contact_name_pattern = r'[A-Za-zÀ-ÖØ-öø-ÿ]+(\s+[A-Za-zÀ-ÖØ-öø-ÿ]+)?(\s+[A-Za-zÀ-ÖØ-öø-ÿ]+)?'

        # Padrão para a lista de nomes separados por vírgulas.
        contact_list_pattern = rf'^\s*({contact_name_pattern})(,\s*{contact_name_pattern})*\s*$'

        # Verifica se a entrada do usuário está no formato esperado
        if re.match(contact_list_pattern, contact_list_input):
            return True
        else:
            return False

    def check_media_path_exists(self, media_file_path):
        '''
        Checa se o arquivo do usuário existe no caminho especificado.
        '''
        if not os.path.exists(media_file_path):
            return False
        else:
            return True

    def check_media_type(self, media_file_path):
        '''
        Checa o se o arquivo do usuário é um arquivo de mídia válido.
        '''
        mimetypes.init()
        mimestart = mimetypes.guess_type(media_file_path)[0]

        if mimestart != None:
            mimestart = mimestart.split('/')[0]
            if mimestart in ['image', 'video']:
                # Se for um arquivo de áudio, imagem ou vídeo, retorna True.
                return True
        return False

    def check_media_size_exceeded(self, media_file_path):
        '''
        Checa se o tamanho do arquivo de mídia do usuário ultrapassa o limite máximo de 16MB.
        '''
        file_size_in_bytes = os.path.getsize(media_file_path)
        file_size_in_mb = file_size_in_bytes / (1024 * 1024)
        return file_size_in_mb > 16
