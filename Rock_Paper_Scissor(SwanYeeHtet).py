#Rock_Paper_Scissor by Swan Yee Htet
from tkinter import *
import random 

# Dictionary
outcomes_2 = { 
    "Rock":{"Rock":1,"Paper":0,"Scissors":2},
    "Paper":{"Rock":2,"Paper":1,"Scissors":0},
    "Scissors":{"Rock":0,"Paper":2,"Scissors":1}
 }

comp_score = 0
player_score = 0


def reset():
   global comp_score 
   global player_score
   player_score_label.config(text="Player Score : 0")
   computer_score_label.config(text="Computer Score : 0")
   outcome_label.config(text="")
   challenge_label.config(text="")
   comp_score = 0
   player_score = 0


def chal():
   global comp_score
   global player_score
   my_chal = (menu.get())
   if my_chal == "5 wins":
      challenge_label.config(text="Win 5 times")
      
      if player_score == 5:
          challenge_label.config(text="")
          player_score_label.config(text="Player Score : 0")
          computer_score_label.config(text="Computer Score : 0") 
          comp_score = 0
          player_score = 0
          outcome_label.config(text="Congrats You won! :) ")
         
      elif comp_score == 5:
          challenge_label.config(text="")
          player_score_label.config(text="Player Score : 0")
          computer_score_label.config(text="Computer Score : 0") 
          comp_score = 0
          player_score = 0
          outcome_label.config(text="You lost :< ")
         
      
      else:
         window.after(100, chal)


   elif my_chal == "10 wins":
      challenge_label.config(text="Win 10 Times")

      if player_score == 10:
          challenge_label.config(text="")
          player_score_label.config(text="Player Score : 0")
          computer_score_label.config(text="Computer Score : 0") 
          comp_score = 0
          player_score = 0
          outcome_label.config(text="Congrats You won! :) ")
         
         
      elif comp_score == 10:
          challenge_label.config(text="")
          player_score_label.config(text="Player Score : 0")
          computer_score_label.config(text="Computer Score : 0") 
          comp_score = 0
          player_score = 0
          outcome_label.config(text="You lost :< ")

      else:
         window.after(100, chal)


   elif my_chal == "20 wins":
      challenge_label.config(text="Win 20 Times")

      if player_score == 20:
          challenge_label.config(text="You won the challenge!")
          player_score_label.config(text="Player Score : 0")
          computer_score_label.config(text="Computer Score : 0") 
          comp_score = 0
          player_score = 0
          outcome_label.config(text="Congrats You won! :) ")
          
         
      elif comp_score == 20:
          challenge_label.config(text="")
          player_score_label.config(text="Player Score : 0")
          computer_score_label.config(text="Computer Score : 0") 
          comp_score = 0
          player_score = 0
          outcome_label.config(text="You lost :< ")

      else:
         window.after(100, chal)

   
   else:
       pass
   

def quit():
    window.quit()

def outcome_handler(user_choice):
     global comp_score
     global player_score 
     outcomes = ["Rock","Paper","Scissors"]
     random_number = random.randint(0,2) 
     computer_choice = outcomes[random_number]
     result = outcomes_2[user_choice][computer_choice]
     
     player_choice_label.config(fg="blue",text="Player Choice : "+str(user_choice)) 
     computer_choice_label.config(fg="red",text="Computer Choice : "+str(computer_choice))
     
     if result == 2: 
        player_score = player_score + 1
        player_score_label.config(text="Player Score : "+str(player_score))
        outcome_label.config(fg="blue",text="Player Won") 
     elif result == 0:
         comp_score = comp_score + 1
         computer_score_label.config(text="Computer Score : "+str(comp_score)) 
         outcome_label.config(fg="blue",text="Computer Won") 
     elif result == 1: 
        player_score = player_score + 0
        comp_score = comp_score + 0 
        player_score_label.config(text="Player Score : "+str(player_score))
        computer_score_label.config(text="Computer Score : "+str(comp_score)) 
        outcome_label.config(fg="blue",text="Draw") 


window = Tk()
window.title("Rock_Paper_Scissors")

# Labels
Label(window,text="Rock_Paper_Scissors",font=("impact",16)).grid(row=0,sticky=N,pady=10,padx=200)
Label(window,text="Select an option",font=("impact",13)).grid(row=1,sticky=N)
player_score_label = Label(window,text="Player Score: 0",font=("impact",13))
player_score_label.grid(row=1,sticky=W,padx=10,pady=5)
computer_score_label = Label(window,text="Computer Score: 0",font=("impact",13))
computer_score_label.grid(row=1,sticky=E,padx=10,pady=5)
player_choice_label = Label(window,font=("impact",13))
player_choice_label.grid(row=3,sticky=W,padx=10,pady=5)
computer_choice_label = Label(window,font=("impact",13))
computer_choice_label.grid(row=3,sticky=E,padx=10,pady=5)
outcome_label = Label(window,font=("impact",13))
outcome_label.grid(row=3,sticky=N)
challenge_label = Label(window,font=("impact",13))
challenge_label.grid(row=5,sticky=N)


# Buttons
Button(window, text="Rock",font=("impact",13),width=18,command=lambda:outcome_handler("Rock")).grid(row=4,sticky=W,padx=50,pady=5)
Button(window, text="Paper",font=("impact",13),width=18,command=lambda:outcome_handler("Paper")).grid(row=4,sticky=N,padx=5,pady=5)
Button(window, text="Scissors",font=("impact",13),width=18,command=lambda:outcome_handler("Scissors")).grid(row=4,sticky=E,padx=50,pady=5)
Button(window, text="Quit",width=10,command=quit).grid(row=8,sticky=E,padx=10,pady=10)
Button(window, text="Reset",width=10,command=reset).grid(row=7,sticky=E,padx=10,pady=10)
Button(window, text="Set challenge",width=10,command=chal).grid(row=5,sticky=E,padx=10,pady=10)


option1 = ("5 wins","10 wins","20 wins")

menu = StringVar()
menu.set("Challange")

my_dropdown = OptionMenu(window ,menu,*option1)
my_dropdown.grid(row=6,sticky=E, padx=10, pady=10)

Label(window).grid(row=5)
Label(window).grid(row=6)
Label(window).grid(row=7)
Label(window).grid(row=8)

window.mainloop()



