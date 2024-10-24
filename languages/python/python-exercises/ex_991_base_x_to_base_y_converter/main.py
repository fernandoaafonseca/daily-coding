'''
Explanation:
base_x_to_decimal: Converts a number from base x to decimal using Python's int() function, 
which takes a string as the number and the original base as an argument.

decimal_to_base_y: Converts a decimal number to base y. It performs successive divisions and stores 
the remainders to form the number in the new base.

convert_base: This is the main function that performs the conversion in two steps: from base x to decimal, 
and then from decimal to base y.

This code accepts any base from 2 to 36 (base 36 includes the digits 0 to 9 and the letters A to Z).
'''

def base_x_to_decimal(n, x):
    """
    Converte um número 'n' da base 'x' para base decimal (10).
    """
    return int(n, x)

def decimal_to_base_y(n, y):
    """
    Converte um número decimal 'n' para a base 'y'.
    """
    if n == 0:
        return '0'
    
    digits = []
    while n:
        digits.append(int(n % y))
        n //= y
    # Inverte a lista e converte os dígitos de volta para string
    return ''.join(str(digit) for digit in digits[::-1])

def convert_base(n, x, y):
    """
    Converte um número 'n' da base 'x' para a base 'y'.
    """
    # Converter da base x para decimal
    decimal_number = base_x_to_decimal(n, x)
    
    # Converter da base decimal para a base y
    return decimal_to_base_y(decimal_number, y)

# Exemplo de uso
n = input("Digite o número: ")  # Exemplo: '1011' para um número binário
x = int(input("Digite a base atual: "))  # Exemplo: 2 para binário
y = int(input("Digite a base de destino: "))  # Exemplo: 10 para decimal

resultado = convert_base(n, x, y)
print(f"O número {n} da base {x} convertido para a base {y} é: {resultado}")
