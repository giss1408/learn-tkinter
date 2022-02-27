from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

# Create a Buttonwidget
myButton = Button(root, text="Click Me!", command=myClick, fg="red").pack()

root.mainloop()