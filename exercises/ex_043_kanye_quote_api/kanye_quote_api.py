from tkinter import *
import requests


URL = 'http://api.kanye.rest'
BG_IMG = 'imgs/background.png'
KANYE_IMG = 'imgs/face.png'
FONT = ('Courier', 18, 'bold')


def get_quote():
    response = requests.get(url=URL)
    response.raise_for_status()

    data = response.json()
    quote = data['quote']
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title('Kanye says...')
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=BG_IMG)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text='Kanye quotes', width=250, font=FONT, fill='black')
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=KANYE_IMG)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()