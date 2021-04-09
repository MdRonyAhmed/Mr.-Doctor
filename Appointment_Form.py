import root as r
import Database as db
from tkinter import messagebox
from tkinter import font
import MakeAppointment
import Database as db

# Frame
tk = r.tk
page = r.root
ButtonBackground_color = "#6CBB3C"
Backgroud_color = "Black"

Frame=tk.Frame(page,highlightbackground=Backgroud_color, highlightthickness=5,bg="white")
Frame.place(x=65,y=300,height=340,width=350)

# Heading & Customize font style
heading =tk.Label(Frame,text="Appointment Form",font=("Open Sans",20,"bold"),bg="white")
heading.place(x=40,y=5)
f = font.Font(heading, heading.cget("font"))
f.configure(underline=True)
heading.configure(font=f)

class appoint_form:
    # input variable
    check_submission = bool()
    patient_name = tk.StringVar()
    patient_age = tk.StringVar()
    contact_number = tk.StringVar()
    doctor_id = int()
    doctorsAvailable_day = []

    # Available Day of Doctor
    def available_day(self,day):
        list = tk.Listbox(Frame, selectmode = "single",height=3,width=15,bg='#DCDCDC') 
        list.place(x=180,y=190)   
        for item in range(len(day)):     
            list.insert(tk.END,  day[item])
        return list

    # Cancle the Form
    def cancle_form(self):
        appoint = MakeAppointment.make_appoint()
        appoint.swap_page()

    def available_dayList(self,id):
        database_connect = db.dbConnect()
        availableDay = database_connect.available_day_doctor(id)
        return availableDay

    # Rise this Page
    def swap_page(self,id):   
        Frame.tkraise()
        global doctorsAvailable_day
        global doctor_id
        
        doctor_id = int(id[0])
        doctorsAvailable_day = self.available_dayList(doctor_id)
        self.InputBox()
        
    def check_allfields_entry(self,selected_day):
        if (self.patient_name.get() == '' or self.patient_age.get()== '' or self.contact_number.get == '' or selected_day == ''):
            messagebox.showerror("Error","All fields are required",parent=page)
            return False
        return True

    def submit_form(self,list):
        
        for i in list.curselection():
            day = list.get(i)
        selected_day = day

        fields_check = self.check_allfields_entry(selected_day)
     
        if(fields_check):
            database = db.dbConnect()
            self.check_submission = database.submit_appointment(doctor_id,self.patient_name.get(),int(self.patient_age.get()),self.contact_number.get(),selected_day)

            if(self.check_submission):
                messagebox.showinfo("Successful","You Have Successfully Made an Appointment",parent = page)
                self.cancle_form()


    def InputBox(self):
        tk.Label(Frame,text="Patient Name   : ",font=("Noto",15,),fg="black",bg="white").place(x=5,y=60)
        tk.Entry(Frame,font=("Open Sans",12),bg="white",textvariable=self.patient_name,relief="raised").place(x=160,y=60,width=150,height=30)
        tk.Label(Frame,text="Patient Age     : ",font=("Noto",15,),fg="black",bg="white").place(x=5,y=105)
        tk.Entry(Frame,font=("Open Sans",12),bg="white",textvariable=self.patient_age,relief="raised").place(x=160,y=105,width=150,height=30)
        tk.Label(Frame,text="Contact Number: ",font=("Noto",15,),fg="black",bg="white").place(x=5,y=150)
        tk.Entry(Frame,font=("Open Sans",12),bg="white",textvariable=self.contact_number,relief="raised").place(x=160,y=150,width=150,height=30)
        tk.Label(Frame,text="Appointment Day  : ",font=("Noto",15,),fg="black",bg="white").place(x=5,y=200)

        list = self.available_day(doctorsAvailable_day)

        tk.Button(Frame, text="Cancle",command=lambda:self.cancle_form(),fg="black",borderwidth=1,bg=ButtonBackground_color,font=("Open sans",12)).place(x=45,y=280,width=100,height=40)
        tk.Button(Frame, text="Confirm",command=lambda:self.submit_form(list),fg="black",borderwidth=1,bg=ButtonBackground_color,font=("Open sans",12)).place(x=200,y=280,width=100,height=40)
