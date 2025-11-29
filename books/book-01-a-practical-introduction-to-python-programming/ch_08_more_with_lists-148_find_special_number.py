'''
Here is an old puzzle question you can solve with a computer program. There is only one five-digit number n that is such that every one of the following ten numbers shares exactly one digit in common in the same position as n. Find n.

    01265, 12171, 23257, 34548, 45970, 56236, 67324, 78084, 89872, 99414
'''


REFERENCE_NUMBERS = [
    '01265', '12171', '23257', '34548', '45970',
    '56236', '67324', '78084', '89872', '99414'
]


def main() -> None:
    unique_number = find_unique_number()
    display_result(unique_number)


def find_unique_number() -> int:
    '''
    Searches the entire five-digit range (10000–99999) and returns the unique number that satisfies the puzzle condition.
    '''
    for number in range(10000, 100000):
        candidate = str(number)
        if satisfies_constraints(candidate):
            return number

    raise ValueError('No number satisfies the constraints.')


def count_matching_positions(a: str, b: str) -> int:
    '''
    Returns the number of positions (0–4) in which the characters of two 5-character strings match exactly.

    Example:
    a = "45839"
    b = "45972"
    => returns 2
    '''
    return sum(1 for i in range(5) if a[i] == b[i])


def satisfies_constraints(candidate: str) -> bool:
    '''
    Determines whether a candidate five-digit string satisfies the rule:
    It must share "exactly one" matching digit in the same position with "each" of the 10 reference numbers.
    '''
    for ref in REFERENCE_NUMBERS:
        if count_matching_positions(candidate, ref) != 1:
            return False
    return True


def display_result(unique_number: int) -> None:
    print('There is only one five-digit number "n" that is such that every one of the following ten numbers shares exactly one digit in common in the same position as "n".')
    print(REFERENCE_NUMBERS)
    print()
    print('The unique number "n" is:')
    print(unique_number)


if __name__ == '__main__':
    main()