from tkinter import *
win =Tk()
win.title("FORM")
win.geometry("200x200")

def a():
    print("\n")

class Class:
    def __init__(self,win):


table = StringVar()

name = Label(win,text="Name:")

email = Label(win,text="Email:")

password = Label(win,text="Password:")

button = Button(win,text="Submit",command=a)

button1 = Button(win,text="Quit", command=win.destroy)

check = Checkbutton(win,text="Keep Me Logged In")

name.grid(row=0)

email.grid(row=1)

password.grid(row=2)

button.grid(rowspan=1)
button1.grid(row=3,column=1)
check.grid(columnspan=2)



entry1 = Entry(win,bg="pink", text = table)
entry2 = Entry(win, text = table)
entry3 = Entry(win, text =  table)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)



win.mainloop()
