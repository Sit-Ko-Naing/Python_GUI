#GUI Calculator by Phone Zaw Maung

import tkinter as tk
from tkinter import font



def addition():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    total = num1 + num2
   
    label_result.config(text=f"Total : {total}",bg='#add8e6')


def subtraction():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    total = num1 - num2

    label_result.config(text=f"Total : {total}",bg='#add8e6')


def multiply():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    total = num1 * num2

    label_result.config(text=f"Total : {total}",bg='#add8e6')


def divide():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    total = num1 / num2

    label_result.config(text=f"Total : {total}",bg='#add8e6')

    
def Power():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    total = num1 ** num2

    label_result.config(text=f"Total : {total}",bg='#add8e6')

root = tk.Tk()
root.title("Mini-Calculater")
root.configure(bg='#bbbbcc') 


root.columnconfigure(0, weight=1, pad=30)
root.columnconfigure(1, weight=1, pad=30)
root.rowconfigure(0, pad=20)
root.rowconfigure(1, pad=20)

first_num = tk.Entry(root, width=20, bg='#f0f8ff')
first_num.grid(row=0, column=1, padx=10, pady=10)

sec_num = tk.Entry(root, width=20, bg='#f0f8ff')
sec_num.grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Enter Num : ", bg='#ffaaff').grid(row=0, column=0, padx=10, pady=10)

tk.Button(root, text="+", bg='#87cefa', fg='black',
 command=addition).grid(row=1, column=0, padx=10, pady=10)

tk.Button(root, text="-",bg='#87cefa', fg='black',
 command=subtraction).grid(row=2, column=0, padx=10, pady=10)

tk.Button(root, text="*",bg="#87cefa", fg="black",
command=multiply).grid(row=1,column=1,padx=20,pady=20)



 

tk.Button(root, text="^",bg="#87cefa", fg="black",
command=Power).grid(row=2,column=2,padx=20,pady=20)


tk.Button(root, text="/",bg="#87cefa", fg="black",
command=divide).grid(row=2,column=1,padx=20,pady=20)


label_result = tk.Label(root, text="Result",  bg='#f0f8ff')
label_result.grid(row=1, column=2, pady=10)

root.mainloop()