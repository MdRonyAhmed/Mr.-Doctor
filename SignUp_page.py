import root as r
import Database as db
import LoginPage as log
from tkinter import messagebox
import HomePage as Home


tk = r.tk
page = r.root
Frame_signup=tk.Frame(page,bg="white")
Frame_signup.place(x=25,y=53,height=600,width=450)

class SignUp_patient:
    submit_confirmation = bool()
    first_name = tk.StringVar()
    last_name = tk.StringVar()
    age = tk.StringVar()
    email =  tk.StringVar()
    password = tk.StringVar()

    def __init__(self):
        self.swap_page()

    def swap_page(self):    
        Frame_signup.tkraise()
        self.InputBox()

    # Home Page
    def home_page(self):
        if  self.submit_confirmation:
            messagebox.showinfo("Welcome","Welcome to Mr.Doctor",parent=page)
        else:
            messagebox.showinfo("Error","You Have Already an Account!",parent=page)
           

    def submit_patient(self):
        # Get Value from the Entries
        name = self.first_name.get() +" "+ self.last_name.get()
        age = int(self.age.get())
        email = self.email.get()
        password = self.password.get()
        
        if self.first_name.get()== "" or self.last_name.get()=="" or age=="" or email==""  or password=="":
            messagebox.showerror("Error","All fields are required",parent=page)

        else:
            # Connect with Database
            dbConnect = db.dbConnect()
            self.submit_confirmation = dbConnect.insertData_patient(name,age,email,password)
            self.home_page()
            home_page = Home.PatientHomePage()
            Frame_signup.destroy()

    def back_logingpage(self):
        Frame_signup.destroy()
        login = log.LoginPage_Patient()
        login.swap_page()

      

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
        tk.Label(Frame_signup,text="*Age:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=250)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.age,relief="raised").place(x=54,y=280,width=350,height=35)

        # Email Address
        tk.Label(Frame_signup,text="*Email Address:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=330)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.email,relief="raised").place(x=54,y=360,width=350,height=35)

        # Password
        tk.Label(Frame_signup,text="*Password:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=410)
        tk.Entry(Frame_signup,font=("Open Sans",18),bg="white",textvariable=self.password,relief="raised",show="*").place(x=54,y=440,width=350,height=35)
        
        # Button
        tk.Button(Frame_signup,command=self.submit_patient,cursor="hand2",text="Signup",fg="white",bg="#e60000",font=("Open sans",18)).place(x=137,y=500,width=180,height=40)

        # Login Here Button
        tk.Button(Frame_signup,command=lambda: self.back_logingpage(), text="Already Have an Account? Login Here.",fg="#000fff",borderwidth=0,bg="white",font=("Open sans",12)).place(x=80,y=550,width=300,height=40)




class SignUp_doctor:
    submit_confirmation =int()
    name = tk.StringVar()
    designation = tk.StringVar()
    email =  tk.StringVar()
    password = tk.StringVar()
    

    def __init__(self):
        self.swap_page()

    def swap_page(self):    
        Frame_signup.tkraise()
        self.InputBox()

    # Home Page
    def home_page(self):
        if  self.submit_confirmation:
            messagebox.showinfo("Welcome","Welcome to Mr.Doctor",parent=page)
        else:
            messagebox.showinfo("Error","You Have Already an Account!",parent=page)


    def submit(self,list):
        # Get Value from the Entries
        name = self.name.get()
        designation = self.designation.get()
        email = self.email.get()
        password = self.password.get()
        dayList = []
        for i in list.curselection():
            day = list.get(i)
            dayList.append(day)
        
        
        if name=="" or designation=="" or email=="" or password=="":
            messagebox.showerror("Error","All fields are required",parent=page)

        else:
            # Connect with Database
            dbConnect = db.dbConnect()
            self.submit_confirmation = dbConnect.insertData_doctor(name,designation,email,password,dayList)
            self.home_page()
            home_page = Home.DoctorHomePage(self.submit_confirmation)
            Frame_signup.destroy()

    def back_logingpage(self):
        Frame_signup.destroy()
        login = log.LoginPage_Doctor()
        login.swap_page()


    def InputBox(self):
       
        # Title of the form
        tk.Label(Frame_signup,text="Doctor",font=("Open Sans",22,"bold"),fg="black",bg="white", borderwidth=3, relief="solid").place(x=182,y=5)

        # Name
        tk.Label(Frame_signup,text="*Name:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=90)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.name,relief="raised").place(x=54,y=120,width=350,height=35)

        # Designation Information
        tk.Label(Frame_signup,text="*Designation:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=170)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.designation,relief="raised").place(x=54,y=200,width=350,height=35)

        # Email Address
        tk.Label(Frame_signup,text="*Email Address:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=250)
        tk.Entry(Frame_signup,font=("Open Sans",12),bg="white",textvariable=self.email,relief="raised").place(x=54,y=280,width=350,height=35)

        # Password
        tk.Label(Frame_signup,text="*Password:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=330)
        tk.Entry(Frame_signup,font=("Open Sans",18),bg="white",textvariable=self.password,relief="raised",show="*").place(x=54,y=360,width=350,height=35)
        
        # Available Day
        tk.Label(Frame_signup,text="*Available Day:",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=50,y=410)
        list = self.Available_Day()
        # Button
        tk.Button(Frame_signup,command=lambda:self.submit(list),cursor="hand2",text="Signup",fg="white",bg="#e60000",font=("Open sans",18)).place(x=137,y=500,width=180,height=40)

        # Login Here Button
        tk.Button(Frame_signup,command=lambda: self.back_logingpage(), text="Already Have an Account? Login Here.",fg="#000fff",borderwidth=0,bg="white",font=("Open sans",12)).place(x=80,y=550,width=300,height=40)

    def Available_Day(self):  
        list = tk.Listbox(Frame_signup, selectmode = "multiple",height=3,width=15,bg='#DCDCDC') 
        list.place(x=230,y=410)
        x= ['Sat','Sun','Mon','Tues','Wed','Thurs','Fri'] 
            
        for item in range(len(x)):     
            list.insert(tk.END,  x[item])   
        return list
