def calc(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

first_num = ''

while type(first_num) != 'float':
    try:
        first_num = float(first_num)
        break
    except:
        first_num = input('What\'s the first number?\n')

operation = ''
valid_operations = ['+', '-', '*', '/']

while operation not in valid_operations:
    print('\n')
    for op in valid_operations:
        print(op)
    operation = input('\nPick an operation:\n')

second_num = ''

while type(second_num) != 'float':
    try:
        second_num = float(second_num)
        break
    except:
        second_num = input('\nWhat\'s the second number?\n')

print(calc(first_num, second_num, operation))