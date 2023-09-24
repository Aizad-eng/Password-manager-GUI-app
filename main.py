from tkinter import *
import pyperclip
from tkinter import messagebox
from random import choice, randint, shuffle
import json

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

def delete_entries():
    password_entry.delete(0, END)
    # website_entry.delete(0, END)
    email_entry.delete(0, END)

def save_data_to_file():

    data = {}
    website= website_entry.get()
    email= email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password": password
        }

    }

    if len(website) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty!")
    if len(password)<5:
        messagebox.showinfo(title="Oops", message="Password must be minimum 5 characters long")

    else:
        messagebox.showinfo(title="Information", message="Your info has been saved")
        try:
            with open("data.json", "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data ={}
        existing_data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(existing_data, file, indent=4)

    delete_entries()
    website_entry.delete(0, END)

def search():

    data_read = {}
    try:
        with open("data.json", "r") as file:
            data_read = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="There are no saved passwords")
    if website_entry.get() in data_read:
        value = data_read[website_entry.get()]
        delete_entries()
        email_entry.insert(0, value['email'] )
        password_entry.insert(0, value['password'])
    else:
        messagebox.showerror(title="Oops", message="No saved passwords")
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

search_button = Button(text= "Search", width=10, command=search)
search_button.grid(column=3, row=2)



window.mainloop()