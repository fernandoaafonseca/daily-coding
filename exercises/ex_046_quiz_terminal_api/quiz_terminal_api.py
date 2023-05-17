import html
import requests


parameters = {
    'amount': 10,
    'category': 15,
    'type': 'boolean'
}
# Category 15: videogames 

response = requests.get('https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
data = response.json()

question_data = data['results']


class Question():
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer


question_bank = []
for question in question_data:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)
    print(new_question)
print(type(question_bank))


class QuizBrain():

    def __init__(self):
        self.question_number = 1
        self.question_list = question_bank
        self.correct_score = 0
        self.incorrect_score = 0


    def game_over(self):
        if self.question_number < len(self.question_list) + 1:
            return False
        else:
            return True
        
 
    def next_question(self):
        valid_answers = ['t', 'f']
        user_answer = ''

        self.current_question = self.question_list[self.question_number - 1]
        question_text = html.unescape(self.current_question.text)
        print(f'\nQuestion {self.question_number}:\n\
{question_text}\n\
True or False?')

        while user_answer not in valid_answers:
            user_answer = input().lower()[0]
        self.check_answer(user_answer, self.current_question.correct_answer.lower()[0])
        self.question_number += 1


    def check_answer(self, user_answer, correct_answer):

        if user_answer == correct_answer:
            self.correct_score += 1
            print('\nRight answer!')
        else:
            print('\nWrong answer!')
            self.incorrect_score += 1
        print(f'\nSCORE:\n{self.correct_score} correct answers.\n{self.incorrect_score} incorrect answers.')


quiz = QuizBrain()

while not quiz.game_over():
    quiz.next_question()

print('No more questions!')
print('Game over!')