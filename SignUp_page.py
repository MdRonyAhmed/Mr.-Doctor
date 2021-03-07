import root as r
import Database as db

tk = r.tk
page = r.root
Frame_signup=tk.Frame(page,bg="white")
Frame_signup.place(x=25,y=53,height=600,width=450)

class SignUp_patient:

    first_name = tk.StringVar()
    last_name = tk.StringVar()
    age = tk.StringVar()
    email =  tk.StringVar()
    password = tk.StringVar()

    def __init__(self):
        self.swap_page(Frame_signup)

    def swap_page(self,frame):    
        frame.tkraise()
        self.InputBox()

    def submit(self):
        # Get Value from the Entries
        name = self.first_name.get() +" "+ self.last_name.get()
        age = int(self.age.get())
        email = self.email.get()
        password = self.password.get()

        # Connect with Database
        dbConnect = db.dbConnect()
        dbConnect.insertData_patient(name,age,email,password)
        



    def InputBox(self):
       
        # Title of the form
        tk.Label(Frame_signup,text="Patient",font=("Open Sans",22,"bold"),fg="black",bg="white", borderwidth=3, relief="solid").place(x=182,y=5)

        # First Name
        tk.Label(Frame_signup,text="*First Name:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=90)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.first_name,relief="raised").place(x=54,y=120,width=350,height=35)

        # Last Name
        tk.Label(Frame_signup,text="*Last Name:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=170)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.last_name,relief="raised").place(x=54,y=200,width=350,height=35)

        # Age
        tk.Label(Frame_signup,text="Age:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=250)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.age,relief="raised").place(x=54,y=280,width=350,height=35)

        # Email Address
        tk.Label(Frame_signup,text="*Email Address:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=330)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.email,relief="raised").place(x=54,y=360,width=350,height=35)

        # Password
        tk.Label(Frame_signup,text="*Password:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=410)
        tk.Entry(Frame_signup,font=("Open Sans",18),bg="white",textvariable=self.password,relief="raised",show="*").place(x=54,y=440,width=350,height=35)
        
        # Button
        tk.Button(Frame_signup,command=lambda:self.submit(),cursor="hand2",text="Signup",fg="white",bg="#e60000",font=("Open sans",18)).place(x=137,y=520,width=180,height=40)




class SignUp_doctor:

    first_name = tk.StringVar()
    last_name = tk.StringVar()
    designation = tk.StringVar()
    email =  tk.StringVar()
    password = tk.StringVar()

    def __init__(self):
        self.swap_page(Frame_signup)

    def swap_page(self,frame):    
        frame.tkraise()
        self.InputBox()

    def submit(self):
        # Get Value from the Entries
        name = self.first_name.get() +" "+ self.last_name.get()
        designation = self.designation.get()
        email = self.email.get()
        password = self.password.get()

        # Connect with Database
        dbConnect = db.dbConnect()
        dbConnect.insertData_doctor(name,designation,email,password)
        



    def InputBox(self):
       
        # Title of the form
        tk.Label(Frame_signup,text="Doctor",font=("Open Sans",22,"bold"),fg="black",bg="white", borderwidth=3, relief="solid").place(x=182,y=5)

        # First Name
        tk.Label(Frame_signup,text="*First Name:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=90)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.first_name,relief="raised").place(x=54,y=120,width=350,height=35)

        # Last Name
        tk.Label(Frame_signup,text="*Last Name:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=170)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.last_name,relief="raised").place(x=54,y=200,width=350,height=35)

        # Designation Information
        tk.Label(Frame_signup,text="*Designation:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=250)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.designation,relief="raised").place(x=54,y=280,width=350,height=35)

        # Email Address
        tk.Label(Frame_signup,text="*Email Address:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=330)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.email,relief="raised").place(x=54,y=360,width=350,height=35)

        # Password
        tk.Label(Frame_signup,text="*Password:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=410)
        tk.Entry(Frame_signup,font=("Open Sans",18),bg="white",textvariable=self.password,relief="raised",show="*").place(x=54,y=440,width=350,height=35)
        
        # Button
        tk.Button(Frame_signup,command=lambda:self.submit(),cursor="hand2",text="Signup",fg="white",bg="#e60000",font=("Open sans",18)).place(x=137,y=520,width=180,height=40)