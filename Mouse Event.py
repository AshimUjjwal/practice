from tkinter import *

win = Tk()

win.title( "Mouse Event")
win.geometry("200x200")

def left(event):
    print("\t\t Left Click")

def middle(event):
    print("\t\t Middle Click")

def right(event):
    print("\t\t Right Click")

frame = Frame(win, width = 200, height = 200)
frame.bind("<Button - 1>",left)
frame.bind("<Button - 2>",middle)
frame.bind("<Button - 3>",right)
frame.pack()

win.mainloop()
