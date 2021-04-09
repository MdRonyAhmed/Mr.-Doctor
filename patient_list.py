import root as r
import Database as db
from tkinter import messagebox

tk = r.tk
page = r.root
ButtonBackground_color = "#6CBB3C"
Backgroud_color = "#6CBB3C"


Frame=tk.Frame(page,highlightbackground=Backgroud_color,bg = 'white', highlightthickness=5)
Frame.place(x=0,y=0,height=700,width=500)


class patient_list:
    X = 10
    Y = 50
    i= 1 

    def swap_page(self,ID):    
        Frame.tkraise()
        self.Elements(ID)


    def Elements(self,ID):
        database_connect = db.dbConnect()
        appointment_list= database_connect.patient_list(ID)

        tk.Label(Frame,text="Appointment List",font=("Open Sans",22,"bold"),fg="white",bg=Backgroud_color,width =27, relief="solid").place(x=0,y=0)
        tk.Label(Frame,text="Name",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=self.X+22,y=self.Y)
        tk.Label(Frame,text="Age",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=self.X+115,y=self.Y)
        tk.Label(Frame,text='Contact Number',font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=self.X+195,y=self.Y)
        tk.Label(Frame,text="Day",font=("Open Sans",15,"bold"),fg="black",bg="white").place(x=self.X+385,y=self.Y)

        if(appointment_list !=None):
            for patient in appointment_list: 
                Name = patient[0]
                age = patient[1]
                contactNumber = patient[2]
                day = patient[3]
            
                tk.Label(Frame,text=str(self.i)+") "+Name,font=("Open Sans",13),fg="black",bg="white").place(x=self.X,y=self.Y+50)
                tk.Label(Frame,text=age,font=("Open Sans",13),fg="black",bg="white").place(x=self.X+120,y=self.Y+50)
                tk.Label(Frame,text=contactNumber,font=("Open Sans",13),fg="black",bg="white").place(x=self.X+210,y=self.Y+50)
                tk.Label(Frame,text=day,font=("Open Sans",13),fg="black",bg="white").place(x=self.X+390,y=self.Y+50)
                self.i= self.i+1
                self.Y = self.Y + 30
        else:
            messagebox.showinfo("No Appointment","No Appointment for Show",parent = page)
        
   