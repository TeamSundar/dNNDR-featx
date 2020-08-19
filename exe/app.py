#!E:\Projects\DrugTargetNN python
# -*- coding: utf-8 -*-
# Program to extract protein and drug target features from IDs

from tkinter import *
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox
from functions import process
#from functions_mlc import process_mlc
from tqdm import tqdm
from tkinter import ttk
import time
import os

# Initialize window
root = Tk()
root.title("DrugPred-NN")
root.iconbitmap("icon.ico")
#root.configure(bg='#FFFFFF')
#root.geometry("400x475")

# Initialize object
obj=process()

# Initialize frames
frame1 = LabelFrame(root, text="Step 1: Import file", padx=20, pady=20)
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

frame2 = LabelFrame(root, text="Step 2: Feature Extraction", padx=20, pady=20)
frame2.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

frame4 = LabelFrame(root, text="Outpul panel", padx=20, pady=20)
frame4.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")


# Function to allow user to choose an input file
def open():
    frame1.filename = filedialog.askopenfilename(
        initialdir="E:/side_projects/GUI_tkinter/",
        title="Select a protein-target file",
        filetypes=(("txt files", "*.txt"),("All files", "*.*"))
    )

    in_path.set(frame1.filename)
    e_in1.insert(0, in_path.get())
    display()
    #Import data 
    return None

# def myClick():
#     hello = "Hello " + e.get()
#     myLabel = Label(root, text = hello)
#     myLabel.pack()

def display():
    file = obj.import_data(in_path.get())
    #my_label = Label(frame1, text=frame1.filename).grid(row=1, column=1, padx=10, pady=10)
    Label(frame4, text="\nNumber of proteins found: " + str(len(file.geneID.unique()))).pack()
    Label(frame4, text="Number of drugs found: " + str(len(file.drugID.unique()))).pack()
    return None

# Function to execute extraction based on the user input
def clicked(value):
    #pass
    cwd = os.getcwd()
    directory='output'
    out_path = os.path.join(cwd, directory) 
    os.mkdir(out_path)

    file = obj.import_data(in_path.get()) 
    fset=pd.DataFrame()
    protein_list=file.geneID.unique()

    # Drug Descriptors
    if value=="All":
        opt = ["AAC", "CKSAAP", "QSOrder", "KSCTriad", "CTriad"]
        k=0
        for typ in tqdm(opt):
            for id in tqdm(protein_list):
                obj.id2seq(id)
                obj.seq2des('dummy.txt', typ)
                enc=pd.read_csv('encoding.tsv', delimiter='\t', encoding='utf-8')
                enc['#']=id
                fset=fset.append(enc)
                progress_var.set(k)
                k += 1
                time.sleep(0.02)
                root.update_idletasks()
            fset.to_csv(out_path +'/fset_prot_'+ typ + '.csv')
    else:
        k=0
        for id in tqdm(protein_list):
            obj.id2seq(id)
            obj.seq2des('dummy.txt', value)
            enc=pd.read_csv('encoding.tsv', delimiter='\t', encoding='utf-8')
            enc['#']=id
            fset=fset.append(enc)
            progress_var.set(k)
            k += 1
            time.sleep(0.02)
            root.update_idletasks()

        fset.to_csv(out_path +'/fset_prot'+ value + '.csv')
    
    #messagebox.showinfo("File saved", "Output file for " + str(value) + " protein feature set saved at " + str(in_path.get()))
    #Label(root, text=response).pack()

    Label(frame4, text=value).pack()
    Label(frame4, textvariable=in_path).pack()

    response = messagebox.askyesno("Extract drug features", "Protein features extracted! Do you want to extract drug features too. It might take a while.")
    if response==1:   
        Label(frame4, text='Downloading mol files').pack()   
        directory = 'output/drug_mol'
        mol_path = os.path.join(cwd, directory) 
        os.mkdir(mol_path)

        drug_list = file.drugID.unique()
        for drug in tqdm(drug_list):
            obj.id2mol(drug, mol_path)
        
        Label(frame4, text='Extracting drug features').pack()
        files=os.listdir(mol_path)
        fset_mol=pd.DataFrame()
        for mol in tqdm(files):
            descriptors=obj.mol2des(mol_path+'/'+mol)
            fset_mol=fset_mol.append(descriptors)

        fset_mol.to_csv(out_path+'/fset_mol.csv')

    my_btn3["state"] = "active"

def new_window():
    #obj_mlc=process_mlc()
    # Variables to store selection
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()

    #Show selected features to process
    def process_features():
        sel = [var1.get(),var2.get(),var3.get(),var4.get(),var5.get()]
        types = ["AAC", "CKSAAP", "QSOrder", "KSCTriad", "CTriad"]
        x_processed=pd.DataFrame()
        for i in range(len(sel)):
            if sel[i]==1:
                x=pd.read_csv('output/fset_prot'+ types[i] +'.csv')
                x=x.drop(['Unnamed: 0'], axis=1)
                try:
                    x=x.drop(['Descriptor calculation failed.'], axis=1)
                except:
                    pass
                x.index=x['#'].values
                x=x.drop(['#'], axis=1)
                try:
                    x= x.drop(['hsa:390956', 'hsa:94009'])
                    print("Empty Dropped for: ", types[i])
                except:
                    print("Nothing Dropped for: ", types[i]) 
            else:
                pass
            x_processed = pd.concat([x, x_processed], axis=1, join='inner')
        
        Label(frame3_n, text="Features processed!").pack()

    top = Toplevel()
    top.title("Neural Network")
    top.iconbitmap("icon.ico")

    # Initialize frames for new window
    frame1_n = LabelFrame(top, text="Step 1: Feature Processing", padx=20, pady=20)
    frame1_n.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    frame2_n = LabelFrame(top, text="Step 2: Feature Extraction", padx=20, pady=20)
    frame2_n.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

    frame3_n = LabelFrame(top, text="Step 2: Output panel", padx=20, pady=20)
    frame3_n.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

    # Choose features to be processed
    Label(frame1_n, text="Choose the features you wish to be model").grid(row=0, column=0,columnspan=3, padx=10, pady=10)
    #"AAC", "CKSAAP", "QSOrder", "KSCTriad", "CTriad"

    c1 = Checkbutton(frame1_n, text= "AAC", variable=var1)
    c1.grid(row=1, column=0, sticky=W)
    c2 = Checkbutton(frame1_n, text= "CKSAAP", variable=var2)
    c2.grid(row=1, column=1, sticky=W)
    c3 = Checkbutton(frame1_n, text= "QSOrder", variable=var3)
    c3.grid(row=1, column=2, sticky=W)
    c4 = Checkbutton(frame1_n, text= "KSCTriad", variable=var4)
    c4.grid(row=2, column=0, sticky=W)
    c5 = Checkbutton(frame1_n, text= "CTriad", variable=var5)
    c5.grid(row=2, column=1, sticky=W)  

    Button(frame1_n, text="Process features", command=process_features).grid(row=6, column=0,columnspan=3, padx=10, pady=10) 

    Label(frame2_n, text="Hello World").grid(row=0, column=0, padx=10, pady=10) 
    Button(frame2_n, text="Close window!", command=top.destroy).grid(row=0, column=1, padx=10, pady=10) 

    MAX=100
    progress_var = DoubleVar()
    theLabel = Label(frame3_n, text="Progress Bar")
    theLabel.pack()
    progressbar = ttk.Progressbar(frame3_n, variable=progress_var, maximum=MAX, length=200)
    progressbar.pack()

# VAriable to store user selected file path
in_path = StringVar()

# Path to user input
lbl_in1 = Label(frame1, text="Input file path")
lbl_in1.grid(row=0, column=1, pady=5)

e_in1 = Entry(frame1, width=40)
e_in1.grid(row=1, column=0, columnspan=3, pady=5)
e_in1.focus_set()

btn_input = Button(frame1, text="Select file", command=open)
btn_input.grid(row=2, column=1, pady=5)

# Variable that stores the selection
feature = StringVar()
# Set default value
feature.set("AAC")
Label(frame2, text= "Select a protein feature to be retrieved \n").grid(row=0, column=0, columnspan=3)

Radiobutton(frame2, text='All', variable=feature, value='All').grid(row=1, column=0,sticky=W)
Radiobutton(frame2, text='AAC', variable=feature, value='AAC').grid(row=1, column=1,sticky=W)
Radiobutton(frame2, text='CKSAAP', variable=feature, value='CKSAAP').grid(row=1, column=2,sticky=W)
Radiobutton(frame2, text='QSOrder', variable=feature, value='QSOrder').grid(row=2, column=0,sticky=W)
Radiobutton(frame2, text='CTriad', variable=feature, value='CTriad').grid(row=2, column=1,sticky=W)
Radiobutton(frame2, text='KSCTriad', variable=feature, value='KSCTriad').grid(row=2, column=2, sticky=W)

# Extract feature label/button-Protein
btn_startex_p = Button(frame2, text="Start extraction", width=35, command=lambda: clicked(feature.get()))
btn_startex_p.grid(row=3, column=0, columnspan=3, pady=5)

# Label/button to new window
my_btn3 = Button(frame2, text="Proceed to model training", command=new_window, width=35)
my_btn3.grid(row=5, column=0, columnspan=3, pady=5)
my_btn3["state"] = "disabled"

MAX=100
progress_var = DoubleVar()
theLabel = Label(frame4, text="Progress Bar")
theLabel.pack()
progressbar = ttk.Progressbar(frame4, variable=progress_var, maximum=MAX, length=200)
progressbar.pack()



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
#     enzyme = Label(frame1, text=in_path.get()).grid(row=2, column=0)
#     gpcr = Label(frame1, text=var2.get()).grid(row=2, column=1)
#     ionchannel = Label(frame1, text=var3.get()).grid(row=2, column=2)
#     nr = Label(frame1, text=var4.get()).grid(row=2, column=3)


# # Tkinter cvariable storing the status of the checkbox
# in_path = StringVar()
# var2 = StringVar()
# var3 = StringVar()
# var4 = StringVar()

# # Create radio buttons
# c1 = Checkbutton(frame1, text= "Enzyme", variable=in_path)
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

# frame4 = LabelFrame(root, text="Step-3", padx=50, pady=50)
# frame4.grid(row=1, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# def show():
#     mRna = Label(frame1, text=in_path.get()).grid(row=2, column=0)
#     meth = Label(frame1, text=var2.get()).grid(row=2, column=1)
#     cnva = Label(frame1, text=var3.get()).grid(row=2, column=2)

# in_path = IntVar()
# var2 = IntVar()
# var3 = IntVar()

#var = StringVar()
#c = Checkbutton(root, text= "mRNA", variable=var).pack()
#c1 = Checkbutton(root, text= "mRNA", variable=in_path, onvalue="On", offvalue="Off").grid(row=1, column=0)
# c1 = Checkbutton(frame1, text= "mRNA", variable=in_path).grid(row=1, column=0)
# c2 = Checkbutton(frame1, text= "Meth", variable=var2).grid(row=1, column=1)
# c3 = Checkbutton(frame1, text= "cnva", variable=var3).grid(row=1, column=2)

# myButton1 = Button(frame1, text="Show Selection", command=show).grid(row=3, column=0, columnspan=3)

root.mainloop()