from tkinter import *
from tkinter import filedialog


win = Tk()

win.title("PyCharm")

win.geometry("300x300")

def msg():
    print("Working")

def resize():
    win.geometry("400x400")

def default():
    win.geometry("300x300")

def browsefunc():
    filename = filedialog.askopenfilename(filetypes =
                                          (("File(*.py)", "*.py"), ("All files(*.*)", "*.*")))

    pathlabel.config(text=filename)
  
menu = Menu(win)

win.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "New File", command = msg)
filemenu.add_command(label = "open", command = browsefunc)
filemenu.add_command(label = "open module", command = msg)
filemenu.add_command(label = "Recent Open", command = msg)
filemenu.add_command(label = "Resize", command = resize)
filemenu.add_command(label = "Default", command = default)
filemenu.add_command(label = "Exit", command = quit)



editmenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Undo", command = msg)
editmenu.add_command(label = "Redo", command = msg)
editmenu.add_command(label = "Cut", command = msg)
editmenu.add_command(label = "Copy", command = msg)

formatmenu = Menu(menu)
menu.add_cascade(label = "Format", menu = formatmenu)
formatmenu.add_command(label = "Indent Region,", command = msg)

runmenu = Menu(menu)
menu.add_cascade(label = "Run", menu = runmenu)
runmenu.add_command(label = "Python Shell", command = msg)
runmenu.add_command(label = "Check Module", command = msg)
runmenu.add_command(label = "Run Module", command = msg)

pathlabel = Label(win)
pathlabel.pack()


win.mainloop()
