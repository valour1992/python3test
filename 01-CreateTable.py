import pymysql
connection = pymysql.connect(host='localhost',port=3306,database='bmpl_database',user='root',autocommit = True)
cursor = connection.cursor()

query= "Create table users (user_id int, user_name text(100), user_sal int, user_address varchar(100))"
cursor.execute(query)
connection.close




##########



#