# from tkinter import*
# root=Tk()
# root.title("Application")
# root.geometry("500x500")
# root.mainloop()

############ library function
'''pack()
place()
grid()
      use pack()'''
# from tkinter import*
# root=Tk()
# root.title("Application")
# root.geometry("500x500")
# lbl=Label(root,text="cadd center",font=('Harlow Solid Italic',50))
# lbl.pack()
# # lbl.pack(side=TOP)
# # lbl.pack(side=RIGHT)
# # lbl.pack(side=LEFT)
# # lbl.pack(side=BOTTOM)
# root.mainloop()


# from tkinter import*
# root=Tk()
# root.title("Application")
# root.geometry("500x500")
# lbl=Label(root,text="Name",font=('Harlow Solid Italic',50))
# lbl.grid(row=0,column=0)
# lbl=Label(root,text="Name",font=('Harlow Solid Italic',50))
# lbl.grid(row=1,column=1)
# root.mainloop()

###########create input field
# from tkinter import*
# root=Tk()
# root.title("Application")
# root.geometry("500x500")
# lbl=Label(root,text="Name",font=('Harlow Solid Italic',50))
# lbl.grid(row=0,column=0)
# entr=Entry(root,width=50)
# entr.grid(row=0,column=1)
# root.mainloop()



######################### myyyyyyyyyyyyyyyyyyy
# from tkinter import*
# root=Tk()
# root.title('form')
# root.geometry('600x600')

# ###heading

# a=Label(root,text='form', foreground='red',font=('arial',25,'bold'))
# a.grid(row=0,column=1,)

# ###name

# lbl=Label(root,text="Name",font=('arial',15))
# lbl.grid(row=1,column=0,padx=5)

# enter=Entry(root,width=40)
# enter.grid(row=1,column=1)

# ####Email
# lbl1=Label(root,text="Email",font=('arial',15))
# lbl1.grid(row=2,column=0,padx=5)

# ente1=Entry(root,width=40)
# ente1.grid(row=2,column=1)

# ###password

# lbl3=Label(root,text='Password', font=('arial',15))
# lbl3.grid(row=3,column=0,padx=5)

# enter2=Entry(root,width=40)
# enter2.grid(row=3,column=1)

# ###submit button
# btn=Button(root,text='Submit',bg='blue',foreground='white',width=35)
# btn.grid(row=4,column=1,pady=10)


# root.mainloop()







############# create button
# from tkinter import*
# root=Tk()
# root.title("Application")
# root.geometry("500x500")
# lbl=Label(root,text="Name",font=('Harlow Solid Italic',50))
# lbl.grid(row=0,column=0)
# entr=Entry(root,width=50)
# entr.grid(row=0,column=1)
# btn=Button(root,text='click',bg='red',fg='white',font=('Harlow Solid Italic',50))
# btn.pack()
# root.mainloop()


################# button action
# from tkinter import*
# root=Tk()
# root.title("Application")
# root.geometry("500x500")
# def click():
#     lbl=Label(root,text="pleace click on this button")
#     lbl.pack()
# btn=Button(root,text='click',bg='red',fg='white',font=('Harlow Solid Italic',50),command=click)
# btn.pack()
# root.mainloop()

# from tkinter import*
# root=Tk()
# root.title("Application")
# root.geometry("500x500")
# lbl=Label(root,text="enter your name")
# lbl.grid(row=0,column=0)
# e=Entry(root)
# e.grid(row=0,column=1)
# def click():
#     lbl=Label(root,text="Hi  "+e.get())
#     lbl.grid(row=1,column=1)
# btn=Button(root,text="submit",bg='red',fg='white',font=('Harlow Solid Italic',15),command=click)
# btn.grid(row=3,column=3)

# root.mainloop()


# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.title("Application")
# root.geometry("500x500")

# lbl = Label(root, text="enter your name")
# lbl.grid(row=0, column=0)

# e = Entry(root)
# e.grid(row=0, column=1)

# def click():
#     lbl2 = Label(root, text="Hi " + e.get())
#     lbl2.grid(row=1, column=1)

# style = ttk.Style()
# style.configure("Rounded.TButton",
#                 padding=10,
#                 relief="flat")

# btn = ttk.Button(root, text="Submit",
#                  style="Rounded.TButton",
#                  command=click)

# btn.grid(row=3, column=3)

# root.mainloop()





# from tkinter import *
# from tkinter import messagebox

# root = Tk()
# root.title("Student Registration Form")
# root.geometry("400x400")

# # ===== Labels =====
# Label(root, text="Student Registration Form", 
#       font=("Arial", 16, "bold")).grid(row=0, column=1, pady=10)

# Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
# Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
# Label(root, text="Gender").grid(row=3, column=0, padx=10, pady=5)
# Label(root, text="Course").grid(row=4, column=0, padx=10, pady=5)

# # ===== Entry Fields =====
# name_entry = Entry(root, width=25)
# name_entry.grid(row=1, column=1)

# email_entry = Entry(root, width=25)
# email_entry.grid(row=2, column=1)

# # ===== Gender (Radiobutton) =====
# gender = StringVar()

# Radiobutton(root, text="Male", variable=gender, value="Male").grid(row=3, column=1, sticky=W)
# Radiobutton(root, text="Female", variable=gender, value="Female").grid(row=3, column=1)

# # ===== Course (Dropdown) =====
# course = StringVar()
# course.set("Select Course")

# OptionMenu(root, course, "Python", "Java", "Web Development").grid(row=4, column=1)

# # ===== Submit Function =====
# def submit():
#     name = name_entry.get()
#     email = email_entry.get()
#     gen = gender.get()
#     cour = course.get()
    
#     messagebox.showinfo("Form Submitted",f"Name: {name}\nEmail: {email}\nGender: {gen}\nCourse: {cour}")

# # ===== Submit Button =====
# Button(root, text="Submit", bg="blue", fg="white",
#        command=submit).grid(row=5, column=1, pady=20)

# root.mainloop()




from tkinter import *
import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        # database="dell_db"
        database="caddcenter"
        
      )
cur=mydb.cursor(buffered=True)
########## create database
try:
      cur.execute("use caddcenter")
except:
      cur.execute("create database caddcenter")
      cur.execute("use caddcenter")
      
########### create table
      
try:
      cur.execute("describe person")
except:
      cur.execute("create table person(Name varchar(20),Id int(10),Email varchar(40),Password int(10))")
      cur.execute("describe person")
                  




root = Tk()
root.title('Form')
root.geometry('400x400')

def Login():
      cur.execute(f"insert into person(Name,Id,Email,Password)values('{enter.get()}','{ente1.get()}','{enter2.get()}','{enter3.get()}')")
      mydb.commit()


# Heading
a = Label(root, text='FORM', foreground='red', font=('Arial', 20, 'bold'))
a.grid(row=0, column=1, pady=10)

# Name
lbl = Label(root, text="Name", font=('Arial', 12))
lbl.grid(row=1, column=0, padx=10, pady=5)

enter = Entry(root, width=30)
enter.grid(row=1, column=1, pady=5)

# ID
l = Label(root, text="ID", font=('Arial', 12))
l.grid(row=2, column=0, padx=10, pady=5)

ente1 = Entry(root, width=30)
ente1.grid(row=2, column=1, pady=5)

# Email
lbl2 = Label(root, text="Email", font=('Arial', 12))
lbl2.grid(row=3, column=0, padx=10, pady=5)

enter2 = Entry(root, width=30)
enter2.grid(row=3, column=1, pady=5)

# Password
lbl3 = Label(root, text="Password", font=('Arial', 12))
lbl3.grid(row=4, column=0, padx=10, pady=5)

enter3 = Entry(root, width=30, show="*")
enter3.grid(row=4, column=1, pady=5)

# Submit Button
btn = Button(root, text="Submit", bg="blue", fg="white",command=Login)
btn.grid(row=5, column=1, pady=20)

root.mainloop()
