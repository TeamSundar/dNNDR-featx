from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("ICON")
root.iconbitmap("icon.ico")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is a popup", "Hello world")
    Label(root, text=response).pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()