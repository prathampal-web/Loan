from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('application')
root.geometry('400x400')

######## lebels
Label(root,text='application',font=('arial',20,'bold')).grid(row=0,column=1,pady=10)

Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
Label(root,text='Email').grid(row=2,column=0,padx=10,pady=5)
Label(root,text='Gender').grid(row=3,column=0,padx=10,pady=5)
Label(root,text='Course').grid(row=4,column=0,padx=10,pady=5)

######## Entry Fields
name=Entry(root,width=30)
name.grid(row=1,column=1)

email_name=Entry(root,width=30)
email_name.grid(row=2,column=1)

########## Gender (Radiobutton) 
gender=StringVar()

Radiobutton(root,text='Male', variable=gender, value='Male').grid(row=3,column=1,sticky=W)
Radiobutton(root,text='female',variable=gender, value='female').grid(row=3,column=1)

########## Course (Radiobutton)
Course=StringVar()
Course.set('Select Course')

OptionMenu(root,Course,'javascript','html','css').grid(row=4,column=1)

def submit():
    na=name.get()
    act=email_name.get()
    gen=gender.get()
    cour=Course.get()
    
    messagebox.showinfo("Form submmited",f"Name:{na}\n Email:{act}\n Gender:{gen}\n Course:{cour}")
Button(root,text='Submit',bg='blue', fg='white',command=submit).grid(row=5,column=1) 

root.mainloop()


