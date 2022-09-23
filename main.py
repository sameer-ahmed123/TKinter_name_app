from tkinter import *
import os

root = Tk()
root.title("my app 1")
root.geometry("700x400")

def hello_user():
    hello_lable = Label(root, text="hello " + myTextbox.get())
    hello_lable.pack()



mylable = Label(root, text="your name")
mylable.pack()

myTextbox = Entry(root, width=60)
myTextbox.pack()


button =Button(root,text="click ", command=hello_user)
button.pack()


root.mainloop()