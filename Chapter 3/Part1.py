import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="4430557869m",
  database = 'Employee_information'
)

# print(mydb)
mycursor = mydb.cursor()

########################################################################

# mycursor.execute("CREATE DATABASE Employee_information")
# mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), Weight_man SMALLINT,Height_man SMALLINT)")


########################################################################


# sql = "INSERT INTO student (name, Weight_man, Height_man) VALUES (%s,%s,%s)"
# values = ("Ahmad",60,175)

# mycursor.execute(sql,values)
# mydb.commit()
# print(mycursor.rowcount,"row was inserted")

########################################################################

# mycursor.execute("SELECT * FROM student")

# for i in mycursor.fetchall():
#       print(i)

########################################################################

sql = "SELECT * FROM student ORDER BY Height_man DESC"
mycursor.execute(sql)

result = mycursor.fetchall()

ls = []
for x in result:
  # print(x[1], x[3],x[2])
  ls.append(x)      

# print(ls)

for x in result:
      for y in result:
        if (x[3]==y[3]) and (x != y) and (x[2] < y[2]):
              ls[ls.index(x)] , ls[ls.index(y)] = ls[ls.index(y)], ls[ls.index(x)]


# print(ls)

for i in ls:
      print(i[1],i[3],i[2]) 
