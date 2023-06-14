import emoji
import re
from time import sleep

from src.utils.constants import *
from src.utils.terminal_fx import TerminalFX
from src.utils.terminal_utils import TerminalUtils


APP_NAME = APP_NAME_PT_BR
DIVIDER_LINE_TOP = DIVIDER_LINE_TOP_PT_BR
DIVIDER_LINE_BOTTOM = DIVIDER_LINE_BOTTOM_PT_BR
WIDTH = WIDTH_PT_BR


class ScreenTexts(TerminalUtils):
    '''
    Contém funções para exibir o título do aplicativo, seguido pelos textos de cada tela do terminal.
    '''

    def __init__(self):
        super().__init__()

    def app_title(self):
        '''
        Imprime o título do app em todas as telas do programa, com formatação e colorização do texto.
        '''
        self.clear_terminal()
        self.terminal_fx.pretty_print(
            DIVIDER_LINE_TOP, f'{APP_NAME_COLOR}{BRIGHT}')
        self.terminal_fx.pretty_print(APP_NAME, APP_NAME_COLOR)
        self.terminal_fx.pretty_print(DIVIDER_LINE_BOTTOM, APP_NAME_COLOR)
        self.terminal_fx.pretty_print()

    def press_enter_to_continue(self):
        '''
        Imprime uma mensagem na tela e aguarda até o usuário pressionar ENTER para o programa continuar.
        '''
        self.terminal_fx.animate_text(
            'Pressione ENTER para continuar...', LIGHT_CYAN, new_line=False)
        input()

    def press_enter_to_exit(self):
        '''
        Imprime uma mensagem na tela e aguarda até o usuário pressionar ENTER para o programa continuar.
        '''
        self.terminal_fx.animate_text(
            'Pressione ENTER para sair...', ALERT_COLOR, new_line=False)
        input()

    def main_screen(self):
        '''
        Imprime o título do app na tela inicial do programa, seguido de uma mensagem de boas-vindas, animando, formatando e colorindo o texto.
        '''
        self.clear_terminal()
        self.terminal_fx.animate_text(DIVIDER_LINE_TOP, APP_NAME_COLOR)
        self.terminal_fx.animate_text(APP_NAME, APP_NAME_COLOR)
        self.terminal_fx.animate_text(DIVIDER_LINE_BOTTOM, APP_NAME_COLOR)
        self.terminal_fx.pretty_print()

        welcome_txt = 'Bem-vindo(a)! 🤖'
        self.terminal_fx.animate_text(welcome_txt.center(WIDTH), f'{BRIGHT}{SUCCESS_COLOR}')
        self.terminal_fx.pretty_print()

        self.terminal_fx.pretty_print(DIVIDER_LINE_TOP, NORMAL_COLOR)

        self.max_txt_width = WIDTH - 5
        self.empty_space_left = 2
        empty_line_space = WIDTH - 2

        txt_1 = '💡 Como usar:'
        self.print_pattern_text_main_screen(txt_1, WARNING_COLOR, has_emoji=True)

        self.terminal_fx.pretty_print('|' + ' ' * empty_line_space + '|', f'{DIM}{NORMAL_COLOR}')

        txt_2 = '• 1 - Escolha o tipo de mensagem (apenas texto ou texto + imagem/vídeo);'
        self.print_pattern_text_main_screen(txt_2, NORMAL_COLOR)

        txt_3 = '• 2 - Insira uma lista de nomes dos seus contatos e/ou grupos separados por vírgulas;'
        self.print_pattern_text_main_screen(txt_3, NORMAL_COLOR)

        txt_4 = '• 3 - Digite a mensagem que você quer enviar;'
        self.print_pattern_text_main_screen(txt_4, NORMAL_COLOR)

        txt_5 = '• 4 - Adicione um arquivo de imagem ou vídeo (opcional);'
        self.print_pattern_text_main_screen(txt_5, NORMAL_COLOR)

        txt_6 = '• 5 - Escaneie o QR code para se conectar à sua conta do WhatsApp;'
        self.print_pattern_text_main_screen(txt_6, NORMAL_COLOR)

        txt_7 = '• 6 - Confira se todos os dados estão corretos;'
        self.print_pattern_text_main_screen(txt_7, NORMAL_COLOR)

        txt_8 = '• 7 - Pronto! Agora é só aguardar o bot enviar automaticamente a mensagem para os seus contatos.'
        self.print_pattern_text_main_screen(txt_8, NORMAL_COLOR)

        self.terminal_fx.pretty_print(DIVIDER_LINE_BOTTOM, NORMAL_COLOR)
        self.terminal_fx.pretty_print()

        empty_space_left = 2
        self.terminal_fx.pretty_print(DIVIDER_LINE_TOP, f'{DIM}{NORMAL_COLOR}')
        footer = '• Este é um projeto pessoal criado por hobby com fins didáticos. Não me responsabilizo por qualquer uso indevido. Seja legal, não envie spam!'
        self.print_pattern_text_main_screen(footer, f'{DIM}{NORMAL_COLOR}', footer=True)

        self.terminal_fx.pretty_print('|' + ' ' * empty_line_space + '|', f'{DIM}{NORMAL_COLOR}')

        signature = f'-> {SIGNATURE}'
        self.print_pattern_text_main_screen(signature, f'{DIM}{NORMAL_COLOR}', footer=True)
        self.terminal_fx.pretty_print(DIVIDER_LINE_BOTTOM, f'{DIM}{NORMAL_COLOR}')
        self.terminal_fx.pretty_print()

        self.press_enter_to_continue()

    def print_pattern_text_main_screen(self, txt, style, has_emoji=False, footer=False):
        txt = self.fix_text_width(txt, text_type='normal_text', max_width=self.max_txt_width)

        for line in txt:
            empty_space_right = WIDTH - len(line) - self.empty_space_left - 2
            if has_emoji:
                empty_space_right -= 1
            if footer:
                self.terminal_fx.pretty_print('|' + ' ' * self.empty_space_left, style, end='')
                self.terminal_fx.pretty_print(line + ' ' * empty_space_right + '|', style)
            else:
                self.terminal_fx.pretty_print(NORMAL_COLOR + '|' + style + ' ' * self.empty_space_left, style, end='')
                self.terminal_fx.pretty_print(line + ' ' * empty_space_right + NORMAL_COLOR + '|', style)

    def get_msg_type_screen(self):
        '''
        Texto da tela da função get_msg_type().
        '''
        self.app_title()
        self.terminal_fx.pretty_print('[🚀] INÍCIO:', SUCCESS_COLOR)
        self.terminal_fx.pretty_print(
            f'• Vamos começar a configuração!', WARNING_COLOR)
        self.terminal_fx.pretty_print()

        self.terminal_fx.animate_text(
            '-> Qual o tipo de mensagem que você quer enviar?', NORMAL_COLOR, new_line=False)
        self.terminal_fx.animate_text('\n\
        1 - Apenas texto \n\
        2 - Mídia (imagem ou vídeo) + texto', NORMAL_COLOR)

    def get_contact_list_screen(self):
        '''
        Texto da tela da função get_contact_list().
        '''
        self.app_title()
        self.terminal_fx.pretty_print('[💡] INSTRUÇÕES:', SUCCESS_COLOR)
        self.terminal_fx.pretty_print(
            f'• Insira os nomes dos seus contatos e/ou grupos separados por {NORMAL_COLOR}vírgulas{WARNING_COLOR}. Cada \ncontato deve conter {NORMAL_COLOR}no máximo 3 nomes{WARNING_COLOR}. Exemplo: {NORMAL_COLOR}"John, Lennon, Paul McCartney, \nGeorge Harrison, Ringo Starr, Ozzy, Ronnie James Dio, Grupo da Banda"{WARNING_COLOR}.', WARNING_COLOR)
        self.terminal_fx.pretty_print(
            '• Certifique-se de digitar os nomes corretamente.', WARNING_COLOR)
        self.terminal_fx.pretty_print()

        self.terminal_fx.animate_text(
            f'-> Digite os nomes dos contatos:', NORMAL_COLOR)

    def get_text_msg_screen(self):
        '''
        Texto da tela da função "get_text_msg()".
        '''
        self.app_title()
        self.terminal_fx.pretty_print('[💡] INSTRUÇÕES:', SUCCESS_COLOR)
        self.terminal_fx.pretty_print(
            f'• Digite {NORMAL_COLOR}"\\n" {WARNING_COLOR}(sem as aspas) ao final da linha para adicionar uma nova linha. \nPor exemplo: {NORMAL_COLOR}"Esta é a primeira linha.\\nAqui começa a segunda linha."{WARNING_COLOR}.', WARNING_COLOR)
        self.terminal_fx.pretty_print(
            f'• Para adicionar um {NORMAL_COLOR}emoji{WARNING_COLOR}, pressione {NORMAL_COLOR}"WINDOWS + ." {WARNING_COLOR}e selecione o emoji. (O \nterminal pode exibir alguns emojis como "�", mas não se preocupe! Eles serão \nenviados corretamente.)', WARNING_COLOR)
        self.terminal_fx.pretty_print(
            f'• Para usar a formatação do WhatsApp, use os seguintes símbolos ao redor da \npalavra ou frase que deseja formatar: {NORMAL_COLOR}_itálico_{WARNING_COLOR}, {NORMAL_COLOR}*negrito*{WARNING_COLOR}, {NORMAL_COLOR}~riscado~{WARNING_COLOR} ou \n{NORMAL_COLOR}```monoespaçado```{WARNING_COLOR}.', WARNING_COLOR)
        self.terminal_fx.pretty_print(
            f'• Use o código {NORMAL_COLOR}"-NOME-" {WARNING_COLOR}(sem as aspas) em qualquer parte do texto e ele será \nsubstituído pelo nome do contato. Exemplo: {NORMAL_COLOR}"Olá, -NOME-!" {WARNING_COLOR}-> {NORMAL_COLOR}"Olá, John!"{WARNING_COLOR}.', WARNING_COLOR)
        self.terminal_fx.pretty_print()

        self.terminal_fx.animate_text(
            '-> Digite a mensagem a ser enviada:', NORMAL_COLOR)

    def get_media_file_path_screen(self):
        '''
        Texto da tela da função get_user_media_file_path().
        '''
        self.app_title()
        self.terminal_fx.pretty_print('[💡] INSTRUÇÕES:', SUCCESS_COLOR)
        self.terminal_fx.pretty_print(
            f'• O tamanho do arquivo de mídia não pode exceder {NORMAL_COLOR}16MB{WARNING_COLOR}.', WARNING_COLOR)
        self.terminal_fx.pretty_print(
            f'• Com a tecla {NORMAL_COLOR}"SHIFT" {WARNING_COLOR}pressionada, clique com o {NORMAL_COLOR}"botão direito" {WARNING_COLOR}no arquivo e \nselecione a opção {NORMAL_COLOR}"Copiar como caminho".', WARNING_COLOR)
        self.terminal_fx.pretty_print(
            f'• Para colar, clique com o {NORMAL_COLOR}"botão direito" {WARNING_COLOR}na tela do terminal.', WARNING_COLOR)
        self.terminal_fx.pretty_print()

        self.terminal_fx.animate_text(
            '-> Cole o caminho do arquivo de mídia que deseja enviar:', NORMAL_COLOR)

    def review_data_scren(self, contact_list, random_sample_msg, media_file_path):
        '''
        Texto da tela da função review_data(),
        '''
        self.review_data_boxes = ReviewDataBoxes()
        self.app_title()
        self.terminal_fx.animate_text('[✓] TUDO CERTO!', SUCCESS_COLOR)
        self.terminal_fx.animate_text(
            '• Fui configurado com sucesso e estou pronto para o trabalho! 🤖', NORMAL_COLOR)
        self.terminal_fx.animate_text(
            '• Confirme os dados abaixo...', NORMAL_COLOR)
        self.terminal_fx.pretty_print()
        self.terminal_fx.animate_text(
            '-> Suas configurações...', SUCCESS_COLOR)

        self.terminal_fx.animate_text(
            '• NOMES:', WARNING_COLOR)
        self.review_data_boxes.print_contact_names(contact_list)
        self.terminal_fx.pretty_print()

        self.terminal_fx.animate_text(
            '• EXEMPLO DE MENSAGEM:', WARNING_COLOR)
        self.review_data_boxes.print_sample_msg(random_sample_msg)
        self.terminal_fx.pretty_print()

        if media_file_path != None:
            self.terminal_fx.animate_text(
            '• LOCALIZAÇÃO DO ARQUIVO DE MÍDIA:', WARNING_COLOR)
            self.review_data_boxes.print_media_path(media_file_path)
            self.terminal_fx.pretty_print()
        self.terminal_fx.pretty_print()

        self.terminal_fx.animate_text('-> Deseja iniciar os envios agora ou voltar e corrigir algo?', NORMAL_COLOR)
        self.terminal_fx.pretty_print('\
        1 - ENVIAR!', f'{BRIGHT}{SUCCESS_COLOR}')
        self.terminal_fx.pretty_print('\
        2 - Corrigir a lista de contatos...', WARNING_COLOR)
        self.terminal_fx.pretty_print('\
        3 - Corrigir a mensagem...', WARNING_COLOR)
        if media_file_path != None:
            self.terminal_fx.pretty_print('\
        4 - Corrigir o arquivo de mídia...', WARNING_COLOR)
            self.terminal_fx.pretty_print('\
        5 - Visualizar o arquivo de mídia...', WARNING_COLOR)
            self.terminal_fx.pretty_print('\
        6 - Deletar o arquivo de mídia...', WARNING_COLOR)
        else:
            self.terminal_fx.pretty_print('\
        4 - Adicionar um arquivo de mídia...', WARNING_COLOR)
        self.terminal_fx.pretty_print('\
        0 - SAIR!', f'{BRIGHT}{ALERT_COLOR}')

    def prepare_to_connect_screen(self):
        '''
        Texto da tela da função prepare_to_connect().
        '''
        self.app_title()
        self.terminal_fx.pretty_print('[💡] INSTRUÇÕES:', SUCCESS_COLOR)
        self.terminal_fx.pretty_print(f'• Pegue seu celular! Abra o WhatsApp, toque em {NORMAL_COLOR}"Mais opções (...)" {WARNING_COLOR}e, em \nseguida, em {NORMAL_COLOR}"Aparelhos conectados"{WARNING_COLOR}. Toque em {NORMAL_COLOR}"Conectar um aparelho"{WARNING_COLOR}. Por fim, \nposicione a câmera do seu aparelho em frente à tela e {NORMAL_COLOR}escaneie o QR code{WARNING_COLOR}.', WARNING_COLOR)
        self.terminal_fx.pretty_print()
        self.terminal_fx.pretty_print('[⚠️] Certifique-se de que o Chrome esteja fechado antes de continuar.', ALERT_COLOR)
        self.terminal_fx.pretty_print()

    def wait_for_loading_scrren(self, remaining_secs):
        '''
        Texto da tela da função wait_for_loading(). Atualiza a cada 1 segundo, até que "remaining_secs" seja igual a 0.
        '''
        for _ in range(remaining_secs):
            self.app_title()
            self.terminal_fx.pretty_print(
                '[⌛] CARREGANDO...', WARNING_COLOR)
            self.terminal_fx.pretty_print('• Aguarde o carregamento da página...', WARNING_COLOR)
            self.terminal_fx.pretty_print()

            self.terminal_fx.pretty_print(f'{remaining_secs}', ALERT_COLOR, end='')
            sleep(0.25)
            for _ in range(3):
                self.terminal_fx.pretty_print('.', ALERT_COLOR, end='')
                sleep(0.25)
            remaining_secs -= 1

    def show_countdown_screen(self, remaining_secs):
        '''
        Texto da tela da função show_countdown(). Atualiza a cada 1 segundo, até que "remaining_secs" seja igual a 0.
        '''
        self.app_title()
        self.terminal_fx.pretty_print(
            '[⌛] CARREGANDO...', SUCCESS_COLOR)
        self.terminal_fx.pretty_print('• Aguarde alguns instantes...', WARNING_COLOR)
        self.terminal_fx.pretty_print()

        self.terminal_fx.pretty_print(f'{remaining_secs}', ALERT_COLOR, end='')
        sleep(0.25)
        for _ in range(3):
            self.terminal_fx.pretty_print('.', ALERT_COLOR, end='')
            sleep(0.25)

    def send_bulk_messages_screen(self, contact_name):
        '''
        Mensagem de página carregada com sucesso.
        '''
        self.app_title()
        self.terminal_fx.pretty_print(
            '[📨] ENVIANDO...', WARNING_COLOR)
        self.terminal_fx.pretty_print(
            f'• Enviando mensagem para {contact_name}...', WARNING_COLOR)
        self.terminal_fx.pretty_print('• Aguarde alguns instantes...', WARNING_COLOR)
        self.terminal_fx.pretty_print()

    def msg_sent_screen(self, contact_name):
        '''
        Texto da tela da função show_countdown(). Atualiza a cada 1 segundo, até que "remaining_secs" seja igual a 0.
        '''
        self.app_title()
        self.terminal_fx.pretty_print(
            '[✉️] MENSAGEM ENVIADA', SUCCESS_COLOR)
        self.terminal_fx.pretty_print(f'• Mensagem enviada com sucesso para {contact_name}!', SUCCESS_COLOR)
        self.terminal_fx.pretty_print()
        self.terminal_fx.pretty_print('• Aguarde alguns instantes...', WARNING_COLOR)

    def exit_app_screen(self):
        '''
        Texto da tela de despedida do app.
        '''
        self.app_title()
        self.terminal_fx.pretty_print(
            '[🎉] FIM!', SUCCESS_COLOR)
        self.play_sound(BYE_SOUND)
        bye_text = '• Programa finalizado! Até a próxima 🤖!'
        self.terminal_fx.animate_text(bye_text.center(len(bye_text)), SUCCESS_COLOR, TEXT_SPEED=0.2)
        self.terminal_fx.pretty_print()

        self.press_enter_to_exit()
        self.clear_terminal()


class ReviewDataBoxes(TerminalUtils):
    '''
    Contém funções para imprimir as caixas de dados da tela de review_data().
    '''
    def __init__(self):
        super().__init__()
        self.terminal_fx = TerminalFX()
        self.max_text_width = WIDTH - 10

    def print_pattern(self, text, empty_space_left, empty_space_right, text_type):
        '''
        Imprime o padrão de texto usado na grade de nomes de contatos, no exemplo de mensagem e no arquivo de mídia.
        '''
        if text_type == 'name':
            # Como a grade de nomes de contatos é printada por colunas e não a linha inteira, o print é ligeiramente diferente.
            self.terminal_fx.pretty_print(' ' * empty_space_left, end='')
            self.terminal_fx.pretty_print(text, end='')
            self.terminal_fx.pretty_print(' ' * empty_space_right, end='')
            self.terminal_fx.pretty_print('|', end='')
        elif text_type == 'msg' or text_type == 'path':
            self.terminal_fx.pretty_print('|', end='')
            self.terminal_fx.pretty_print(' ' * empty_space_left, end='')
            self.terminal_fx.pretty_print(text, end='')

    def print_contact_names(self, contact_list):
        '''
        Imprime uma grade com 3 colunas, em que cada coluna é do mesmo tamanho e cada linha contém o mesmo número de nomes de contatos (exceto possivelmente a última, se a lista não for um múltiplo de 3).O espaço à esquerda é padrinizado, fazendo com que todos os nomes fiquem alinhados.
        '''
        columns = 3
        cell_width = WIDTH / columns
        empty_space_left = 2
        contacts_amount = len(contact_list)
        # Quantidade de linhas vazias que devo adicionar ao final da última linha.
        remainder = len(contact_list) % columns
        empty_cells = columns - remainder
        empty_cell_spaces = int(cell_width - 1)

        self.terminal_fx.pretty_print(DIVIDER_LINE_TOP)
        for i in range(contacts_amount):
            contact_name = contact_list[i]
            # O tamanho máximo do nome deve ser o tamanho da célula, menos o espaço vazio à esquerda, menos 3 (dois "|" e pelo menos um espaço vazio à direita).
            contact_name_max_width = int(cell_width - empty_space_left - 3)
            contact_name = self.fix_text_width(contact_name, text_type='name', max_width=contact_name_max_width)
            contact_size = len(contact_name)
            # Empaço à direita é igual tamanho da céula, menos o espaço ainda não ocupado pelo nome do contato, pelo espaço à esquerda e por 2 "!".
            empty_space_right = int(
                cell_width - contact_size - empty_space_left - 2)
            if i % 3 == 0 and i == 0:
                # Printa o primeiro caractere da linha.
                self.terminal_fx.pretty_print('|', end='')
                self.print_pattern(contact_name, empty_space_left, empty_space_right, text_type='name')
            elif i % 3 == 0 and i != 0:
                # Pula para a próxima linha e printa o primeiro caractere e da linha.
                self.terminal_fx.pretty_print()
                self.terminal_fx.pretty_print('|', end='')
                self.print_pattern(contact_name, empty_space_left, empty_space_right, text_type='name')
            else:
                empty_space_right += 1
                self.print_pattern(contact_name, empty_space_left, empty_space_right, text_type='name')
            empty_space_right -= 2

        # Se o resto da divisão (quantidade de contatos ÷ quantidade de colunas) for != 0, então existirão espaços vazios na grade. Eles serão preenchidos com espaçoes até completar a linha final da grade..
        if remainder != 0:
            for i in range(empty_cells):
                self.terminal_fx.pretty_print(' ' * empty_cell_spaces, end='')
                self.terminal_fx.pretty_print('|', end='')
        self.terminal_fx.pretty_print()
        self.terminal_fx.pretty_print(DIVIDER_LINE_BOTTOM)

    def print_sample_msg(self, random_sample_msg):
        '''
        Imprime a mensagem de exemplo dentro de uma caixa.
        '''
        empty_space_left = 2
        empty_line_space = WIDTH - 2
        # Divide a mensagem em uma lista de substrings, separando-a por quebra de linha "\n".
        msg_lines = random_sample_msg.splitlines()

        self.terminal_fx.pretty_print(DIVIDER_LINE_TOP)
        for msg_line in msg_lines:
            fixed_msg_lines = self.fix_text_width(msg_line, text_type='msg', max_width=self.max_text_width)
            if msg_line == '':
                # Se encontrar uma quebra de linha, printa um espaço vazio cercado com dois "|".
                print('|' + ' ' * empty_line_space + '|')
            for fixed_line in fixed_msg_lines:
                # Troca o caractere "\u200d", que alguns emojis têm e que aumenta o espaço em braco, por um vazio.
                zero_width_joiner = '\u200d'
                fixed_line = fixed_line.replace(zero_width_joiner, '')
                emoji_count = emoji.emoji_count(fixed_line)
                emojis_pattern = r'(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])'
                emoji_len = len(re.findall(emojis_pattern, fixed_line))
                line_width = WIDTH - 5
                if emoji_count > emoji_len:
                    line_width -= emoji_count - emoji_len
                bar = '|'
                line = f'{fixed_line:<{line_width}}{bar:>2}\n'
                self.print_pattern(line, empty_space_left, empty_space_right=0, text_type='msg')
        self.terminal_fx.pretty_print(DIVIDER_LINE_BOTTOM)

    def print_media_path(self, user_media_file_path):
        lines = self.fix_text_width(user_media_file_path, text_type='path', max_width=self.max_text_width)

        self.terminal_fx.pretty_print(DIVIDER_LINE_TOP)
        for line in lines:
            empty_space_right = self.max_text_width - len(line) + 6
            self.terminal_fx.pretty_print('|', end='')
            self.terminal_fx.pretty_print(' ' * 2, end='')
            self.terminal_fx.pretty_print(line, end='')
            self.terminal_fx.pretty_print(' ' * empty_space_right, end='')
            self.terminal_fx.pretty_print('|', end='')
            self.terminal_fx.pretty_print()
        self.terminal_fx.pretty_print(DIVIDER_LINE_BOTTOM)
