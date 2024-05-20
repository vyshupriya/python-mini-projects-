from tkinter import *

calc_win = Tk()
# main window size
calc_win.geometry("320x426")
calc_win.resizable(0, 0) # resizing disabled
calc_win.title("Calculator")
# calculator icon image
calc_img_icon = PhotoImage(file=r'C:\Users\Admin\pythontkinter\images\icons8-calculator-48.png')
calc_win.iconphoto(False, calc_img_icon)

# set default value 0
def temp_text(e):
    calc_text_entry.delete(0,"end")

calc_input = StringVar()

# input text box
calc_text_frame = Frame(calc_win,width= 320,height=70,bd=0,highlightbackground='black')
calc_text_frame.pack(side=TOP)

calc_text_entry = Entry(calc_text_frame,font=('airal',24,'bold'),bg='#eee',textvariable=calc_input,width=70,bd=0,justify=RIGHT)
calc_text_entry.grid(row=0,column=0)
calc_text_entry.pack(ipady=50)
calc_text_entry.insert(0,"0")
calc_text_entry.bind("<FocusIn>",temp_text)

calc_win.mainloop()