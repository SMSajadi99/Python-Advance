import mysql.connector
import re

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="4430557869m",
  database ='info_email'
)

# print(mydb)
mycursor = mydb.cursor()

#######################################################################

# mycursor.execute("CREATE DATABASE info_email")
# mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), password VARCHAR(50))")

#######################################################################

# sql = "INSERT INTO student (username, password) VALUES (%s,%s)"
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b'

# def check(email):
#     if(re.match(regex, email)):
#         print("Valid Email")

#     else:
#         a = 1
#         print("Invalid Email")

# if __name__ == '__main__':
#     email = input()
#     check(email)

#     while re.match(regex, email) == None:
#         print("expression@string.string")
#         email = input()

# input_password = input()
# values = (email,input_password)

# mycursor.execute(sql,values)
# mydb.commit()
# print(mycursor.rowcount,"row was inserted")


########################################################################

mycursor.execute("SELECT * FROM student")

for i in mycursor.fetchall():
      print(i)


########################################################################

# mycursor.execute("DELETE FROM student WHERE username='ankitrai326.com' LIMIT 1")
# mydb.commit()