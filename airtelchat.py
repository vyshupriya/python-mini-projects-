from tkinter import *
from tkinter import messagebox
# GUI
root = Tk()
root.title("Chatbot")

print("")

BG_GRAY = "#5f9ea0"
BG_COLOR = "#b6d2d3"
TEXT_COLOR = "#100c08"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

txt=['END']


def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()


    if (user == "network-related issues"):

     txt.insert(END, "\n" + "AIRTEL -> help us identify your issue from the options below","\n1. internet issue","\n2. issue with call","\n3. 5G queries","\n4. international roaming")


    else:
        txt.insert(END, "\n" + "AIRTEL -> Sorry! I didn't understand that")

        e.delete(0, END)

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="airtel chat!", font=FONT_BOLD, pady=10, width=20,height=1).grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,command=send).grid(row=2, column=1)

root.mainloop()
