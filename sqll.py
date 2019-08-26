import pymysql

data = pymysql.connect(user = "root", password = "", host = "127.0.0.1" ,database ="test1")

my = data.cursor()

my.execute("select version()")

print(my.fetchall())

###sql = """create table sparrow(first char(20),last char(20))"""

###my.execute(sql)

my.execute("show tables")

###sq = """insert into sparrow(first,last) values('Anjali','Saanvi'),('Dipti','Shandilya')"""

###my.execute(sq)

dq = """update sparrow set last ='Ujjwal' where  id =3 """

my.execute(dq)

print(my.fetchall())

data.commit()
