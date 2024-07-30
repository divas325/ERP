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


class viewrec:
    def __init__(self):
        self.root3 = Tk()
        self.root3.title("student management System")
        self.root3.geometry("750x600+400+100")
        self.root3.configure(bg="teal")
        l1 = Label(self.root3, text="Welcome To Management system", bg="skyblue", fg="black")
        l1.config(font=("Arial", 25))
        l1.place(x=150, y=50)

        l2=Label(self.root3,text="viewing all records",bg="skyblue",fg="brown")
        l2.config(font=("arial",20))
        l2.place(x=200,y=100)

        self.b= Button(self.root3,text="Click to view all records",command=self.fetch, width=45,bg="red",fg="black")
        self.b.config(font=("Arial",15))
        self.b.place(x=100,y=200)

        self.root3.mainloop()

def fetch(self):
    mydb=connection()
    cursor=mydb.cursor()
    sql="select * from stdent"
    cursor.execute(sql)
    messagebox.showinfo("success","Here all recorde is displayed")
    mydb.close()