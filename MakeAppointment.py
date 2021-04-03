import root as r
import Database as db
from tkinter import messagebox
import json
import Appointment_Form as appointment
import tkinter.scrolledtext as st

tk = r.tk
page = r.root
ButtonBackground_color = "#6CBB3C"
Backgroud_color = "red"


Frame=tk.Frame(page,highlightbackground=Backgroud_color,bg = 'white', highlightthickness=5)
Frame.place(x=0,y=0,height=700,width=500)
text_area = st.ScrolledText(Frame,bg='#d7e7dc',fg="black",width = 46,height = 20)
text_area.place(x=1,y=50)


def swap_page():    
    Frame.tkraise()
    Elements()

def appointment_form(list):
    doct_id = []
    for i in list.curselection():
        id = list.get(i)
        doct_id.append(id)
    appointment.swap_page(doct_id)

def Available_Day(idList):
    list = tk.Listbox(Frame, selectmode = "single",height=3,width=10,bg='#DCDCDC') 
    list.place(x=215,y=430)
        
    for item in range(len(idList)):     
        list.insert(tk.END,  idList[item]) 

    return list
    # doct_id = list.curselection()
    # for i in list.curselection():
    #     id = list.get(i)
    #     doct_id.append(id)
    # return doct_id

def Elements():
    text_area.delete('1.0',tk.END)
    database_connect = db.dbConnect()
    doctorList= database_connect.doctor_list()
    doctor_id_list = []

    tk.Label(Frame,text="Doctor List",font=("Open Sans",22,"bold"),fg="white",bg=Backgroud_color,width =27, relief="solid").place(x=0,y=0)
    X = 5
    Y = 50
    for doctor_info in doctorList:  
        doctor_id = doctor_info[0]
        doctor_id_list.append(doctor_id)
        doctor_name = doctor_info[1]
        doctor_designation = doctor_info[2]
        doctor_avalaibleDay = json.loads(doctor_info[3])
        text_area.insert(tk.INSERT,doctor_name +"\n" + doctor_designation + "\n" + 'Available Day : ' + doctor_avalaibleDay[0]+', '+doctor_avalaibleDay[1]+ ', '+ doctor_avalaibleDay[2] + "\n" +'Doctor ID: ' + str(doctor_id) + "\n\n")
    

    tk.Label(Frame,text="Doctor ID :",anchor="center",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=65,y=450) 
    lsit = Available_Day(doctor_id_list)
    tk.Button(Frame, text="Appointment",command=lambda:appointment_form(lsit),fg="White",bg=ButtonBackground_color,font=("Open sans",15)).place(x=180,y=550)



