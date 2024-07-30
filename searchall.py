from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import  mysql.connector
from mysql.connector import Error

def connection():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="user_id")

    except Error as e:
        print("error while connecting to database",e)
    return mydb


class searchrec:
    def __init__(self):
        self.root6 = Tk()
        self.root6.title("student management System")
        self.root6.geometry("750x600+400+100")
        self.root6.configure(bg="blue")
        l1 = Label(self.root6, text="Welcome To Management system", bg="blue", fg="yellow")
        l1.config(font=("Arial", 20))
        l1.place(x=50, y=50)

        l2 = Label(self.root6, text="search All Records", bg="cyan", fg="red")
        l2.config(font=("arial", 20))
        l2.place(x=250, y=130)

        l3 = Label(self.root6, text="enter Roll Number", bg="cyan", fg="red")
        l3.config(font=("arial", 15))
        l3.place(x=50, y=200)

        self.roll = StringVar()
        self.e11 = Entry(self.root6, textvariabel=self.roll, width=20)
        self.e11.config(font=("Arial", 15))
        self.e11.place(x=250, y=200)

        self.b = Button(self.root6, text="search",command=self.searchrecord, width=25, bg="Purple", fg="black")
        self.b.place(x=500, y=200)

        self.root4.mainloop()

    def serachrecord(self):
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

        l2 = Label(self.root6, text="Roll Number:", bg="cyan", fg="red")
        l2.config(font=("Arial", 20))
        l2.place(x=200, y=200)

        l3 = Label(self.root6, text="Name:", bg="cyan", fg="red")
        l3.config(font=("Arial", 20))
        l3.place(x=200, y=230)

        l4 = Label(self.root6, text="Standard:", bg="cyan", fg="red")
        l4.config(font=("Arial", 20))
        l4.place(x=200, y=260)

        l5 = Label(self.root6, text="Section:", bg="cyan", fg="red")
        l5.config(font=("Arial", 20))
        l5.place(x=200, y=290)

        l6 = Label(self.root6, text="Gender", bg="cyan", fg="red")
        l6.config(font=("Arial", 20))
        l6.place(x=200, y=320)

        l7 = Label(self.root6, text="Address:", bg="cyan", fg="red")
        l7.config(font=("Arial", 20))
        l7.place(x=200, y=350)

        self.roll = StringVar()
        self.name = StringVar()
        self.std = StringVar()
        self.sec = StringVar()
        self.gen = StringVar()
        self.add = StringVar()

        self.e1 = Entry(self.root6, width=40, bg="white", textvariable=self.roll)
        self.e1.insert(0, self.a)
        self.e1.place(x=330, y=280)

        self.e2 = Entry(self.root6, width=40, bg="white", textvariable=self.name)
        self.e2.insert(0, self.b)
        self.e2.place(x=330, y=310)

        self.e3 = Entry(self.root6, width=40, bg="white", textvariable=self.std)
        self.e3.insert(0, self.c)
        self.e3.place(x=330, y=340)

        self.e4 = Entry(self.root6, width=40, bg="white", textvariable=self.sec)
        self.e4.insert(0, self.d)
        self.e4.place(x=330, y=370)

        self.e5 = Entry(self.root6, width=40, bg="white", textvariable=self.gen)
        self.e5.insert(0, self.e)
        self.e5.place(x=330, y=400)

        self.e6 = Entry(self.root6, width=40, bg="white", textvariable=self.add)
        self.e6.insrt(0, self.f)
        self.e6.place(x=330, y=410)

        self.b1 = Button(self.root6, text="Exit", command=self.root4.destroy, width=15, bg="purple", fg="black")
        self.b1.config(font=("courier", 12))
        self.b1.place(x=250, y=440)

