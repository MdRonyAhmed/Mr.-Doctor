import SignUp_page as signup
import root as r

tk = r.tk
page = r.root
Frame_login=tk.Frame(page,bg="white")
Frame_login.place(x=75,y=210,height=340,width=350)

class LoginPage_Doctor:
    def __init__(self):
            self.swap_page(Frame_login)

    def signup_page(self):               
        signup.SignUp_page()
        Frame_login.destroy()

    def swap_page(self,frame):    
        frame.tkraise()
        self.InputBox()
    
    def InputBox(self):
    
        tk.Label(Frame_login,text="User Name",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=10) 
        user_name = tk.Entry(Frame_login,font=("Open Sans",12),bg="lightgray")
        user_name.place(x=25,y=50,width=300,height=35)

        tk.Label(Frame_login,text="Password",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=110) 
        password = tk.Entry(Frame_login,font=("Open Sans",18),bg="lightgray",show="*")
        password.place(x=25,y=150,width=300,height=35)

        tk.Button(Frame_login, text="Login",fg="White",bg="#D82A2A",font=("Open sans",18)).place(x=85,y=220,width=180,height=40)
        
        tk.Button(Frame_login,command=lambda:self.signup_page(), text="No Account? Sign Up Here.",fg="#000fff",borderwidth=0,bg="white",font=("Open sans",12)).place(x=28,y=270,width=300,height=40)
         
    
    
class LoginPage_Patient:
    def __init__(self):
            self.swap_page(Frame_login)

    def signup_page(self):               
        signup.SignUp_page()
        Frame_login.destroy()

    def swap_page(self,frame):    
        frame.tkraise()
        self.InputBox()
    
    def InputBox(self):
    
        tk.Label(Frame_login,text="User Name",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=10) 
        user_name = tk.Entry(Frame_login,font=("Open Sans",12),bg="lightgray")
        user_name.place(x=25,y=50,width=300,height=35)

        tk.Label(Frame_login,text="Password",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=110) 
        password = tk.Entry(Frame_login,font=("Open Sans",18),bg="lightgray",show="*")
        password.place(x=25,y=150,width=300,height=35)

        tk.Button(Frame_login, text="Login",fg="White",bg="#D82A2A",font=("Open sans",18)).place(x=85,y=220,width=180,height=40)
        
        tk.Button(Frame_login,command=lambda:self.signup_page(), text="No Account? Sign Up Here.",fg="#000fff",borderwidth=0,bg="white",font=("Open sans",12)).place(x=28,y=270,width=300,height=40)
         