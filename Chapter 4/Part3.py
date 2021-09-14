import re
import requests
import mysql.connector
from bs4 import BeautifulSoup


#--------------------------------------

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="4430557869m",
  database='Price_car'
)

# print(mydb)
mycursor = mydb.cursor()


################################################################

# mycursor.execute("CREATE DATABASE Price_car")
# mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, price VARCHAR(50), mile VARCHAR(50))")

################################################################

# sql = "INSERT INTO student (price, mile) VALUES (%s,%s)"

# input_name_car = input()

# res = requests.get('https://www.truecar.com/used-cars-for-sale/listings/' + input_name_car)
# # print(res.text)

# soup = BeautifulSoup(res.text,'html.parser')
# val_Price = soup.find_all('div',attrs={'class':'heading-3 margin-y-1 font-weight-bold'})
# val_Mile = soup.find_all('div',attrs={'class':'font-size-1 text-truncate','data-test':'vehicleMileage'})


###### print(len(val_Price) , len(val_Mile))
###### print(val_Price[14].text)
###### print(val_Mile[14].text)

# for i in range(20):
#     # print(i)    

#     trash_Price = val_Price[i].text.split()
#     trash_Mile = val_Mile[i].text

#     # print(trash_Price[0])
#     # print(trash_Mile)


#     values = (trash_Price[0],trash_Mile)

#     mycursor.execute(sql,values)
#     mydb.commit()
#     print(mycursor.rowcount,"row was inserted")


################################################################


mycursor.execute("SELECT * FROM student")

for i in mycursor.fetchall():
      print(i)


