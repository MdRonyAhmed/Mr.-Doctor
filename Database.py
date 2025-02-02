import mysql.connector
import json


class dbConnect:
   
    def __init__(self):
        self.mydb = mysql.connector.connect(host="btvaoyhqtsmlkjltiwrt-mysql.services.clever-cloud.com",user="uf1ygntvtqzaqscg",passwd ="FnV84ZOV59iEVrdIeNC0",database="btvaoyhqtsmlkjltiwrt")
        self.mycursor = self.mydb.cursor()
    

    def insertData_patient(self,name, age, email, password):
        try:
            sql_query = "Insert into patient_info(name,age,email,password) values(%s,%s,%s,%s)"
            info = [(name,age,email,password)]
            self.mycursor.executemany(sql_query, info)
            self.mydb.commit()
            return True
        except :
            return False

    
    def insertData_doctor(self,name, designation, email, password,avalable_day):
        
        # Covert the Available Day list to JSON format for insert into the DB
        day_json = json.dumps(avalable_day)

        try:
            id = self.id_doctor()
            sql_query = "Insert into doctor_info(id,email,name,designation,password,Available_day) values(%s,%s,%s,%s,%s,%s)"
            info = [(id,email,name,designation,password,day_json)]
            self.mycursor.executemany(sql_query, info)
            self.mydb.commit()
            return id
        except :
            return None


  

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
        sql_query = "SELECT ID,email,password FROM doctor_info"
        self.mycursor.execute(sql_query)

        for (ID,email,password) in self.mycursor:
            if Email == email and Password == password:
                login = {'confirm':True,
                        'id': ID
                    }
                break  
            else:
                login = {'confirm': False}

        return login

    # Create Id for Doctor
    def id_doctor(self):
        sql_query = "(SELECT MAX(ID) FROM doctor_info)"
        self.mycursor.execute(sql_query)
        for ID in self.mycursor:
            for item in ID:
                id = item
        if id == None:
            id = 1000
        return id+1

    # Get the list of Doctor from the Database
    def doctor_list(self):
        sql_query = "SELECT ID,name,Designation,Available_day FROM doctor_info"
        self.mycursor.execute(sql_query)
        return (self.mycursor.fetchall())
    
    def patient_list(self,id):
        pat_list = []
        sql_query = "SELECT Doctor_id,Patient_Name,Age,Contact_number,day FROM appointment_list"
        self.mycursor.execute(sql_query)
       
        for (Doctor_id,Patient_Name,Age,Contact_number,day) in self.mycursor:
            if(Doctor_id == id):
                pat_list.append([Patient_Name,Age,Contact_number,day])
        
        return pat_list


    
    def available_day_doctor(self,id):
        sql_query = "SELECT ID,Available_day FROM doctor_info"
        self.mycursor.execute(sql_query)

        for (ID,Available_day) in self.mycursor:
            if (ID == id):
                return json.loads(Available_day)

    def submit_appointment(self,doc_id, patient_name, patient_age, patient_number, day):

        try:  
            sql_query = "Insert into appointment_list(Patient_Name,Age,Contact_number,Doctor_id,day) values(%s,%s,%s,%s,%s)"
            info = [(patient_name,patient_age,patient_number,doc_id,day)]
            self.mycursor.executemany(sql_query, info)
            self.mydb.commit()
            return True
        except :
            return False


    

     
