question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class Question():
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_bank = []
for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)


class QuizBrain():

    def __init__(self):
        self.question_number = 0
        self.question_list = question_bank
        self.correct_score = 0
        self.incorrect_score = 0


    def game_over(self):
        if self.question_number < len(self.question_list):
            return False
        else:
            return True
        
 
    def next_question(self):
        current_question = self.question_list[self.question_number]       
        print(f'\nQuestion {self.question_number + 1}:\n\
{current_question.text}\n\
True or False?')
        valid_answers = ['true', 'false']
        user_answer = []
        while user_answer not in valid_answers:
            user_answer = input().lower()
        self.check_answer(user_answer, current_question.answer.lower())
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