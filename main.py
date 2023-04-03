from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}
to_learn = {}

#-------------------READING DATA FILE---------------------#

try:
    data =pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    
#--------------------------Next CARD---------------------------#
def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card, image = card_front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text = current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)
#----------------------------STORE KNOWN CARDS-------------------#
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()
#----------------------------FLIP CARD------------------------#
def flip_card():
    canvas.itemconfig(card, image= card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text = current_card["English"], fill="white")
    
#--------------------------------UI--------------------------------#
window = Tk()
window.title("Flah Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
#Card
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card =canvas.create_image(400 , 268, image=card_front_img)
canvas.grid(column=1,row=0, columnspan=2, padx=15, pady=15)
#Title Text
title =canvas.create_text(400, 150, text="", font=TITLE_FONT)
#Word Text
word = canvas.create_text(400, 263, text="", font = WORD_FONT)
#Wrong Button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card,highlightthickness=0)
wrong_button.grid(column=1, row=1)
#Right Button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, command=is_known,highlightthickness=0)
right_button.grid(column=2, row=1)
next_card()
window.mainloop()
#========================================#