from database import *
import datetime

class Bank():
    def __init__(self , username , acc_no):
        self.__username = username
        self.__acc_no = acc_no

    def create_transaction_table(self):
        exe(f"CREATE TABLE IF NOT EXISTS {self.__username}_Details ( timedate VARCHAR(80) , acc_no INTEGER , remarks VARCHAR(30) , amount INTEGER)")


    def bankenquiry(self ):
                    temp = exe(f"SELECT balance FROM customer where username = '{self.__username}' ;")
                    cash = temp[0][0]
                    print(f"Hello {self.__username}, Your account balance is {cash}")

    def deposit(self , amount):
        temp = exe(f"SELECT balance FROM customer where username = '{self.__username}' ;")
        cash = temp[0][0]
        cash += amount
        exe(f"UPDATE customer SET balance = '{cash}' WHERE username = '{self.__username}'; ")
        self.bankenquiry()  
        exe(f"INSERT INTO {self.__username}_Details VALUES ( '{datetime.datetime.now}' ,'{self.__acc_no}' , 'Amount Deposit' , '{amount}' );") 
        mydb.commit()


    def withdraw(self , amount):
        temp = exe(f"SELECT balance FROM customer where username = '{self.__username}' ;")
        if amount > temp[0][0]:
              print('Insufficient Balance')
        else :
            cash = temp[0][0]
            cash -= amount
            exe(f"UPDATE customer SET balance = '{cash}' WHERE username = '{self.__username}'; ")
            self.bankenquiry()  
            exe(f"INSERT INTO {self.__username}_Details VALUES ( '{datetime.datetime.now}' ,'{self.__acc_no}' , 'Amount Withdraw' , '{amount}' );") 
            mydb.commit()

   
    def fundtransfer(self ,receiver_acc, amount):
        acc_no = receiver_acc
        temp1 = exe(f"SELECT balance FROM customer where acc_no = '{acc_no}' ;")
        temp2 = exe(f"SELECT balance FROM customer where username = '{self.__username}' ;")
        receiver_name = exe(f"SELECT username FROM customer where acc_no = '{acc_no}' ;")
        if amount > temp2[0][0]:
              print('Insufficient Balance')
        else :
            cash1 = temp1[0][0]
            cash2 = temp2[0][0]
            cash1 += amount
            cash2 -= amount
            exe(f"UPDATE customer SET balance = '{cash1}' WHERE acc_no = '{acc_no}'; ")
            exe(f"UPDATE customer SET balance = '{cash2}' WHERE username = '{self.__username}'; ")
            self.bankenquiry()  
            exe(f"INSERT INTO {self.__username}_Details VALUES ( '{datetime.datetime.now}' ,'{self.__acc_no}' , 'Amount Tranferred' , '{amount}' );") 
            exe(f"INSERT INTO {receiver_name[0][0]}_Details VALUES ( '{datetime.datetime.now}' ,'{self.__acc_no}' , 'Amount Recieved' , '{amount}' );") 
            mydb.commit()