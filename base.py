from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn to Code at Codemy.com")


button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()
root.mainloop()