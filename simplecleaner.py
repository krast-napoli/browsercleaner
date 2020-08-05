import os
from tkinter import *

root = Tk()

e = Entry(width=20)
b = Button (text="Change")
l = Label(bg='black', fg='white', width=20)

username = os.getlogin()

path1 = r"C:\Users"
path2 = r"AppData\Local\Google\Chrome\User Data\Default\History"
chromepath = path1 + '\\' + '\\' + path2

def clean_history(event):
    os.remove (chromepath)


b.bind('<Button-1>', clean_history)

e.pack()
b.pack()
l.pack()
root.mainloop()



