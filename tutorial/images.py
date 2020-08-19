from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("ICON")
root.iconbitmap("icon.ico")

my_img = ImageTk.PhotoImage(Image.open("pic.jpeg"))
my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

button_quit = Button(root, text="End program!", command=root.quit)
button_quit.grid(row=1, column=1)

root.mainloop()