import calendar
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

def print_magic_calendar(calendar_number):
    cal = calendar.Calendar(firstweekday=6)  # Começa no domingo
    current_year = 2024  # Altere conforme necessário
    current_month = 9    # Altere conforme necessário

    # Imprime o cabeçalho do calendário
    print(Fore.GREEN + f"Calendário mágico ({calendar_number})" + Style.RESET_ALL)
    print(Fore.YELLOW + " DOM     SEG     TER     QUA     QUI     SEX     SÁB" + Style.RESET_ALL)

    # Define os dias a serem coloridos em azul para cada calendário
    blue_days = {
        1: [i for i in range(1, 32) if i % 2 != 0],  # Mágico (1): ímpares
        2: [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31],  # Mágico (2)
        3: [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31],  # Mágico (3)
        4: [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31],  # Mágico (4)
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
                    days_grid[month_days.index(week)][i] = f"{Fore.BLUE}{day:>2}"  # Alinhado à direita
                else:
                    days_grid[month_days.index(week)][i] = f"{Fore.WHITE}{day:>2}"  # Alinhado à direita

    # Define a largura e alinhamento das colunas
    col_widths = [9, 13, 10, 10, 10, 10, 10]  # Larguras das colunas
    alignments = ['>', '<', '<', '<', '<', '<', '<']  # Alinhamentos

    # Imprime a matriz de dias com formatos específicos
    for row in days_grid:
        formatted_row = ' '.join(f"{day:{alignments[i]}{col_widths[i]}}" for i, day in enumerate(row))
        print(formatted_row.rstrip() + Style.RESET_ALL)  # Alinhamento

# Exemplo de uso
for i in range(1, 6):  # Imprime os calendários mágicos de 1 a 5
    print_magic_calendar(i)
