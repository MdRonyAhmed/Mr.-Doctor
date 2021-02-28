import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk


def login_page(root):
    #Functions

    #Frame swap Functions
    def swap_function(frame):
        frame.tkraise()


    #Login page button function under the login_page function
    def login_function():
        if txt_pass.get()=="" or txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=page)
        elif txt_pass.get()!="12345" or txt_user.get()!="admin":
            messagebox.showerror("Error","Invalid Username/Password",parent=page)
        else:
            messagebox.showinfo("Welcome","Welcome to Med Reminder App",parent=page)
            swap_function(Frame_signup)


    #Signup page button function under the login_page function
    def signup_function():
        if txt_firstname.get()=="" or txt_lastname.get()=="" or txt_email.get()=="" or txt_spass.get()=="" or txt_conpass.get()==""  :
            messagebox.showerror("Error","Please fillup the fields first!",parent=page)
        else:
            messagebox.showinfo("Welcome","Welcome to Med Reminder App",parent=page)
            Frame_signup.destroy()
            swap_function(Frame_login)


    #Forgot password page button function under the login_page function
    def forgotpassdone_function():
        if txt_tpass.get()=="" or txt_tconpass.get()=="":
            messagebox.showerror("Error","Please fillup the fields first!",parent=page)
        else:
            messagebox.showinfo("Welcome","Password Changed Successfully!",parent=page)
            Frame_fpass.destroy()
            swap_function(Frame_login)

    page=root
    #Overall structure

    #*****************************************************************Signup frame strats*********************************************************************
    Frame_signup=tk.Frame(page,bg="light blue")
    Frame_signup.place(x=0,y=0,height=700,width=500)

    title=tk.Label(Frame_signup,text="Signup",font=("Open Sans",22,"bold"),fg="black",bg="light blue").place(x=200,y=5)

    #Input Box
    lbl_firstname=tk.Label(Frame_signup,text="*First Name:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=90)
    txt_firstname=tk.Entry(Frame_signup,font=("Open Sans",12),bg="lightgray")
    txt_firstname.place(x=54,y=120,width=350,height=35)

    lbl_lastname=tk.Label(Frame_signup,text="*Last Name:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=170)
    txt_lastname=tk.Entry(Frame_signup,font=("Open Sans",12),bg="lightgray")
    txt_lastname.place(x=54,y=200,width=350,height=35)

    lbl_age=tk.Label(Frame_signup,text="Age:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=250)
    txt_age=tk.Entry(Frame_signup,font=("Open Sans",12),bg="lightgray")
    txt_age.place(x=54,y=280,width=350,height=35)

    lbl_email=tk.Label(Frame_signup,text="*Email Address:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=330)
    txt_email=tk.Entry(Frame_signup,font=("Open Sans",12),bg="lightgray")
    txt_email.place(x=54,y=360,width=350,height=35)

    lbl_spass=tk.Label(Frame_signup,text="*Password:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=410)
    txt_spass=tk.Entry(Frame_signup,font=("Open Sans",12),bg="lightgray")
    txt_spass.place(x=54,y=440,width=350,height=35)

    lbl_conpass=tk.Label(Frame_signup,text="*Confirm Password:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=490)
    txt_conpass=tk.Entry(Frame_signup,font=("Open Sans",12),bg="lightgray")
    txt_conpass.place(x=54,y=520,width=350,height=35)

    #Signup and forgot password button
    Signup_btn=tk.Button(Frame_signup,command=signup_function,cursor="hand2",text="Signup",fg="white",bg="#e60000",font=("Open sans",18)).place(x=150,y=570,width=180,height=40)

    #********************************************************#Signup frame ends**************************************************************************





    #*****************************************************************Forgot password frame strats*********************************************************************
    Frame_fpass=tk.Frame(page,bg="light blue")
    Frame_fpass.place(x=0,y=0,height=700,width=500)

    #Input Box
    lbl_tpass=tk.Label(Frame_fpass,text="Type Password:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=250)
    txt_tpass=tk.Entry(Frame_fpass,font=("Open Sans",12),bg="lightgray")
    txt_tpass.place(x=54,y=280,width=350,height=35)

    lbl_tconpass=tk.Label(Frame_fpass,text="Confirm Password:",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=50,y=330)
    txt_tconpass=tk.Entry(Frame_fpass,font=("Open Sans",12),bg="lightgray")
    txt_tconpass.place(x=54,y=360,width=350,height=35)

    #Login and forgot password button
    Done_btn=tk.Button(Frame_fpass,command=forgotpassdone_function,cursor="hand2",text="Done",fg="white",bg="#e60000",font=("Open sans",18)).place(x=150,y=460,width=180,height=40)

    #********************************************************#Forgot password frame ends**************************************************************************




    #*****************************************************************Login frame strats*********************************************************************

    page.title("Med Reminder App")
    page.geometry("500x700")
    page.resizable(False,False)

    #Page background image
    page.cover=Image.open("E:\practice\picture\Picture1.jpg").rotate(270)
    page.cover=ImageTk.PhotoImage(page.cover)
    page.bg=tk.Label(page,image=page.cover).place(x=0,y=0,relwidth=1,relheight=1)

    Frame_login=tk.Frame(page,bg="light blue")
    Frame_login.place(x=75,y=390,height=290,width=350)

    title=tk.Label(Frame_login,text="Login Here",font=("Open Sans",22,"bold"),fg="black",bg="light blue").place(x=92,y=5)

    #Input Box
    lbl_user=tk.Label(Frame_login,text="Username",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=20,y=60)
    txt_user=tk.Entry(Frame_login,font=("Open Sans",12),bg="lightgray")
    txt_user.place(x=24,y=90,width=300,height=35)

    lbl_pass=tk.Label(Frame_login,text="Password",font=("Open Sans",15,"bold"),fg="black",bg="light blue").place(x=20,y=140)
    txt_pass=tk.Entry(Frame_login,font=("Open Sans",12),bg="lightgray")
    txt_pass.place(x=24,y=170,width=300,height=35)

    #Login and forgot password button
    Login_btn=tk.Button(Frame_login,command=login_function,cursor="hand2",text="Login",fg="white",bg="blue",font=("Open sans",18)).place(x=84,y=215,width=180,height=40)
    Signup_btn=tk.Button(Frame_login,command=lambda:swap_function(Frame_signup),cursor="hand2",text="New member? Signup here",fg="black",bg="light blue",font=("Open sans",10),bd=0).place(x=15,y=265,width=180,height=20)
    Forgot_btn=tk.Button(Frame_login,command=lambda:swap_function(Frame_fpass),cursor="hand2",text="Forgot Password?",fg="black",bg="light blue",font=("Open sans",10),bd=0).place(x=215,y=265,width=120,height=20)
    #*****************************************************************#Login frame ends**************************************************************************



root=tk.Tk()
login_page(root)
root.mainloop()
