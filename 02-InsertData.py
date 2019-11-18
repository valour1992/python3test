import pymysql
connection = pymysql.connect(host='localhost',port=3306,database='bmpl_database', user='root',autocommit =True)

cursor = connection.cursor()

id = 102
name = "Ramesh"
sal = 320000
address = 'Noida'


query = "insert into users values (%s,%s,%s,%s)"
cursor.execute(query,(id,name,sal,address))
connection.close()