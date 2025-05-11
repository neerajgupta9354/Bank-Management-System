from database import *

class CreateCus :
    def __init__(self  , username , password , name , age , city , acc_no):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city 
        self.__acc_no = acc_no

    def insertdata(self):
            temp = exe(f"INSERT INTO customer VALUES ('{self.__username}' , '{self.__password}' , '{self.__name}' , '{self.__age}' , '{self.__city}' , '{self.__acc_no}' , 0, 1)")
            mydb.commit()
            print("Account Created Successfully")

