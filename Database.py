import mysql.connector
import time 

class dbConnect:
   
    def __init__(self):
        self.mydb = mysql.connector.connect(host="btvaoyhqtsmlkjltiwrt-mysql.services.clever-cloud.com",user="uf1ygntvtqzaqscg",passwd ="FnV84ZOV59iEVrdIeNC0",database="btvaoyhqtsmlkjltiwrt")
        self.mycursor = self.mydb.cursor()
    
    # To Generate a unique Id use real Time(milisecond) as Integer
    def time(self):
        ms = int(round(time.time())) 
        return ms

    def insertData_patient(self,name, age, email, password):
        try:
            sql_query = "Insert into patient_info(name,age,email,password) values(%s,%s,%s,%s)"
            patient = [(name,age,email,password)]
            self.mycursor.executemany(sql_query, patient)
            self.mydb.commit()
            return True
        except :
            return False

    
    def insertData_doctor(self,name, designation, email, password):
        try:
            sql_query = "Insert into doctor_info(email,name,designation,password) values(%s,%s,%s,%s)"
            doctor = [(email,name,designation,password)]
            self.mycursor.executemany(sql_query, doctor)
            self.mydb.commit()
            return True
        except :
            return False

  

    # Match email and password with the database for Patient
    def login_patient(self,Email,Password):
        login = bool()
        sql_query = "SELECT email,password FROM patient_info"
        self.mycursor.execute(sql_query)

        for (email,password) in self.mycursor:
            if Email == email and Password == password:
                login = True
                break  
            else:
                login = False

        return login
               
    
      # Match email and password with the database for Doctor
    def login_doctor(self,Email,Password):
        sql_query = "SELECT email,password FROM doctor_info"
        self.mycursor.execute(sql_query)

        for (email,password) in self.mycursor:
            if Email == email and Password == password:
                login = True
                break  
            else:
                login = False

        return login
