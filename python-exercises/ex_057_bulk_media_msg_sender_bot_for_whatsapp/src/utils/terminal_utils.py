from src.utils.terminal_fx import TerminalFX
from src.utils.constants import *

import os
import textwrap
from time import sleep

import pygame
# Esconde a mensagem de suporte do Pygame.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


class TerminalUtils:
    '''
    Contém funções para tocar sons, limpar o terminal, corrigir a largura da linha do texto, imprimir o título do app e imprimir o "Pressione ENTER para continuar/sair...".
    '''

    def __init__(self):
        self.terminal_fx = TerminalFX()
        pygame.init()

    def play_sound(self, file):
        sound = pygame.mixer.Sound(file)
        sound.play()
        sleep(0.1)

    def clear_terminal(self):
        '''
        Limpa o terminal usando "cls", se OS for Windows ou "clear", se o OS for Unix (Linux ou MacOS).
        '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def fix_text_width(self, text, text_type, max_width):
        '''
        Conserta a largura do texto, de acordo com o tipo.
        '''
        if text_type == 'normal_text' or text_type == 'msg':
            # Divide o texto em uma lista de substrings, separando-as de acordo com a largura máxima, sem dividir palavras ao meio.
            text = textwrap.wrap(text, width=max_width)
        elif text_type == 'name':
            if len(text) > max_width:
                # Se o nome for maior que o tamanho máximo da célula, retorna somente o primeiro nome, até o caractere número "max_width".
                text = text.split()[0][:max_width]
        elif text_type == 'path':
            path = text.replace('/', '\\')
            text = textwrap.wrap(path, width=max_width)
            text = [line.replace('\\', '/') for line in text]
        return text
