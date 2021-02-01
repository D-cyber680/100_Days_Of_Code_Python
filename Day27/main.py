from tkinter import *

def button_clicked():
    my_label.config(text = "Button clicked")

window = Tk()
window.config(padx = 50, pady = 50)
window.title('My first gui program')
window.minsize(500, 300)

my_label = Label(text = 'I am a Label', font = ("Arial",24,"bold"))
my_label.config(text = "New text")
my_label.grid(column = 0 , row = 0)

button =Button(text = "Click Me", command = button_clicked)
button.grid(column = 1, row = 1)

button2 = Button(text = "NB")
button2.grid(column = 2, row = 0)
input = Entry(width = 10)
print(input.get())
input.grid(column = 3, row = 3)
window.mainloop()