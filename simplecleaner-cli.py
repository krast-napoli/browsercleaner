import os

username = os.getlogin()

path1 = r"C:\Users"
path2 = r"AppData\Local\Google\Chrome\User Data\Default\History"
chromepath = path1 + '\\' + username + '\\' + path2

os.remove (chromepath)