'''import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
def Hello():
    print("hello")
button = tk.Button(r,text='Stop',width=25, command=Hello)
button.pack()
r.mainloop()


import tkinter as tk


def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()'''

from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
window.mainloop()