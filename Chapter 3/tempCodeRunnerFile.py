mycursor.execute("SELECT * FROM student")

for i in mycursor.fetchall():
      print(i)