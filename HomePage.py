import root as r
import MakeAppointment as appointment


tk = r.tk
page = r.root
ButtonBackground_color = "#6CBB3C"
Backgroud_color = "red"
Frame=tk.Frame(page,highlightbackground=Backgroud_color, highlightthickness=5)
Frame.place(x=0,y=0,height=700,width=500)

class DoctorHomePage:
    def __init__(self):
        Frame.tkraise()
        tk.Label(Frame,text="Home",font=("Open Sans",22,"bold"),fg="white",bg=Backgroud_color,width =27, relief="solid").place(x=0,y=0)
        self.optionlist()
        

    
    def optionlist(self):
       tk.Button(Frame, text="See Appointment\nList",fg="White",bg=ButtonBackground_color,font=("Open sans",18)).place(x=135,y=125,width=200,height=100)


class PatientHomePage:
    def __init__(self):
        Frame.tkraise()
        tk.Label(Frame,text="Home",font=("Open Sans",22,"bold"),fg="white",bg=Backgroud_color,width =27, relief="solid").place(x=0,y=0)
        self.optionlist()
        
    def makeAppointment(self):
        Frame.destroy()
        appointment.swap_page()
    
    def optionlist(self):
       tk.Button(Frame, text="Make An\nAppointment",command =lambda:self.makeAppointment(),fg="White",bg=ButtonBackground_color,font=("Open sans",18)).place(x=135,y=150,width=200,height=100)
       tk.Button(Frame, text="See Appointment\nDetails",fg="White",bg=ButtonBackground_color,font=("Open sans",18)).place(x=135,y=320,width=200,height=100)
