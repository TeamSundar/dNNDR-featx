from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3

root = Tk()
root.title("ICON")
root.iconbitmap("icon.ico")
root.geometry("400x400")

# # Create table
# conn = sqlite3.connect("add_profiles.db")
# c = conn.cursor()
# c.execute("""CREATE TABLE addresses (
#         first_name text, 
#         last_name text,
#         addres text,
#         city text,
#         stat text,
#         zipcode integer
#         )""")

# conn.commit()
# conn.close()

# Create submit function
def submit():
	# Create a database or connect to one
    conn = sqlite3.connect('add_profiles.db')

	# Create cursor
    c = conn.cursor()
	# Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :addres, :city, :stat, :zipcode)",
		{
			'f_name': f_name.get(),
			'l_name': l_name.get(),
			'addres': address.get(),
			'city': city.get(),
			'stat': state.get(),
			'zipcode': zipcode.get()
		})

	#Commit Changes
    conn.commit()

	# Close Connection 
    conn.close()

    # Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    conn = sqlite3.connect('add_profiles.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create text box labels
f_name_label = Label(root, text = "First name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text = "Last name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text = "Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text = "City")
city_label.grid(row=3, column=0)
state_label = Label(root, text = "State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row=5, column=0)

# Create submit buttons
submit_button = Button(root, text="Add record to DataBase", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Show data button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

root.mainloop()