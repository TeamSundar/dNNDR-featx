from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("ICON")
root.iconbitmap("icon.ico")

def open():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("png files", "*.png"),("All files", "*.*")))
    my_label = Label(root, text=root.filename).pack()


my_btn = Button(root, text="Open file", command=open).pack()
root.mainloop()