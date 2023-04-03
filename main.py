from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

#--------------------------------UI--------------------------------#
window = Tk()
window.title("Flah Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#Card
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400 , 268, image=card_front_img)
canvas.grid(column=1,row=0, columnspan=2, padx=15, pady=15)
#Title Text
canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
#Word Text
canvas.create_text(400, 263, text="Word", font = WORD_FONT)
#Wrong Button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=1, row=1)
#Right Button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=2, row=1)
window.mainloop()
#========================================#