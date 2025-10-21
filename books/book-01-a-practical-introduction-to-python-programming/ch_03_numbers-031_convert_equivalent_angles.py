'''
Write a program that asks the user to enter an angle between −180◦ and 180◦. Using an expression with the modulo operator, convert the angle to its equivalent between 0◦ and 360◦.
'''


def main() -> None:
    user_angle = float(input('Enter an angle between -180° and 180°: '))
    converted_angle = convert_angle(user_angle)
    
    print(f'Equivalent angle between 0° and 360°: {converted_angle:.2f}°.')


def convert_angle(user_angle: float) -> float:
    return user_angle % 360


if __name__ == '__main__':
    main()