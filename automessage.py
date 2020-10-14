# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:13:27 2020

@author: new
"""

from tkinter import *
import pywhatkit 
root= Tk()
root.geometry("400x400")
canvas1 = Frame(root, width = 300, height = 300)
canvas1.pack()

Label(root, text='Ph number with country code:').place(x=50,y=80,height=50,width=290)
entry1 = Entry(root)
entry1.place(x=150,y=120,height=20,width=100)

Label(root, text='Enter the text:').place(x=50,y=140,height=50,width=290)
entry2 = Entry(root)
entry2.place(x=150,y=180,height=20,width=100)

Label(root, text='Schedule time (hours:minutes) in 24hr format').place(x=50,y=200,height=50,width=290)
entry3 = Entry(root)
entry3.place(x=170,y=240,height=20,width=20)
entry4 = Entry(root)
entry4.place(x=200,y=240,height=20,width=20)


def sendMessage():  
    x1 = entry1.get()    
    x2 = entry2.get()
    x3 = int(entry3.get())
    x4 = int(entry4.get())
    pywhatkit.sendwhatmsg(x1,x2,x3,x4)   
button1 = Button(text='Send', command=sendMessage)
button1.place(x=150, y=280, width=100, height=50)


root.mainloop()