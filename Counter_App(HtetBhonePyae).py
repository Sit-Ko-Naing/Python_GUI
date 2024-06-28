#Counter_App_by_Htet_Bhone_Pyae

import tkinter as tk

root = tk.Tk()
root.title("Counter App")

root.geometry("400x400")

counter = 0

label = tk.Label(root, text=f"Counter: {counter}", font=("Helvetica", 16))
label.pack(pady=20)

easter_egg_label = tk.Label(root, text="", fg="red", font=("Helvetica", 14))
easter_egg_label.pack(pady=20)

def update_counter():
    global counter
    counter += 1
    label.config(text=f"Counter: {counter}")
    
    if counter == 10:
        easter_egg_label.config(text="You reached 10 clicks!")
    elif counter == 25:
        easter_egg_label.config(text="25 clicks! Keep going!")
        root.config(bg="lightblue")
    elif counter == 50:
        easter_egg_label.config(text="Wow! 50 clicks!")
        root.config(bg="lightgreen")
    elif counter == 75:
        easter_egg_label.config(text="75 clicks! Almost there!")
        button.config(text="Almost There!")
    elif counter == 100:
        easter_egg_label.config(text="100 clicks! You're amazing!")
        root.config(bg="yellow")
    elif counter == 150:
        easter_egg_label.config(text="150 clicks! You're unstoppable!")
        root.config(bg="orange")
        button.config(state="normal")
    elif counter == 200:
        easter_egg_label.config(text="200 clicks! What a journey!")
        root.config(bg="purple")
        button.config(text="Keep Going!")
    elif counter == 250:
        easter_egg_label.config(text="250 clicks! You're a legend!")
        root.config(bg="pink")
    elif counter == 300:
        easter_egg_label.config(text="300 clicks! You're out of this world!")
        root.config(bg="cyan")
        button.config(text="Unstoppable!")
    else:
        easter_egg_label.config(text="")
        root.config(bg="SystemButtonFace")
        button.config(text="Increment")

button = tk.Button(root, text="Click Me", command=update_counter, font=("Helvetica", 14))
button.pack(pady=20)

root.mainloop()
