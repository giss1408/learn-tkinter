from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn to Code at Codemy.com")

def popup():
    response = messagebox.askokcancel("This is my popup", "Hello world!")
    if response == 1:
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked No").pack()

Button(root, text="Popup", command=popup).pack()

button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()
root.mainloop()