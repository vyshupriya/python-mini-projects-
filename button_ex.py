from tkinter import *

root = Tk()
root.title('My option')
root.geometry('500x300')

choice = None


def choice1():
    global choice
    choice = 'Choice 1'


def choice2():
    global choice
    choice = 'Choice 2'


def start():
    global choice


if choice == 'Choice 1':
    choice1 = "foo1()"
elif choice == 'Choice 2':
    choice2 = "foo2()"
else:
    choice = "none"

button = Button(root, text='Choice 1', command=choice1)
button.pack()
button2 = Button(root, text='Choice 2', command=choice2)
button.pack()
Start_Button = Button(root, text='Start', command=start)
button.pack()


root.mainloop()