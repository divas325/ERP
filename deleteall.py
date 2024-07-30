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


class deleterec:
    def __init__(self):
        self.root5 = Tk()
        self.root5.title("student management System")
        self.root5.geometry("750x600+400+100")
        self.root5.configure(bg="blue")
        l1 = Label(self.root5, text="Welcome To Management system", bg="skyblue", fg="black")
        l1.config(font=("Arial", 20))
        l1.place(x=150, y=50)

        l2 = Label(self.root5, text="Delete  record", bg="skyblue", fg="red")
        l2.config(font=("arial", 20))
        l2.place(x=250, y=130)

        l3 = Label(self.root5, text="Enter Roll no", bg="skyblue", fg="red")
        l3.config(font=("arial", 15))
        l3.place(x=50, y=200)

        self.Roll_number= StringVar()
        self.e11 = Entry(self.root5, textvariabel= self.Roll_number, width=20)
        self.e11.config(font=("Arial", 15))
        self.e11.place(x=250, y=200 )

        self.b1 = Button(self.root5, text="delete",command=self.retrive,width=20 , bg="cyan", fg="Black")
        self.b1.place(x=500,y=200)

        self.root4.mainloop()

    def retrive(self):
            self.a = StringVar()
            self.b = StringVar()
            self.c = StringVar()
            self.d = StringVar()
            self.e = StringVar()
            self.f = StringVar()

            mydb = connection()
            cursor = mydb.cursor()
            sql = "select * from users where Roll_no=%s"
            vd = [self.e11.get()]
            result = cursor.execute(sql, vd)
            resultnew = cursor.fetchall()
            for row in resultnew:
                self.a = row[0]
                self.b = row[1]
                self.c = row[2]
                self.d = row[3]
                self.e = row[4]
                self.f = row[5]

            l2 = Label(self.root5, text="Roll Number:", bg="cyan", fg="red")
            l2.config(font=("Arial", 20))
            l2.place(x=200, y=200)

            l3 = Label(self.root5, text="Name:", bg="cyan", fg="red")
            l3.config(font=("Arial", 20))
            l3.place(x=200, y=230)

            l4 = Label(self.root5, text="Standard:", bg="cyan", fg="red")
            l4.config(font=("Arial", 20))
            l4.place(x=200, y=260)

            l5 = Label(self.root5, text="Section:", bg="cyan", fg="red")
            l5.config(font=("Arial", 20))
            l5.place(x=200, y=290)

            l6 = Label(self.root5, text="Gender", bg="cyan", fg="red")
            l6.config(font=("Arial", 20))
            l6.place(x=200, y=320)

            l7 = Label(self.root5, text="Address:", bg="cyan", fg="red")
            l7.config(font=("Arial", 20))
            l7.place(x=200, y=350)

            self.Roll_number = StringVar()
            self.Name = StringVar()
            self.Standard = StringVar()
            self.Section = StringVar()
            self.Gender = StringVar()
            self.Address = StringVar()

            self.e1 = Entry(self.root5, width=40, bg="white", textvariable=self.Roll_number)
            self.e1.insert(0, self.a)
            self.e1.place(x=330, y=280)

            self.e2 = Entry(self.root5, width=40, bg="white", textvariable=self.Name)
            self.e2.insert(0, self.b)
            self.e2.place(x=330, y=310)

            self.e3 = Entry(self.root5, width=40, bg="white", textvariable=self.Standard)
            self.e3.insert(0, self.c)
            self.e3.place(x=330, y=340)

            self.e4 = Entry(self.root5, width=40, bg="white", textvariable=self.Section)
            self.e4.insert(0, self.d)
            self.e4.place(x=330, y=370)

            self.e5 = Entry(self.root5, width=40, bg="white", textvariable=self.Gender)
            self.e5.insert(0, self.e)
            self.e5.place(x=330, y=400)

            self.e6 = Entry(self.root5, width=40, bg="white", textvariable=self.Address)
            self.e6.insrt(0, self.f)
            self.e6.place(x=330, y=410)

            self.b1 = Button(self.root5, text="Exit", command=self.root4.destroy, width=15, bg="purple", fg="black")
            self.b1.config(font=("courier", 12))
            self.b1.place(x=200, y=440)

            self.b2 = Button(self.root5, text="Delete", command=self.finaldelete, width=15, bg="purple", fg="black")
            self.b2.config(font=("courier", 12))
            self.b2.place(x=400, y=440)

    def finaldelete(self):
        mydb= connection()
        cursor= mydb.cursor()
        sql="delete from users where Roll_number =%s"
        vd= [(self.e1.get()),]
        cursor.execute(sql,vd)
        messagebox.showinfo("Success","Record Deleted Successfully")
        mydb.commit()
        mydb.close()


