from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
IMG_CARD_FRONT = 'imgs/card_front.png'
IMG_CARD_BACK = 'imgs/card_back.png'
IMG_WRONG = 'imgs/wrong.png'
IMG_RIGHT = 'imgs/right.png'
FONT_TITLE = ('Courier', 28, 'italic')
FONT_WORD = ('Courier', 50, 'bold')
WORDS = 'data/french_words.csv'

data = pd.read_csv(WORDS)
words_to_learn = data.to_dict(orient='records')
data = pd.DataFrame(words_to_learn)
data.to_csv('data/unknown_words.csv')
current_word = {}


def next_word():
    global current_word, flip_timer
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text='French', fill='green')
    canvas.itemconfig(card_word, text=current_word['French'], fill='green')
    canvas.itemconfig(card_bg, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def known_word():
    global current_word
    words_to_learn.remove(current_word)
    data = pd.DataFrame(words_to_learn)
    data.to_csv('data/041_flash_card_app_unknown_words.csv')


def flip_card():
    canvas.itemconfig(card_title, text='English translation', fill='white')
    canvas.itemconfig(card_word, text=current_word['English'], fill='white')
    canvas.itemconfig(card_bg, image=back_img)


window = Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file=IMG_CARD_FRONT)
back_img = PhotoImage(file=IMG_CARD_BACK)
card_bg = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, font=FONT_TITLE)
card_word = canvas.create_text(400, 263, font=FONT_WORD)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file=IMG_WRONG)
wrong_button = Button(image=wrong_image, command=next_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file=IMG_RIGHT)
right_button = Button(image=right_image, command=known_word)
right_button.grid(row=1, column=1)


next_word()
window.mainloop()