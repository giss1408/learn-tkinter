from tkinter import *

root = Tk()

# Create a Label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name Is Regisse")
# Showing it into the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()