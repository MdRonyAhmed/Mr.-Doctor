import root as r
import Database as db
from tkinter import messagebox
import json
import Appointment_Form as appointment

tk = r.tk
page = r.root
ButtonBackground_color = "#6CBB3C"
Backgroud_color = "red"
Frame=tk.Frame(page,highlightbackground=Backgroud_color, highlightthickness=5)
Frame.place(x=0,y=0,height=700,width=500)

def swap_page():    
    Frame.tkraise()
    Elements()

def appointment_form(id,dayList):
    appointment.swap_page(id,dayList)

def Elements():
    database_connect = db.dbConnect()
    doctorList= database_connect.doctor_list()

    tk.Label(Frame,text="Doctor List",font=("Open Sans",22,"bold"),fg="white",bg=Backgroud_color,width =27, relief="solid").place(x=0,y=0)
    X = 5
    Y = 50
    for doctor_info in doctorList:  
        doctor_id = doctor_info[0]
        doctor_name = doctor_info[2]
        doctor_designation = doctor_info[3]
        doctor_avalaibleDay = json.loads(doctor_info[5])

        tk.Label(Frame,text=doctor_name,font=("Open Sans",15),fg="#008000").place(x=X,y=Y)
        tk.Label(Frame,text=doctor_designation,font=("Noto",11),fg="black").place(x=X,y=Y+25)
        tk.Label(Frame,text='Available Day : '+doctor_avalaibleDay[0]+', '+doctor_avalaibleDay[1]+ ', '+ doctor_avalaibleDay[2],font=("Noto",10),fg="black").place(x=X,y=Y+45)
        tk.Button(Frame, text="Appointment",command=lambda:appointment_form(doctor_id,doctor_avalaibleDay),fg="White",bg=ButtonBackground_color,font=("Open sans",15)).place(x=X+350,y=Y+10)

        Y = Y + 85




