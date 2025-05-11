from database import *
import random
from customer import *
from bank import *

def SingUp():
    username = input("Enter your username name : ")
    temp = exe(f"SELECT username FROM customer where username = '{username}';")
    if temp:
        print("Username isn't Avaiable")
        SingUp()
    else:
        print("Username Avaiable")
        password = input("Enter your password: ")
        name = input("Enter your name : ")
        age = int(input("Enter your age : "))
        city = input("Enter your city name : ")
        while True:
            acc_no = random.randint(1000000 , 9999999)
            temp = exe(f"SELECT acc_no FROM customer WHERE acc_no = '{acc_no}';")
            if temp is None:
                continue
            else:
                print(f"Account no : {acc_no}")
                break
 
    cusobj = CreateCus(username , password , name , age , city , acc_no)
    cusobj.insertdata()
    bankobj = Bank(username , acc_no)
    bankobj.create_transaction_table()


def SignIn():
     while True:
        username = input("Enter your username: ")
        temp = exe(f"SELECT username FROM customer WHERE username = '{username}';")
        if temp:
            password = input(f"{username}, Enter your password: ")
            temp = exe(f"SELECT password FROM customer WHERE username = '{username}';")
            if temp[0][0] == password:
                print("Login Successfully")
                return username
            else:
                print("invalid password")
                continue      
        else:
            print("Enter a valid username")
            SignIn()