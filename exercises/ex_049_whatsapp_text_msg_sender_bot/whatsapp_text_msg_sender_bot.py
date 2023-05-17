from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
import random
import urllib


# constante do endereço da página inicial do WhatsApp Web
URL_WHATS_APP_WEB = 'http://web.whatsapp.com/'


class Robot():
    def __init__(self):
        # método construtor do robô
        self.clear_terminal()
        self.amount = self.get_amout()
        self.nums_list = self.get_nums(self.amount)
        self.msg = self.get_msg()
        self.driver = self.browser()
        self.clear_terminal()
        self.send_msg(self.driver, self.amount, self.nums_list, self.msg)
        # aguarda 15 segundos após terminar o programa
        sleep(15)
        # finaliza o robô
        self.driver.quit()


    def clear_terminal(self):
    # limpa o terminal com "cls", se o OS for Windows
    # ou "clear", se o OS for Linux
        os.system('cls' if os.name == 'nt' else 'clear')


    def browser(self):
        # inicializa o navegador
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')

        return driver


    def get_amout(self):
        # recebe o input da quantidade de pessoas para as quais
        # o usuário quer enviar a mensagem
        print('Para quantas pessoas você deseja enviar a mensagem?')
        self.amount = None
        while type(self.amount) != int:
            # enquanto a quantidade não for um número inteiro,
            # o código vai continuar tentando obter um input
            try:
                self.amount = int(input())
            except:
                pass
        
        return self.amount


    def get_nums(self, amount):
        # recebe os inputs dos números para os quais o usuário
        # irá enviar a mensagem
        print()
        print('Digite o número do celular precedido dos 2 dígitos do DDD.')
        # cria uma lista vazia para ser preenchida no for loop
        nums_list = []

        for i in range(amount):
            # roda "amount" vezes, ou seja, a quantidade que o usuário digitou
            print()
            print(f'Digite o {i + 1}º celular: ')
            num = ''
        
            # checa se o input contém apenas números inteiros (num.isdigit())
            # e checa se o número tem 11 dígitos
            while not (num.isdigit() and len(num) == 11):
                try:
                    # recebe o input quantas vezes forem necessárias
                    num = input()
                except:
                    pass
            
            # adiciona o número da iteração atual à lista
            nums_list.append(num)

        return nums_list


    def get_msg(self):
        # recebe o input da mensagem que o usuário quer enviar
        print()
        print('Digite a mensagem a ser enviada:')
        msg_input = input()
        # converte a mensagem para o formato de URL
        msg = urllib.parse.quote(msg_input)

        return msg


    def send_msg(self, driver, amount, nums_list, msg):
        # função para enviar as mensagens
        # abre a página inicial do WhatsApp Web
        driver.get(URL_WHATS_APP_WEB)
        # aguarda a página inicial carregar por 30 segundos
        # é possível que tenha que escanear o QR code neste momento
        print()
        print('CHEQUE SEU NAVEGADOR! ESCANEIE O QR CODE, SE NECESSÁRIO!')
        sleep(30)

        for i in range(amount):
            # roda "amount" vezes, ou seja, vai enviar as mensagens uma por uma
            # o número de celular na iteração atual vai ser a lista na posição "i",
            # ou seja, o elemento número "i" da lista
            number = nums_list[i]

            # a url na iteração atual será o endereço do WhatsApp + o "number",
            # que é passado logo após "?phone="
            # + '"msg", que é passada depois de "&text=" na url
            url = 'https://web.whatsapp.com/send/?phone='  + number + '&text=' + msg

            # abre a url
            driver.get(url)
            sleep(5)

            while True:
                try:
                    # checando se a página do contato carregou
                    # se não, aguarda 15 seg e tenta novamente
                    elem = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '._1OT67')))
                except:
                    # se não carregou corretamente, o número não existe
                    # o robô aperta "TAB" e "ENTER" para fechar o popup de "número inexistente"
                    actions = ActionChains(driver)
                    actions.send_keys(Keys.TAB)
                    actions.send_keys(Keys.ENTER)
                    actions.perform()
                    break
                else:
                    # se a página do contato for carregada corretamente,
                    # o robô vai enviar a mensagem

                    actions = ActionChains(driver)
                    # o robô pressiona ENTER para enviar a mensagem
                    actions.send_keys(Keys.ENTER)
                    actions.perform()
                    sleep(3)
                    # termina a iteração do número atual
                    break
 

def main():
    # função que inicia o programa
    # inicializa o robô
    robot = Robot()


if __name__ == '__main__':
    # inicia a função principal
    main()