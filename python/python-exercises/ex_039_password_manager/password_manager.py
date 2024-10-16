from tkinter import *
from tkinter import messagebox
import os
import random
import string


FONT = ('Courier', 12)
LOGO_IMG_LOCATION = './imgs/logo.png'
PASSWORDS_FILE_LOCATION = './data/passwords.txt'


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    password_dict = {'Website': website, 'Email': email, 'Password': password}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error!', message='Please fill in all the fields!')
    else:
        wanna_save = messagebox.askokcancel(title=website, message=f'Email/Username: {email}\nPassword: {password}\n\nDo you want to saVe?')

        if wanna_save:
            if os.path.getsize(PASSWORDS_FILE_LOCATION) > 0:
                with open(PASSWORDS_FILE_LOCATION, 'a') as data_file:
                    data_file.write(f'\n')

            for k, v in password_dict.items():
                with open(PASSWORDS_FILE_LOCATION, 'a') as data_file:
                    data_file.write(f'{k}: {v}\n')
            
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    n_letters = random.randint(1, 5)
    n_numbers = random.randint(1, 5)
    n_symbols= random.randint(1, 5)

    def generator (n_letters, n_numbers, n_symbols):
        password = []
        for char in range(1, n_letters+1):
            password.append(random.choice(letters))
            
        for num in range(1, n_numbers+1):
            password.append(random.choice(numbers))
            
        for symbol in range(1, n_symbols+1):
            password.append(random.choice(symbols))

        random.shuffle(password)

        password_string = ''.join(password)
        return password_string

    generated_password = generator(n_letters, n_numbers, n_symbols)
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_img = PhotoImage(file=LOGO_IMG_LOCATION)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:', font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(text='', font=FONT, width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text='Email/Username:', font=FONT)
email_label.grid(row=2, column=0)

email_entry = Entry(text='', font=FONT, width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password', font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(text='', font=FONT, width=23)
password_entry.grid(row=3, column=1)

generate_button = Button(text='Generate', font=FONT,width=9, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', font=FONT, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()