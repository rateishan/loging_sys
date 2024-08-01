from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
 



class my_logingClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Log In")
        self.root.geometry("1000x500+200+100")


        self.root.focus_force()
        self.root.resizable(False,False)

        self.my_image=ImageTk.PhotoImage(file="C:/python/python project/loging/water drop.jpg")
        self.lbl_image=Label(self.root,image=self.my_image).place(x=0,y=0)


        self.var_username=StringVar()
        self.var_password=StringVar()

        #==================frame==================
        data_frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        data_frame.place(x=500, y=170, width=350, height=220)

        lab_loging=Label(data_frame,text="Loging",font=("times new roman",30,"bold"),bg="white").place(x=100,y=10)

        lab_username=Label(data_frame,text="Username",font=("times new roman",15,"bold"),bg="white").place(x=35,y=70)
        lab_password=Label(data_frame,text="password",font=("times new roman",15,"bold"),bg="white").place(x=35,y=110)

        entry_username=Entry(data_frame,textvariable=self.var_username,font=("time",15),bg='white',fg='black',bd=0,justify=CENTER)
        entry_username.place(x=150,y=70,width=150)
        entry_username.focus()
        Frame(data_frame,width=275,height=1,bg='black').place(x=120,y=100)


        entry_password=Entry(data_frame,textvariable=self.var_password,font=("time",15),bg='white',fg='black',bd=0,justify=CENTER,show='*')
        entry_password.place(x=150,y=110,width=150)
        entry_password.focus()
        Frame(data_frame,width=275,height=1,bg='black').place(x=120,y=140)

        login_btn=Button(data_frame,text='Login',command=self.login,font=("time",13,'bold'),bg='#6EACDA',fg='black',bd=0).place(x=35,y=170,width=100,height=30)
        Frame(data_frame,width=175,height=1,bg='black').place(x=150,y=140,width=220)


    def login(self):
        sqlcon=mysql.connector.connect(host="localhost",user="root",password="#@19is16Pro",database="mydb")
        cur=sqlcon.cursor()
        cur.execute("select * from login where username=%s and password=%s",(self.var_username.get(),self.var_password.get()))
        result=cur.fetchall()
        if len(result)>0:
            messagebox.showinfo("Success","Username and Password are Correct...................!")
        else:
            messagebox.showinfo("Error","Username and Password are Incorrect.........!")

    
if __name__ == "__main__":
    root = Tk()
    obj= my_logingClass(root)
    root.mainloop()
