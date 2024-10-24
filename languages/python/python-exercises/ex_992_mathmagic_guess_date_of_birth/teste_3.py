import calendar
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

class CalendarPrinter:
    def __init__(self, fmt, sep=' '):
        """
        @param fmt: list of tuple(heading, width)
                    heading: str, column label
                    width: int, column width in chars
        @param sep: string, separation between columns
        """
        self.fmt = str(sep).join(f'{{:{width}}}' for heading, width in fmt)
        self.head = [heading for heading, width in fmt]

    def row(self, data):
        # Garante que sempre temos 7 colunas preenchidas (transformando valores em string)
        data = [str(d) for d in data]  # Certifica-se de que todos os itens são strings
        data = (data + [''] * 7)[:7]  # Completa com strings vazias se faltar valores
        return self.fmt.format(*data)

    def __call__(self, dataList):
        _r = self.row
        res = []  # Remove a duplicação do cabeçalho aqui
        res.extend(_r(data) for data in dataList)  # Adiciona os dias do calendário
        return '\n'.join(res)

def print_magic_calendar(calendar_number):
    cal = calendar.Calendar(firstweekday=6)  # Começa no domingo
    current_year = 2024
    current_month = 9

    # Formato para os dias da semana e largura das colunas
    fmt = [
        ('DOM', 5),
        ('SEG', 5),
        ('TER', 5),
        ('QUA', 5),
        ('QUI', 5),
        ('SEX', 5),
        ('SÁB', 5)
    ]

    # Instância de CalendarPrinter
    table_printer = CalendarPrinter(fmt)

    # Imprime o cabeçalho correto uma única vez
    print(Fore.GREEN + f"Calendário mágico ({calendar_number})" + Style.RESET_ALL)
    print(Fore.YELLOW + table_printer.row([heading for heading, _ in fmt]) + Style.RESET_ALL)

    # Define os dias a serem coloridos em azul
    blue_days = {
        1: [i for i in range(1, 32) if i % 2 != 0],  # Mágico (1): ímpares
        2: [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31],
        3: [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31],
        4: [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31],
        5: [i for i in range(16, 32)]  # Mágico (5): 16 a 31
    }

    # Preenche o calendário
    month_days = cal.monthdayscalendar(current_year, current_month)

    # Se não houver um dia 31, adiciona manualmente à última semana
    if 31 not in [day for week in month_days for day in week]:
        if len(month_days[-1]) < 7:  # Se a última semana tiver espaço
            month_days[-1].append(31)
        else:  # Se não houver espaço, cria uma nova semana
            month_days.append([31] + [0] * 6)

    days_grid = []
    for week in month_days:
        formatted_week = []
        for day in week:
            if day == 0:
                formatted_week.append("     ")  # Dia vazio com 5 espaços para alinhar
            else:
                color = Fore.BLUE if day in blue_days[calendar_number] else Fore.WHITE
                formatted_week.append(f"{color}{day:>2}{Style.RESET_ALL}   ")  # 3 espaços após o número
        
        # Remove o último espaço extra do último dia da semana
        if formatted_week and formatted_week[-1].strip():
            formatted_week[-1] = formatted_week[-1].rstrip()  # Remove espaço extra do último dia

        days_grid.append(formatted_week)

    # Imprime os dias formatados (sem duplicar o cabeçalho)
    print(table_printer(days_grid))

# Exemplo de uso
for i in range(1, 6):
    print_magic_calendar(i)
