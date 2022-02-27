from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")
root.geometry("400x400")

var = IntVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue=5, offvalue=6)
c.pack()



def show():
    myLabel = Label(root, text=var.get()).pack()

myButton = Button(root, text="Show Selection", command=show).pack()
button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()
root.mainloop()