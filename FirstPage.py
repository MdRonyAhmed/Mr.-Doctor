from PIL import Image,ImageTk
import LoginPage as login
import root as r

page = r.root
tk = r.tk
def FirstPage():
    
    def login_doctor_page():               
        login.LoginPage_Doctor()
        Frame_login.destroy()
    
    def login_patient_page():               
        login.LoginPage_Patient()
        Frame_login.destroy()
    

    page.cover = Image.open("E:\Projects\practice\picture\pic14.jpg")
    page.cover = ImageTk.PhotoImage(page.cover)  
    page.bg=tk.Label(page,image=page.cover).place(x=0,y=0,relwidth=1,relheight=1) 

    Frame_login=tk.Frame(page,bg="white")
    Frame_login.place(x=101,y=275,height=200,width=300)

    tk.Button(Frame_login,command=lambda:login_doctor_page(),text="Login As Doctor",fg="White",bg="#D82A2A",font=("Open sans",18)).place(x=60,y=55,width=180,height=40)
    tk.Button(Frame_login,command=lambda:login_patient_page(),text="Login As Patient",fg="White",bg="#D82A2A",font=("Open sans",18)).place(x=60,y=110,width=180,height=40)    
        

    