#1
import  tkinter as tk
from tkinter import *
r = tk.Tk()
Label(r,text ="HELLO WORLD").grid(row =0)
def exit():
          sys.exit()

button =tk.Button(r,text ="Exit",width=25,command = exit).grid(row =1)
r.mainloop()

#2
import tkinter as tk
from tkinter import *
r = tk.Tk()
r.title('Display Text')
def Hello():
    Label(r, text="Hi..!! whatsup..").grid(row=0)
button = tk.Button(r,text='Magic',width=25, command=Hello).grid(row =1)
r.mainloop()

#3
import  tkinter as tk
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM)

Label(frame,text ="HELLO WORLD").grid(row =0)
def exit():
          sys.exit()

redbutton =tk.Button(frame,text ="Exit",fg='red',command = exit).grid(row =1)



def Hello():
    Label(frame, text="Hi..!! whatsup..").grid(row=0)
brownbutton = tk.Button(frame,text='Change',fg='brown', command=Hello).grid(row =3)

root.mainloop()


#4
from tkinter import *
import tkinter as tk

master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def Print():
    Label(master, text=(e1.get()+e2.get())).grid(row=4)


button = tk.Button(master,text='Magic',width=25, command=Print).grid(row =3)

mainloop()

