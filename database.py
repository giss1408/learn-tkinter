from os import lseek
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Learn to Code at Codemy.com")
root.geometry("400x600")

conn = sqlite3.connect('address_book.db')
# Create a cursor
c = conn.cursor()

#Create table
'''
c.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)
""")
'''

# Create Function To Delete A Record
def delete():
    # Create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    #Delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())
    delete_box.delete(0, END)





    #Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Create Submit Function For Database
def submit():
    # Database
    # Create or connect to a database
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': Zipcode.get()
        }
    )

    #Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    Zipcode.delete(0, END)


def query():
    # Create or connect to a database

    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    
    # Loop through results
    print_records = ' '
    for record in records:
        print_records += str(record[0]) + " " + str(record[1] + " \t\t" + str(record[6]))+ "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    #Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Create edit function to update a record
def edit():
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry("400x600")

    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()
    c.execute("SELE")
    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    Zipcode_editor = Entry(editor, width=30)
    Zipcode_editor.grid(row=5, column=1, padx=20)

    # Create Text Box Label
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_name_label = Label(editor, text="Address")
    address_name_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    Zipcode_label = Label(editor, text="Zipcode")
    Zipcode_label.grid(row=5, column=0)

    edit_btn = Button(editor, text="Save Record", command=edit)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=136)


# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
Zipcode = Entry(root, width=30)
Zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, padx=20, pady=5)

# Create Text Box Label
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_name_label = Label(root, text="Address")
address_name_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
Zipcode_label = Label(root, text="Zipcode")
Zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database",command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Record", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=134)

# Create an Update BUtton
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=141)

#Commit
conn.commit()

# Close connection
conn.close()

#button_exit = Button(root, text="Exit Program", command=root.quit)
#button_exit.pack()
root.mainloop()