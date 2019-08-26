##import mysql.connector
#db= mysqli.connect(user = "root",password = "",host="127.0.0.1", database ="dbtest")




import pymysql

db = pymysql.connect(user = "root", password = "", host = "127.0.0.1", database= "test")

mycursor=db.cursor()

##mycursor.execute("SHOW TABLES")

##print(mycursor.fetchall())

mycursor.execute("SELECT VERSION()")

print(mycursor.fetchall())

#delete the table

##mycursor.execute("DROP TABLE app")

#create table

###sql= """create table app(first_name char(20), last_name char(20), age int, sex char(1))"""

#mycursor.execute(sql)



##insert values
##sql = """insert into app(first_name, last_name,age,sex)
    ###values('Aakash','verma','20','M'),('Ashim','Ujjwal','20','m')"""

##sql = "update app set age = 18,sex='f' where id=2"
sql = "delete from app  where age "


mycursor.execute(sql)

mycursor.execute("show tables")

print(mycursor.fetchall())



db.commit()






