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

# input variable
patient_name = tk.StringVar()
patient_age = tk.StringVar()
doctorsAvailable_day = []

# Available Day of Doctor
def available_day(day):
    list = tk.Listbox(Frame, selectmode = "single",height=3,width=15,bg='#DCDCDC') 
    list.place(x=180,y=160)   
    for item in range(len(day)):     
        list.insert(tk.END,  day[item]) 

# Cancle the Form
def cancle_form():
    MakeAppointment.swap_page()

def available_dayList(id):
    database_connect = db.dbConnect()
    availableDay = database_connect.available_day_doctor(id)
    return availableDay

# Rise this Page
def swap_page(id):   
    Frame.tkraise()
    global doctorsAvailable_day
    
    doctor_id = int(id[0])
    doctorsAvailable_day = available_dayList(doctor_id)

    InputBox()

def InputBox():
    tk.Label(Frame,text="Patient Name   : ",font=("Noto",15,),fg="black",bg="white").place(x=5,y=60)
    tk.Entry(Frame,font=("Open Sans",12),bg="white",textvariable=patient_name,relief="raised").place(x=160,y=60,width=150,height=30)
    tk.Label(Frame,text="Patient Age      : ",font=("Noto",15,),fg="black",bg="white").place(x=5,y=105)
    tk.Entry(Frame,font=("Open Sans",12),bg="white",textvariable=patient_age,relief="raised").place(x=160,y=105,width=150,height=30)
    tk.Label(Frame,text="Appointment Day : ",font=("Noto",15,),fg="black",bg="white").place(x=5,y=175)

    available_day(doctorsAvailable_day)

    tk.Button(Frame, text="Cancle",command=lambda:cancle_form(),fg="black",borderwidth=1,bg=ButtonBackground_color,font=("Open sans",12)).place(x=45,y=280,width=100,height=40)
    tk.Button(Frame, text="Confirm",fg="black",borderwidth=1,bg=ButtonBackground_color,font=("Open sans",12)).place(x=200,y=280,width=100,height=40)

