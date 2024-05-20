from tkinter import *
from tkinter import messagebox
from tkinter import Tk
root=Tk()
root.title=("ABC")
root.geometry('500x500')

clicked1 = StringVar()


options1 = [
    "1",
    "2",
    "3"

]

def num(select):
    clik = clicked1.get()
    if clik == "1":
        messagebox.showinfo("Message", "its A.")
    elif clik =="2":
         messagebox.showinfo("Message", "its B.")
    if clik=="3":
        messagebox.showinfo("Message", "its C.")






lable = Label(root, text = "abc").place(x=20,y=50)
drop = OptionMenu(root, clicked1, *options1,command=num).place(x=70, y=50)





root.mainloop()