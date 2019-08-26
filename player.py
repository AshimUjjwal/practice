from tkinter import *
from pygame import mixer
win=Tk()
win.title('Music Player')
win.geometry('300x300')
a='pause'

def play():
    mixer.init()
    mixer.music.load('1.mp3')
    mixer.music.play()
def pause():
   
    global a
    if a=='pause':
        
        mixer.music.pause()
        a='unpause'
    
    else:
        
        mixer.music.unpause()
        a='pause'
def stop():
    mixer.music.stop()
def resize():
    win.geometry('400x400')

def default():
    win.geometry('300x300')
    
button=Button(win,text='Play',command=play,bg='red',bd='10',fg='pink')
button.pack()
button1=Button(win,text='Pause',command=pause,bg='blue',bd='10',fg='orange')
button1.pack()
button2=Button(win,text='Stop',command=stop,bg='blue',bd='10',fg='orange')
button2.pack()
button3=Button(win,text='Resize',command=resize,bg='violet',bd='10',fg='yellow')
button3.pack()
button4=Button(win,text='Default',command=default,bg='yellow',bd='10',fg='red')
button4.pack()
win.mainloop()
