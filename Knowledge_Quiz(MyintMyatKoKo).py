#Knowledge Quiz By Myint Myat Ko KO

from tkinter import *

question = {
	"Who invented the light bulb?": ['Albert Einstien', 'Thomas Edison', 'Adolf Hitler', 'Alexander Grahambell', 'Barack Obama', 'Abraham Lincoln'],
	"How fast is Mach 1?": ['343 m/s', '380 m/s', '300000 km/s' , 'Infinite', '10 m/s', '20 m/s'],
	"What is the gravitational constant? ": ['1.52 m/s^2', '9.81 m/s^2', '9.88 m/s^2', '7.91 m/s^2', '10.882 m/s^2', 'Undefined'],
    "How big is the universe? ": ['Undefined', '100000000 light years', '1x10^10 light years', 'Infinite', 'Limited but Undefined', '1 trillion light years'],
    "Who discovered gravity?" : ['Issac Newton', 'Albert Einstein', 'Max Planck', 'Steven Hawkins', 'Elon Musk', 'Mark Zukerberg'],
    "What is Theory of Relativity about?" : ['Space-Time', 'Life', 'Relatives', 'Forests', 'Oceans', 'Earth'],
    "Where is Myanmar?" : ['South-East Asia', 'North-East Asia', 'Middle East', 'Middle West', 'North China Sea', 'Western Europe'],
    "Which year did the Nazi gain power?" : ['1942', '1945', '1933', '1934', '1905', '1947'],
    "Where was Adolf Hitler born? " : ['Austria', 'Australia', 'Germany', 'Bulgaria', 'Argentina', 'Belgium'],
    "How much quarters are in a dollar?" : ['4', '2', '6', '5', '10', '8'],
    "If Billy has 14 sweets and gave 6 to his friend, how much does he have lefft? ": ['6', '7', '8', '9', '10', '11'],
    "If you run at 20 m/s, how much distance have you gone in 1 hour?" : ['8200 m', '72294 m', '72000 m', '20 m', '2000 m', '5230 m'],
    "If your v = 11 m/s and there's no air resistance, how far can you possibly reach without including stamina?" : ['Infinite', 'As possible as you can', 'Undefined', '20000 m', '1000000 m', 'Finite'],
    "What is the so-called 'universal speed limit'?" : ['The Speed of Light(c)', 'The Speed of Sound', 'The Speed of Earth', 'The Speed of Galaxy', 'The Speed of Human', 'The Speed of Sun'],
    "If you have a mass of 20 kg, how much do you weigh on Earth?" : ['20 kg', '70 kg', '30 kg', '110 kg', '150 kg', '196 kg'],
    "What is the 31st Element on the periodic table?" : ['Gallium(Ga)', 'Hydrogen(H)', 'Arsenic(As)', 'Flourine(F)', 'Yttrium(Y)', 'Titanuim(Ti)'],
    "If 7x + 23 = 98, find the value of x." : ['x = 10.71', 'x = 10.89', 'x = 9.01', 'x = 98', 'x = 102', 'x = 120'],
    "What is the value of y if 291 + 72y = 91?" : ['y = -2.78', 'y = 2.78', 'y = 98.2', 'y = 7.2', 'y = -8.3', 'y = -901'],
    "What type of mass does a 'Tachyon' have?" : ['Negative Mass', 'Normal Mass', 'Irregular Mass', 'Regular Mass', 'Massless', 'Infinite Mass'],
    "How many electrons are there in a Yttrium atomic structure?" : ['12', '13', '18', '30', '39', '50'],
    "What is the long form of 'UV Light'?" : ['United Vein Light', 'Ultra Vision Light', 'Ultra Violet Light', 'Ultra Velcro Light', 'Ugenda Vanatic Light', 'Ultra Vanish Light'],
    "What is the largest animal on Earth?" : ['Whale', 'Blue Whale', 'Great White Shark', 'African Elephant', 'Cheetah', 'Lion'],
    "What is the rarest item in the whole universe?" : ['Diamond', 'Emerald', 'Ruby', 'Jade', 'Wood', 'Iron'],
    "What is the 27th Element on the periodic table?" : ['Copper(Cu)', 'Neon(Ne)', 'Zinc(Zn)', 'Gallium(Ga)', 'Iron(Fe)', 'Cobalt(Co)'],
    "If a ball with a mass of 20 kg were to hit a wall at v = 10 m/s, how much energy does it create?" : ['2000 J', '5000 J', '1000 J', 'Not Enough Information', '20000 J', '3200 J'],
    "What is the temperature for absolute zero?" :['270°C', '-270°C', '180°C', '90°C', '10°C', '-973°C']
}
ans = ['Thomas Edison', '343 m/s', '9.81 m/s^2', 'Undefined', 'Issac Newton', 'Space-Time', 'South-East Asia', '1933', 'Austria', '4', '8', '72000 m', 'As possible as you can', 'The Speed of Light(c)', '196 kg', 'Gallium(Ga)', 'x = 10.71', 'y = -2.78', 'Negative Mass', '39', 'Ultra Violet Light', 'Blue Whale', 'Wood', 'Cobalt(Co)', '1000 J', '-270°C']

current_question = 0


def start_quiz():
	start_button.forget()
	next_button.pack()
	next_question()


def next_question():
	global current_question
	if current_question < len(question):
		check_ans()
		user_ans.set('None')
		c_question = list(question.keys())[current_question]
		clear_frame()
		Label(f1, text=f"Question : {c_question}", padx=15,
			font="calibre 12 normal").pack(anchor=NW)
		for option in question[c_question]:
			Radiobutton(f1, text=option, variable=user_ans,
						value=option, padx=28).pack(anchor=NW)
		current_question += 1
	else:
		next_button.forget()
		check_ans()
		clear_frame()
		output = f"Your Score is {user_score.get()} out of {len(question)}."
		Label(f1, text=output, font="calibre 25 bold").pack()
		Label(f1, text="Congrats on your marks! Thank You For Orbiting This Quiz!",
			font="calibre 18 bold").pack()


def check_ans():
	temp_ans = user_ans.get()
	if temp_ans != 'None' and temp_ans == ans[current_question-1]:
		user_score.set(user_score.get()+1)


def clear_frame():
	for widget in f1.winfo_children():
		widget.destroy()


if __name__ == "__main__":
	root = Tk()
	root.title("Knowledge Quiz(One Go for One Question Each Round)")
	root.geometry("850x520")
	root.minsize(800, 400)

	user_ans = StringVar()
	user_ans.set('None')
	user_score = IntVar()
	user_score.set(0)

	Label(root, text="ALL KNOWLEDGE!", 
		font="calibre 40 bold",
		relief=SUNKEN, background="red", 
		padx=10, pady=9).pack()
	Label(root, text="", font="calibre 10 bold").pack()
	start_button = Button(root, 
						text="Accelerate!",
						command=start_quiz, 
						font="calibre 17 bold")
	start_button.pack()

	f1 = Frame(root)
	f1.pack(side=TOP, fill=X)

	next_button = Button(root, text="Next Velocity!",
						command=next_question, 
						font="calibre 17 bold")

	root.mainloop()