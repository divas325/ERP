from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

def connection():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="user_id")

    except Error as e:
        print("error while connecting to database",e)
    return mydb
class addstdrec:
    def __init__(self):
        self.root2 = Tk()
        self.root2.title("student management System")
        self.root2.geometry("750x600+400+100")
        self.root2.configure(bg="teal")
        l1 = Label(self.root2, text="Welcome To Management system", bg="skyblue", fg="Black")
        l1.config(font=("Arial", 30))
        l1.place(x=100, y=50)

        l2= Label(self.root2,text="Roll_Number:",bg="skyblue",fg="black")
        l2.config(font=("Arial",20))
        l2.place(x=220,y=200)

        l3 = Label(self.root2, text="Name:", bg="skyblue", fg="black")
        l3.config(font=("Arial", 20))
        l3.place(x=220, y=230)

        l4 = Label(self.root2, text="Standard:", bg="skyblue", fg="black")
        l4.config(font=("Arial", 20))
        l4.place(x=220, y=260)

        l5 = Label(self.root2, text="Section:", bg="skyblue", fg="black")
        l5.config(font=("Arial", 20))
        l5.place(x=220, y=290)

        l6 = Label(self.root2, text="Gender",bg="skyblue", fg="black")
        l6.config(font=("Arial", 20))
        l6.place(x=220, y=320)

        l7 = Label(self.root2, text="Address:", bg="skyblue", fg="black")
        l7.config(font=("Arial", 20))
        l7.place(x=220, y=350)



        self.Roll_number= IntVar()
        self.Name= StringVar()
        self.Standard= IntVar()
        self.Section = StringVar()
        self.Gender= StringVar()
        self.Address = StringVar()
        self.password =  StringVar()


        self.e1= Entry(self.root2,width=40,bg="black",textvariable=self.Roll_number)
        self. e1.place(x=330,y=200)

        self.e2=Entry(self.root2,width=40,bg="black",textvariable=self.Name)
        self.e2.place(x=330,y=230)

        self.e3=Entry(self.root2,width=40,bg="black",textvariable=self.Standard)
        self.e3.place(x=330,y=260)

        self.a1= ["A","B","C","D"]
        self.cd= ttk.Combobox(self.root2,state='readonly',values=self.a1,textvariable=self.Section)
        self.cd.place(x=330,y=290)


        self.a2=["Male","Female"]
        self.cd1 = ttk.Combobox(self.root2,state='readonly',values=self.a2,textvariable=self.Gender)
        self.cd1.place(x=330,y=320)

        self.e4 = Entry(self.root2, width=40, bg="black",textvariable=self.Address)
        self.e4.place(x=330, y=350)



        self.b1=Button(self.root2,text="Exit",command=self.root2.destroy,width=15,bg="skyblue",fg="black")
        self.b1.config(font=("courier",12))
        self.b1.place(x=200,y=410)

        self.b2=Button(self.root2,text="Add Record",command= self.insertrecord ,width=15,bg="skyblue",fg="black")
        self.b2.config(font=("courier",12))
        self.b2.place(x=400,y=410)

        self.root2.mainloop()


    def insertrecord(self):
       mydb=connection()
       cursor = mydb.cursor()
       sql="INSERT INT0 Student values(%s,%s,%s,%s,%s,%s)"
       vd=( self.e1.get(), self.e2.get(),self.e3.get(),self.cd.get(),self.cd1.get(),self.e4.get())
       cursor.execute(sql,vd)
       messagebox.showinfo("Success","Record Inserted Successfully")
       mydb.commit()
       mydb.close()











