from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")
root.geometry("400x400")

vertical = Scale(root, from_=0, to= 200)
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get() + 400) + "x" + str(vertical.get() + 200))

horizontal = Scale(root, from_=0, to= 200, orient=HORIZONTAL)
horizontal.pack()




my_btn = Button(root, text="Click Me!", command=slide).pack()

button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()
root.mainloop()