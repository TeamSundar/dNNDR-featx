from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("ICON")
root.iconbitmap("icon.ico")
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack() #add pack sepereately

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack() #add pack sepereately

print(horizontal)

root.mainloop()