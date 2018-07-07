#from tkinter import *

#top = Tk()
#mb = Menubutton (top, text = "Menu")
#mb.grid()
#mb.menu = Menu (mb, tearoff = 0 )                   #used to create a menu button
#mb['menu'] = mb.menu
#cVar = IntVar()
#aVar = IntVar()
#mb.menu.add_checkbutton (label ='Contact', variable = cVar)
#mb.menu.add_checkbutton (label ='About', variable =aVar)
#mb.pack()
#top.mainloop()


#from tkinter import *

#root = Tk()
#menu = Menu(root)
#root.config(menu=menu)
#filemenu = Menu(menu)
#menu.add_cascade(label='File', menu=filemenu)
#filemenu.add_command(label='New')
#filemenu.add_command(label='open...')
#filemenu.add_separator()
#filemenu.add_command(label='Exit', command=root.quit)
#helpmenu =Menu(menu)
#menu.add_cascade(label='Help', menu=helpmenu)
#helpmenu.add_command(label='About')
#mainloop()

#from tkinter import *
#main = Tk()
#ourMessage = 'This is our message'
#messageVar = Message(main, text = ourMessage)
#messageVar.config(bg='lightgreen')
#messageVar.pack()
#main.mainloop()

#import tkinter as tk
#root=tk.Tk()
#v = tk.IntVar()
#tk.Label(root,text="""Choose a programming languages:""").pack()
#tk.Radiobutton(root,text="Python",variable=v,value=1).pack(anchor=tk.W)
#tk.Radiobutton(root,text="Perl",variable=v,value=2).pack(anchor=tk.W)
#root.mainloop()

#from tkinter import *
#master = Tk()
#w = Scale(master, from_=0, to=42)
#w.pack()
#w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
#w.pack()
#mainloop()


#from tkinter import *
#root = Tk()
#scrollbar = Scrollbar(root)
#scrollbar.pack( side = RIGHT, fill = Y)
#mylist = Listbox(root, yscrollcommand = scrollbar.set )
#for line in range(100):
#   mylist.insert(END, 'This is line number' + str(line))
#mylist.pack( side = LEFT, fill = BOTH)
#scrollbar.config( command = mylist.yview )
#mainloop()


#from tkinter import *
#root = Tk()
#T = Text(root, height=2, width=30)
#T.pack()
#T.insert(END, "Just a text widget\nin two lines\n")
#mainloop()


#from tkinter import *
#root = Tk()
#root.title('Ruby')
#top = Toplevel()
#top.title('Python')
#top.mainloop()

#from tkinter import *
#master = Tk()
#w = Spinbox(master, from_=0, to=10)
#w.pack()
#mainloop()


'''from tkinter import *
m1 = PanedWindow()
m1.pack(fill = BOTH, expand = 1)
left = Entry(m1, bd=5)
m1.add(left)
m2 = PanedWindow(m1, orient = VERTICAL)
m1.add(m2)
top = Scale( m2, orient = HORIZONTAL)
m2.add(top)
mainloop()

from tkinter import *
from tkinter import messagebox

def show():
    messagebox.showwarning("title","desc")
root=Tk()
button = button(root)
button(root,command=show)'''

import operator
d = {}
count = 0
while count < 3:
      name = input("Enter your name: ")
      mark = input("Enter your mark out of 100: ")
      if name not in d:
          d[name] = mark
          count = count + 1

print(d)
print("\n")

