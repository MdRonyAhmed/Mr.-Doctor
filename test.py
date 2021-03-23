import json
import mysql.connector


list = ['sun','mon','tues']
id = 1001
email = 'rony@gmail.com'
name = 'rony'
designation = 'MBBS'
password = 123
jsonList = json.dumps(list)

mydb = mysql.connector.connect(host="btvaoyhqtsmlkjltiwrt-mysql.services.clever-cloud.com",user="uf1ygntvtqzaqscg",passwd ="FnV84ZOV59iEVrdIeNC0",database="btvaoyhqtsmlkjltiwrt")
mycursor = mydb.cursor()


# sql_query = "Insert into doctor_info(id,email,name,designation,password,Available_day) values(%s,%s,%s,%s,%s,%s)"
# doctor = [(id,email,name,designation,password,jsonList)]
# mycursor.executemany(sql_query, doctor)
# mydb.commit()

# sql_query = "SELECT id,Available_day FROM doctor_info"
# mycursor.execute(sql_query)

# for (id,Available_day) in mycursor:
#     print(id,Available_day)
#     day = json.loads(Available_day)
#     print(day[2])
#     for item in day:
#         print(item)



sql_query = "SELECT * FROM doctor_info"
mycursor.execute(sql_query)

doctorList = mycursor.fetchall()
print(len(doctorList))
print(doctorList[0])

