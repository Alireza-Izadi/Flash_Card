from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
french_word = ""
#-------------------READING DATA FILE---------------------#
file =pandas.read_csv("./data/french_words.csv")
french_dict = {row["French"]:row["English"] for index, row in file.iterrows()}
french_words = [key for key in french_dict.keys()]
#---------------------RANDOM WORD------------------------#
def random_word():
    global french_word
    french_word =random.choice(french_words)
    return  french_word
#--------------------------Next CARD---------------------------#
def next_card():
    global flip_timer
    window.after_cancel(flip_timer)
    random_word()
    canvas.itemconfig(card, image = card_front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text = f"{french_word}", fill="black")
    flip_timer = window.after(3000, flip_card)
#----------------------------FLIP CARD------------------------#
def flip_card():
    canvas.itemconfig(card, image= card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text = f"{french_dict[french_word]}", fill="white")
    
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
title =canvas.create_text(400, 150, text="French", font=TITLE_FONT)
#Word Text
word = canvas.create_text(400, 263, text=f"{random_word()}", font = WORD_FONT)
#Wrong Button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card,highlightthickness=0)
wrong_button.grid(column=1, row=1)
#Right Button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, command=next_card,highlightthickness=0)
right_button.grid(column=2, row=1)
next_card()
window.mainloop()
#========================================#