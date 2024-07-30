from tkinter import *
import sys
from addstdrec import addstdrec
from viewall import viewrec
from editall import editrec
from deleteall import deleterec
from searchall import searchrec



def close():
    sys.exit()

def insert():
    obj= addstdrec()


def view():
    obj= viewrec()


def edit():
    obj= editrec()


def delete():
    obj= deleterec()


def search():
    obj= searchrec()


class stdmgmt:
    def __init__(self):
        self.root1 = Tk()
        self.root1.title("student management System")
        self.root1.geometry("750x600+400+100")
        self.root1.configure(bg="teal")
        l1= Label(self.root1 ,text="Welcome To Management system",bg="teal",fg="black")
        l1.config(font=("Arial",25))
        l1.place(x=100,y=30)

        b1= Button(self.root1,text="Add Record",command=insert,width=45,bg="Skyblue",fg="black")
        b1.config(font=("courier",15))
        b1.place(x=100,y=200)

        b1 = Button(self.root1, text="View all records", command=view,width=45, bg="Skyblue", fg="black")
        b1.config(font=("Courier", 15))
        b1.place(x=100, y=250)

        b1= Button(self.root1,text="Edit Record",command=edit,width=45,bg="Skyblue",fg="black")
        b1.config(font=("Courier",15))
        b1.place(x=100,y=300)

        b1 = Button(self.root1, text="Delete Records",command=delete, width=45, bg="skyblue", fg="black")
        b1.config(font=("Courier", 15))
        b1.place(x=100, y=350)

        b1 = Button(self.root1, text="search Records", command=search,width=45, bg="skyblue", fg="Black")
        b1.config(font=("Courier", 15))
        b1.place(x=100, y=400)

        b1 = Button(self.root1, text="Exit",command=close, width=45, bg="red", fg="black")
        b1.config(font=("Courier", 15))
        b1.place(x=100, y=450)

        self.root1.mainloop()