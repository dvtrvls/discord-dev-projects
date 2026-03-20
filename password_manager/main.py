from tkinter import *
import random
import pygame as pg
import pyperclip
from tkinter import messagebox
import json

yellow = "#FFDE42"
blue1 = "#53CBF3"
blue2 = "#5478FF"
blue3 = "#111FA2"
FONT = "Courier"


characters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%^&*()>?"
password_length = 8

def generate_password():
    global password_input
    password = ""
    for _ in range(password_length):
        password+=random.choice(characters)
    pyperclip.copy(password)
    password_input.set(password)


def to_overwrite(site, email, password):
    msgbox = messagebox.askyesno("Overwrite", "this site already exist.\ndo you want to\noverwrite it?")
    if msgbox:
        return True
    return False


def search():
    site = site_input.get()
    try:
        with open("password.json", "r") as file:
            data = json.load(file) #json to python
    except FileNotFoundError:
        response_label.config(text="the file does not exist yet")
        return
    try:
        email = data[site]["mail"]
        password = data[site]["password"]
    except KeyError:
        response_label.config(text="site not found")
        return
    else:
        info = f"Site: {site}\nEmail: {email}\nPassword: {password}"
        messagebox.showinfo("credentials", info)

def check_credentials():
    gmail = gmail_input.get()
    site = site_input.get()
    password = password_input.get()

    if gmail.strip() == "" or site.strip() == "" or password.strip() == "":
        return False
    return True

def check_pass_length():
    if len(password_input.get()) < password_length:
        return False
    return True 
def write_to_file():

    mail = gmail_input.get()
    site = site_input.get()
    password = password_input.get()
    data = {}
    try:
        with open("password.json", "r") as file:
            data = json.load(file) #json to python
    except FileNotFoundError:
        response_label.config(text="we have created a file\nsince it does not exist.")
        with open("password.json", "w") as file:
            json.dump(data, file)
    except json.JSONDecodeError:
        with open("password.json", "w") as file:
            json.dump(data, file)
    finally:
        
        alr_exists = site in data.keys()
          
        if alr_exists:
            if to_overwrite(site, mail, password):
                new_data = {site:{"mail":mail, "password":password}}
                data.update(new_data) #modify the data
                with open("password.json", "w") as f:   
                    json.dump(data, f, indent=4) #python to json
                response_label.config(text="saved successfully")
                return True
        else:
            new_data = {site:{"mail":mail, "password":password}}
            data.update(new_data) #modify the data
            with open("password.json", "w") as f:   
                json.dump(data, f, indent=4) #python to json
            response_label.config(text="saved successfully")
            return True
   
def submit():

    choice = messagebox.askokcancel("are you sure?", "are you sure\nyou want to save this?")
    if not choice:
        return
    if not check_credentials():
        response_label.config(text="any fields cannot be empty")
        beep.play()
        return
    if not check_pass_length():
        response_label.config(text=f"password must be {password_length} characters long")
        beep.play()
        return
    result = write_to_file()
    if result:
        response_label.config(text="saved successfully")
        name_entry.delete(0, END)
        site_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        response_label.config(text=result)

screen = Tk()
screen.title("Password Manager")
screen.geometry("700x500")
screen.resizable(False, False)
screen.config(bg=blue1, padx=20, pady=20)
lock_image = PhotoImage(file="lock.png")
pg.mixer.init()
beep = pg.mixer.Sound("errorsfx.mp3") # load sound
beep.set_volume(0.2) 

title_label = Label(screen, text="Password Manager", font=("Consolas", 30, "bold"), bg=blue1, fg=yellow)
title_label.grid(row=0, column=1)

lock_image_label = Label(screen, image=lock_image, bg=blue1)
lock_image_label.grid(row=1, column=1)


gmail_input = StringVar()
site_input = StringVar()
password_input = StringVar()


gmail_label = Label(screen, text="EMail :", font=(FONT, 14, "bold"), bg=blue1, fg=blue2)
gmail_label.grid(row=2, column=0)

name_entry = Entry(screen, font=(FONT, 14, "bold"), fg=blue3, textvariable=gmail_input, width=30)
name_entry.grid(row=2, column=1)


search_button = Button(screen, text="search", font=(FONT, 10, "bold"), bg=yellow, fg=blue2,width=20, command=search)
search_button.grid(row=3, column=2)

site_label = Label(screen, text="Site :", font=(FONT, 14, "bold"), bg=blue1, fg=blue2)
site_label.grid(row=3, column=0)

site_entry = Entry(screen, font=(FONT, 14, "bold"), fg=blue3, textvariable=site_input,width=30)
site_entry.grid(row=3, column=1)

password_label = Label(screen, text="Password :", font=(FONT, 14, "bold"), bg=blue1, fg=blue2)
password_label.grid(row=4, column=0)

password_entry = Entry(screen, font=(FONT, 14, "bold"), fg=blue3, textvariable=password_input,width=10)
password_entry.grid(row=4, column=1)

gen_pass_button = Button(screen, text="generate password", font=(FONT, 10, "bold"), bg=yellow, fg=blue2,width=20, command=generate_password)
gen_pass_button.grid(row=4, column=2)

submit_button = Button(screen, text="submit", font=(FONT, 10, "bold"), bg=yellow, fg=blue2, width=30, command=submit)
submit_button.grid(row=5, column=1, pady=20)

response_label = Label(screen, text="", font=("Consolas", 10, "bold"), bg=blue1, fg="darkred")
response_label.grid(row=6, column=1)


screen.mainloop()