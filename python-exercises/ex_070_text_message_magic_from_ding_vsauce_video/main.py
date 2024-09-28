'''
Text message magic (by Michael Stevens (from "Vsauce", taken from a video from his second channel "D!NG")


Site que puxa uma carta aleatória de um baralho:
https://www.calculatorsoup.com/calculators/statistics/random-card-generator.php
                    
                    
Se começar sem uma saudação, a carta é um A. Se o nome do participante (ou do computador) que vai adivinhar estiver logo após a saudação, é a primeira das 3 cartas. Se o nome estiver no final da mensagem, é a terceira das 3 cartas. Se estiver em qualquer outro lugar no meio da pergunta, é a carta do meio das 3 cartas.

Hey, PC, what's the card I'm holding?
6 of Spades


Suits:
- If the question ends with no punctuation:
Hearts (Copas)

- If the question ends with ".":
Diamonds (Ouros)

- If the question ends with "?":
Clubs (Paus)

- If the question ends with "!":
Spades (Espadas)


Ranks:
Números: de 2 a 10.
Figuras: J (Jack), Q (Queen), K (King).
O Ás (Ace) também faz parte dos "ranks".
'''

import unicodedata


def remove_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


palavra = 'olá'
palavra_sem_acento = remove_acentos(palavra)

"""unicodedata.normalize('NFD', texto) separa os caracteres acentuados em caracteres de base e seus diacríticos.
O código 'Mn' refere-se à categoria de diacríticos (marcas não espaciadas), que são removidos no processo."""

# greetings with 2 letters
greetings_1 = ['Hi', 'Yo', 'Ah', 'Oi', 'Ei']

# greetings with 3 letters
greetings_2 = ['Hey', 'Olá', 'Oiê']

# greetings with more letters:
greetings_3 = ['Hello', 'Greetings', 'Saudações', 'Beleza?']

greetings = greetings_1 + greetings_2 + greetings_3

# Unifica saudações em minúsculas e remove acentos para comparação uniforme
greetings = [remove_acentos(greeting.lower()) for greeting in greetings]


'''
Evite Duplicatas:

Se você quiser garantir que não haja saudações duplicadas, pode converter a lista em um conjunto (set) após a padronização e depois voltar a convertê-la em lista, se necessário:
python

greetings = list(set(greetings))
'''

# no greeting
card_ranks_1 = ['Ace']

# greeting with 2 letters
card_ranks_2 = [1, 2, 3]

# greeting with 3 letters
card_ranks_3 = [4, 5, 6]

# greeting with 4 or more letters
card_ranks_4 = [7, 8, 9]

# no greeting, but ending with 'ready'
card_ranks_5 = ['J', 'Q', 'K']


magic_question = 'Oh, hey, what\'s the card I\'m holding?'
# The output result of this magic_question should be "6 of "

words = magic_question.split(' ')

# next, I want to take out non-letters from the words, like ",", "!", "?" or anything else
words = [word for word in words if word.isalpha()]


def check_if_contains_greeting():
    for i in range(len(words)):
        # Remove accents from the words and makes them lowercase for comparison
        word = remove_acentos(words[i]).lower()
        if word in greetings:
            if len(word) == 2:
                # card_rank is in [2, 3, 4]
                possible_card_ranks_list = card_ranks_2
                card_rank = guess_the_card_rank(possible_card_ranks_list, i)
            elif len(word) == 3:
                # card_rank is in [5, 6, 7]
                possible_card_ranks_list = card_ranks_3
                card_rank = guess_the_card_rank(possible_card_ranks_list, i)
            elif len(word) >= 4:
                # card_rank is in [8, 9, 10]
                possible_card_ranks_list = card_ranks_4
                card_rank = guess_the_card_rank(possible_card_ranks_list, i)
        elif word == 'ready':
            # card_rank is in ['J', 'Q', 'K']
            possible_card_ranks_list = card_ranks_5
            card_rank = guess_the_card_rank(possible_card_ranks_list, i)
        else:
            # card_rank is in ['Ace']
            card_rank = card_ranks_1[0]

    return card_rank


def guess_the_card_rank(possible_card_ranks_list, i):
    if i == 0:
        # card_rank is the first one on the list
        card_rank = possible_card_ranks_list[0]
    elif i == -1:
        # card_rank is the last one on the list
        card_rank = possible_card_ranks_list[-1]
    else:
        # card_rank is the middle one on the list
        card_rank = possible_card_ranks_list[1]

    return card_rank


resultado = check_if_contains_greeting()
print(resultado)  # Exibe o resultado
