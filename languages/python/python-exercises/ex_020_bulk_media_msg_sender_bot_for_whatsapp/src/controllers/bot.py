from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from src.utils.constants import *


class Bot:
    '''
    Módulo que recebe de "app" todas as configurações do usuário e realiza todas as operações automatizadas de envio das mensagens.
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

    def init_data(self, contact_list, final_msgs, media_file_path):
        '''
        Recebe os dados enviados pelo usuário.
        '''
        self.contact_list = contact_list
        self.final_msgs = final_msgs
        self.media_file_path = media_file_path

    def start(self):
        '''
        Inicializa a importação da língua correta e a execução das tarefas.
        '''
        self.prepare_to_connect()
        self.init_webdriver()
        self.load_whatsapp_web()
        self.wait_for_loading()
        self.send_bulk_messages()
        self.driver.quit()

    def prepare_to_connect(self):
        '''
        Pede ao usuário que prepare seu smartphone para que escaneie o QR code.
        '''
        self.screen_texts.prepare_to_connect_screen()
        self.screen_texts.press_enter_to_continue()

    def init_webdriver(self):
        '''
        Instala e inicializa driver do navegador.
        '''
        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()))
        '''
        O código abaixo serve para que o QR code não precise ser escaneado toda vez que o bot for usado. O caminho deve ser substituído pelo caminho da instalação do Chrome.
        '''
        # options = webdriver.ChromeOptions()
        # options.add_argument(
        #     r'--user-data-dir=C:\\Users\\ferna\\AppData\\Local\\Google\\Chrome\\User Data\\')
        # self.driver = webdriver.Chrome(
        #     executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)

    def load_whatsapp_web(self):
        '''
        Abre o navegador e carrega a página inicial do WhatsApp Web.
        '''
        self.driver.get(URL_WHATSAPP_WEB)

    def wait_for_loading(self):
        '''
        Checa se a página inicial do WhatsApp Web foi carregada corretamente.
        '''
        while True:
            sleep(5)
            try:
                '''
                Checa se a página do contato carregou, baseando-se na existência do XPATH  do "campo de pesquisa" (já que ele só carrega se o WhatsApp Web abriu). Se não, aguarda alguns segundos "(self.driver, SLEEP_DURATION)" e tenta novamente.
                '''
                self.screen_texts.wait_for_loading_scrren(SLEEP_DURATION)
                elem = WebDriverWait(self.driver, SLEEP_DURATION).until(
                    EC.presence_of_element_located((By.XPATH, SEARCH_FIELD_XPATH)))
            except:
                # Se não, exibe mensagem de erro e tenta novamente.
                self.alert_msgs.whatsapp_web_not_loaded()
                self.driver.quit()
                self.load_whatsapp_web()
            else:
                # Página do contato carregada com sucesso. O bot vai enviar as mensagens.
                break

    def send_bulk_messages(self):
        for i in range(len(self.contact_list)):
            contact_name = self.contact_list[i]
            msg = self.final_msgs[i]
            self.screen_texts.send_bulk_messages_screen(contact_name)

            # O bot abre a página do contato.
            self.find_contact(contact_name)
            sleep(3)

            # O bot digita a mensagem
            self.write_text_msg(msg)

            # Se o usuário tiver enviado um arquivo de mídia, ele será anexado.
            if self.media_file_path != None:
                self.attach_media(self.media_file_path)
                sleep(3)
            # O bot envia a mensagem.
            self.perform_action_send()
            self.screen_texts.msg_sent_screen(contact_name)
            sleep(TIME_BTW_MSGS)

    def find_contact(self, contact_name):
        '''
        Função para o bot digitar o nome do contato na barra de pesquisa do WhatsApp Web e entrar na página do contato.
        '''
        search_field = self.driver.find_element(
            By.XPATH, SEARCH_FIELD_XPATH)
        sleep(3)
        search_field.click()
        search_field.send_keys(contact_name)
        search_field.send_keys(Keys.ENTER)

    def write_text_msg(self, msg):
        '''
        Escreve a mensagem de texto no campo de mensagem.
        '''
        msg_field = self.driver.find_elements(By.XPATH, MSG_FIELD_XPATH)
        msg_field[1].click()
        actions = ActionChains(self.driver)

        for letter in msg:
            if letter == '\n':
                # Se o usuário inseriu uma quebra de linha, o bot vai pressionar Shift + ENTER.
                actions.key_down(Keys.SHIFT).send_keys(
                    Keys.ENTER).key_up(Keys.SHIFT).perform()
            elif letter == '�':
                # input('Emoji incompatível ignorado.')
                pass
            elif letter == '`':
                actions.send_keys(letter)
            else:
                self.driver.execute_script(
                    f'''
    const text = `{letter}`;
    const dataTransfer = new DataTransfer();
    dataTransfer.setData('text', text);
    const event = new ClipboardEvent('paste', {{
    clipboardData: dataTransfer,
    bubbles: true
    }});
    arguments[0].dispatchEvent(event)
    ''',
                    msg_field[1])

    def attach_media(self, media_file_path):
        '''
        O bot aperta o botão de "anexar" e, em seuida, o botão de "mídia". Por fim, ele envia o caminho da mídia do usuário.
        '''
        attach_button = self.driver.find_element(
            By.CSS_SELECTOR, ATTACH_BUTTON_SELECTOR)
        attach_button.click()
        sleep(1)

        img_input = self.driver.find_element(
            By.CSS_SELECTOR, IMG_INPUT_SELECTOR)
        img_input.send_keys(media_file_path)
        sleep(2)

    def perform_action_send(self):
        '''
        Aperta o ENTER para enviar a mensagem.
        '''
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER).perform()
        except:
            send_button = self.driver.find_element(
                By.XPATH, SEND_BUTTON_XPATH)
            send_button.click()

        sleep(5)
