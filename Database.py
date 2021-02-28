import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="rony",passwd ="rhrony049",database="mr.doctor")

mycursor = mydb.cursor()

sqlform = "Insert into doctor(Id,Name,Info,Available_date) values(%s,%s,%s,%s)"

doctors = [("102","Dr. MD. RONY AHMED","MBBS(Medicine)","2021-02-15")]

mycursor.executemany(sqlform, doctors)

mydb.commit()