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
        id = self.time() 
        sqlform = "Insert into patient_info(id,name,age,email,password) values(%s,%s,%s,%s,%s)"
        patient = [(id,name,age,email,password)]
        self.mycursor.executemany(sqlform, patient)
        self.mydb.commit()