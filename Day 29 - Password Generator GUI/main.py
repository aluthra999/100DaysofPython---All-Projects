import random
from tkinter import *
from tkinter import messagebox
import string
import pyperclip


# -------- PASSWORD GENERATOR ------------ #


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))

    password_entry.insert(0, password)
    pyperclip.copy(password)


# -------------- SAVE PASSWORDS -----------------------#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please do not leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Email and Password for "{website.upper()}" is'
                                                              f'\nEmail: {email} \nPassword: {password} '
                                                              f'\nAll looks good?')
        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------- CLEAR BUTTON -----------------------#
def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# def clear_all():
#     website_entry.delete(0, END)
#     password_entry.delete(0, END)
#     email_entry.delete(0, END)


# ------------------- UI SETUP ------------------------ #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "youremail@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=36)
password_entry.grid(column=1, row=3, columnspan=3)

generate_button = Button(text="Generate Password", width=31, command=generate_password)
generate_button.grid(column=1, row=4, columnspan=2)

clear_button = Button(text='Clear', width=31, command=clear)
clear_button.grid(column=1, row=5, columnspan=2)

# clear_all_button = Button(text='Clear All', width=15, command=clear_all)
# clear_all_button.grid(column=2, row=4)

add_button = Button(text="Add", width=31, command=save)
add_button.grid(column=1, row=6, columnspan=2)

window.mainloop()
