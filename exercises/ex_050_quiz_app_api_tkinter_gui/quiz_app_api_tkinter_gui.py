import csv
import html
import os
from tkinter import *
from tkinter import ttk
import pygame
import requests
from PIL import Image, ImageTk


FONT_SMALL = ('Courier', 16, 'italic bold')
FONT_MEDIUM = ('Courier', 22, 'bold')
FONT_BIG = ('Courier', 38, 'bold')
FONT_GAME_OVER = ('Courier', 50, 'bold')
FONT_MENU = ('Courier', 10)
FONT_Q_TEXT = ('Courier',15, 'italic')
FONT_SCORE = ('Courier', 22, 'bold')

THEME_COLOR_BLUE = '#375362'
THEME_COLOR_LIGHT_BLUE = '#B0D8F5'
THEME_COLOR_DARK_BLUE = '#22344A'
THEME_COLOR_GREEN = '#50AD67'
THEME_COLOR_YELLOW = '#AD9850'
THEME_COLOR_RED = '#BA5D3A'

TRUE_BUTTON_IMG_PATH = 'imgs/true_button.png'
FALSE_BUTTON_IMG_PATH = 'imgs/false_button.png'
RIGHT_ANSWER_SOUND_FX_PATH = 'sounds/right_answer_sound_fx.mp3'
WRONG_ANSWER_SOUND_FX_PATH = 'sounds/wrong_answer_sound_fx.mp3'

COOLDOWN_MS = 1000
DIFFICULTY_OPTIONS = ['Easy', 'Medium', 'Hard']
QUESTION_AMOUNT_OPTIONS = [3, 5, 10, 20, 50]
WIDTH = 360
HEIGHT = 640

global category
global difficulty
global question_amount
global user_score


class GetRequests:
    def __init__(self):
        global category
        self.get_categories_file()


    def get_categories_file(self):
        if os.path.isfile('data/categories.csv'):
            self.categories_list, self.categories_ids, self.categories_names, self.categories = self.read_categories_csv()

        else:
            self.categories = self.get_categories()
            self.categories_list = self.get_categories_lists()
            self.categories_ids = self.get_categories_ids()
            self.categories_names = self.get_categories_names()
            self.write_categories_csv()


    def read_categories_csv(self):
        with open('data/050_categories.csv', mode='r') as file:
            reader = csv.reader(file)
            categories_list_raw = next(reader)
            categories_list = [eval(string_tuple) for string_tuple in categories_list_raw]
            categories_ids = next(reader)
            categories_names = next(reader)
            categories = next(reader)
        file.close()

        return categories_list, categories_ids, categories_names, categories


    def write_categories_csv(self):
        if not os.path.exists('data'):
            os.makedirs('data')

        with open('data/050_categories.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.categories_list)
            writer.writerow(self.categories_ids)
            writer.writerow(self.categories_names)
            writer.writerow(self.categories)
        file.close()


    def get_categories(self):
        response = requests.get('https://opentdb.com/api_category.php')
        response.raise_for_status()
        categories = response.json()

        return categories


    def get_categories_lists(self):
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

        return categories_list


    def get_categories_ids(self):
        categories_ids = []
        for id in self.categories_list:
            new_id = id[0]
            categories_ids.append(new_id)

        return categories_ids


    def get_categories_names(self):
        categories_names = []
        for name in self.categories_list:
            new_name = name[1]
            categories_names.append(new_name)

        return categories_names


class SoundFXController:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()


    def play_right_answer_sound_fx(self):
        pygame.mixer.music.load(RIGHT_ANSWER_SOUND_FX_PATH)
        pygame.mixer.music.play()


    def play_wrong_answer_sound_fx(self):
        pygame.mixer.music.load(WRONG_ANSWER_SOUND_FX_PATH)
        pygame.mixer.music.play()


class StandardWindowGUI(Tk):
    def __init__(self):
        super().__init__()
        global WIDTH
        global HEIGHT
        self.create_window()


    def centralize_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_pos = int(screen_width/2 - WIDTH/2)
        y_pos = int(screen_height/2 - HEIGHT/2)
        self.geometry(f'{WIDTH}x{HEIGHT}+{x_pos}+{y_pos}')


    def create_window(self):
        self.title('QUIZ')
        self.config(
            padx=25,
            pady=25,
            bg=THEME_COLOR_BLUE)
        self.centralize_window()
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)


    def create_true_button(self):
        self.true_image = ImageTk.PhotoImage(
            Image.open(TRUE_BUTTON_IMG_PATH)
            .resize(
            (107, 107),
            Image.Resampling.LANCZOS))
        self.true_button = Button(
            image=self.true_image,
            bg=THEME_COLOR_BLUE,
            activebackground=THEME_COLOR_BLUE,
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
            Image.Resampling.LANCZOS))
        self.false_button = Button(
            image=self.false_image,
            bg=THEME_COLOR_BLUE,
            activebackground=THEME_COLOR_BLUE,
            highlightthickness=0,
            relief=FLAT)
        self.false_button.grid(
            row=3,
            column=1,
            sticky='e',
            )

        return self.false_button


    def create_empty_label(self):
        self.empty_label = Label(
            bg=THEME_COLOR_BLUE)
        self.empty_label.grid(
            row=0,
            column=0
        )

        return self.empty_label


class MainScreenController(GetRequests):
    def __init__(self):
        super().__init__()


    def get_selected_category(self):
        category_selected_name = self.categories_menu.get()
        for id_and_name in self.categories_list:
            if id_and_name[1] == category_selected_name:
                category_selected_id = id_and_name[0]
                break

        return category_selected_id


    def get_selected_difficulty(self):
        selected_difficulty_raw = self.difficulty_menu.get()
        selected_difficulty = selected_difficulty_raw.lower()

        return selected_difficulty


    def get_selected_question_amount(self):
        selected_question_amount = self.question_amount_menu.get()

        return selected_question_amount


    def start_button_pressed(self):
        global category
        global difficulty
        global question_amount
        category = self.get_selected_category()
        question_amount = self.get_selected_question_amount()
        difficulty = self.get_selected_difficulty()
        self.window.destroy()
        quiz_screen = QuizScreenGUI()


    def quit_button_pressed(self):
        self.window.destroy()


class MainScreenGUI(MainScreenController):
    def __init__(self):
        super().__init__()
        self.window = StandardWindowGUI()
        self.create_screen()
        self.window.mainloop()


    def create_screen(self):
        # self.window.wm_attributes('-transparentcolor', self.window['bg'])
        self.window.option_add('*TCombobox*Listbox*Font', FONT_MENU)
        self.create_quiz_top_label()
        self.empty_label_1 = self.window.create_empty_label()
        self.empty_label_1.config(
            pady=25)
        self.empty_label_1.grid(
            row=1)
        self.create_categories_label()
        self.create_categories_menu()
        self.create_question_amount_label()
        self.create_question_amount_menu()
        self.create_difficulty_label()
        self.create_difficulty_menu()
        self.empty_label_2 = self.window.create_empty_label()
        self.empty_label_2.config(
            pady=50)
        self.empty_label_2.grid(
            row=8)
        self.create_start_button()
        self.create_quit_button()


    def create_quiz_top_label(self):
        self.quiz_top_label = Label(
            text='QUIZ GAME\nSETTINGS',
            fg=THEME_COLOR_YELLOW,
            bg=THEME_COLOR_BLUE,
            font=FONT_BIG)
        self.quiz_top_label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky='n',
            pady=15)


    def create_categories_label(self):
        self.categories_label = Label(
            text='Select a category:',
            fg=THEME_COLOR_LIGHT_BLUE,
            bg=THEME_COLOR_BLUE,
            font=FONT_SMALL)
        self.categories_label.grid(
            row=2,
            column=0,
            columnspan=2,
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
            row=3,
            column=0,
            columnspan=2,
            sticky='w')


    def create_difficulty_label(self):
        self.difficulty_label = Label(
            text='Difficulty:',
            fg=THEME_COLOR_LIGHT_BLUE,
            bg=THEME_COLOR_BLUE,
            font=FONT_SMALL)
        self.difficulty_label.grid(
            row=4,
            column=0,
            columnspan=2,
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
            row=5,
            column=0,
            columnspan=2,
            sticky='w')


    def create_question_amount_label(self):
        self.question_amount_label = Label(
            text='How many questions?',
            fg=THEME_COLOR_LIGHT_BLUE,
            bg=THEME_COLOR_BLUE,
            font=FONT_SMALL)
        self.question_amount_label.grid(
            row=6,
            column=0,
            columnspan=2,
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
            row=7,
            column=0,
            columnspan=2,
            sticky='w')


    def create_start_button(self):
        self.start_button = Button(
            text='START!',
            highlightthickness=0,
            font=FONT_MEDIUM,
            bg=THEME_COLOR_GREEN,
            activebackground='orange',
            width=7,
            height=1,
            command=self.start_button_pressed)
        self.start_button.grid(
            row=9,
            column=0,
            sticky='w',
            pady=0)


    def create_quit_button(self):
        self.quit_button = Button(
            text='QUIT',
            highlightthickness=0,
            font=FONT_MEDIUM,
            bg=THEME_COLOR_RED,
            activebackground='brown',
            width=7,
            height=1,
            command=self.quit_button_pressed)
        self.quit_button.grid(
            row=9,
            column=1,
            sticky='e',
            pady=0)


class QuizBrain:
    def __init__(self):
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
        self.question_bank = self.get_question_bank()
        self.game_over = self.is_game_over()


    def get_question_bank(self):
        response = requests.get('https://opentdb.com/api.php', params=self.parameters)
        response.raise_for_status()
        question_data = response.json()

        question_bank = []
        for question in question_data['results']:
            new_question = question['question'], question['correct_answer']
            question_bank.append(new_question)

        return question_bank


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


class QuizScreenController:
    def __init__(self):
        pass


    def get_next_question(self):
        self.clear_canvas_config()

        self.game_over = self.is_game_over()
        if not self.game_over:
            global correct_answer
            correct_answer, q_number_text, q_text = self.next_question()
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
        user_answer = self.check_answer('True', correct_answer)
        self.disable_buttons()
        self.give_feedback(user_answer)


    def false_button_pressed(self):
        global correct_answer
        user_answer = self.check_answer('False', correct_answer)
        self.disable_buttons()
        self.give_feedback(user_answer)


    def give_feedback(self, user_answer):
        if user_answer == 'right answer':
            self.sound_fx_controller.play_right_answer_sound_fx()
            self.show_right_screen()
            self.increase_score()
        elif user_answer == 'wrong answer':
            self.sound_fx_controller.play_wrong_answer_sound_fx()
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
            bg=THEME_COLOR_GREEN)
        self.canvas.itemconfig(
            self.question_text,
            text='RIGHT!',
            font=FONT_BIG,
            fill='white')
        self.right_wrong_screens_config()


    def show_wrong_screen(self):
        self.canvas.config(
            bg=THEME_COLOR_RED)
        self.canvas.itemconfig(
            self.question_text,
            text='WRONG!',
            font=FONT_BIG,
            fill='white')
        self.right_wrong_screens_config()


    def increase_score(self):
        global user_score
        user_score += 1
        self.score.set(f'Right answers: {user_score}')


    def show_final_screen(self):
        self.window.destroy()
        self.final_screen = FinalScreenGUI()


class QuizScreenGUI(QuizBrain, QuizScreenController):
    def __init__(self):
        super().__init__()
        self.sound_fx_controller = SoundFXController()
        global user_score
        user_score = 0
        self.quiz_controller = QuizScreenController()
        self.window = StandardWindowGUI()
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
            f'Right answers: {user_score}')
        self.score_label = Label(
            text=f'Score:',
            textvariable=self.score,
            fg=THEME_COLOR_LIGHT_BLUE,
            bg=THEME_COLOR_BLUE,
            font=FONT_SCORE,
            anchor='center')
        self.score_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=10
            )


    def create_canvas(self):
        self.canvas = Canvas(
        width=360,
        height=360,
        bg='white',)
        self.canvas_width = int(self.canvas['width'])


        self.question_number_text = self.canvas.create_text(
            self.canvas_width / 2 - 25,
            50,
            text='',
            fill=THEME_COLOR_DARK_BLUE,
            font=FONT_MEDIUM
        )

        self.question_text = self.canvas.create_text(
            self.canvas_width / 2 - 50,
            200,
            text='',
            width=280,
            fill=THEME_COLOR_BLUE,
            font=FONT_Q_TEXT
            )

        self.true_or_false_text = self.canvas.create_text(
            self.canvas_width / 2 - 25,
            300,
            text='True or False?',
            fill=THEME_COLOR_BLUE,
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
            fill=THEME_COLOR_BLUE)
        self.canvas.coords(
            self.question_text,
            self.canvas_width / 2 - 25,
            180)
        self.canvas.itemconfig(
            self.true_or_false_text,
            text='True or False?')


    def right_wrong_screens_config(self):
        self.canvas.itemconfig(
            self.question_number_text,
            text='')
        self.canvas.coords(
            self.question_text,
            self.canvas_width / 2 - 25,
            180)
        self.canvas.itemconfig(
            self.true_or_false_text,
            text='')



class FinalScreenGUI:
    def __init__(self):
        self.window = StandardWindowGUI()
        self.window.config(
        bg=THEME_COLOR_DARK_BLUE)
        self.create_screen()
        self.window.mainloop()


    def create_screen(self):
        self.create_game_over_label()
        self.create_final_score_label()
        self.empty_label = self.window.create_empty_label()
        self.empty_label.config(
            bg=THEME_COLOR_DARK_BLUE,
            pady=30
        )
        self.empty_label.grid(
            row=2,
            column=0
        )
        self.create_continue_label()
        self.continue_button = self.window.create_true_button()
        self.continue_button.config(
            command=self.continue_button_pressed,
            bg=THEME_COLOR_DARK_BLUE)
        self.continue_button.grid(
            row=4,
            column=0,
            sticky='w',
            pady=25)

        self.quit_button = self.window.create_false_button()
        self.quit_button.config(
            command=self.quit_button_pressed,
            bg=THEME_COLOR_DARK_BLUE)
        self.quit_button.grid(
            row=4,
            column=1,
            sticky='w')


    def create_game_over_label(self):
        self.game_over_label = Label(
            text='GAME\nOVER',
            fg='red',
            bg=THEME_COLOR_DARK_BLUE,
            font=FONT_GAME_OVER)
        self.game_over_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=25)


    def create_final_score_label(self):
        global user_score
        global question_amount
        self.final_score_label = Label(
            text=f'Final score: {user_score}/{question_amount}',
            fg=THEME_COLOR_LIGHT_BLUE,
            bg=THEME_COLOR_DARK_BLUE,
            font=FONT_MEDIUM)
        self.final_score_label.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=5)


    def create_continue_label(self):
        self.continue_label = Label(
            text=f'CONTINUE?',
            fg=THEME_COLOR_GREEN,
            bg=THEME_COLOR_DARK_BLUE,
            font=FONT_BIG)
        self.continue_label.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=25)


    def continue_button_pressed(self):
        self.window.destroy()
        self.main_screen = MainScreenGUI()


    def quit_button_pressed(self):
        self.window.destroy()


if __name__ == '__main__':
    main_screen = MainScreenGUI()