import csv
import html
import os
import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


FONT_SMALL = ('Courier', 14, 'bold')
FONT_MEDIUM = ('Courier', 17, 'bold')
FONT_BIG = ('Courier', 30, 'bold')
FONT_MENU = ('Courier', 10)
FONT_Q_TEXT = ('Courier',10, 'italic')
FONT_SCORE = ('Courier', 25, 'bold')
THEME_COLOR = '#375362'
TRUE_BUTTON_IMG_PATH = 'imgs/true_button.png'
FALSE_BUTTON_IMG_PATH = 'imgs/false_button.png'

COOLDOWN_MS = 1000
DIFFICULTY_OPTIONS = ['Easy', 'Medium', 'Hard']
QUESTION_AMOUNT_OPTIONS = [3, 5, 10, 20, 50]
global category
global difficulty
global question_amount
global user_score


class MainScreen():
    def __init__(self):
        self.get_categories()
        self.window = StandardWindow()
        self.create_screen()
        self.window.mainloop()


    def create_screen(self):
        self.window.option_add('*TCombobox*Listbox*Font', FONT_MENU)
        self.create_quiz_top_label()
        self.create_categories_label()
        self.create_categories_menu()
        self.create_question_amount_label()
        self.create_question_amount_menu()
        self.create_difficulty_label()
        self.create_difficulty_menu()
        self.create_start_button()
        
        
    def create_quiz_top_label(self):
        self.quiz_top_label = Label(
            text='QUIZ GAME\nSETTINGS',
            fg='yellow',
            bg=THEME_COLOR,
            font=FONT_BIG)
        self.quiz_top_label.grid(
            row=0,
            column=0,
            sticky='n',
            pady=100)               
        
        
    def create_categories_label(self):
        self.categories_label = Label(
            text='Select a category:',
            fg='white',
            bg=THEME_COLOR,
            font=FONT_SMALL)
        self.categories_label.grid(
            row=1,
            column=0,
            sticky='w')


    def create_categories_menu(self):
        self.categories_menu = ttk.Combobox(
            values=self.categories_names,
            state='readonly')
        self.categories_menu.current(4)
        self.categories_menu.config(
            width=37,
            font=FONT_MENU)
        self.categories_menu.grid(
            row=2,
            column=0,
            sticky='w')


    def create_question_amount_label(self):
        self.question_amount_label = Label(
            text='How many questions?',
            fg='white',
            bg=THEME_COLOR,
            font=FONT_SMALL)
        self.question_amount_label.grid(
            row=5,
            column=0,
            sticky='w')


    def create_question_amount_menu(self):
        self.question_amount_menu = ttk.Combobox(
            values=QUESTION_AMOUNT_OPTIONS,
            state='readonly')
        self.question_amount_menu.current(0)
        self.question_amount_menu.config(
            width=37,
            font=FONT_MENU)
        self.question_amount_menu.grid(
            row=6,
            column=0,
            sticky='w')


    def create_difficulty_label(self):
        self.difficulty_label = Label(
            text='Difficulty:',
            fg='white',
            bg=THEME_COLOR,
            font=FONT_SMALL)
        self.difficulty_label.grid(
            row=3,
            column=0,
            sticky='w')


    def create_difficulty_menu(self):
        self.difficulty_menu = ttk.Combobox(
            values=DIFFICULTY_OPTIONS,
            state='readonly')
        self.difficulty_menu.current(1)
        self.difficulty_menu.config(
            width=37,
            font=FONT_MENU)
        self.difficulty_menu.grid(
            row=4,
            column=0,
            sticky='w')


    def create_start_button(self):
        self.start_button = Button(
            text='Start!',
            highlightthickness=0,
            font=FONT_MEDIUM,
            anchor='center',
            command=self.start_button_pressed)
        self.start_button.grid(
            row=7,
            column=0,
            pady=175)


    def get_categories(self):
        if os.path.isfile('data/050_categories.csv'):
            self.categories_list, self.categories_ids, self.categories_names = self.read_categories_csv()

        else:
            self.connect_to_api_category()
            self.categories_list, self.categories_ids, self.categories_names = self.get_categories_lists_ids_names()
            self.write_categories_csv()


    def read_categories_csv(self):
        with open('data/050_categories.csv', mode='r') as file:
            reader = csv.reader(file)
            categories_list_raw = next(reader)
            categories_list = [eval(string_tuple) for string_tuple in categories_list_raw]
            categories_ids = next(reader)
            categories_names = next(reader)
        file.close()

        return categories_list, categories_ids, categories_names

    
    def write_categories_csv(self):
        with open('data/050_categories.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.categories_list)
            writer.writerow(self.categories_ids)
            writer.writerow(self.categories_names)
        file.close()


    def connect_to_api_category(self):
        response = requests.get('https://opentdb.com/api_category.php')
        response.raise_for_status()
        self.categories = response.json()


    def get_categories_lists_ids_names(self):
        categories_list = []
        for category in self.categories['trivia_categories']:
            new_category = category['id'], category['name']
            get_amount = requests.get(f'https://opentdb.com/api_count.php?category={str(new_category[0])}')
            get_amount.raise_for_status()
            new_category_json = get_amount.json()
            new_category_amount = new_category_json['category_question_count']

            if new_category_amount['total_question_count'] > 100:
                categories_list.append(new_category)

        categories_list.sort(key=lambda x: x[1])

        categories_ids = []
        for id in categories_list:
            new_id = id[0]
            categories_ids.append(new_id)

        categories_names = []
        for name in categories_list:
            new_name = name[1]
            categories_names.append(new_name)

        return categories_list, categories_ids, categories_names


    def get_selected_category(self):
        category_selected_name = self.categories_menu.get()
        for id_and_name in self.categories_list:
            if id_and_name[1] == category_selected_name:
                category_selected_id = id_and_name[0]
                break

        return category_selected_id

   
    def get_selected_question_amount(self):
        selected_question_amount = self.question_amount_menu.get()

        return selected_question_amount


    def get_selected_difficulty(self):
        selected_difficulty_raw = self.difficulty_menu.get()
        selected_difficulty = selected_difficulty_raw.lower()

        return selected_difficulty


    def start_button_pressed(self):
        global category
        global difficulty
        global question_amount
        category = self.get_selected_category()
        question_amount = self.get_selected_question_amount()
        difficulty = self.get_selected_difficulty()
        self.window.destroy()
        quiz_screen = QuizScreen()


class QuizScreen():
    def __init__(self):
        global user_score
        user_score = 0
        self.quiz_brain = QuizBrain()
        self.window = StandardWindow()
        self.create_screen()
        self.current_question = self.get_next_question()
        self.window.mainloop()


    def create_screen(self):
        self.create_score_label()
        self.create_canvas()
        self.true_button = self.window.create_true_button()
        self.true_button.config(
            command=self.true_button_pressed,)
        self.false_button = self.window.create_false_button()
        self.false_button.config(
            command=self.false_button_pressed)


    def create_score_label(self):
        global user_score
        self.score = StringVar()
        self.score.set(
            f'SCORE: {user_score}')
        self.score_label = Label(
            text=f'Score:',
            textvariable=self.score,
            fg='yellow',
            bg=THEME_COLOR,
            font=FONT_SCORE)
        self.score_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=25)


    def create_canvas(self):
        self.canvas = Canvas(
        width=720,
        height=900,
        bg='white',)
        self.canvas_width = int(self.canvas['width'])


        self.question_number_text = self.canvas.create_text(
            self.canvas_width / 2 - 25,
            175,
            text='',
            fill=THEME_COLOR,
            font=FONT_MEDIUM
        )

        self.question_text = self.canvas.create_text(
            self.canvas_width / 2 - 50,
            450,
            text='',
            width=600,
            fill=THEME_COLOR,
            font=FONT_Q_TEXT
            )

        self.true_or_false_text = self.canvas.create_text(
            self.canvas_width / 2 - 25,
            690,
            text='True or False?',
            fill=THEME_COLOR,
            font=FONT_MEDIUM,
        )
        self.canvas.grid(
        row=2,
        column=0,
        columnspan=2,
        pady=25)



    def clear_canvas_config(self):
        self.canvas.config(
            bg='white')
        self.canvas.itemconfig(
            self.question_text,
            font=FONT_Q_TEXT,
            fill=THEME_COLOR)
        self.canvas.coords(
            self.question_text,
            self.canvas_width / 2 - 25,
            420)
        self.canvas.itemconfig(
            self.true_or_false_text,
            text='True or False?')


    def get_next_question(self):
        self.clear_canvas_config()

        game_over = self.quiz_brain.is_game_over()
        if not game_over:
            global correct_answer
            correct_answer, q_number_text, q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(
                self.question_number_text,
                text=q_number_text)
            self.canvas.itemconfig(
                self.question_text,
                text=q_text)
        else:
            self.show_final_screen()


    def true_button_pressed(self):
        global correct_answer
        user_answer = self.quiz_brain.check_answer('True', correct_answer)
        self.disable_buttons()
        self.give_feedback(user_answer)


    def false_button_pressed(self):
        global correct_answer
        user_answer = self.quiz_brain.check_answer('False', correct_answer)
        self.disable_buttons()
        self.give_feedback(user_answer)


    def give_feedback(self, user_answer):
        if user_answer == 'right answer':
            self.show_right_screen()
            self.increase_score()
        elif user_answer == 'wrong answer':
            self.show_wrong_screen()

        self.window.after(COOLDOWN_MS, self.get_next_question)


    def disable_buttons(self):
        self.true_button.config(
            state='disabled')
        self.false_button.config(
            state='disabled')
        self.window.after(COOLDOWN_MS, self.enable_buttons)


    def enable_buttons(self):
        self.true_button.config(
            state='normal')
        self.false_button.config(
            state='normal')


    def show_right_screen(self):
        self.canvas.config(
            bg='green')
        self.canvas.itemconfig(
            self.question_number_text,
            text='')
        self.canvas.itemconfig(
            self.question_text,
            text='RIGHT!',
            font=FONT_BIG,
            fill='white')
        self.canvas.coords(
            self.question_text,
            self.canvas_width / 2,
            440)
        self.canvas.itemconfig(
            self.true_or_false_text,
            text='')


    def show_wrong_screen(self):
        self.canvas.config(
            bg='red')
        self.canvas.itemconfig(
            self.question_number_text,
            text='')
        self.canvas.itemconfig(
            self.question_text,
            text='WRONG!',
            font=FONT_BIG,
            fill='white')
        self.canvas.coords(
            self.question_text,
            self.canvas_width / 2,
            440)
        self.canvas.itemconfig(
            self.true_or_false_text,
            text='')


    def increase_score(self):
        global user_score
        user_score += 1
        self.score.set(f'SCORE: {user_score}')


    def show_final_screen(self):
        self.window.destroy()
        self.final_screen = FinalScreen()


class QuizBrain():

    def __init__(self):
        # self.get_questions()
        global category
        global difficulty
        global question_amount
        self.question_number = 1
        self.parameters = {
            'amount': question_amount,
            'category': category,
            'difficulty': difficulty,
            'type': 'boolean'
        }

        response = requests.get('https://opentdb.com/api.php', params=self.parameters)
        response.raise_for_status()
        self.question_data = response.json()   

        self.question_bank = []
        for question in self.question_data['results']:
            new_question = question['question'], question['correct_answer']
            self.question_bank.append(new_question)


    def next_question(self):
        self.current_question = self.question_bank[self.question_number - 1]
        question_text = html.unescape(self.current_question[0])
        correct_answer = self.current_question[1]

        q_number_text = f'Question {self.question_number}:'
        q_text = f'{question_text}'
        self.question_number += 1

        return correct_answer, q_number_text, q_text


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            return 'right answer'
        else:
            return 'wrong answer'


    def is_game_over(self):
        if self.question_number < len(self.question_bank) + 1:
            return False
        else:
            return True


class FinalScreen():
    def __init__(self):
        self.window = StandardWindow()
        self.window.config(
        bg='black')
        self.create_screen()
        self.window.mainloop()


    def create_screen(self):
        self.create_game_over_label()
        self.create_final_score_label()
        self.create_empty_label()
        self.create_continue_label()
        self.continue_button = self.window.create_true_button()
        self.continue_button.config(
            command=self.continue_button_pressed,
            bg='black')
        self.continue_button.grid(
            row=4,
            column=0,
            sticky='w'
        )
        
        self.quit_button = self.window.create_false_button()
        self.quit_button.config(
            command=self.quit_button_pressed,
            bg='black')
        self.quit_button.grid(
            row=4,
            column=1,
            sticky='w'
        )


    def create_game_over_label(self):
        self.game_over_label = Label(
            text='GAME OVER',
            fg='red',
            bg='black',
            font=FONT_BIG)
        self.game_over_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=100)


    def create_final_score_label(self):
        global user_score
        global question_amount
        self.final_score_label = Label(
            text=f'Final score: {user_score}/{question_amount}',
            fg='white',
            bg='black',
            font=FONT_SMALL)
        self.final_score_label.grid(
            row=1,
            column=0,
            sticky='e',
            pady=50)


    def create_empty_label(self):
        self.empty_label = Label(
            text='',
            bg='black')
        self.empty_label.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=200)


    def create_continue_label(self):
        self.continue_label = Label(
            text=f'CONTINUE?',
            fg='yellow',
            bg='black',
            font=FONT_SMALL)
        self.continue_label.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=50)


    def continue_button_pressed(self):
        self.window.destroy()
        self.main_screen = MainScreen()


    def quit_button_pressed(self):
        self.window.destroy()


class StandardWindow(Tk):
    def __init__(self):
        super().__init__()
        self.create_window()


    def create_window(self):
        self.title('QUIZ')
        self.config(
            padx=25,
            pady=25,
            bg=THEME_COLOR)
        self.geometry('720x1280')
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.eval('tk::PlaceWindow . center')


    def create_true_button(self):
        self.true_image = ImageTk.PhotoImage(
            Image.open(TRUE_BUTTON_IMG_PATH)
            .resize(
            (107, 107),
            Image.ANTIALIAS))
        self.true_button = Button(
            image=self.true_image,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            highlightthickness=0,
            relief=FLAT)
        self.true_button.grid(
            row=3,
            column=0,
            sticky='w'
            )
        
        return self.true_button


    def create_false_button(self):
        self.false_image = ImageTk.PhotoImage(
            Image.open(FALSE_BUTTON_IMG_PATH)
            .resize(
            (107, 107),
            Image.ANTIALIAS))
        self.false_button = Button(
            image=self.false_image,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            highlightthickness=0,
            relief=FLAT)
        self.false_button.grid(
            row=3,
            column=1,
            sticky='e',
            )
        
        return self.false_button


if __name__ == '__main__':
    main_screen = MainScreen()