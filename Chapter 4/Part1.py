import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b'
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

def check(email):
    if(re.match(regex, email)):
        print("OK")

    else:
        print("WRONG")

if __name__ == '__main__':
    email = input()
    check(email)