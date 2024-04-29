from tkinter import *
from tkinter import font, messagebox
import string
import random

def minimize_window():
    window.state('iconic')

def maximize_window():
    if window.state() == 'normal':
        window.state('zoomed')
    else:
        window.state('normal')

def close_window():
    window.destroy()

def drag_window(event):
    x = window.winfo_pointerx() - event.widget.winfo_rootx()
    y = window.winfo_pointery() - event.widget.winfo_rooty()
    window.geometry(f"+{x}+{y}")

def generate_password():
    length = int(length_var.get())
    if length < 4:
        messagebox.showwarning("Warning", "Minimum length should be 4.")
        return

    password_characters = string.ascii_lowercase
    if var_upper.get():
        password_characters += string.ascii_uppercase
    if var_number.get():
        password_characters += string.digits
    if var_symbol.get():
        password_characters += string.punctuation

    password = ''.join(random.choice(password_characters) for i in range(length))
    password_var.set(password)

window = Tk()
window.geometry("400x250")
window.config(bg="#FFC0CB")  # Set overall background to grey
window.overrideredirect(True)

custom_font = font.Font(family="Helvetica", size=12, weight="bold")

title_bar = Frame(window, bg='#808080', relief='raised', bd=0)  # Grey background for the title bar
title_bar.pack(fill=X)

title_text = Label(title_bar, text="Password Generator", bg='#808080', fg='white', font=custom_font)
title_text.pack(side=LEFT, padx=10)

close_button = Button(title_bar, text='X', command=close_window, bg='red', fg='white', padx=10, pady=2, borderwidth=0)
close_button.pack(side=RIGHT)

minimize_button = Button(title_bar, text='-', command=minimize_window, bg='gray', fg='white', padx=10, pady=2, borderwidth=0)
minimize_button.pack(side=RIGHT)

maximize_button = Button(title_bar, text='□', command=maximize_window, bg='gray', fg='white', padx=10, pady=2, borderwidth=0)
maximize_button.pack(side=RIGHT)

title_bar.bind("<ButtonPress-1>", drag_window)
title_bar.bind("<B1-Motion>", drag_window)

frame_main = Frame(window, bg='#0096FF', padx=10, pady=10)  # Grey background for the main frame
frame_main.pack(expand=True, fill=BOTH)

length_var = StringVar(value="12")
password_var = StringVar()

Label(frame_main, text="Length:", font=("Arial", 12, "bold"), bg='#808080', fg='white').grid(row=0, column=0)
Entry(frame_main, textvariable=length_var, font=("Arial", 12, "normal")).grid(row=0, column=1, sticky='ew')

var_upper = BooleanVar(value=True)
Checkbutton(frame_main, text="Include Uppercase", variable=var_upper, bg='#808080', fg='white', selectcolor='#808080').grid(row=1, column=0, columnspan=2, sticky='w')

var_number = BooleanVar(value=True)
Checkbutton(frame_main, text="Include Numbers", variable=var_number, bg='#808080', fg='white', selectcolor='#808080').grid(row=2, column=0, columnspan=2, sticky='w')

var_symbol = BooleanVar(value=True)
Checkbutton(frame_main, text="Include Symbols", variable=var_symbol, bg='#808080', fg='white', selectcolor='#808080').grid(row=3, column=0, columnspan=2, sticky='w')

Button(frame_main, text="Generate Password", command=generate_password, bg='gray', fg='white').grid(row=4, column=0, columnspan=2, pady=5)
Entry(frame_main, textvariable=password_var, font=("Arial", 12, "bold"), state='readonly').grid(row=5, column=0, columnspan=2, sticky='ew', pady=5)

window.mainloop()
