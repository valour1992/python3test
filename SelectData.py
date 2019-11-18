import pymysql
connection = pymysql.connect(host='localhost',port=3306,database='bmpl_database',user='root',autocommit = True)
cursor = connection.cursor()


id = 104
name = 'Ram'

query= "select * from users where user_id = %s and user_name = %s"
cursor.execute(query,(id,name))

if cursor.rowcount > 0:
    data = cursor.fetchall()
    print(data)
else:
    print("Data Not found")

connection.close