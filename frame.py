from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")



frame = LabelFrame(root, text="This is my Frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Dont click here").pack()


frame2 = LabelFrame(root, text="This is my Frame2...", padx=5, pady=5)
frame2.pack(padx=10, pady=10)
b = Button(frame2, text="Dont click here").pack()

button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()
root.mainloop()