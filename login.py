from tkinter import *
import sys
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from stdmgmt import stdmgmt




def loginValidate():
    try:
        mydb = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="user_id")
        cursor=mydb.cursor()
        sql = "select * from Student where Name=%s and Password=%s"
        vd = (uid.get(),pass1.get())
        cursor.execute(sql,vd)
        results= cursor.fetchall()
        i = 0
        for row in results:
            if uid.get()==row[1] and pass1.get()==row[6]:
                i=1
                obj = stdmgmt()
        if i==0:
            messagebox.showinfo("Error","Try Again!!! userId or Password is incorrect!")
    except Error as e:
        print("Error while connecting to database",e)






if __name__ == "__main__" :
    root= Tk()
    root.title=("Student Management System")
    root.geometry("750x600+400+100")
    root.configure(bg="teal")
    l1 = Label(root,text="Welcome To Student Management System",bg="Skyblue",fg="Black")
    l1.configure(font=("Arial",20))
    l1.place(x=150,y=50)


    Label1=Label(root,text="User ID:",bg="Skyblue",fg="Black",font="Arial")
    Label2=Label(root, text="Password:",bg="Skyblue",fg="Black",font="arial")

    Label1.place(x=200,y=200)
    Label2.place(x=200,y=230)

    uid = StringVar()
    pass1 = StringVar()

    e1 = Entry(root, textvariable=uid,width=40)
    e2 = Entry(root, textvariable=pass1,width=40,show="*")
    e1.place(x=300,y=200)
    e2.place(x=300,y=230)

    b=Button(root,text="login",command=loginValidate, width=20,bg="purple",fg="Red")
    b.place(x=350,y=260)






    root.mainloop()
