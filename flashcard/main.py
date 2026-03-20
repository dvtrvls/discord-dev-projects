from tkinter import *
import pandas as pd

screen = Tk()
screen.config(padx=50,pady=50, bg="#7FB77E")
words = pd.read_csv("words.csv")

window_width, window_height = 900, 700
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
screen.geometry(f"{window_width}x{window_height}+{x}+{y}")

known_words = []

try:
    with open("known_words.txt", "r") as file:
        known_words = file.readlines()
except FileNotFoundError:
    with open("known_words.txt", "w") as file:
        pass
known_words = [word.strip() for word in known_words]
print(known_words)

time = 0
is_front = True
index = 0

def flipping_logic():
    global is_front, index, time
    time += 1
    if index >= len(words):
        index = 0    
    
    if is_front and time == 3:
        flip_back()
        time = 0
        index += 1
        is_front = False
    elif not is_front and time == 3:
        flip_front()
        time = 0
        is_front = True
        
    screen.after(1000, flipping_logic)

def flip_back():
    canvas.itemconfig(dyk_text, text="Answer")
    canvas.itemconfig(card, image=back_image)
    canvas.itemconfig(title_text, text="Tagalog")
    canvas.itemconfig(word_text, text=f"{words.iloc[index]["Tagalog"]}") 

def flip_front():
 
    canvas.itemconfig(card, image=front_image)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=f"{words.iloc[index]["English"]}")
    if words.iloc[index]["English"] in known_words:
        canvas.itemconfig(dyk_text, text="You already know this word!")
        canvas.itemconfig(dyk_text, fill="#F7C85C")
    else:
        canvas.itemconfig(dyk_text, text="Do you know this word in Tagalog?")
        canvas.itemconfig(dyk_text, fill="white")

def check_word():

    global index, is_front, time
    current_word = f"{words.iloc[index]["English"]}"

    if current_word not in known_words:
        with open("known_words.txt", "a") as file:
            file.write(f"{current_word}\n")
    index += 1
    flip_front()
    is_front = True
    time = 0

def exis_word():
    global is_front, index, time
    if is_front:
        flip_back()
        is_front = False
        time = 0
        index += 1

front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
check_image = PhotoImage(file="./images/right.png")
exis_image = PhotoImage(file="./images/wrong.png")

canvas = Canvas(screen, height=526, width=800, bg="#7FB77E", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card = canvas.create_image(400, 263, image=front_image)


dyk_text = canvas.create_text(400, 80, text="Do you know this word in Tagalog?", font=("Courier", 25, "bold"))
title_text =  canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text=f"{words.iloc[index]["English"]}", font=("Ariel", 60, "bold"))
flip_front()                         
check_button =  Button(screen, image=check_image, command=check_word)
check_button.grid(row=1, column=0, pady=10)

exis_button =  Button(screen, image=exis_image, command=exis_word)
exis_button.grid(row=1, column=1, pady=10)

flipping_logic()
screen.mainloop()