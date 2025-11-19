'''
Write a simple lottery drawing program. The lottery drawing should consist of six different numbers between 1 and 48.
'''


import random


def main():
    lottery_drawing = get_lottery_drawing()
    display_result(lottery_drawing)


def get_lottery_drawing() -> list[int]:
    lottery_drawing = []

    for _ in range(6):
        new_num = draw_a_random_number()
        lottery_drawing.append(new_num)

    return lottery_drawing


def draw_a_random_number() -> int:
    return random.randint(1, 48)


def display_result(lottery_drawing: list[int]) -> None:
    print('LOTTERY DRAWING:')
    print(lottery_drawing)


if __name__ == '__main__':
    main()