from tkinter import *
from tkinter import messagebox
import mysql.connector
import re

# -------- Database Connection --------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cur = mydb.cursor(buffered=True)

# Create database if not exists
cur.execute("CREATE DATABASE IF NOT EXISTS caddcenter")
cur.execute("USE caddcenter")

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS person(
    Name VARCHAR(50),
    Id INT,
    Email VARCHAR(50),
    Password VARCHAR(50)
)
""")

# -------- GUI Window --------
root = Tk()
root.title('Form')
root.geometry('400x420')

# -------- Functions --------
def clear_form():
    enter.delete(0, END)
    ente1.delete(0, END)
    enter2.delete(0, END)
    enter3.delete(0, END)

def validate():
    name = enter.get().strip()
    idd = ente1.get().strip()
    email = enter2.get().strip()
    password = enter3.get().strip()

    # Empty check
    if name=="" or idd=="" or email=="" or password=="":
        messagebox.showerror("Error","All fields are required")
        return False

    # ID must be number
    if not idd.isdigit():
        messagebox.showerror("Error","ID must be numeric")
        return False

    # Email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern,email):
        messagebox.showerror("Error","Invalid Email")
        return False

    return True

def submit():
    if not validate():
        return

    try:
        cur.execute(
            "INSERT INTO person(Name,Id,Email,Password) VALUES(%s,%s,%s,%s)",
            (enter.get(), ente1.get(), enter2.get(), enter3.get())
        )
        mydb.commit()
        messagebox.showinfo("Success","Data Saved Successfully")
        clear_form()

    except Exception as e:
        messagebox.showerror("Database Error",str(e))

# -------- Heading --------
Label(root, text='FORM', fg='red', font=('Arial',20,'bold')).grid(row=0,column=1,pady=15)

# Name
Label(root, text="Name", font=('Arial',12)).grid(row=1,column=0,padx=10,pady=5)
enter = Entry(root,width=30)
enter.grid(row=1,column=1)

# ID
Label(root, text="ID", font=('Arial',12)).grid(row=2,column=0,padx=10,pady=5)
ente1 = Entry(root,width=30)
ente1.grid(row=2,column=1)

# Email
Label(root, text="Email", font=('Arial',12)).grid(row=3,column=0,padx=10,pady=5)
enter2 = Entry(root,width=30)
enter2.grid(row=3,column=1)

# Password
Label(root, text="Password", font=('Arial',12)).grid(row=4,column=0,padx=10,pady=5)
enter3 = Entry(root,width=30,show="*")
enter3.grid(row=4,column=1)

# Buttons
Button(root,text="Submit",bg="blue",fg="white",width=12,command=submit).grid(row=5,column=1,pady=15)
Button(root,text="Clear",bg="gray",fg="white",width=12,command=clear_form).grid(row=6,column=1)

root.mainloop()