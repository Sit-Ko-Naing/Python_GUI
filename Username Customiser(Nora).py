#Username Customiser by Nora

from tkinter import *
window = Tk()
window.title("Username customiser")
window.geometry('400x300')
window.config(bg='#9EB6F7')
option0 = ("Happy","Sad","Handsome","Pretty","Hungry","Funny","Goofy","Carefree","Confident","Elegant","Mighty","N/A")
option1 = ("Red","Orange","Yellow","Green","Blue","Purple","Pink","Black","Grey","White","Rainbow","N/A")
option2 = ("Panda","Zebra","Bunny","Cat","Unicorn","Eagle","Dolphin","Dog","Koala","Penguin","Butterfly","N/A")
option3 = ("2","4","6","8","10","12","14","16","18","20","N/A")
menu0 = IntVar()
menu0.set("Pick an adjective: ")
menu1 = IntVar()
menu1.set("pick a colour: ")
menu2 = IntVar()
menu2.set("pick an animal: ")
menu3 = IntVar()
menu3.set("pick an even number: ")
my_dropdown0 = OptionMenu(window, menu0, *option0)
my_dropdown0.grid(row=0, column=1, padx=10, pady=10)
my_dropdown1 = OptionMenu(window, menu1, *option1)
my_dropdown1.grid(row=0, column=2, padx=10, pady=10)
my_dropdown2 = OptionMenu(window, menu2, *option2)
my_dropdown2.grid(row=0, column=3, padx=10, pady=10)
my_dropdown3 = OptionMenu(window, menu3, *option3)
my_dropdown3.grid(row=0, column=4, padx=10, pady=10)

lbl = Label(window, text="Click if your done -->")
lbl.grid(column=2, row=1)
def clicked():
    lbl.configure(text="You've gotten your brand new username above !!")
btn = Button(window, text="Click Me !", command=clicked, bg='#FEEDB8')
btn.grid(column=3, row=1)
window.mainloop()
