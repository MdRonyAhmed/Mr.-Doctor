
class LoginPage_Doctor:
    def __init__(self,root,tk):
        self.page = root
        self.tk = tk
        self.swap_page( self.frame())


    def swap_page(self,frame):    
        frame.tkraise()
        self.InputBox()

    def frame(self):   
        Frame_login=self.tk.Frame(self.page,bg="white")
        Frame_login.place(x=75,y=210,height=340,width=350)
        return Frame_login
    
    def InputBox(self):
        Frame = self.frame()
        self.tk.Label(Frame,text="User Name",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=10) 
        user_name = self.tk.Entry(Frame,font=("Open Sans",12),bg="lightgray")
        user_name.place(x=25,y=50,width=300,height=35)

        self.tk.Label(Frame,text="Password",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=110) 
        password = self.tk.Entry(Frame,font=("Open Sans",12),bg="lightgray")
        password.place(x=25,y=150,width=300,height=35)

        self.tk.Button(Frame, text="Login",fg="White",bg="#D82A2A",font=("Open sans",18)).place(x=85,y=220,width=180,height=40)
        
        self.tk.Button(Frame, text="No Account? Sign Up Here.",fg="#000fff",borderwidth=0,bg="white",font=("Open sans",12)).place(x=28,y=270,width=300,height=40)
         
    
    
class LoginPage_Patient:
    def __init__(self,root,tk):
        self.page = root
        self.tk = tk
        self.swap_page( self.frame())


    def swap_page(self,frame):    
        frame.tkraise()
        self.InputBox()

    def frame(self):   
        Frame_login=self.tk.Frame(self.page,bg="white")
        Frame_login.place(x=75,y=210,height=340,width=350)
        return Frame_login
    
    def InputBox(self):
        Frame = self.frame()
        self.tk.Label(Frame,text="User Name",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=10) 
        user_name = self.tk.Entry(Frame,font=("Open Sans",12),bg="lightgray")
        user_name.place(x=25,y=50,width=300,height=35)

        self.tk.Label(Frame,text="Password",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=25,y=110) 
        password = self.tk.Entry(Frame,font=("Open Sans",12),bg="lightgray")
        password.place(x=25,y=150,width=300,height=35)

        self.tk.Button(Frame, text="Submit",fg="White",bg="#D82A2A",font=("Open sans",18)).place(x=85,y=220,width=180,height=40) 

        self.tk.Button(Frame, text="No Account? Sign Up Here.",fg="#000fff",borderwidth=0,bg="white",font=("Open sans",12)).place(x=28,y=270,width=300,height=40)
    
    