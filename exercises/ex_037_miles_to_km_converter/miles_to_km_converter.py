from tkinter import *


FONT = ('Courier', 12)
CONVERSION_RATIO =  1.609347218694


def miles_to_km():
    miles = float(input.get())
    km = miles * CONVERSION_RATIO
    result_label.config(text = f'{km:.5f}')


window = Tk()
window.title('Miles to Km converter')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

input = Entry(width=20, text='0')
input.grid(column=0, row=0)

miles_label = Label(text='Miles', font=FONT)
miles_label.grid(column=1, row=0)

result_label = Label(text='', font=FONT)
result_label.grid(column=0, row=2)

km_label = Label(text='Km', font=FONT)
km_label.grid(column=1, row=2)

calc_button = Button(text='Calculate', font=FONT, command=miles_to_km)
calc_button.grid(column=0, row=1)

window.mainloop()