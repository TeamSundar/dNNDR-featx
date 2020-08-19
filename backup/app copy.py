#!E:\Projects\DrugTargetNN python
# -*- coding: utf-8 -*-
# Program to extract protein and drug target features from IDs

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from functions import process

# Initialize window
root = Tk()
root.title("DrugPred-NN")
root.iconbitmap("icon.ico")
#root.geometry("400x475")

# Import functions
obj=process()

frame1 = LabelFrame(root, text="Import file", padx=20, pady=20)
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

frame2 = LabelFrame(root, text="DAta retrieval", padx=20, pady=20)
frame2.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

frame3 = LabelFrame(root, text="Outpul panel", padx=20, pady=20)
frame3.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

global file

def open():
    frame1.filename = filedialog.askopenfilename(initialdir="E:/side_projects/GUI_tkinter/", title="Select a protein-target file", filetypes=(("txt files", "*.txt"),("All files", "*.*")))
    var1.set(frame1.filename)
    #Import data 
    file = obj.import_data(frame1.filename)
    #my_label = Label(frame1, text=frame1.filename).grid(row=1, column=1, padx=10, pady=10)
    Label(frame3, text="Import Done! ").pack()
    Label(frame3, text="Number of proteins found: " + str(len(file.geneID.unique()))).pack()
    Label(frame3, text="Number of drugs found: " + str(len(file.drugID.unique()))).pack()
    return file

# def start():
#     my_label = Label(frame3, textvariable=var1).pack()
#     return None

def clicked(value):
    Label(frame3, textvariable=var1).pack()

var1 = StringVar()

lbl1 = Label(frame1, text="Select file to be processed")
lbl1.grid(row=0, column=0, padx=10, pady=10)
my_btn1 = Button(frame1, text="Select file", command=open)
my_btn1.grid(row=0, column=1, padx=10, pady=10)

features = [
	("AAC", "AAC"),
	("CKSAAP", "CKSAAP"),
	("QSOrder", "QSOrder"),
	("KSCTriad", "KSCTriad"),
    ("CTriad", "CTriad"),
    ("All", "All")
]

feature = StringVar()
feature.set("All")

Label(frame2, text= "Select the feature to be retrieved \n").grid(row=0, column=0, columnspan=2)

for a, b in features:
    Radiobutton(frame2, text=a, variable=feature, value=b).grid(column=0, columnspan=2)

lbl2 = Label(frame2, text="Retrieve protein/drug features")
lbl2.grid(row=8, column=0, padx=10, pady=10)
my_btn2 = Button(frame2, text="Click Me!", command=lambda: clicked(feature.get()))
my_btn2.grid(row=8, column=1, padx=10, pady=10)



#out_lbl = Label(frame2, textvariable="Out").grid(row=0, column=0, padx=10, pady=10)
#out_btn = Button(frame2, text="Get Time", command=callback).grid()












# proteins = [
# 	("enzyme", "enzyme"),
# 	("gpcr", "gpcr"),
# 	("ionchannel", "ionchannel"),
# 	("nr", "nr"),
# ]

# protein = StringVar()
# protein.set("enzyme")

# for protein, kind in proteins:
#     	Radiobutton(frame1, text=protein, variable=protein, value=kind).pack(anchor=W)

# def clicked(value):
#     	myLabel = Label(frame1, text=value)
# 	myLabel.pack()	

# myButton = Button(frame1, text="Click Me!", command=lambda: clicked(protein.get()))


# def show():
#     enzyme = Label(frame1, text=var1.get()).grid(row=2, column=0)
#     gpcr = Label(frame1, text=var2.get()).grid(row=2, column=1)
#     ionchannel = Label(frame1, text=var3.get()).grid(row=2, column=2)
#     nr = Label(frame1, text=var4.get()).grid(row=2, column=3)


# # Tkinter cvariable storing the status of the checkbox
# var1 = StringVar()
# var2 = StringVar()
# var3 = StringVar()
# var4 = StringVar()

# # Create radio buttons
# c1 = Checkbutton(frame1, text= "Enzyme", variable=var1)
# c1.deselect()
# c1.grid(row=1, column=0)

# c2 = Checkbutton(frame1, text= "GPCR", variable=var2)
# c2.deselect()
# c2.grid(row=1, column=1)

# c3 = Checkbutton(frame1, text= "Ion-Channel", variable=var3)
# c3.deselect()
# c3.grid(row=1, column=2)

# c4 = Checkbutton(frame1, text= "Nuclear receptor", variable=var4)
# c4.deselect()
# c4.grid(row=1, column=3)

# myButton1 = Button(frame1, text="Show Selection", command=show).grid(row=3, column=0, columnspan=3)


# frame2 = LabelFrame(root, text="Step-2", padx=50, pady=50)
# frame2.grid(row=0, column=1, padx=10, pady=10)

# frame3 = LabelFrame(root, text="Step-3", padx=50, pady=50)
# frame3.grid(row=1, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# def show():
#     mRna = Label(frame1, text=var1.get()).grid(row=2, column=0)
#     meth = Label(frame1, text=var2.get()).grid(row=2, column=1)
#     cnva = Label(frame1, text=var3.get()).grid(row=2, column=2)

# var1 = IntVar()
# var2 = IntVar()
# var3 = IntVar()

#var = StringVar()
#c = Checkbutton(root, text= "mRNA", variable=var).pack()
#c1 = Checkbutton(root, text= "mRNA", variable=var1, onvalue="On", offvalue="Off").grid(row=1, column=0)
# c1 = Checkbutton(frame1, text= "mRNA", variable=var1).grid(row=1, column=0)
# c2 = Checkbutton(frame1, text= "Meth", variable=var2).grid(row=1, column=1)
# c3 = Checkbutton(frame1, text= "cnva", variable=var3).grid(row=1, column=2)

# myButton1 = Button(frame1, text="Show Selection", command=show).grid(row=3, column=0, columnspan=3)

root.mainloop()