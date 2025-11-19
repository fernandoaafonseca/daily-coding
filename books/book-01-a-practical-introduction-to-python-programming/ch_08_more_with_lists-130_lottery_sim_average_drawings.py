'''
Write a program that estimates the average number of drawings it takes before the user’s numbers are picked in a lottery that consists of correctly picking six different numbers that are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of user numbers and simulates drawings until the user’s numbers are drawn. Find the average number of drawings needed over the 1000 times the loop runs.
'''


import random


SIM_LENGTH = 1000


def main():
    attempts_list = run_simulation()
    average_attempts = get_average_attempts(attempts_list)
    display_result(average_attempts)


def run_simulation() -> list[int]:
    '''
    Run the simulation SIM_LENGTH times.
    Each time: generate a user ticket, simulate draws until it matches.
    Return a list containing the attempts needed for each run.
    '''
    attempts_list = []

    for _ in range(SIM_LENGTH):
        user_ticket = generate_lottery_ticket()
        attempts_needed = simulate_until_match(user_ticket)
        attempts_list.append(attempts_needed)

    return attempts_list


def simulate_until_match(user_ticket: list[int]) -> int:
    '''
    Repeatedly generate lottery drawings until one matches user_ticket.
    Return the number of attempts needed.
    '''
    attempts = 0
    lottery_draw = []

    while lottery_draw != user_ticket:
        lottery_draw = generate_lottery_ticket()
        attempts += 1

    return attempts


def generate_lottery_ticket() -> list[int]:
    '''
    Generate a list of six different numbers between 1 and 10.
    Return the sorted ticket.
    '''
    ticket = []

    while len(ticket) < 6:
        new_num = draw_a_random_number()
        if new_num not in ticket:
            ticket.append(new_num)

    ticket.sort()
    return ticket


def draw_a_random_number() -> int:
    return random.randint(1, 10)


def get_average_attempts(attempts_list: list[int]) -> float:
    '''
    Return the average value from the attempts_list.
    '''
    total = 0

    for attempts in attempts_list:
        total += attempts

    return total / SIM_LENGTH


def display_result(average_attempts: float) -> None:
    print('LOTTERY SIMULATION RESULT')
    print(f'Average number of drawings: {average_attempts:.2f}')


if __name__ == '__main__':
    main()