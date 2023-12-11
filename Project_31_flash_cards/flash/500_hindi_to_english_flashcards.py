import random
from tkinter import *

# TODO : -----------------------------importing data from csv---------------------------------------------
import pandas
data = pandas.read_csv("../data/top_500_hindi_words.csv")
words_list = data.to_dict(orient="records")

choice = {}
def random_card():
    global choice, card_timer
    window.after_cancel(card_timer)
    choice = random.choice(words_list)
    canvas.itemconfig(lang, text="Hindi", fill="black")
    canvas.itemconfig(word, text=choice["Hindi"], fill="black")
    canvas.itemconfig(card_background, image=image_fg)
    card_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=choice["English"], fill="white")
    canvas.itemconfig(card_background, image=image_bg)

def is_known():
    words_list.remove(choice)
    random_card()


# TODO : ----------------------------------SETUP - UI-----------------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

card_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_bg = PhotoImage(file="../images/card_back.png")
image_fg = PhotoImage(file="../images/card_front.png")
card_background = canvas.create_image(400, 263, image=image_fg)
lang = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

random_card()

# buttons
wrong_img = PhotoImage(file="../images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, borderwidth=0, command=random_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="../images/right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)

window.mainloop()
