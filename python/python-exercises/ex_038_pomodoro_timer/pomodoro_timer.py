from tkinter import *
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_IMG_LOCATION = 'imgs/tomato.png'
repetitions = 0
timer = None


def start_timer():
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    global repetitions
    repetitions += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global overall_count

    if repetitions % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text='Long\nbreak', fg=RED)
    elif repetitions % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text='Short\nbreak', fg=PINK)
    elif repetitions % 2 == 1:
        countdown(work_sec)
        title_label.config(text='Work\n', fg=GREEN)


def reset_timer():
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    global repetitions
    repetitions = 0
    window.after_cancel(timer)
    title_label.config(text='Timer\n')
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = '0' + str(count_sec)
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(repetitions/2)
        for _ in range(work_sessions):
            marks += '✓'
        check_marks.config(text=marks)


window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=TOMATO_IMG_LOCATION)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 36, 'bold'))
canvas.grid(column=1, row=1)


title_label = Label(text='Timer\n', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 48, 'bold'))
title_label.grid(column=1, row=0)

start_button = Button(text='Start', bg=YELLOW, font=(FONT_NAME, 10), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', bg=YELLOW, font=(FONT_NAME, 10), command=reset_timer)
reset_button.config(state="disabled")
reset_button.grid(column=2, row=2)

check_marks = Label(text='', fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()