from tkinter import *
import pandas as pd
import random
import time

#                   ---------------------- READING CSV -------------------------
df = pd.read_csv ('data/french_words.csv')
dict_words = df.to_dict("records")

random_number = random.randint(0,100)
words_known =[]

def flip_card(canvas,id_language,id_word):
    time.sleep(1)
    canvas.itemconfigure(id_language, text = 'English',fill = 'white')
    canvas.configure(bg = "#B1DDC6")
    canvas.itemconfigure(id_word, text = dict_words[random_number]["English"],fill= "white")


def new_random_word(id_word,id_language,canvas):
    global random_number
    if canvas.itemcget(id_word,'text') != "Word":
        words_known.append(canvas.itemcget(id_word,'text'))
        dict_words.remove(dict_words[random_number])
    random_number = random.randint(0, 100)
    word_chosen = dict_words[random_number]["French"]
    canvas.itemconfigure(id_word,text = word_chosen,fil = 'black')
    canvas.itemconfigure(id_language,text = "French",fill = 'black')
    canvas.configure(bg = "white")

BACKGROUND_COLOR = "#B1DDC6"

#                    ------------------------ UI SETUP --------------------------
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50,bg = BACKGROUND_COLOR)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

 
canvas = Canvas(window,height = 400, width = 566,bg = 'white',cursor = "question_arrow",relief = "flat")

id_display= canvas.create_rectangle(200,200,200,200,fill = "red")
id_language = canvas.create_text(270,100,text = "Title",font = ("Arial", 40,"italic"))
id_word = canvas.create_text(270,230,text = "Word",font = ("Arial", 60,"bold"))
canvas.grid(row=0,column=0, columnspan=2)

button_wrong = Button(image=wrong_image, highlightthickness=0, bd = 0,command = lambda : flip_card(canvas,id_language,id_word))
button_right = Button(image=right_image, highlightthickness=0, bd = 0, command = lambda : new_random_word(id_word,id_language,canvas))

button_wrong.grid(row = 1, column = 0,pady = 50)
button_right.grid(row = 1, column = 1, pady = 50)

window.mainloop()



