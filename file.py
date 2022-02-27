from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Learn to Code at Codemy.com")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/home/regis/Rdev/python/tkinter/images", title="Select a File", filetypes=(("png files","*png"),("All files","*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage( Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open file", command=open).pack()
#my_btn.pack()
button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()
root.mainloop()