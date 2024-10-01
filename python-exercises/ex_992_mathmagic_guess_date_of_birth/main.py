'''
no calendário mágico (1), os números em azul seriam os ímpares. O restante (os pares) em branco.

no calendário mágico (2), os números em azul seriam: 2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 e 31. O restante em branco.

no calendário mágico (3), os números em azul seriam 4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 e 31. O restante em branco.

no calendário mágico (4), os números em azul seriam 8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 e 31. O restante em branco.

no calendário mágico (5), os números em azul seriam todos do 16 ao 31. O restante em branco.


por último, gostaria de imprimir a seguinte lista:

"Signos do zodíaco (na cor verde)

Áries                                21/03 a 20/04 (em branco)
Touro                               21/04 a 20/05 (em azul)
(...) prossegue com o resto dos signos e datas (...)
Peixes                              20/02 a 20/03 (em azul)"

com as datas alinhadas, seguindo esse padrão branco-azul-branco-azul até o último signo, em ordem.
'''

import calendar
from colorama import Fore, Style, init

# Inicializa o Colorama
init()


def print_magic_calendar(calendar_number):
    # Cria um objeto Calendar
    cal = calendar.Calendar(firstweekday=6)  # Começa no domingo
    current_year = 2024  # Altere conforme necessário
    current_month = 9    # Altere conforme necessário

    # Imprime o cabeçalho do calendário
    print(Fore.GREEN +
          f"Calendário mágico ({calendar_number})" + Style.RESET_ALL)
    print(Fore.YELLOW + "DOM  SEG  TER  QUA  QUI  SEX  SÁB" + Style.RESET_ALL)

    # Define os dias a serem coloridos em azul para cada calendário
    blue_days = {
        1: [i for i in range(1, 32) if i % 2 != 0],  # Mágico (1): ímpares
        # Mágico (2)
        2: [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31],
        # Mágico (3)
        3: [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31],
        # Mágico (4)
        4: [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31],
        5: [i for i in range(16, 32)],  # Mágico (5): 16 a 31
    }

    # Cria uma lista para armazenar os dias formatados
    days_grid = [["   " for _ in range(7)] for _ in range(5)]

    # Preenche a matriz de dias
    month_days = cal.monthdayscalendar(current_year, current_month)

    for week in month_days:
        for i, day in enumerate(week):
            if day != 0:  # Verifica se o dia é válido
                # Aplica a cor azul se o dia estiver na lista azul
                if day in blue_days[calendar_number]:
                    days_grid[month_days.index(week)][i] = f"{Fore.BLUE}{
                        day:>2} "  # Alinhado à direita
                else:
                    days_grid[month_days.index(week)][i] = f"{Fore.WHITE}{
                        day:>2} "  # Alinhado à direita

    # Imprime a matriz de dias
    for row in days_grid:
        # Concatena a linha e reseta a cor
        print(''.join(row) + Style.RESET_ALL)


def print_zodiac_signs():
    # Lista de signos do zodíaco e suas datas
    signs = [
        ("Áries", "21/03 a 20/04"),
        ("Touro", "21/04 a 20/05"),
        ("Gêmeos", "21/05 a 20/06"),
        ("Câncer", "21/06 a 22/07"),
        ("Leão", "23/07 a 22/08"),
        ("Virgem", "23/08 a 22/09"),
        ("Libra", "23/09 a 22/10"),
        ("Escorpião", "23/10 a 21/11"),
        ("Sagitário", "22/11 a 21/12"),
        ("Capricórnio", "22/12 a 20/01"),
        ("Aquário", "21/01 a 19/02"),
        ("Peixes", "20/02 a 20/03"),
    ]

    print(Fore.GREEN + "Signos do zodíaco:" + Style.RESET_ALL)
    for i, (sign, date_range) in enumerate(signs):
        # Aplica a cor azul nos signos com base na ordem
        if i % 2 == 0:
            print(f"{Fore.WHITE}{sign:<30} {date_range}")
        else:
            print(f"{Fore.BLUE}{sign:<30} {date_range}")


# Chama as funções para imprimir os calendários e a lista de signos
for i in range(1, 6):
    print_magic_calendar(i)
    print("\n")  # Espaço entre os calendários

print_zodiac_signs()


'''
Explicação do Código:
Função print_magic_calendar:

Cria cinco calendários mágicos com a coloração específica para os dias.
Os dias a serem coloridos em azul são definidos em um dicionário blue_days com base no número do calendário.
A formatação garante que os dias estejam alinhados corretamente.
Função print_zodiac_signs:

Imprime a lista dos signos do zodíaco.
Os signos e suas datas são armazenados em uma lista de tuplas.
A coloração alterna entre branco e azul com base na posição do signo.
Chamada das Funções:

A função de calendário é chamada cinco vezes para os calendários mágicos, seguidas pela impressão da lista de signos.
Considerações:
O uso do Fore.WHITE e Fore.BLUE garante que as cores sejam aplicadas conforme desejado.
O :<30 no formato de impressão dos signos garante que eles fiquem alinhados à esquerda com um espaço adequado para as datas.
Sim, criar todos esses prints pode ser cansativo, mas com esse código você pode facilmente gerar o que precisa sem se preocupar com a formatação manual! Se precisar de mais ajustes ou tiver outras ideias, é só avisar!
'''


'''
ESPAÇAMENTO:
O espaçamento entre os números dos dias no calendário é controlado na linha onde os dias são formatados para impressão. Aqui está a parte relevante do código, destacando onde você pode ajustar o espaçamento:

Parte Relevante do Código:
python
Copiar código
# Aplica a cor azul se o dia estiver na lista azul
if day in blue_days[calendar_number]:
    days_grid[month_days.index(week)][i] = f"{Fore.BLUE}{day:>2} "  # Alinhado à direita
else:
    days_grid[month_days.index(week)][i] = f"{Fore.WHITE}{day:>2} "  # Alinhado à direita
Como Ajustar o Espaçamento:
O :>2 indica que o número será alinhado à direita e ocupará pelo menos 2 espaços. Para adicionar mais espaço entre os números dos dias, você pode aumentar esse número. Por exemplo, para adicionar um espaço extra, você poderia mudar para :>3 ou :>4.

Além disso, você pode adicionar espaços adicionais após o número (os espaços após as aspas) para aumentar a distância entre os números.

Exemplo de Ajuste:
Para adicionar mais espaço entre os dias, você poderia modificar a linha assim:

python
Copiar código
# Alinhado à direita e adicionando 1 espaço extra
if day in blue_days[calendar_number]:
    days_grid[month_days.index(week)][i] = f"{Fore.BLUE}{day:>3}  "  # 2 espaços após
else:
    days_grid[month_days.index(week)][i] = f"{Fore.WHITE}{day:>3}  "  # 2 espaços após
Resultados Esperados:
Maior Alinhamento: O uso de :>3 fará com que os números dos dias ocupem 3 espaços, melhorando o alinhamento.
Espaçamento Visual: A adição de espaços após os números criará uma aparência mais espaçada entre os dias, tornando o calendário mais legível.
Sinta-se à vontade para ajustar esses valores conforme necessário até obter o alinhamento e o espaçamento desejados! Se precisar de mais ajuda, é só avisar.


Sim, o alinhamento deve funcionar no terminal do VSCode, desde que as configurações de fonte estejam corretas. Aqui estão algumas dicas para garantir que o alinhamento funcione bem no terminal do VSCode:

Fonte Monoespaçada: Certifique-se de que o terminal do VSCode está usando uma fonte monoespaçada (como Consolas, Courier New, ou Fira Code). Fontes monoespaçadas garantem que todos os caracteres ocupem o mesmo espaço, o que é essencial para um bom alinhamento.

Espaçamento: Quando você ajusta o número de espaços, lembre-se de que cada espaço ocupa o mesmo espaço horizontal. Por exemplo, se você usar :>3 e adicionar um ou dois espaços depois, o espaçamento deve ser consistente.

Ajuste o Código: Como mencionado anteriormente, você pode usar :>3 ou mais para o alinhamento e adicionar mais espaços após os números dos dias. Aqui está um exemplo de como poderia ficar:




Não é possível definir a fonte do terminal diretamente pelo código Python. As configurações de fonte do terminal são controladas pelas configurações do próprio terminal ou do editor (como o VSCode), e não por scripts ou programas em execução.

Como Definir a Fonte Monoespaçada no VSCode:
Abrir Configurações:

Vá para o menu superior e clique em File (Arquivo) > Preferences (Preferências) > Settings (Configurações).
Ou, você pode usar o atalho Ctrl + , (Windows/Linux) ou Cmd + , (macOS).
Pesquisar Fonte do Terminal:

Na barra de pesquisa das configurações, digite terminal font ou Font Family.
Configurar a Fonte:

Você deve encontrar uma opção chamada "Terminal > Integrated: Font Family". Aqui, você pode definir uma fonte monoespaçada, como:
arduino
Copiar código
'Courier New', 'Consolas', 'Monaco', 'Fira Code', monospace
Salvar e Fechar:

Após fazer a alteração, feche as configurações. A nova fonte deve ser aplicada imediatamente no terminal integrado.
Dica Extra:
Após mudar a fonte, você pode querer reiniciar o terminal (clique no botão de trash para fechar e depois em + para abrir um novo) para garantir que as novas configurações sejam aplicadas corretamente.
Teste de Alinhamento:
Depois de configurar a fonte, execute novamente seu código Python no terminal do VSCode para verificar se o alinhamento dos números está correto. Se houver mais alguma dúvida ou se precisar de ajuda com outra parte do seu projeto, estou à disposição!
'''

'''
Os números dos calendários são organizados a partir de somas de potências de 2.

--- Calendário 1:
2^0 = 1

Então os ímpares são azuis e os pares, brancos.

Azul: ímpares
Branco: pares

--- Calendário 2:
2^1 = 2

A partir do 2, ou seja, o 1 é branco, se pinta 2 de azul (2 e 3), 2 de branco (4 e 5) etc.

Branco: 1
loop:
    Azul: os próximos 2 números (por exemplo, na 1ª interação: 2 e 3);
    Branco: os próximos 2 números (por exemplo, na 1ª iteração: 4 e 5);
    fim do loop

--- Calendário 3:
2^2 = 4

A partir do 4 - ou seja, 1, 2 e 3 são brancos -, se pinta 4 de azul (4, 5, 6 e 7) e 4 de branco (8, 9, 10 e 11) etc.

Branco: 1, 2 e 3
loop:
    Azul: os próximos 4 números (por exemplo, na 1ª interação: 4, 5, 6 e 7);
    Branco: os próximos 4 números (por exemplo, na 1ª iteração: 8, 9, 10 e 11);
    fim do loop

--- Calendário 4:
2^3 = 8

A partir do 8 - ou seja, de 1 a 7 são brancos -, se pinta 8 de azul (de 8 a 15) e 8 de branco (16 a 23) etc.

Branco: 1 a 7
loop:
    Azul: os próximos 8 números (por exemplo, na 1ª interação: 8 a 15);
    Branco: os próximos 8 números (por exemplo, na 1ª iteração: 16 a 23);
    Aqui, o loop termina no meio da 2ª iteração, antes de chegar na cor branca novamente, sendo:
    Azul: os próximos 8 números (24 a 31);
    fim do loop

--- Calendário 5:
2^4 = 16

A partir do 16 - ou seja, a primeira metade de números é branca e a segunda metade (+ 1 número) é azul.

Branco: 1 a 15
Azul: 16 a 31
'''


def print_magic_calendar(calendar_number):
    cal = calendar.Calendar(firstweekday=6)  # Começa no domingo
    current_year = 2024  # Altere conforme necessário
    current_month = 9    # Altere conforme necessário

    # Imprime o cabeçalho do calendário
    print(Fore.GREEN +
          f"Calendário mágico ({calendar_number})" + Style.RESET_ALL)
    print(Fore.YELLOW + "DOM  SEG  TER  QUA  QUI  SEX  SÁB" + Style.RESET_ALL)

    # Define os dias a serem coloridos em azul para cada calendário
    blue_days = {
        1: [i for i in range(1, 32) if i % 2 != 0],  # Mágico (1): ímpares
        # Mágico (2)
        2: [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31],
        # Mágico (3)
        3: [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31],
        # Mágico (4)
        4: [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31],
        5: [i for i in range(16, 32)],  # Mágico (5): 16 a 31
    }

    # Cria uma lista para armazenar os dias formatados
    days_grid = [["    " for _ in range(7)] for _ in range(5)]

    # Preenche a matriz de dias
    month_days = cal.monthdayscalendar(current_year, current_month)

    for week in month_days:
        for i, day in enumerate(week):
            if day != 0:  # Verifica se o dia é válido
                # Aplica a cor azul se o dia estiver na lista azul
                if day in blue_days[calendar_number]:
                    days_grid[month_days.index(week)][i] = f"{Fore.BLUE}{
                        day:>2} "  # Alinhado à direita
                else:
                    days_grid[month_days.index(week)][i] = f"{Fore.WHITE}{
                        day:>2} "  # Alinhado à direita

    # Imprime a matriz de dias
    for row in days_grid:
        # Concatena a linha e reseta a cor
        print(''.join(row) + Style.RESET_ALL)
