from tkinter import *

# define question dictionary
question = {
	"What is the output of the following code? str =pynative print (str[1:3])": ["py",'yn','pyn','yna'],
	" The in operator is used to check if a value exists within an iterable object container such as a list." 
	"Evaluate to True if it finds a variable in the specified sequence and False otherwise.": ['true','false'],
	"def calculate (num1, num2=4):;res = num1 * num2;print(res);calculate(5, 6)": ['20', '30', 'error', '7'],
	"for x in range(0.5, 5.5, 0.5):; print(x)":['(0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5)','(0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)', 'The Program executed with errors']
}
# define answer list
ans = ['pyn', 'true', 'error','The Program executed with errors']

current_question = 0


def start_quiz():
	start_button.forget()
	next_button.pack()
	next_question()


def next_question():
	global current_question
	if current_question < len(question):
		# get key or question that need to be printed
		check_ans()
		user_ans.set('None')
		c_question = list(question.keys())[current_question]
		# clear frame to update its content
		clear_frame()
		# printing question
		Label(f1, text=f"Question : {c_question}", padx=15,
			font="calibre 12 normal").pack(anchor=NW)
		# printing options
		for option in question[c_question]:
			Radiobutton(f1, text=option, variable=user_ans,
						value=option, padx=28).pack(anchor=NW)
		current_question += 1
	else:
		next_button.forget()
		check_ans()
		clear_frame()
		output = f"Your Score is {user_score.get()} out of {len(question)}"
		Label(f1, text=output, font="calibre 25 bold").pack()
		Label(f1, text="Thanks for Participating",
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
	# setup basic window
	root.title(" QUIZ APP")
	root.geometry("850x520")
	root.minsize(800, 400)

	user_ans = StringVar()
	user_ans.set('None')
	user_score = IntVar()
	user_score.set(0)

	Label(root, text="Quiz App", 
		font="calibre 40 bold",
		relief=SUNKEN, background="cyan", 
		padx=10, pady=9).pack()
	Label(root, text="", font="calibre 10 bold").pack()
	start_button = Button(root, 
						text="Start Quiz",
						command=start_quiz, 
						font="calibre 17 bold")
	start_button.pack()

	f1 = Frame(root)
	f1.pack(side=TOP, fill=X)

	next_button = Button(root, text="Next Question",
						command=next_question, 
						font="calibre 17 bold")

	root.mainloop()
