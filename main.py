import csv
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
new_data = []
learn_data = {}
question = {}


# -----------------------TURN CARD ---------------#

# Wait for 3secs
def turn_card():
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=f"{question['English']}")
    canvas.itemconfig(card, image=back_img)

# ----------------------CHANGE QUESTION ---------#


# press the button
# random question


def change_question():
    global question, timer
    windows.after_cancel(timer)
    question = random.choice(new_data)
    canvas.itemconfig(card, image=canvas_image)
    canvas.itemconfig(word, text=f"{question['French']}")
    canvas.itemconfig(title, text="French")
    timer = windows.after(3000, func=turn_card)
# ------------------------LOAD PROGRESS ----------#


try:
    file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    file = pandas.read_csv("data/french_words.csv")
finally:
    data = pandas.DataFrame(file)
    new_data = data.to_dict(orient="records")


def remember():
    new_data.remove(question)
    update_data = pandas.DataFrame(new_data)
    update_data.to_csv("data/words_to_learn.csv", index=False)
    change_question()


# -------------------------UI SETUP---------------#


windows = Tk()
windows.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=canvas_image)
canvas.grid(column=0, row=0, columnspan=2)
back_img = PhotoImage(file="images/card_back.png")
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, command=remember)
right_btn.grid(column=1, row=1)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, command=change_question)
wrong_btn.grid(column=0, row=1)
timer = windows.after(3000, func=turn_card)

change_question()

windows.mainloop()
