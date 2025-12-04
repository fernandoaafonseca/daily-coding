import os


def main() -> None:
    x, y = get_numbers()
    operation: int = get_operation()
    perform_operation(operation, x, y)


def press_any_key_to_continue() -> None:
    input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def get_number(prompt: str) -> float:
    while True:
        try:
            clear_terminal()
            return float(input(prompt))
        except ValueError:
            print('\nPlease enter a valid number.')
            press_any_key_to_continue()


def get_numbers() -> tuple[float, float]:
    x = get_number('Enter the value of x: ')
    y = get_number('Enter the value of y: ')
    return x, y


def get_operation() -> int:
    while True:
        clear_terminal()
        print('Choose an operation:')
        print('1 - Addition')
        print('2 - Subtraction')
        print('3 - Multiplication')
        print('4 - Division')
        print('5 - Square of x')
        print('6 - Square of y')

        try:
            op = int(input('\nEnter your choice: '))
            if 1 <= op <= 6:
                return op
        except ValueError:
            print('\nInvalid option.')
            press_any_key_to_continue()


def perform_operation(operation: int, x: float, y: float) -> None:
    if operation == 1:
        print(f'Result: {add(x, y)}')
    elif operation == 2:
        print(f'Result: {subtract(x, y)}')
    elif operation == 3:
        print(f'Result: {multiply(x, y)}')
    elif operation == 4:
        print(f'Result: {divide(x, y)}')
    elif operation == 5:
        print(f'Result: {square(x)}')
    elif operation == 6:
        print(f'Result: {square(y)}')


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    return x / y


def square(n: float) -> float:
    return n * n


if __name__ == '__main__':
    main()