'''
I was watching a short YouTube video about Python's native "random" function from "Week 5: Libraries" of the CS50P course ("CS50's Introduction to Programming with Python") and wondering how "random" the function really is for common use cases.

This is a simple program that takes user input on how many tests to run and compares the results of these tests using the "random" module with the statistically expected values.

Source:
https://www.youtube.com/watch?v=yec-UUauUV8
'''

import random


# List of card faces and their respective weights
cards_faces = ['Jack', 'Queen', 'King']
cards_weights = [60, 30, 10]


def main():
    '''
    Main function that coordinates the execution of the program:
        1. Retrieves the number of tests from the user.
        2. Calculates expected results based on weights.
        3. Simulates card draws.
        4. Counts actual occurrences of each card.
        5. Displays all results.
    '''
    # Step 1: Get the number of tests
    num_of_tests = get_num_of_tests()

    # Step 2: Compute expected results
    expected_results = calculate_expected_results(cards_weights, num_of_tests)

    # Step 3: Simulate draws
    cards_chosen = choose_cards(cards_faces, cards_weights, num_of_tests)

    # Step 4: Count occurrences
    repetitions = count_repetitions(cards_faces, cards_chosen)

    # Step 5: Show results
    display_results(cards_faces, cards_weights, num_of_tests,
                    expected_results, repetitions)


def get_num_of_tests() -> int:
    '''
    Prompt the user to input the number of tests.
    Ensures the input is a positive integer.
    '''
    while True:
        try:
            # Prompt user
            num_of_tests = int(input('Enter the number of tests: '))

            # Return valid input
            if num_of_tests >= 1:
                return num_of_tests
            else:
                continue
        except:
            continue


def calculate_expected_results(cards_weights: list[int], num_of_tests: int) -> list[int]:
    '''
    Calculate the expected number of times each card is drawn,
    based on the weights and the total number of tests.

    Args:
    - cards_weights (list[int]): The weights assigned to each card.
    - num_of_tests (int): The total number of tests.

    Returns:
    - list[int]: Expected occurrences of each card.
    '''
    # Sum of all weights
    total_weight = sum(cards_weights)

    # Calculate expected results
    expected_results = [int((weight / total_weight) * num_of_tests)
                        for weight in cards_weights]

    return expected_results


def choose_cards(cards_faces: list[str], cards_weights: list[int], num_of_tests: int) -> list[str]:
    '''
    Randomly choose cards based on their weights.

    Args:
    - cards_faces (list[str]): The faces of the cards (e.g., 'Jack', 'Queen', 'King').
    - cards_weights (list[int]): The weights assigned to each card.
    - num_of_tests (int): The total number of draws.

    Returns:
    - list[str]: List of drawn cards.
    '''
    # Perform random choices based on weights
    return random.choices(cards_faces, weights=cards_weights, k=num_of_tests)


def count_repetitions(cards_faces: list[str], cards_chosen: list[str]) -> list[int]:
    '''
    Count the number of times each card face appears in the chosen cards.

    Args:
    - cards_faces (list[str]): The faces of the cards.
    - cards_chosen (list[str]): The list of randomly chosen cards.

    Returns:
    - list[int]: Number of occurrences for each card face.
    '''
    # Count occurrences of each face
    return [cards_chosen.count(face) for face in cards_faces]


def display_results(cards_faces: list[str], cards_weights: list[int], num_of_tests: int, expected_results: list[int], repetitions: list[int]) -> None:
    '''
    Display the results of the simulation, including:
    - The card faces and weights.
    - The number of tests.
    - The statistically expected results.
    - The actual results.
    '''
    # Display card faces and weights
    print('=' * 20)
    print('Card faces and their weights:')
    print()
    for face, weight in zip(cards_faces, cards_weights):
        print(f"Face: {face} - Weight: {weight}")

    # Display number of tests
    print('=' * 20)
    print(f'Number of tests: {num_of_tests}')

    # Display actual results
    print('=' * 20)
    print("Results:")
    print()
    for face, count in zip(cards_faces, repetitions):
        print(f"{face}: {count}")

    # Display comparison of actual vs expected results
    print('=' * 20)
    print('Comparison (Actual vs Expected):')
    print()
    for i, (face, expected, actual) in enumerate(zip(cards_faces, expected_results, repetitions)):
        abs_error = abs(actual - expected)
        rel_error = (abs_error / expected * 100) if expected > 0 else "N/A"

        print(f'{face}:')
        print(f'Expected {expected}, Got {actual} | AE: {
              abs_error} | RE: {rel_error:.2f}%')

        # Only print dashed line if it's not the last iteration
        if i < len(cards_faces) - 1:
            print('-' * 20)

    print('=' * 20)


if __name__ == '__main__':
    main()
