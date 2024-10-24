import os
import sys
from time import sleep


APP_TITLE = 'STUDENT ASSESSMENT SYSTEM'
TXT_SPEED = 0.01


class Student:
    def __init__(self, name, answer_key, grade):
        global num_questions

        self.name = name
        self.answer_key = answer_key
        self.grade = round(grade, 2)


    def print_name_grade(self):
        terminal.animate(f'Name: {self.name}')
        terminal.animate(f'Grade: {self.grade}')
        print()
        terminal.animate('Press any key to continue...')


    def print_results(self):
        print()
        print(f'Name: {self.name}')
        print(f'Grade: {self.grade}')
        print(f'Answer key: {self.answer_key}')
        print()
        input('Press any key to continue...')


class TerminalPrint:
    def animate(self, text, TXT_SPEED=0.01):
        for letter in text:
            print(letter, end='', flush=True)
            sleep(TXT_SPEED)
        print()


    def print_title(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'=' * len(APP_TITLE))
        print(APP_TITLE)
        print(f'=' * len(APP_TITLE))
        print()


    def print_register(self):
        print(f'=' * len(APP_TITLE))
        print('ANSWER KEY REGISTER')
        print(f'=' * len(APP_TITLE))
        print()


    def print_student_num(self):
        print(f'=' * len(APP_TITLE))
        print(f'STUDENT {s + 1}:')
        print(f'=' * len(APP_TITLE))
        print()


    def print_final_grades(self):
        print(f'=' * len(APP_TITLE))
        print('FINAL GRADES:')
        print(f'=' * len(APP_TITLE))
        print()


    def print_student_checker(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        student_checker_str = 'STUDENT CHECKER'
        print(f'=' * len(student_checker_str))
        print('STUDENT CHECKER')
        print(f'=' * len(student_checker_str))
        print()


terminal = TerminalPrint()
terminal.print_title()
terminal.print_register()

terminal.animate(f'How many questions?')
num_questions = ''
while type(num_questions) is not int:
    try:
        num_questions = int(input())
    except:
        pass
question_value = 10 / num_questions
print(question_value)

test_answer_key = []
valid_answers = ['a', 'b', 'c', 'd']
for q in range(num_questions):
    terminal.print_title()
    terminal.print_register()
    terminal.animate(f'Answer to the question {q + 1}:')
    new_q_answer = ''
    while new_q_answer not in valid_answers:
        try:
            new_q_answer = input().lower()[0]
        except:
            pass
        test_answer_key.append(new_q_answer)


terminal.print_title()
terminal.animate('How many students took the test?')
num_students = ''
while type(num_students) is not int:
    try:
        num_students = int(input())
    except:
        pass


students_list = []
for s in range(num_students):
    terminal.print_title()
    terminal.print_student_num()
    terminal.animate(f'Enter the name of the student {s + 1}:')
    student_name = input()

    student_answer_key = []
    for q in range(num_questions):
        terminal.print_title()
        terminal.print_student_num()
        terminal.animate(f'Answer to the question {q + 1}:')

        new_q_answer = ''
        while new_q_answer not in valid_answers:
            try:
                new_q_answer = input().lower()[0]
            except:
                pass
        student_answer_key.append(new_q_answer)

    student_grade = 0
    for q in range(num_questions):
        if student_answer_key[q] == test_answer_key[q]:
            student_grade += question_value

    students_list.append(Student(
        student_name, student_answer_key, student_grade))


for s in students_list:
    terminal.print_title()
    terminal.print_final_grades()
    s.print_name_grade()
    input()


check_student = True
while check_student:
    terminal.print_student_checker()
    print('Do you want to check any student information? (y/n)')
    answer = ''
    while answer not in ['y', 'n']:
        try:
            answer = input().lower()[0]
        except:
            pass
    if answer == 'y':
        check_student = True
    else:
        print()
        terminal.animate('Exiting the app...')
        sleep(3)
        check_student = False
        break

    terminal.print_student_checker()
    print('Enter the name of the student you want to check:')
    name = input().lower()

    student_found = True
    for s in students_list:
        if name == s.name.lower():
            s.print_results()
            student_found = True
            break
    if not student_found:
        print('There is no student with that name')