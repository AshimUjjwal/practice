from tkinter import *

win = Tk()

win.title("Class")

win.geometry("200x100")


def print_Msg():
     print("It's working")
       
            
class Class:
    def __init__(self,win):
        frame = Frame(win)
        frame.pack()

        self.button = Button(frame, text = "Click Me", command =print_Msg)
        self.button.pack()

        self.button1 = Button(frame, text = "Quit", command = quit)
        self.button1.pack()


b = Class(win)


win.mainloop()
