from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("DrugPred-NN")
root.iconbitmap("icon.ico")
root.geometry("600x400")

frame1 = LabelFrame(root, text="Step-1", padx=50, pady=50)
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = LabelFrame(root, text="Step-2", padx=50, pady=50)
frame2.grid(row=0, column=1, padx=10, pady=10)

frame3 = LabelFrame(root, text="Step-3", padx=50, pady=50)
frame3.grid(row=1, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

def show():
    mRna = Label(frame1, text=var1.get()).grid(row=2, column=0)
    meth = Label(frame1, text=var2.get()).grid(row=2, column=1)
    cnva = Label(frame1, text=var3.get()).grid(row=2, column=2)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

#var = StringVar()
#c = Checkbutton(root, text= "mRNA", variable=var).pack()
#c1 = Checkbutton(root, text= "mRNA", variable=var1, onvalue="On", offvalue="Off").grid(row=1, column=0)
c1 = Checkbutton(frame1, text= "mRNA", variable=var1).grid(row=1, column=0)
c2 = Checkbutton(frame1, text= "Meth", variable=var2).grid(row=1, column=1)
c3 = Checkbutton(frame1, text= "cnva", variable=var3).grid(row=1, column=2)

myButton1 = Button(frame1, text="Show Selection", command=show).grid(row=3, column=0, columnspan=3)

b1 = Checkbutton(frame2, text= "mRNA", variable=var1).grid(row=1, column=0)
b2 = Checkbutton(frame2, text= "Meth", variable=var2).grid(row=1, column=1)
b3 = Checkbutton(frame2, text= "cnva", variable=var3).grid(row=1, column=2)

myButton2 = Button(frame2, text="Show Selection").grid(row=3, column=0, columnspan=3)

root.mainloop()