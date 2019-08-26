from tkinter import *

win = Tk()

win.geometry("100x100")
win.title("BIND")

def a(event):
    print("Yogesh is Nalla")

    
    
    
    

button = Button(win,text="Click Me")
button.bind("<Button-1>",a)
button.pack()









win.mainloop()
