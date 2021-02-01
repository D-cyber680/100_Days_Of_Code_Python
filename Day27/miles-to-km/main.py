from tkinter import *
def converter():
    miles = float(input.get())
    km = miles * 1.609
    ans.config(text = km)
    return 0

window = Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)
window.config(padx = 10, pady = 20)
equal_to = Label(text='is equal to', font=("Arial", 10))
equal_to.grid(column=0, row=1)
input = Entry(width=10)
input.grid(column=1, row=0)
ans = Label(text='0', font=("Arial", 10))
ans.grid(column=1, row=1)
button = Button(text="Calculate", font=('Arial', 10),command = converter)
button.grid(column=1, row=2)
km = Label(text='km', font=("Arial", 10))
km.grid(column=2, row=1)
miles = Label(text='miles', font=("Arial", 10))
miles.grid(column=2, row=0)





window.mainloop()
