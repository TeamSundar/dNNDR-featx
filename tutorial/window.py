from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ICON")
root.iconbitmap("icon.ico")

def open():
    top = Toplevel()
    top.title("ICON")
    top.iconbitmap("icon.ico")
    Label(top, text="Hello World").pack()
    Button(top, text="Close window!", command=top.destroy).pack()

btn = Button(root, text="Open second window!", command=open).pack()

root.mainloop()