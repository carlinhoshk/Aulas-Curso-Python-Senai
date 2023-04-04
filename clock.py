from tkinter import *
import tkinter
import pyglet

from datetime import datetime
pyglet.font.add_file('digital-7.ttf')

# defina as cores
cor2 = "#00FF00"
cor1 = "#000000"

root=Tk()
root.title("RELOGIO-CLOCK")
root.geometry('340x200')
root.resizable(width=FALSE, height=FALSE)
root.configure(background=cor1)
root.iconbitmap('zap.ico')

def clock():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")
    l1.config(text=hour)
    l1.after(200, clock)

    l2.config(text=weekday + "" +str(day) + "/" +str(month) + "/" + (year))
    
l1=Label(root, font=('digital-7 80'), bg=cor1, fg=cor2)
l1.grid(row=0, column=0, sticky=NW)

l2=Label(root, font=('digital-7 20'), bg=cor1, fg=cor2)
l2.grid(row=1, column=0, sticky=NW)

clock()
root.mainloop()