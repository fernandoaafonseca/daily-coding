# Mega Sena constants
MIN_NUMBER = 1
MAX_NUMBER = 60
NUMBERS_PER_TICKET = 6

# Prices (official values)
TICKET_PRICE_SIX_NUMBERS = 5.00


import random


def generate_official_draw() -> set[int]:
    """Generates the official Mega Sena draw (6 unique numbers from 1–60)."""
    return set(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_TICKET))


def generate_random_ticket() -> set[int]:
    """Generates a cheap (6-number) random ticket."""
    return set(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_TICKET))


def check_win(ticket: set[int], draw: set[int]) -> bool:
    """Returns True if the ticket matches all official drawn numbers."""
    return ticket == draw


def count_matches(ticket: set[int], draw: set[int]) -> int:
    """Returns the amount of matching numbers between ticket and draw."""
    return len(ticket.intersection(draw))
