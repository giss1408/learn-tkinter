from cgitb import text
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")
root.geometry("400x400")

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def show():
    myLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(root, clicked, *options).pack()

myButton = Button(root, text="Show Selection", command=show).pack()
button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()
root.mainloop()