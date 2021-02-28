from PIL import Image,ImageTk
import LoginPage as login

def FirstPage(page,tk):
    
    def login_doctor_page():               
        login.LoginPage_Doctor(page,tk)
        Frame_login.destroy()
    
    def login_patient_page():               
        login.LoginPage_Patient(page,tk)
        Frame_login.destroy()
    

    page.cover = Image.open("E:\practice\picture\pic14.jpg")
    page.cover = ImageTk.PhotoImage(page.cover)  
    page.bg=tk.Label(page,image=page.cover).place(x=0,y=0,relwidth=1,relheight=1) 

    Frame_login=tk.Frame(page,bg="white")
    Frame_login.place(x=101,y=275,height=200,width=300)

    tk.Button(Frame_login,command=lambda:login_doctor_page(),text="Login As Doctor",fg="White",bg="#D82A2A",font=("Open sans",18)).place(x=60,y=50,width=180,height=40)
    tk.Button(Frame_login,command=lambda:login_patient_page(),text="Login As Patient",fg="White",bg="#D82A2A",font=("Open sans",18)).place(x=60,y=105,width=180,height=40)    
        

    