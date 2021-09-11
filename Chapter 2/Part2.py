from datetime import date
 
def calculateAge(birthDate):
    days_in_year = 365.2425   
    age = int((date.today() - birthDate).days / days_in_year)
    return age
         
# Driver code
date_input = list(map(int,input().split("/")))
if (date_input[1]<= 12) and (date_input[2]<= 31):
    print(calculateAge(date(date_input[0], date_input[1], date_input[2])))
else:
    print('WRONG')