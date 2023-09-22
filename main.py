from tkinter import *
import pyperclip
from tkinter import messagebox
from random import choice, randint, shuffle

YELLOW = "#f7f5dd"


def random_password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(8,10))]
    password_list = password_letters + password_numbers + password_symbols
    print(password_list)
    shuffle(password_list)
    password = "".join(password_list)
    print(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save_data_to_file():
    website= website_entry.get()
    email= email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty!")
    if len(password)<5:
        messagebox.showinfo(title="Oops", message="Password must be minimum 5 characters long")

    else:
        is_ok = messagebox.askokcancel(title=website, message= f"These are details entered: \nEmail: {email} \nPassword: {password}\nIs it ok to save?")
        if is_ok:
            messagebox.showinfo(title="Information", message="Your info has been saved")
            with open("data.txt","a") as file:
                data = f"{website} | {email} | {password}\n"
                password_entry.delete(0, END)
                website_entry.delete(0, END)
                email_entry.delete(0,END)
                file.write(data)


window = Tk()

logo = PhotoImage(file="logo.png")
window.config(padx=150, pady=150, bg=YELLOW)
canvas = Canvas(width=200, height=200, background= YELLOW, highlightthickness=0 )
window.title("Password Manager")
canvas.create_image(100, 100, image= logo)
canvas.grid(column=1, row=1)

website_label = Label(text= "Website")
website_label.grid(column=0, row=2)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=2, columnspan=2)
email_label = Label(text="Email")
email_label.grid(column=0, row=3)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=3, columnspan=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=4)
password_entry = Entry(width=26)
password_entry.grid(column=1, row=4)

password_button = Button(text="Generate Password",width=15, command=random_password_generator)
password_button.grid(column=2, row=4, columnspan=2)
add_button = Button(text="Add",width=30,command=save_data_to_file)
add_button.grid(column=1, row=5, columnspan=2)



window.mainloop()