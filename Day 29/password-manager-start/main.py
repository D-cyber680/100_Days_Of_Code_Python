from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password(pass_text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_text.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_account(username,password,website):
    if password.get() == "" or website.get() == "" or username.get() == "":
        messagebox.showinfo("Oops","You should not leave any text fields empty")
    else:
        si_no = messagebox.askokcancel(title="User-data", message="Do you want to save that data in accounts.txt?")
        if si_no and (password.get() != "" and username.get() != "" and website.get() != ""):
            with open("accounts.txt", 'a', encoding='utf-8') as file:
                file.write(f"Website : {website.get()} | Username : {username.get()} | Password : {password.get()} |\n")
                website.delete(0, END)
                password.delete(0, END)
        else:
            website.delete(0, END)
            password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx = 50,pady = 50)
logo_img = PhotoImage(file = "logo.png")
logo_grid = Label(image = logo_img,padx = 30, pady =100)
logo_grid.grid(row = 0 , column = 1)
label_website = Label(text = "Website :")
label_website.grid(row = 1,column = 0)
label_username = Label(text = "Email/username : ")
label_username.grid(row = 2,column = 0)
label_username = Label(text = "Password : ")
label_username.grid(row = 3,column = 0)
name1 = StringVar()
name2 = StringVar()
name3 = StringVar()
website_textbox = Entry(window, width = 35, textvariable = name1)
website_textbox.focus()
website_textbox.grid(column = 1, row = 1,columnspan=2)
username_textbox = Entry(window, width = 35, textvariable = name2)
username_textbox.grid(column = 1, row = 2,columnspan=2)
username_textbox.insert(0,"danielsantosmendez@live.com")
password_textbox = Entry(window, width = 21, textvariable = name3)
password_textbox.grid(column = 1, row = 3)
generate_pass = Button(window, text ="Generate Password",command = lambda : generate_password(password_textbox))
generate_pass.grid(row = 3, column = 2)
add_btn = Button(window, text ="Add",width = 36,command = lambda : add_account(username_textbox,password_textbox,website_textbox))
add_btn.grid(row = 4, column = 1,columnspan=2)
window.mainloop()
