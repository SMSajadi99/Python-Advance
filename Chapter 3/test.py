import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="4430557869m",
  database = 'school'
)

# print(mydb)
mycursor = mydb.cursor()


########################################################################

# mycursor.execute("CREATE DATABASE school")
# mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age SMALLINT)")



########################################################################

# sql = "INSERT INTO student (name, age) VALUES (%s,%s)"
# values = ("pedram",28)

# mycursor.execute(sql,values)
# mydb.commit()
# print(mycursor.rowcount,"row was inserted")

########################################################################

# mycursor.execute("SELECT * FROM student WHERE name='pedram'")

# for i in mycursor.fetchall():
#       print(i)


########################################################################

# mycursor.execute("UPDATE student SET age=30 WHERE name='pedram'")
# mydb.commit()

# mycursor.execute("SELECT * FROM student WHERE name='pedram'")

# for i in mycursor.fetchall():
#       print(i)


########################################################################

mycursor.execute("DELETE FROM student WHERE name='john' LIMIT 1")
mydb.commit()

mycursor.execute("SELECT * FROM student")

for i in mycursor.fetchall():
      print(i)