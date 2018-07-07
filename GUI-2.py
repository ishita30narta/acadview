#1
from tkinter import *
import  tkinter as tk
#r=tk.Tk()
root = tk.Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y)

DICT = {'Ishita':123,'Nitika':345,'prachi':456,'abc':789,'asd':7654,'fgh':6543,'aaa':7654,'ggg':543,'hhh':876,'yyy':987,'xxx':765,'ade':9865}
mylist =Listbox(root, yscrollcommand = scrollbar.set )
for i in DICT:
    mylist.insert(END,i,DICT[i])
mylist.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = mylist.yview)

#2
def insert():
   DICT['radh']=67
   print(DICT)

button =tk.Button(root,text='Insertion',command=insert)
button.pack()
root.mainloop()