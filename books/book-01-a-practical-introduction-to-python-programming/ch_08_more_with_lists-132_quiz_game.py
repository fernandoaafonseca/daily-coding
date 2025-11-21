'''
Write a simple quiz game that has a list of ten questions and a list of answers to those questions. The game should give the player four randomly selected questions to answer. It should ask the questions one-by-one, and tell the player whether they got the question right or wrong. At the end it should print out how many out of four they got right.
'''


import os, random


QUESTIONS = [
    'What is the capital of France?',
    'What is the largest planet in our solar system?',
    'How many continents are there on Earth?',
    'What gas do plants absorb from the air during photosynthesis?',
    'What is the fastest land animal?',
    'Who wrote the play "Romeo and Juliet"?',
    'How many degrees are in a right angle?',
    'What is the process of water turning into vapor called?',
    'What do bees collect from flowers to make honey?',
    'What is the square root of 81?'
    ]
ANSWERS = [
    'Paris',
    'Jupiter',
    'Seven',
    'Carbon dioxide',
    'Cheetah',
    'William Shakespeare',
    '90',
    'Evaporation',
    'Nectar',
    '9'
    ]


def main():
    selected_questions_indices = get_questions()
    score = run_quiz(selected_questions_indices)
    display_result(score)


def press_any_key_to_continue() -> None:
    input('\nPRESS ANY KEY TO CONTINUE...')


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def run_quiz(selected_questions_indices) -> int:
    score = 0

    while True:
        for i in range(len(selected_questions_indices)):
            press_any_key_to_continue()
            clear_terminal()
            print('QUIZ GAME')
            print('=' * 30)

            new_index = selected_questions_indices[i]
            new_question = QUESTIONS[new_index]
            new_correct_answer = ANSWERS[new_index]

            print(f'Question #{i + 1}:')
            print(new_question)
            answer = get_answer()

            if answer.lower() == new_correct_answer.lower():
                score += 1
                print('RIGHT ANSWER!')
            else:
                print('WRONG ANSWER')

            if i == len(selected_questions_indices) - 1:
                return score


def get_questions() -> list[int]:
    '''
    Return a list with the indices for the quiz questions.
    '''
    selected_questions_indices = []

    for _ in range(4):
        new_index = ''
        while new_index not in selected_questions_indices:
            new_index = random.randint(0, 9)
            if new_index not in selected_questions_indices:
                selected_questions_indices.append(new_index)

    return selected_questions_indices


def get_answer() -> str:
    while True:
        try:
            answer = str(input('Enter your answer: '))

            if len(answer.replace(' ', '')) > 0:
                return answer
            else:
                raise ValueError

        except ValueError:
            print('\nPlease enter your answer.')


def display_result(score: int) -> None:
    press_any_key_to_continue()
    clear_terminal()

    print('GAME OVER')
    print(f'Your final score: {score}')


if __name__ == '__main__':
    main()