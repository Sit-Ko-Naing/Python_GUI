#Book International Flight Tickets Instanly by Hsu Wati Tun

from datetime import date
import tkinter as tk

small_font= ('Arial', 19)
def buttonFunction():
  
    Result= int(calculateAge_entry.get())
    if Result<2:
        print("Payment for Infant is free.")
    elif Result<=10:
        print("Payment for Child is $50.")
    elif Result<=18:
        print("Payment for Teenager is $100.")
    else:
        print("Payment for Adult is $200.")

                                                                                                                        
from tkinter import Button, Label, PhotoImage, Tk, ttk

window = tk.Tk()
window.title("Book International Flight Tickets Instanly")
window.geometry = ("500x600")

frame = tk.Frame(window)
frame.pack()

user_info_frame= tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0)

Leaving_from_label = tk.Label(user_info_frame, text= "Flying From", font="Arial")
Leaving_from_combobox= ttk.Combobox (user_info_frame, values = ["Singapore","Malasia", "London", "USA", "Hungary","Myanmar", "France", "Russia"])
Leaving_from_label.grid(row=4, column=0)
Leaving_from_combobox.grid(row=5,column=0)

Going_to_label = tk.Label(user_info_frame, text="Flying to")
Going_to_combobox= ttk.Combobox (user_info_frame, values= ["Thailand", "Spain", "Italy", "UK", "Netherlands"])
Going_to_label.grid(row=4, column=3)
Going_to_combobox.grid(row=5, column=3)

Number_of_passanger= tk.Label(user_info_frame, text="Number of Passangers")
Number_of_passanger_spinbox= tk.Spinbox(user_info_frame, from_=1, to=12)
Number_of_passanger.grid(row=7, column=0)
Number_of_passanger_spinbox.grid(row=8, column=0)

tk.Label(user_info_frame, text="Gender").grid(row=7,column=3)
gender_var= tk.StringVar()
gender_menu= ttk.Combobox(user_info_frame, textvariable= gender_var, values= ["Male", "Female", "Other"])
gender_menu.grid(row=8, column=3)

calculateAge= tk.Label(user_info_frame, text="Enter your Age")
calculateAge_entry= tk.Entry(user_info_frame)
calculateAge.grid(row=9, column=2)
calculateAge_entry.grid(row=10, column=2)


calculate_button= tk.Button(user_info_frame, text="Calculate", command= buttonFunction)
calculate_button.grid(row=11, columnspan=4)

display_label= tk.Label(user_info_frame, text="")
display_label.grid(row=12, column=2)

Email= tk.Label(user_info_frame, text="Email", font="Arial")
Email_entry=tk.Entry (user_info_frame)
Email.grid(row=13, column=0)
Email_entry.grid(row=13, column=2)

Phone_Number_1= tk.Label(user_info_frame, text="Phone Number")
Phone_Number_2= tk.Entry (user_info_frame)
Phone_Number_1.grid(row=14, column=0)
Phone_Number_2.grid(row=14, column=2)

Travel_Class= tk.Label(user_info_frame, text="Travel Class")
Travel_Class_combobox= ttk.Combobox(user_info_frame, values=["Economy", "Premium Economy", "Business", "First Class"])
Travel_Class.grid(row=15, column=0)
Travel_Class_combobox.grid(row=15, column=2)

b2=tk.Button(user_info_frame, bg="orange", text="Search & Book", height=3)
b2.grid(row=16, column=3)
for widget in window.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()