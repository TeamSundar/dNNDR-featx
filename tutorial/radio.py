from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("RADIO")
root.iconbitmap("icon.ico")

r = IntVar()
r.set("1")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value).pack()

# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get()).pack()
myButton = Button(root, text="Click me!", command=lambda: clicked(pizza.get())).pack()

root.mainloop()