import SignUp_page as signup
import root as r
import Database as db

tk = r.tk
page = r.root
Frame_login=tk.Frame(page,bg="white")
Frame_login.place(x=75,y=210,height=340,width=350)

class LoginPage_Doctor:
    email =  tk.StringVar()
    password = tk.StringVar()

    def __init__(self):
            self.swap_page(Frame_login)

    def signup_page(self):               
        signup.SignUp_doctor()
        Frame_login.destroy()

    def swap_page(self,frame):    
        frame.tkraise()
        self.InputBox()

    # Login Match From Database)
    def login(self):
        email = self.email.get()
        password = self.password.get()
        dbConnect = db.dbConnect()
        login_confirmation = dbConnect.login_doctor(email,password)
        print(login_confirmation)

    # Login Form
    def InputBox(self):
        # User Name or Email
        tk.Label(Frame_login,text="User Name/Email",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=10) 
        user_name = tk.Entry(Frame_login,font=("Open Sans",12),bg="lightgray",textvariable=self.email)
        user_name.place(x=25,y=50,width=300,height=35)

        # Password
        tk.Label(Frame_login,text="Password",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=110) 
        password = tk.Entry(Frame_login,font=("Open Sans",18),bg="lightgray",show="*",textvariable=self.password)
        password.place(x=25,y=150,width=300,height=35)

        # Login Button
        tk.Button(Frame_login,command=lambda:self.login(), text="Login",fg="White",bg="#D82A2A",font=("Open sans",18)).place(x=85,y=220,width=180,height=40)
        
        # SingUp Button 
        tk.Button(Frame_login,command=lambda:self.signup_page(), text="No Account? Sign Up Here.",fg="#000fff",borderwidth=0,bg="white",font=("Open sans",12)).place(x=28,y=270,width=300,height=40)
         
    
    
class LoginPage_Patient:
    email =  tk.StringVar()
    password = tk.StringVar()

    def __init__(self):
            self.swap_page(Frame_login)

    def signup_page(self):               
        signup.SignUp_patient()
        Frame_login.destroy()

    def swap_page(self,frame):    
        frame.tkraise()
        self.InputBox()
    
    # Login Match From Database)
    def login(self):
        email = self.email.get()
        password = self.password.get()
        dbConnect = db.dbConnect()
        login_confirmation = dbConnect.login_patient(email,password)
        print(login_confirmation)

    # Login Form
    def InputBox(self):
        # User Name
        tk.Label(Frame_login,text="User Name",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=10) 
        user_name = tk.Entry(Frame_login,font=("Open Sans",12),bg="lightgray",textvariable=self.email)
        user_name.place(x=25,y=50,width=300,height=35)

        # Password
        tk.Label(Frame_login,text="Password",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=110) 
        password = tk.Entry(Frame_login,font=("Open Sans",18),bg="lightgray",show="*",textvariable=self.password)
        password.place(x=25,y=150,width=300,height=35)

        # Login Button
        tk.Button(Frame_login,command=lambda:self.login(), text="Login",fg="White",bg="#D82A2A",font=("Open sans",18)).place(x=85,y=220,width=180,height=40)

        # SingUp Button 
        tk.Button(Frame_login,command=lambda:self.signup_page(), text="No Account? Sign Up Here.",fg="#000fff",borderwidth=0,bg="white",font=("Open sans",12)).place(x=28,y=270,width=300,height=40)
         