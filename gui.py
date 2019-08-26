from tkinter import *
win = Tk()
win.title("FORM")
win.geometry("200x200")
Name = Label(win,text="Name")
topframe = Frame(win)
topframe.pack()
rightframe = Frame(win)
rightframe.pack()
leftframe = Frame(win)
leftframe.pack()
bottomframe = Frame(win)
bottomframe.pack()
glabel = Label(win,text="Apple",fg="red",bg="black")
glabel.pack(fill=X)

hlabel = Label(win,text="Boy",fg="orange",bg="black")
hlabel.pack(side=LEFT,fill=Y)
jlabel = Label(win,text="Cat",fg="pink",bg="black")
jlabel.pack(side=RIGHT,fill=Y)
klabel = Label(win,text="Dog",fg="blue",bg="black")
klabel.pack(side=BOTTOM,fill=X)

name = Label(win,text="Name:")
name.pack()
entry1= Entry(win)
entry1.pack()

email = Label(win,text="Eamil:")
email.pack()
entry2= Entry(win)
entry2.pack()

password = Label(win,text="Password:")
password.pack()
entry3= Entry(win)
entry3.pack()







button1 = Button(bottomframe,text="A",fg="orange",bg="black")
button2 = Button(bottomframe,text="B",fg="yellow",bg="black")
button3 = Button(bottomframe,text="C",fg="blue",bg="black")
button4 = Button(bottomframe,text="D",fg="red",bg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)









win.mainloop()
