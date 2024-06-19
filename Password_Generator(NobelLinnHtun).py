#Password Generator by Nobel Linn Htun

import tkinter as tk
from tkinter import font
from tkinter import *
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_gen():
    
    letter_amount = int(entry_letter.get())
    num_amount = int(entry_number.get())
    symbol_amount = int(entry_symbol.get())

    letter_list = []
    number_list = []
    symbol_list = []

    for i in range(0, letter_amount):
        letter = letters[random.randint(0, len(letters) - 1)]
        letter_list.append(letter)

    for i in range(0, num_amount):
        number = numbers[random.randint(0, len(numbers) - 1)]
        number_list.append(number)

    for i in range(0, symbol_amount):
        symbol = symbols[random.randint(0, len(symbols) - 1)] 
        symbol_list.append(symbol)

    password = letter_list + number_list + symbol_list
    random.shuffle(password)
    password_str = "".join(password)
    password_result.config(text = password_str)
    

window = tk.Tk()
window.title("Password Generator")
window.configure(bg = "light blue")
custom_font = font.Font(family="century", size= 13)

label_letter = tk.Label(window, text="Letter", font=custom_font, bg = "#F8DF7C")
label_letter.grid(row = 0 , column=0, padx = 10)
entry_letter = tk.Entry(window, bg = "grey")
entry_letter.grid(row= 0, column=1, pady = 20, padx = 20)

label_number = tk.Label(window, text= "Number", font=custom_font, bg = "#F8DF7C")
label_number.grid(row = 1, column = 0, padx = 10)
entry_number = tk.Entry(window, bg = "grey")
entry_number.grid(row= 1, column = 1, pady = 20, padx = 20 )

label_symbol = tk.Label(window, text = "Symbol", font = custom_font, bg = "#F8DF7C")
label_symbol.grid(row = 2, column = 0, padx = 10)
entry_symbol = tk.Entry(window, bg = "grey")
entry_symbol.grid(row = 2, column = 1, pady = 20, padx=20)

tk.Button(window, text = "Gen", font = custom_font, bg = "#B093F2" , command=password_gen).grid(row = 3,column = 0, pady = 20, padx = 20 )
password_result = tk.Label(window, text = "password", font = custom_font, bg = "#5DE2E7")
password_result.grid(row = 3, column = 1, pady = 20, padx = 20)


window.mainloop()
