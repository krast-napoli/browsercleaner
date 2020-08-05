import os
from tkinter import *

root = Tk()

b = Button (text="Clean history")
l = Label(bg='black', fg='white', width=30)

username = os.getlogin()

path1 = r"C:\Users"
path2 = r"AppData\Local\Google\Chrome\User Data\Default\History"
chromepath = path1 + '\\' + '\\' + path2

def clean_history(event):
    os.remove (chromepath)
    l.['text'] = 'Done!'


b.bind('<Button-1>', clean_history)

b.pack()
l.pack()
root.mainloop()



