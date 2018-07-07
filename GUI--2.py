'''import tkinter as tk
from tkinter import *
kav = tk.Tk()
kav.title("info")
dict={'name':'megha','mobile_number':217895}
scrollbar=Scrollbar(kav)
scrollbar.pack(side=LEFT,fill=Y)
mylist=Listbox(kav,yscrollcommand = scrollbar.set)
for key in dict. __iter__():
         mylist.insert(END,key)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
def kavy():
    kav.quit()
b=Button(kav,text="enter",command=kavy)
b.pack()
kav.mainloop()'''

my_dict = {'Ishita':1234, 'Nitika': 2345, 'Prachi':3456, 'Shivangi':4567}

# update value
#my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)
